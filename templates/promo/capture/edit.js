(site) => {
  // the film's text rules, then the cut's own names (site: {"from": "to"}, applied in order, longest phrases first in the file)
  const MAP = [[' \u2014 ', ': '], [' \u2013 ', ', '], ['\u2014', ', ']].concat(Object.entries(site || {}));
  const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT); let n;
  while ((n = w.nextNode())) for (const [a, b] of MAP) n.nodeValue = n.nodeValue.split(a).join(b);
  // no mono labels: monospace and letter-spaced caps are set in sentence-case Inter; numbered section eyebrows go
  const st = document.createElement('style');
  st.textContent = '.font-mono,[class*="font-mono"],[class*="mono"]{font-family:inter,"inter Fallback",system-ui,sans-serif !important;letter-spacing:-0.005em !important;text-transform:none !important;font-weight:500 !important}' +
    '.uppercase{text-transform:none !important;letter-spacing:-0.005em !important}';
  document.head.appendChild(st);
  [...document.querySelectorAll('*')].filter(e => e.children.length < 3 && e.getBoundingClientRect().height < 40 && (/six engines/i.test(e.textContent) || /^\s*0\d\s*\/\s/.test(e.textContent))).forEach(e => {
    e.style.visibility = 'hidden'; const prev = e.previousElementSibling; if (prev && !prev.textContent.trim()) prev.style.visibility = 'hidden';
  });
  // no Grok, no Pricing link
  document.querySelectorAll('svg title').forEach(t => { if (/grok/i.test(t.textContent)) t.parentElement.style.display = 'none'; });
  document.querySelectorAll('img').forEach(i => { if (/grok/i.test(i.alt + i.src)) i.style.display = 'none'; });
  [...document.querySelectorAll('*')].filter(e => e.children.length === 0 && e.textContent.trim() === 'Grok').forEach(e => {
    let c = e; while (c.parentElement && !c.querySelector('svg,img')) c = c.parentElement; c.style.visibility = 'hidden';
  });
  document.querySelectorAll('a').forEach(a => { if (a.textContent.trim() === 'Pricing') a.style.display = 'none'; });
}
