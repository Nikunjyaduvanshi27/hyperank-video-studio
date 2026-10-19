"""Minimal BrowserOS neo MCP client (HTTP), for logged-in captures of gated tool results.

    python neo.py tools                      # list tool names
    python neo.py call <tool> '<json args>'  # call one tool, print the text result
"""
import json, sys, urllib.error, urllib.request
from pathlib import Path

URL = "http://127.0.0.1:9010/mcp"
AGENT = "claude-code-videos"
SID_FILE = Path(__file__).with_name(".neo-session")  # one session across invocations keeps tab ownership
_sid = SID_FILE.read_text().strip() if SID_FILE.exists() else None


def _post(msg: dict) -> dict:
    global _sid
    h = {"Content-Type": "application/json", "Accept": "application/json, text/event-stream"}
    if _sid:
        h["mcp-session-id"] = _sid
    req = urllib.request.Request(URL, json.dumps(msg).encode(), h)
    with urllib.request.urlopen(req, timeout=150) as r:
        _sid = r.headers.get("mcp-session-id") or _sid
        body = r.read().decode("utf-8")
    for line in body.splitlines():  # SSE: the last data line carrying our id is the answer
        if line.startswith("data:") and '"id"' in line:
            return json.loads(line[5:])
    return json.loads(body) if body.strip().startswith("{") else {}


def init() -> None:
    global _sid
    if _sid:
        return
    _post({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {
        "protocolVersion": "2025-06-18", "capabilities": {}, "clientInfo": {"name": AGENT, "version": "1"}}})
    _post({"jsonrpc": "2.0", "method": "notifications/initialized"})
    SID_FILE.write_text(_sid or "")


def call(tool: str, args: dict) -> str:
    args = {"agentName": AGENT, **args}
    try:
        r = _post({"jsonrpc": "2.0", "id": 2, "method": "tools/call", "params": {"name": tool, "arguments": args}})
    except urllib.error.HTTPError as e:  # 404 = the shared session id expired: start a new session below
        if e.code != 404:
            raise
        r = {"error": "session expired"}
    if "error" in r and "session" in str(r["error"]).lower():
        global _sid
        _sid = None
        SID_FILE.unlink(missing_ok=True)
        init()
        r = _post({"jsonrpc": "2.0", "id": 2, "method": "tools/call", "params": {"name": tool, "arguments": args}})
    if "error" in r:
        raise RuntimeError(r["error"])
    return "\n".join(c.get("text", "") for c in r["result"].get("content", []))


if __name__ == "__main__":
    init()
    if sys.argv[1] == "tools":
        r = _post({"jsonrpc": "2.0", "id": 3, "method": "tools/list"})
        for t in r["result"]["tools"]:
            print(t["name"], "|", t.get("description", "")[:140].replace("\n", " "))
    else:
        print(call(sys.argv[2], json.loads(sys.argv[3]) if len(sys.argv) > 3 else {}))
