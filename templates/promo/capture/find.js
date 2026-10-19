([op, arg]) => {
  const norm = (s) => s.replace(/\s+/g, ' ').trim();
  const leaf = (t) => [...document.querySelectorAll('*')].find(e => e.children.length < 3 && norm(e.textContent) === t);
  const R = (r, o) => ({ x: +(r.x - (o ? o.x : 0)).toFixed(1), y: +(r.y - (o ? o.y : 0)).toFixed(1), w: +r.width.toFixed(1), h: +r.height.toFixed(1) });
  const chipEl = (name) => { let c = [...document.querySelectorAll('*')].find(e => e.children.length === 0 && e.textContent.trim() === name && e.getBoundingClientRect().y < 900); while (c.parentElement && !c.querySelector('svg,img')) c = c.parentElement; return c; };
  const card = (t) => { let c = leaf(t); for (let i = 0; i < 8; i++) { c = c.parentElement; if (c.getBoundingClientRect().width > 400 && getComputedStyle(c).borderTopWidth !== '0px') break; } return c; };
  if (op === 'chips') return Object.fromEntries(['ChatGPT', 'Claude'].map(n => { const g = chipEl(n), pill = [...g.querySelectorAll('div')].find(d => /rounded-\[13px\]/.test(d.className)); return [n, { group: R(g.getBoundingClientRect()), pill: R(pill.getBoundingClientRect()) }]; }));
  if (op === 'chipEl') return chipEl(arg);
  if (op === 'chipYou') { const g = chipEl(arg); [...g.querySelectorAll('span')].forEach(s => { if (s.children.length === 0 && /^Recommends/.test(s.textContent.trim())) s.textContent = 'Recommends you'; }); return true; }
  if (op === 'scrollTo') { let s = [...document.querySelectorAll('h1,h2,h3,h4,p,div,span')].filter(e => norm(e.textContent) === arg).pop(); for (let i = 0; i < 8; i++) { s = s.parentElement; if (s.getBoundingClientRect().width > 1000 && getComputedStyle(s).borderTopWidth !== '0px') break; } document.documentElement.style.scrollBehavior = 'auto'; window.scrollTo({ top: Math.round(s.getBoundingClientRect().top + scrollY - 38), behavior: 'instant' }); return scrollY; }
  if (op === 'isolate') { // only this element paints, on a transparent page: its glass and shadow keep their alpha (opacity, not visibility, so shared SVG masks still resolve)
    const el = arg === 'table' ? card('Sources deciding the answer') : chipEl(arg);
    el.scrollIntoView({ block: 'center', behavior: 'instant' });
    for (let a = el; a.parentElement; a = a.parentElement) {
      [...a.parentElement.children].forEach(x => { if (x !== a && x.tagName !== 'STYLE' && x.tagName !== 'SCRIPT') x.style.opacity = '0'; });
      Object.assign(a.parentElement.style, { background: 'transparent', boxShadow: 'none', borderColor: 'transparent' });
    }
    return R(el.getBoundingClientRect());
  }
  // a card found by a text inside it: the nearest ancestor at least minw wide with a border or a shadow
  if (op === 'mark') { const [t, minw] = arg; let c = leaf(t) || [...document.querySelectorAll('*')].find(e => e.children.length < 4 && norm(e.textContent).startsWith(t));
    for (let i = 0; i < 9 && c.parentElement; i++) { const r = c.getBoundingClientRect(), cs = getComputedStyle(c); if (r.width >= minw && r.height > 60 && (cs.borderTopWidth !== '0px' || cs.boxShadow !== 'none')) break; c = c.parentElement; }
    document.querySelectorAll('[data-pick]').forEach(e => e.removeAttribute('data-pick')); c.setAttribute('data-pick', ''); c.scrollIntoView({ block: 'center', behavior: 'instant' }); return R(c.getBoundingClientRect()); }
  if (op === 'isolatePicked') { const el = document.querySelector('[data-pick]');
    for (let a = el; a.parentElement; a = a.parentElement) {
      [...a.parentElement.children].forEach(x => { if (x !== a && x.tagName !== 'STYLE' && x.tagName !== 'SCRIPT') x.style.opacity = '0'; });
      Object.assign(a.parentElement.style, { background: 'transparent', boxShadow: 'none', borderColor: 'transparent' });
    }
    return R(el.getBoundingClientRect()); }
  // rects of named parts inside the picked card (relative to it): texts given as an array
  if (op === 'partsOf') { const el = document.querySelector('[data-pick]'), o = el.getBoundingClientRect();
    return arg.map(t => { const e = [...el.querySelectorAll('*')].find(x => x.children.length < 3 && norm(x.textContent) === t); return e ? R(e.getBoundingClientRect(), o) : null; }); }
  if (op === 'scrollHead') { const h = [...document.querySelectorAll('h1,h2,h3')].find(e => norm(e.textContent).startsWith(arg)); let s = h;
    for (let i = 0; i < 8; i++) { s = s.parentElement; if (s.getBoundingClientRect().width > 1000 && getComputedStyle(s).borderTopWidth !== '0px') break; }
    document.documentElement.style.scrollBehavior = 'auto'; window.scrollTo({ top: Math.round(s.getBoundingClientRect().top + scrollY - 38), behavior: 'instant' }); return scrollY; }
  if (op === 'icons') return [...card(arg).querySelectorAll('li')].map(li => [...li.querySelectorAll('svg title')].filter(t => getComputedStyle(t.parentElement).display !== 'none').map(t => t.textContent).join(', '));
  if (op === 'box') return R(card(arg).getBoundingClientRect());
  if (op === 'card') return card(arg);
  if (op === 'parts') {
    const c = card(arg), o = c.getBoundingClientRect();
    const rows = [...c.querySelectorAll('li')].map(li => {
      const ps = li.querySelectorAll('p'), sub = ps[1], tn = sub.firstChild, i = tn.nodeValue.indexOf('also wins');
      const rg = document.createRange(); rg.setStart(tn, i); rg.setEnd(tn, tn.nodeValue.length);
      const add = [...li.querySelectorAll('button,a,span,div')].filter(e => /Add$/.test(e.textContent.trim()) && e.getBoundingClientRect().height > 20).sort((a, b) => a.getBoundingClientRect().width - b.getBoundingClientRect().width)[0];
      return { row: R(li.getBoundingClientRect(), o), domain: R(ps[0].getBoundingClientRect(), o), domainText: ps[0].textContent.trim(), sub: R(sub.getBoundingClientRect(), o), wins: R(rg.getBoundingClientRect(), o), winsText: tn.nodeValue.slice(i), add: R(add.getBoundingClientRect(), o) };
    });
    return { card: R(o), header: R(c.querySelector('p').getBoundingClientRect(), o), rows };
  }
}
