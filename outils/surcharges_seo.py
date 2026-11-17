"""Applique outils/seo-surcharges.json (title, meta description, og, H1) aux pages de src/contenus.
Idempotent. Appelé à la fin de traduire.py, pour qu'une régénération des traductions garde le SEO,
et utilisable seul pour les pages écrites à la main : python outils/surcharges_seo.py"""
import html, json, os, re

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def appliquer():
    surcharges = json.load(open(os.path.join(RACINE, 'outils/seo-surcharges.json'), encoding='utf-8'))
    for url, s in surcharges.items():
        assert len(s['title']) <= 60 and len(s['description']) <= 155, url
        base = os.path.join(RACINE, 'src/contenus', url.strip('/').replace('.html', ''))
        tp, bp = base + '.tete.html', base + '.html'
        t, b = open(tp, encoding='utf-8').read(), open(bp, encoding='utf-8').read()
        e = lambda x: html.escape(x, quote=True)
        avant_d = html.unescape(re.search(r'<meta name="description" content="([^"]*)"', t).group(1))
        t = re.sub(r'<title>.*?</title>', lambda _: f'<title>{e(s["title"])}</title>', t, count=1)
        for prop, val in (('name="description"', s['description']), ('property="og:title"', s['title']), ('property="og:description"', s['description'])):
            t = re.sub(r'(<meta ' + prop + r' content=")[^"]*(")', lambda m: m.group(1) + e(val) + m.group(2), t, count=1)
        m = re.search(r'<h1([^>]*)>(.*?)</h1>', b, re.S)
        ancien_h1 = re.sub(r'<[^>]+>', '', m.group(2)).strip()
        b = b[:m.start()] + f'<h1{m.group(1)}>{s["h1"]}</h1>' + b[m.end():]
        b = b.replace(f'"headline": "{ancien_h1}"', f'"headline": "{s["h1"]}"').replace(f'"description": "{avant_d}"', f'"description": "{s["description"]}"')
        open(tp, 'w', encoding='utf-8', newline='\n').write(t)
        open(bp, 'w', encoding='utf-8', newline='\n').write(b)
    return len(surcharges)


if __name__ == '__main__':
    print(appliquer(), 'pages surchargées')
