() => {
  const norm = (s) => s.replace(/\s+/g, ' ').trim();
  const out = [];
  for (const head of ['Every answer, kept word for word', 'Make the sources you are missing', 'The traffic AI sends you, separated from the traffic it does not', 'Nothing here asks you to move your stack']) {
    const h = [...document.querySelectorAll('h1,h2,h3')].find(e => norm(e.textContent).startsWith(head.slice(0, 20)));
    if (!h) { out.push('MISS ' + head); continue; }
    let s = h; for (let i = 0; i < 6; i++) { s = s.parentElement; if (s.getBoundingClientRect().width > 1000) break; }
    const w = document.createTreeWalker(s, NodeFilter.SHOW_TEXT); let n; const t = [];
    while ((n = w.nextNode())) { const v = norm(n.nodeValue); if (v) t.push(v); }
    out.push('=== ' + head + ' :: ' + t.join(' | '));
  }
  return out.join(String.fromCharCode(10));
}
