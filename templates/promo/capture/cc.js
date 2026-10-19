(cc) => {
  // names, then whole phrases, across every text node
  const MAP = Object.entries(cc.names).concat(Object.entries(cc.text));
  const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT); let n;
  while ((n = w.nextNode())) for (const [a, b] of MAP) n.nodeValue = n.nodeValue.split(a).join(b);
  const q = (s) => document.querySelector(s), qa = (s) => Array.from(document.querySelectorAll(s));
  // the brand avatar in the shell
  qa('span').forEach((s) => { if (s.children.length === 0 && s.textContent.trim() === 'L' && /background/.test(s.getAttribute('style') || '')) { s.textContent = 'Y'; s.style.background = '#5e4bf6'; } });
  // no engine counts on screen
  qa('.cc-strip a').forEach((a) => { if (/^Engines/.test(a.textContent.trim())) a.style.display = 'none'; });
  qa('*').forEach((e) => { if (e.children.length < 3 && /^Engines sending/.test(e.textContent.trim())) { let c = e; while (c.parentElement && c.getBoundingClientRect().width < 120) c = c.parentElement; c.style.visibility = 'hidden'; } });
  // headline numbers for a brand AI rarely names
  const hero = q('[data-m="hero"]');
  if (hero) { hero.querySelector('.ccx-hero-v b').textContent = cc.named + '%'; const up = hero.querySelector('.ccx-up'); if (up) up.textContent = '▲ 1 pt'; }
  const kpi = q('[data-m="kpi-sov"]');
  if (kpi) { kpi.querySelector('.ckt-v b').textContent = cc.sov[0][1] + '%'; const up = kpi.querySelector('.ccx-up'); if (up) up.textContent = '▲ 1 pt'; }
  qa('svg text').forEach((t) => { if (/^\d+% you$/.test(t.textContent.trim())) t.textContent = cc.named + '% you'; });
  // mentions by brand: one bar per brand, scaled to the largest
  const sov = q('[data-m="sov"] svg');
  if (sov) {
    const max = Math.max(...cc.sov.map((r) => r[1]));
    sov.innerHTML = cc.sov.map(([name, v], i) => {
      const y = 15 + i * 30, wd = (v / max) * 370, on = i === 0 ? ' is-on' : '';
      return '<text x="0" y="' + y + '" dominant-baseline="central" class="ccx-ax' + on + '">' + name + '</text>' +
        '<path d="M132 ' + (y - 8) + ' H' + (128 + wd).toFixed(1) + ' a4 4 0 0 1 4 4 V' + (y + 4) + ' a4 4 0 0 1 -4 4 H132 Z" fill="' + (i === 0 ? '#5e4bf6' : '#c9c4b6') + '"/>' +
        '<text x="' + (144 + wd).toFixed(1) + '" y="' + y + '" dominant-baseline="central" class="ccx-val' + on + '">' + v + '%</text>';
    }).join('');
  }
  // who each engine names: the first column is the tracked brand
  qa('.ccx-hm-r').forEach((r, i) => { const c = r.nextElementSibling; if (c && cc.you[i] != null) { c.textContent = cc.you[i]; c.style.background = '#e4e0fd'; c.style.color = '#1f1e1b'; } });
  // no mono: app subtitles and footnotes in Inter; the brand bars centred in their plot
  qa('*').forEach((e) => { const cs = getComputedStyle(e); if (/mono/i.test(cs.fontFamily)) { e.style.fontFamily = '"__Inter_f367f3", Inter, sans-serif'; e.style.letterSpacing = '-0.005em'; } });
  const plot = q('[data-m="sov"] .ccx-plot'); if (plot) { plot.style.display = 'flex'; plot.style.alignItems = 'center'; }
  if (sov) { sov.style.width = '100%'; sov.style.height = 'auto'; const card = q('[data-m="sov"]'); card.style.height = 'auto'; card.style.alignSelf = 'start'; if (plot) { plot.style.display = 'block'; plot.style.flex = 'none'; plot.style.height = 'auto'; } }
  // the laptop shows the "What changed" zone
  const sc = q('.scroller'), z = q('[data-m="changed"]');
  const top = (z.getBoundingClientRect().top - sc.getBoundingClientRect().top) / 1.125;
  sc.style.transform = 'scale(1.125) translateY(' + (-(top - 34)) + 'px)';
  const r = q('[data-m="sov"]').getBoundingClientRect(), k = q('[data-m="kpi-sov"]').getBoundingClientRect();
  return { sov: { x: r.x, y: r.y, w: r.width, h: r.height }, kpi: { x: k.x, y: k.y, w: k.width, h: k.height } };
}
