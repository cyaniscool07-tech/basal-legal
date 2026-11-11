"""Assemble les versions en/es/de d'une page à partir de la page française (site Astro, src/).

Chaque traduction vit dans outils/traductions/<cle>.py : PAGES = {lang: {...}}, avec
  slug      adresse de la page traduite (ex. '/en/macro-calculator.html')
  tete      dict(title, description, og_title, og_description, locale, og_type)
  main      le <main> traduit (HTML complet)
  script    liste de (texte français, traduction) appliquée aux <script> non JSON-LD, si la page en a
  ld        liste de dicts JSON-LD (fil d'Ariane compris)
Le script : écrit src/contenus/<lang>/<fichier>.html et .tete.html, src/pages/<slug>.astro, ajoute les
hreflang réciproques à la page française et aux traductions, met à jour public/sitemap.xml.
Usage : python outils/traduire.py <cle> [<cle>…]   (depuis la racine du dépôt basal-legal)
Traductions NON VÉRIFIÉES par un locuteur natif.
"""
import importlib.util, json, os, re, sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RACINE, 'outils', 'traductions'))
SITE = 'https://basal-app.fr'
LANGS = ['en', 'es', 'de']


def lire(p):
    return open(os.path.join(RACINE, p), encoding='utf-8').read()


def ecrire(p, s):
    p = os.path.join(RACINE, p)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8', newline='\n').write(s)


def esc(s):
    return s.replace('&', '&amp;').replace('"', '&quot;').replace('<', '&lt;')


def alternates(urls):
    return '\n'.join(f'<link rel="alternate" hreflang="{l}" href="{SITE}{u}">' for l, u in urls.items()) + f'\n<link rel="alternate" hreflang="x-default" href="{SITE}{urls["fr"]}">'


def avec_hreflang(tete, urls):
    tete = re.sub(r'<link rel="alternate" hreflang="[^"]+" href="[^"]+">\n?', '', tete)
    return re.sub(r'(<link rel="canonical" href="[^"]+">)', lambda m: m.group(1) + '\n' + alternates(urls), tete, count=1)


def traiter(cle):
    spec = importlib.util.spec_from_file_location(cle, os.path.join(RACINE, 'outils/traductions', f'{cle}.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    fr_path = mod.FR  # ex. '/calcul-macros.html'
    fr_nom = 'index' if fr_path.endswith('/') else fr_path.strip('/').rsplit('/', 1)[-1].replace('.html', '')
    fr_dossier = fr_path.strip('/').rsplit('/', 1)[0] if fr_path.strip('/').count('/') or fr_path.endswith('/') else ''
    fr_base = f'src/contenus/{fr_dossier + "/" if fr_dossier else ""}{fr_nom}'
    corps_fr = lire(fr_base + '.html')
    existants = getattr(mod, 'EXISTANTS', {})  # traductions déjà écrites à la main : reliées, pas réécrites
    urls = {'fr': fr_path, **{l: existants.get(l) or mod.PAGES[l]['slug'] for l in LANGS if l in mod.PAGES or l in existants}}
    for l, u in existants.items():
        rel = u.lstrip('/')
        base_e = f'src/contenus/{rel.rstrip("/") + "/index" if rel.endswith("/") else rel.replace(".html", "")}'
        ecrire(base_e + '.tete.html', avec_hreflang(lire(base_e + '.tete.html'), urls))
    # Page française : hreflang vers les traductions.
    ecrire(fr_base + '.tete.html', avec_hreflang(lire(fr_base + '.tete.html'), urls))
    scripts = re.findall(r'(?s)<script>.*?</script>', corps_fr)
    for l, p in mod.PAGES.items():
        t = p['tete']
        tete = f'''<title>{t["title"]}</title>
<meta name="description" content="{esc(t["description"])}">
<link rel="canonical" href="{SITE}{p["slug"]}">
<meta property="og:title" content="{esc(t["og_title"])}">
<meta property="og:description" content="{esc(t["og_description"])}">
<meta property="og:type" content="{t.get("og_type", "website")}">
<meta property="og:url" content="{SITE}{p["slug"]}">
<meta property="og:image" content="{SITE}/img/og-en.png">
<meta property="og:locale" content="{t["locale"]}">
'''
        tete = avec_hreflang(tete, urls)
        js = ''
        for s in scripts:
            for a, b in p.get('script', []):
                if a not in s:
                    raise SystemExit(f'{cle}/{l} : texte absent du script : {a[:60]}')
                s = s.replace(a, b)
            js += s + '\n'
        ld = ''.join(f'\n<script type="application/ld+json">\n{json.dumps(x, ensure_ascii=False, indent=2)}\n</script>\n' for x in p.get('ld', []))
        corps = p['main'].strip() + '\n\n' + js + ld
        rel = p['slug'].lstrip('/')
        nom = 'index' if rel.endswith('/') else rel.rsplit('/', 1)[-1].replace('.html', '')
        dossier = rel.rstrip('/') if rel.endswith('/') else rel.rsplit('/', 1)[0]
        base = f'src/contenus/{dossier}/{nom}'
        ecrire(base + '.tete.html', tete)
        ecrire(base + '.html', corps)
        profondeur = '../' * (dossier.count('/') + 2)
        ecrire(f'src/pages/{dossier}/{nom}.astro', f"""---
import Base from '{profondeur}layouts/Base.astro';
import tete from '{profondeur}contenus/{dossier}/{nom}.tete.html?raw';
import corps from '{profondeur}contenus/{dossier}/{nom}.html?raw';
---
<Base lang="{l}" tete={{tete}} corps={{corps}} />
""")
    # Sitemap : une entrée par version, chacune avec ses alternatives.
    sm = lire('public/sitemap.xml')
    alt = ''.join(f'<xhtml:link rel="alternate" hreflang="{l}" href="{SITE}{u}"/>' for l, u in urls.items()) + f'<xhtml:link rel="alternate" hreflang="x-default" href="{SITE}{urls["fr"]}"/>'
    for l, u in urls.items():
        loc = f'{SITE}{u}'
        sm = re.sub(r'\s*<url>\s*<loc>' + re.escape(loc) + r'</loc>.*?</url>', '', sm, flags=re.S)
        sm = sm.replace('  <!-- recettes:debut -->', f'  <url><loc>{loc}</loc><lastmod>{mod.DATE}</lastmod><priority>0.8</priority>{alt}</url>\n  <!-- recettes:debut -->', 1)
    ecrire('public/sitemap.xml', sm)
    print(cle, '→', ', '.join(f'{l}:{u}' for l, u in urls.items()))


if __name__ == '__main__':
    for c in sys.argv[1:]:
        traiter(c)
