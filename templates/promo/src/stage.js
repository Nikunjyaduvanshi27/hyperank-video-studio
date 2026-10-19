// v3 stage library, inlined into every scene sub-composition by build.py. All times are scene-local seconds and every
// helper writes onto the scene's one paused timeline. Layout is measured once while the timeline is built.
function Stage(ID, DATA) {
  const all = document.querySelectorAll('[data-composition-id="' + ID + '"]');
  const root = all[all.length - 1]; // the mounted template root, not the host slot
  const q = (s) => root.querySelector(s), qa = (s) => Array.from(root.querySelectorAll(s));
  const tl = gsap.timeline({ paused: true });
  const D = DATA.D;
  const norm = (s) => s.toLowerCase().replace(/[^a-z0-9%]/g, "");
  // time of the k-th spoken word matching `word` in line i (whisper word starts), or of the line start when not found
  const w = (i, word, k) => {
    const L = DATA.W[i] || [], n = norm(word);
    let hit = -1;
    for (const [x, t] of L) if (norm(x).startsWith(n) && (k = (k || 0) - 1) < 0) { hit = t; break; }
    if (hit < 0) console.warn(ID + ": word not found: " + word + " in line " + i);
    return DATA.B[i] + Math.max(0, hit);
  };
  qa(".scene *").forEach((n) => { n.setAttribute("data-layout-allow-occlusion", ""); n.setAttribute("data-layout-allow-overlap", ""); n.setAttribute("data-layout-allow-overflow", ""); });

  // ---------- supers: one line, words rise in; a super may land in segments, each on its own word ----------
  function super_(spec) {
    const d = document.createElement("div"); d.className = "super";
    const segs = spec.text.split(" / "), times = [].concat(spec.t);
    // word spacing is a margin, not a text node, so it survives however the template is mounted
    d.innerHTML = segs.map((s, j) => s.split(" ").map((x) => '<span class="w' + (x.includes("|") ? " v" : "") + '" data-seg="' + j + '">' + x.replace(/\|/g, "") + "</span>").join("")).join("");
    q(".supers").appendChild(d);
    segs.forEach((_, j) => tl.fromTo(d.querySelectorAll('[data-seg="' + j + '"]'), { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.6, ease: "power3.out", stagger: 0.06 }, times[Math.min(j, times.length - 1)]));
    if (spec.out != null) tl.to(d.querySelectorAll(".w"), { opacity: 0, y: -20, duration: 0.3, ease: "power2.in", stagger: 0.025 }, spec.out);
  }
  (DATA.supers || []).forEach(super_);

  // ---------- the composer: types at a human cadence, clears, sends ----------
  function Composer(el) {
    const caret = el.querySelector(".caret"), ph = el.querySelector(".ph");
    const sel = document.createElement("span"); sel.className = "sel"; el.querySelector(".txt").prepend(sel);
    const lines = Array.from(el.querySelectorAll(".q")).map((qq) => {
      const s = qq.textContent; qq.innerHTML = Array.from(s).map((c) => "<span>" + (c === " " ? "&nbsp;" : c) + "</span>").join("");
      const cs = Array.from(qq.children), x = cs.map((c) => c.offsetLeft + c.offsetWidth);
      return { s, cs, x };
    });
    gsap.set(caret, { x: 0 });
    const hash = (i) => { const v = Math.sin(i * 12.9898 + 78.233) * 43758.5453; return v - Math.floor(v); };
    return {
      el, lines,
      // reveal line n from t at about `cps` characters per second, with a typist's uneven rhythm; returns the end time
      type(t, n, cps) {
        const L = lines[n], g = 1 / (cps || 17);
        tl.set(ph, { opacity: 0 }, t);
        let at = t;
        L.cs.forEach((c, i) => {
          tl.set(c, { opacity: 1 }, at); tl.set(caret, { x: L.x[i] }, at);
          const ch = L.s[i];
          at += g * (0.62 + 0.76 * hash(i + n * 31)) * (ch === " " ? 1.5 : /[,?.]/.test(ch) ? 1.8 : 1);
        });
        return at;
      },
      shown(n) { lines[n].cs.forEach((c) => gsap.set(c, { opacity: 1 })); gsap.set(ph, { opacity: 0 }); gsap.set(caret, { x: lines[n].x[lines[n].x.length - 1] }); },
      // select all, then delete: a short highlight, then the line is gone
      clear(t, n) {
        const L = lines[n];
        gsap.set(sel, { width: L.x[L.x.length - 1] + 4 });
        tl.set(sel, { opacity: 1, width: L.x[L.x.length - 1] + 4 }, t);
        tl.set(L.cs.concat([sel]), { opacity: 0 }, t + 0.16);
        tl.set(caret, { x: 0 }, t + 0.16);
        return t + 0.2;
      },
      // the caret blinks (sharp on/off, 1.06 s period) between t0 and t1
      blink(t0, t1) { for (let t = t0; t < t1 - 0.53; t += 1.06) { tl.set(caret, { opacity: 0 }, t + 0.53); tl.set(caret, { opacity: 1 }, Math.min(t + 1.06, t1)); } },
      caret(t, v) { tl.set(caret, { opacity: v }, t); },
      send(t) {
        const b = el.querySelector(".send");
        tl.to(b, { scale: 0.86, duration: 0.09, ease: "power2.out" }, t);
        tl.to(b, { scale: 1, duration: 0.4, ease: "back.out(1.2)" }, t + 0.09);
        tl.fromTo(b, { boxShadow: "0 0 0 0 rgba(94,75,246,0.5)" }, { boxShadow: "0 0 0 22px rgba(94,75,246,0)", duration: 0.7, ease: "power2.out", immediateRender: false }, t + 0.05);
      },
    };
  }

  // ---------- the answer card ----------
  function Card(el) {
    const rows = Array.from(el.querySelectorAll(".row"));
    const lines = [el.querySelector(".intro")].concat(rows);
    lines.forEach((l) => l.classList.add("mline"));
    const api = {
      el, rows, chips: rows.map((r) => r.querySelector(".chip")).filter(Boolean), names: rows.map((r) => r.querySelector(".nmv")),
      full() { gsap.set(lines, { "--m": 0 }); },
      hide() { gsap.set(lines, { "--m": 100 }); gsap.set(el.querySelector(".hd"), { opacity: 0 }); },
      // header settles, then the intro streams behind its mask; returns when the intro has landed
      stream(t, dur) {
        tl.fromTo(el.querySelector(".hd"), { opacity: 0, y: 10 }, { opacity: 1, y: 0, duration: 0.6, ease: "power3.out", immediateRender: false }, t);
        tl.fromTo(lines[0], { "--m": 100 }, { "--m": 0, duration: dur || 1.1, ease: "sine.inOut", immediateRender: false }, t + 0.18);
        return t + 0.18 + (dur || 1.1);
      },
      // one row streams: the mask runs left to right while the row rises a few pixels and settles
      row(t, i, dur) {
        tl.fromTo(rows[i], { "--m": 100 }, { "--m": 0, duration: dur || 0.75, ease: "sine.out", immediateRender: false }, t);
        tl.fromTo(rows[i], { y: 14 }, { y: 0, duration: 0.8, ease: "back.out(1.2)", immediateRender: false }, t);
      },
      // a blurred name glows violet for a beat ("is it you?")
      pulse(t, i) {
        const n = api.names[i];
        tl.to(n, { color: "#5e4bf6", textShadow: "0 0 22px rgba(94,75,246,0.7)", duration: 0.35, ease: "power2.out" }, t);
        tl.to(n, { color: "#17161c", textShadow: "0 0 0 rgba(94,75,246,0)", duration: 0.7, ease: "power2.inOut" }, t + 0.55);
      },
      // a slow focus pull: the names resolve
      unblur(t, dur) { tl.to(api.names, { filter: "blur(0px)", duration: dur || 0.9, ease: "power2.inOut", stagger: 0.12 }, t); },
    };
    return api;
  }

  // ---------- depth stage camera: CSS variables on .world, read by every layer ----------
  const world = q(".world");
  function camTo(t, v, dur, ease) { const o = { duration: dur == null ? 1 : dur, ease: ease || "sine.inOut" }; for (const k in v) o["--" + k] = v[k]; tl.to(world, o, t); }
  function lay(el, t, v, dur, ease) { const o = { duration: dur == null ? 0.8 : dur, ease: ease || "power3.out" }; for (const k in v) o["--" + k] = v[k]; tl.to(el, o, t); }
  function place(el, v) { const o = {}; for (const k in v) o["--" + k] = v[k]; gsap.set(el, o); }

  // ---------- laptop rig ----------
  const SCREEN = { x: 160, y: 22, w: 1440, h: 900 };
  const fr = (s, cx, cy) => ({ s, x: cx - s * 880, y: cy - s * 490 });
  const FR = { RISE: fr(0.72, 960, 596), HOLD: fr(0.77, 960, 578), NEAR: fr(0.82, 960, 560), WIDE: fr(0.56, 960, 590), FAR: fr(0.46, 960, 690), LOW: fr(0.8, 960, 1700) };
  const cam = q(".cam"), lap = q(".laptop"), drift = q(".drift");
  let camF = FR[DATA.cam0 || "HOLD"];
  if (cam) gsap.set(cam, { x: camF.x, y: camF.y, scale: camF.s, force3D: false });
  // a slow continuous camera move, a pure function of film time, so it carries across hard cuts between scenes
  if (drift) {
    const f = (T) => ({ x: 14 * Math.sin(T / 6.1), y: 7 * Math.sin(T / 4.7 + 1.3), scale: 1.018 + 0.016 * Math.sin(T / 8.3 + 0.4) });
    gsap.set(drift, f(DATA.T0));
    const ks = []; for (let t = 0.5; t < D + 0.5; t += 0.5) ks.push({ ...f(DATA.T0 + Math.min(t, D)), duration: Math.min(0.5, D - t + 0.5), ease: "none" });
    tl.to(drift, { keyframes: ks }, 0);
  }
  const view = (f, r) => ({ x: f.x + f.s * r.x, y: f.y + f.s * r.y, w: f.s * r.w, h: f.s * r.h });
  // a rect in page css px (1440 x 900 screen) -> world (laptop) px
  const world_ = (r) => ({ x: SCREEN.x + r.x, y: SCREEN.y + r.y, w: r.w, h: r.h });
  function frameRect(r, cap, cy, pad) {
    const p = pad == null ? 70 : pad, rr = { x: r.x - p, y: r.y - p * 0.6, w: r.w + 2 * p, h: r.h + 1.2 * p };
    const s = Math.min(cap || 1.6, 1920 / rr.w, 700 / rr.h);
    return { s, x: 960 - s * (rr.x + rr.w / 2), y: (cy || 580) - s * (rr.y + rr.h / 2) };
  }
  let zTop = 1;
  qa(".pg").forEach((pg, i) => { if (i > 0) gsap.set(pg, { clipPath: "inset(100% 0% 0% 0%)" }); });  // later pages wait below the screen until wiped in
  const api = {
    tl, root, q, qa, D, B: DATA.B, E: DATA.E, C: DATA.C || {}, w, at: (i, f) => DATA.B[i] + f * (DATA.E[i] - DATA.B[i]), FR, Composer, Card,
    camTo, lay, place, view, world: world_, get camF() { return camF; },
    // a push-in brings up a soft veil under the super, so the line never sits on the screen's own chrome
    cam(t, spec, dur, ease) {
      const f = typeof spec === "string" ? FR[spec] : frameRect(world_(spec.r), spec.cap, spec.cy, spec.pad), d = dur == null ? 1 : dur;
      tl.to(cam, { x: f.x, y: f.y, scale: f.s, duration: d, ease: ease || "power2.inOut", force3D: false }, t); camF = f;
      tl.to(qa(".veilT, .veilB"), { opacity: typeof spec === "string" ? 0 : 1, duration: Math.min(d, 0.8), ease: "power2.inOut" }, t);  // and a scrim under the captions
      return f;
    },
    // depth of field on the laptop world while something in front holds focus
    dof(t, px, dur) { tl.to(drift, { filter: "blur(" + px + "px)", duration: dur == null ? 0.6 : dur, ease: "power2.inOut" }, t); },
    dim(t, v, dur) { tl.to(q(".dim"), { opacity: v, duration: dur || 0.45, ease: "power2.inOut" }, t); },
    // the laptop rises from below the frame, tilted back, and settles flat
    rise(t, dur) {
      const d = dur || 1.1;
      tl.fromTo(lap, { y: 1220 }, { y: 0, duration: d, ease: "expo.out", immediateRender: true }, t);
      tl.fromTo(lap, { rotationX: 24, transformPerspective: 2400 }, { keyframes: [{ rotationX: -1.1, duration: d * 0.72, ease: "power3.out" }, { rotationX: 0, duration: d * 0.6, ease: "sine.inOut" }], immediateRender: true }, t);
    },
    streak(t, dur) { const s = q(".streak"); tl.fromTo(s, { x: -420, opacity: 0 }, { x: 1700, opacity: 1, duration: dur || 1.6, ease: "power1.inOut", immediateRender: false }, t); tl.to(s, { opacity: 0, duration: 0.25 }, t + (dur || 1.6)); },
    // a screen swap: the new page wipes up inside the screen (never two UIs cross-faded)
    page(t, k, dur) {
      const np = q('.pg[data-page="' + k + '"]'); zTop += 1; gsap.set(np, { zIndex: zTop });
      tl.fromTo(np, { clipPath: "inset(100% 0% 0% 0%)" }, { clipPath: "inset(0% 0% 0% 0%)", duration: dur || 0.6, ease: "power3.inOut", immediateRender: false }, t);
    },
    // an image crop lifts out of the screen: from its page rect (css px) to view space, tilted, with a real shadow
    // (the element is laid out at its final size and grows to scale 1, so text rasterizes crisp where it rests)
    lift(t0, el, from, to, o) {
      o = o || {};
      const r0 = view(camF, world_(from)), k1 = to.w / from.w, h1 = from.h * k1;
      const x1 = to.cx - to.w / 2, y1 = to.cy - h1 / 2;
      gsap.set(el, { x: r0.x, y: r0.y, width: to.w, height: h1, scale: r0.w / to.w, transformPerspective: 1600, rotationX: 0, opacity: 0 });
      tl.set(el, { opacity: 1 }, t0);
      tl.fromTo(el, { rotationX: 0 }, { rotationX: o.tilt == null ? 10 : o.tilt, duration: 0.4, ease: "power2.out", immediateRender: false }, t0);
      tl.to(el, { rotationX: o.rest == null ? 4 : o.rest, duration: 0.8, ease: "power3.out" }, t0 + 0.4);
      tl.to(el, { x: x1, y: y1, scale: 1, duration: o.dur || 0.95, ease: "back.out(1.15)" }, t0);
      return { x: x1, y: y1, w: to.w, h: h1, k: k1 };
    },
    // a lift settles back into the screen where it came from, then hands over to the page underneath
    drop(t, el, from, dur) {
      const r0 = view(camF, world_(from)), d = dur || 0.6;
      tl.to(el, { x: r0.x, y: r0.y, scale: r0.w / el.offsetWidth, rotationX: 0, duration: d, ease: "power2.inOut" }, t);
      tl.set(el, { opacity: 0 }, t + d);
    },
    // a view-space element arrives: rises a little, settles with a slight overshoot
    arrive(t, el, o) { o = o || {}; tl.fromTo(el, { opacity: 0, y: o.y == null ? 36 : o.y, scale: o.s || 0.97 }, { opacity: 1, y: 0, scale: 1, duration: o.dur || 0.85, ease: "back.out(1.2)", immediateRender: true }, t); },
    leave(t, el, o) { o = o || {}; tl.to(el, { opacity: 0, y: o.y == null ? -24 : o.y, scale: o.s || 0.97, filter: "blur(6px)", duration: o.dur || 0.45, ease: "power2.in" }, t); },
    done() { tl.set({}, {}, D); window.__timelines[ID] = tl; },
  };
  return api;
}
