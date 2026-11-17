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
        # H2 : {ancien: nouveau}, comparés sans balises ni différence d'apostrophe ; déjà remplacé = rien à faire.
        norm = lambda x: re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', x)).replace('’', "'").strip()
        for ancien, nouveau in s.get('h2', {}).items():
            h2s = list(re.finditer(r'<h2([^>]*)>((?:(?!</?h[1-6]).)*?)</h2>', b, re.S))
            if any(norm(h.group(2)) == norm(nouveau) for h in h2s):
                continue
            cibles = [h for h in h2s if norm(h.group(2)) == norm(ancien)]
            assert len(cibles) == 1, (url, ancien, len(cibles))
            h = cibles[0]
            b = b[:h.start()] + f'<h2{h.group(1)}>{nouveau}</h2>' + b[h.end():]
        b = sommaire(b)
        sit = s.get('situation')
        if sit and 'class="en-bref en-situation"' not in b:
            assert '</header>' in b, url
            i = b.index('</header>') + len('</header>')
            b = b[:i] + f'\n\n  <div class="en-bref en-situation">\n    <p class="surtitre">{sit["titre"]}</p>\n    <p>{sit["texte"]}</p>\n  </div>\n' + b[i:]
        open(tp, 'w', encoding='utf-8', newline='\n').write(t)
        open(bp, 'w', encoding='utf-8', newline='\n').write(b)
    return len(surcharges)


def sommaire(b):
    """Entrées de sommaire (<li><a href="#id">) alignées sur le texte du H2 qui porte cet id."""
    for h in re.finditer(r'<h2 id="([^"]+)"[^>]*>((?:(?!</?h[1-6]).)*?)</h2>', b, re.S):
        b = re.sub(r'(<li><a href="#' + re.escape(h.group(1)) + r'">)[^<]*(</a>)', lambda m: m.group(1) + h.group(2) + m.group(2), b)
    return b


if __name__ == '__main__':
    print(appliquer(), 'pages surchargées')
