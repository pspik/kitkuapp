import json, os, screens
from playwright.sync_api import sync_playwright
HERE = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(HERE, '../../podrecznik/img'); os.makedirs(out, exist_ok=True)
meta = []
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
    pg = b.new_page(viewport={'width': 390, 'height': 844}, device_scale_factor=2)
    for slug, title, intro, html, steps in screens.S:
        os.makedirs('/tmp/podr-screens', exist_ok=True); f = f'/tmp/podr-screens/{slug}.html'; open(f, 'w').write(html)
        pg.set_viewport_size({'width': 390, 'height': 844})
        pg.goto('file://' + os.path.abspath(f)); pg.wait_for_timeout(150)
        h = max(844, pg.evaluate('document.documentElement.scrollHeight'))
        pg.set_viewport_size({'width': 390, 'height': h})
        taps = pg.evaluate('''() => [...document.querySelectorAll('[data-tap]')].map(e => { const r = e.getBoundingClientRect(); return [ +e.dataset.tap, Math.max(14, r.left + 4), Math.max(14, r.top + 4) ]; })''')
        pg.screenshot(path=f'{out}/{slug}.jpg', type='jpeg', quality=82, full_page=True)
        meta.append({'slug': slug, 'title': title, 'intro': intro, 'h': h, 'taps': {str(n): [round(x / 390 * 100, 2), round(y / h * 100, 2)] for n, x, y in taps}, 'steps': steps})
    b.close()
json.dump(meta, open(os.path.join(HERE, 'meta.json'), 'w'), ensure_ascii=False, indent=1)
print([(m['slug'], m['h'], len(m['taps']), len(m['steps'])) for m in meta])
