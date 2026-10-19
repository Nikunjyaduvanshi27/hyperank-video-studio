"""Logged-in run of a gated hyperank tool through BrowserOS neo (Profile 1 only), saving the unlocked result.

    python neo_capture.py <tool-url> <out-dir> VALUE [VALUE..] --page N [--engines "A,B"]

--page: a tab you own in the Profile 1 window (a tab never changes profile, while new tabs land in whichever
profile is active). The tab is pointed at chrome://version and checked right before the run.

Read-only: runs the free tool and reads the page. Refuses to act unless chrome://version shows Profile 1.
Writes neo-api.json, neo-result-sec.html, neo-result-text.txt, neo-result.png to <out-dir>.
"""
import base64, json, msvcrt, re, sys, time
from pathlib import Path
import neo

GAP = 75  # seconds between logged-in runs: hyperank rate-limits the account too, so all agents queue here
lock = open(Path(__file__).with_name(".neo-lock"), "a+")
print("waiting for the shared neo queue (one run at a time)...", flush=True)
while True:  # one neo run at a time across every process; the OS frees the lock if this process dies
    try:
        msvcrt.locking(lock.fileno(), msvcrt.LK_NBLCK, 1)
        break
    except OSError:
        time.sleep(5)
last_run = Path(__file__).with_name(".neo-last")
wait = GAP - (time.time() - float(last_run.read_text() or 0)) if last_run.exists() else 0
if wait > 0:
    time.sleep(wait)
print("neo queue: my turn", flush=True)

args = sys.argv[1:]
engines = None
if "--engines" in args:
    i = args.index("--engines"); engines = args[i + 1].split(","); del args[i:i + 2]
i = args.index("--page"); page = int(args[i + 1]); del args[i:i + 2]
url, out, values = args[0], Path(args[1]), args[2:]
out.mkdir(parents=True, exist_ok=True)
neo.init()


def ev(page: int, code: str, n: int = 5000) -> object:
    r = neo.call("evaluate", {"page": page, "code": code, "maxChars": n})
    body = r.split("\n", 1)[-1] if r.startswith("[UNTRUSTED") else r  # drop the untrusted-content header line
    body = body.split("[END_UNTRUSTED")[0].strip()
    try:
        return json.loads(body)
    except json.JSONDecodeError:
        return body


neo.call("navigate", {"page": page, "url": "chrome://version/"})
prof = neo.call("grep", {"page": page, "pattern": "Profile Path", "over": "content"})
if not prof.split("Profile Path")[1].split("\n")[0].rstrip().endswith("Profile 1"):
    sys.exit("REFUSED: active neo profile is not Profile 1:\n" + prof)
neo.call("navigate", {"page": page, "url": url})
time.sleep(4)
fill = json.dumps(values)
eng = json.dumps(engines)
print(ev(page, f"""
window.__api = [];
const of = window.fetch;
window.fetch = async (...a) => {{ const r = await of(...a); try {{ const u = String(a[0]?.url || a[0]);
  if (u.includes('/api/')) r.clone().json().then(j => window.__api.push({{url: u, req: a[1]?.body || null, body: j}})).catch(() => {{}}); }} catch (e) {{}} return r; }};
const set = Object.getOwnPropertyDescriptor(HTMLInputElement.prototype, 'value').set;
const setT = Object.getOwnPropertyDescriptor(HTMLTextAreaElement.prototype, 'value').set;
const f = [...document.querySelectorAll('main form input[type=text], main form input[type=url], main form textarea')];
{fill}.forEach((v, i) => {{ (f[i].tagName === 'TEXTAREA' ? setT : set).call(f[i], v); f[i].dispatchEvent(new Event('input', {{bubbles: true}})); }});
const want = {eng};
if (want) [...document.querySelectorAll('main form button[type=button]')].forEach(b => {{
  const on = b.getAttribute('aria-pressed') === 'true';
  if (want.includes(b.innerText.trim()) !== !!on) b.click(); }});
return 'filled';
"""))
# submit in its own call: hidden neo tabs throttle page timers, so no setTimeout between fill and click
print(ev(page, "document.querySelector('main form button[type=submit]').click(); return 'submitted';"))
last, stable = 0, 0
deadline = time.time() + 360  # never hold the shared lock longer than this
for _ in range(90):
    time.sleep(2)
    if time.time() > deadline:
        sys.exit("TIMEOUT: no stable result within 6 minutes")
    st = ev(page, """const b = document.querySelector('main form button[type=submit]');
return {n: document.querySelector('main').innerText.length, busy: !b || b.disabled || /ing\\b/i.test(b.innerText), api: window.__api.length, rl: /quite a few tools/i.test(document.body.innerText)};""")
    if isinstance(st, dict) and st.get("rl"):
        last_run.write_text(str(time.time() + 300))  # limited: the next queued run waits 5 extra minutes
        sys.exit("RATE LIMITED: hyperank says too many tools in a short window; retry later")
    stable = stable + 1 if isinstance(st, dict) and st["n"] == last and not st["busy"] and st["api"] else 0
    last = st["n"] if isinstance(st, dict) else last
    if stable >= 2:
        break
res = ev(page, """const f = document.querySelector('main form'); const s = f.closest('section') || f.parentElement;
return {sec: s.outerHTML, text: document.querySelector('main').innerText, api: window.__api};""", 3000000)
if not isinstance(res, dict):  # truncated or wrapped: say so instead of crashing on res["api"]
    sys.exit("NO RESULT: final read was not JSON: " + str(res)[:300])
(out / "neo-api.json").write_text(json.dumps(res["api"], indent=1), encoding="utf-8")
# a hidden neo tab never runs the entrance animations: settle them to the visible state build.py expects
sec = re.sub(r"opacity:\s*0;\s*filter:\s*blur\(\d+px\);\s*transform:\s*translateY\(\d+px\);?", "opacity: 1; filter: blur(0px); transform: none;", res["sec"])
(out / "neo-result-sec.html").write_text(sec, encoding="utf-8")
(out / "neo-result-text.txt").write_text(res["text"], encoding="utf-8")
r = neo._post({"jsonrpc": "2.0", "id": 9, "method": "tools/call", "params": {"name": "screenshot", "arguments": {
    "agentName": neo.AGENT, "page": page, "format": "png", "fullPage": True, "size": {"width": 1440, "height": 900}}}})
for c in r.get("result", {}).get("content", []):
    if c.get("type") == "image":
        (out / "neo-result.png").write_bytes(base64.b64decode(c["data"]))
last_run.write_text(str(time.time()))
print("page", page, "chars", len(res["sec"]), "api", len(res["api"]))
