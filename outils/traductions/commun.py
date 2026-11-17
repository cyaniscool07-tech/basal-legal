"""Gabarit et adresses communs aux guides traduits (voir outils/traduire.py)."""

# Adresse de chaque page dans chaque langue : une seule table pour les liens entre articles.
U = {
    'accueil': {'en': '/en/', 'es': '/es/', 'de': '/de/'},
    'guides': {'en': '/en/guides/', 'es': '/es/guias/', 'de': '/de/ratgeber/'},
    'recettes': {'en': '/en/recipes/', 'es': '/es/recetas/', 'de': '/de/rezepte/'},
    'calculateurs': {'en': '/en/calculators/', 'es': '/es/calculadoras/', 'de': '/de/rechner/'},
    'tdee': {'en': '/en/calorie-calculator.html', 'es': '/es/calculadora-calorias.html', 'de': '/de/kalorienrechner.html'},
    'macros': {'en': '/en/macro-calculator.html', 'es': '/es/calculadora-macros.html', 'de': '/de/makrorechner.html'},
    'calc-proteines': {'en': '/en/protein-calculator.html', 'es': '/es/calculadora-proteinas.html', 'de': '/de/proteinrechner.html'},
    '1rm': {'en': '/en/one-rep-max-calculator.html', 'es': '/es/calculadora-1rm.html', 'de': '/de/1rm-rechner.html'},
    'depense-reelle': {'en': '/en/real-expenditure-calculator.html', 'es': '/es/gasto-real.html', 'de': '/de/tatsaechlicher-verbrauch.html'},
    'metabolisme-de-base': {'en': '/en/basal-metabolic-rate.html', 'es': '/es/metabolismo-basal.html', 'de': '/de/grundumsatz.html'},
    'metabolisme-adaptatif': {'en': '/en/adaptive-metabolism.html', 'es': '/es/metabolismo-adaptativo.html', 'de': '/de/metabolische-anpassung.html'},
    'deficit': {'en': '/en/calorie-deficit.html', 'es': '/es/deficit-calorico.html', 'de': '/de/kaloriendefizit.html'},
    'combien': {'en': '/en/how-many-calories-per-day.html', 'es': '/es/cuantas-calorias-al-dia.html', 'de': '/de/wie-viele-kalorien-am-tag.html'},
    'proteines': {'en': '/en/protein-per-day.html', 'es': '/es/proteinas-al-dia.html', 'de': '/de/protein-pro-tag.html'},
    'prise-de-masse': {'en': '/en/bulking.html', 'es': '/es/volumen-muscular.html', 'de': '/de/masseaufbau.html'},
    'nutrition-musculation': {'en': '/en/nutrition-for-strength-training.html', 'es': '/es/nutricion-y-fuerza.html', 'de': '/de/ernaehrung-krafttraining.html'},
    'series': {'en': '/en/sets-per-muscle.html', 'es': '/es/series-por-musculo.html', 'de': '/de/saetze-pro-muskel.html'},
    'variations': {'en': '/en/daily-weight-fluctuations.html', 'es': '/es/variaciones-de-peso.html', 'de': '/de/gewichtsschwankungen.html'},
    'meal-prep': {'en': '/en/meal-prep.html', 'es': '/es/meal-prep.html', 'de': '/de/meal-prep.html'},
    'peser': {'en': '/en/weigh-food-raw-or-cooked.html', 'es': '/es/pesar-crudo-o-cocinado.html', 'de': '/de/roh-oder-gekocht-wiegen.html'},
    'compteur-gratuit': {'en': '/en/free-calorie-counter.html', 'es': '/es/contador-calorias-gratis.html', 'de': '/de/kalorienzaehler-kostenlos.html'},
    'sans-compte': {'en': '/en/calorie-app-without-account.html', 'es': '/es/app-calorias-sin-cuenta.html', 'de': '/de/kalorien-app-ohne-konto.html'},
    'alternative-mfp': {'en': '/en/myfitnesspal-alternative.html', 'es': '/es/alternativa-myfitnesspal.html', 'de': '/de/myfitnesspal-alternative.html'},
    'comparatif': {'en': '/en/nutrition-apps-compared.html', 'es': '/es/comparativa-apps-nutricion.html', 'de': '/de/ernaehrungs-apps-vergleich.html'},
    'seche': {'en': '/en/cutting.html', 'es': '/es/definicion-muscular.html', 'de': '/de/definitionsphase.html'},
    'plateau': {'en': '/en/weight-loss-plateau.html', 'es': '/es/estancamiento-perdida-de-peso.html', 'de': '/de/plateau-beim-abnehmen.html'},
    'reverse-diet': {'en': '/en/reverse-diet.html', 'es': '/es/dieta-inversa.html', 'de': '/de/reverse-diet.html'},
    'diet-break': {'en': '/en/diet-break.html', 'es': '/es/pausa-de-dieta.html', 'de': '/de/diaetpause.html'},
    'recomposition': {'en': '/en/body-recomposition.html', 'es': '/es/recomposicion-corporal.html', 'de': '/de/body-recomposition.html'},
    'cyclage': {'en': '/en/carb-cycling.html', 'es': '/es/ciclado-de-carbohidratos.html', 'de': '/de/carb-cycling.html'},
    'surcharge': {'en': '/en/progressive-overload.html', 'es': '/es/sobrecarga-progresiva.html', 'de': '/de/progressive-ueberlastung.html'},
    'compter': {'en': '/en/how-to-count-calories.html', 'es': '/es/como-contar-calorias.html', 'de': '/de/kalorien-zaehlen.html'},
    'fast-food': {'en': '/en/fast-food-calories.html', 'es': '/es/calorias-comida-rapida.html', 'de': '/de/fast-food-kalorien.html'},
    'methode': {'en': '/en/method.html', 'es': '/es/metodo.html', 'de': '/de/methode.html'},
    'faq': {'en': '/en/faq.html', 'es': '/es/preguntas-frecuentes.html', 'de': '/de/haeufige-fragen.html'},
    'apropos': {'en': '/en/about.html', 'es': '/es/sobre-basal.html', 'de': '/de/ueber-basal.html'},
    'confidentialite': {'en': '/en/privacy.html', 'es': '/es/privacidad.html', 'de': '/de/datenschutz.html'},
    'suppression': {'en': '/en/delete-account.html', 'es': '/es/eliminar-cuenta.html', 'de': '/de/konto-loeschen.html'},
    'cgu': {'en': '/en/terms.html', 'es': '/es/condiciones.html', 'de': '/de/nutzungsbedingungen.html'},
    'mentions': {'en': '/en/legal-notice.html', 'es': '/es/aviso-legal.html', 'de': '/de/impressum.html'},
}

L = {
    'en': dict(fil='Breadcrumb', accueil='Home', guides='Guides', sommaire='Contents', par='By', createur='creator of Basal', publie='Published on', maj='Updated on',
               note='This article is for information only. Basal is not a medical device and does not replace advice from a health professional.',
               play='Get it on Google Play', apple='Download on the App Store', pays='gb', locale='en_GB'),
    'es': dict(fil='Ruta de navegación', accueil='Inicio', guides='Guías', sommaire='Índice', par='Por', createur='creador de Basal', publie='Publicado el', maj='Actualizado el',
               note='Este artículo es informativo. Basal no es un dispositivo médico y no sustituye el consejo de un profesional sanitario.',
               play='Disponible en Google Play', apple='Descargar en la App Store', pays='es', locale='es_ES'),
    'de': dict(fil='Brotkrümelnavigation', accueil='Startseite', guides='Ratgeber', sommaire='Inhalt', par='Von', createur='Entwickler von Basal', publie='Veröffentlicht am', maj='Aktualisiert am',
               note='Dieser Artikel dient nur der Information. Basal ist kein Medizinprodukt und ersetzt nicht den Rat medizinischen Fachpersonals.',
               play='Jetzt bei Google Play', apple='Laden im App Store', pays='de', locale='de_DE'),
}

def _date(iso, l):
    y, m, d = iso.split('-')
    mois = {'en': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
            'es': ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'],
            'de': ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember']}[l][int(m) - 1]
    return {'en': f'{int(d)} {mois} {y}', 'es': f'{int(d)} de {mois} de {y}', 'de': f'{int(d)}. {mois} {y}'}[l]


def stores(l, campagne):
    t = L[l]
    return f'''<div class="cta">
        <a class="store-badge play" data-goatcounter-click="store-play-{campagne}" href="https://play.google.com/store/apps/details?id=com.reqquiem07.calorietracker&amp;hl={l}&amp;referrer=utm_source%3Dbasal-app.fr%26utm_medium%3Dsite%26utm_campaign%3D{campagne}">
          <img src="/img/google-play-en.png" alt="{t["play"]}" width="148" height="44" loading="lazy">
        </a>
        <a class="store-badge apple" data-goatcounter-click="store-apple-{campagne}" href="https://apps.apple.com/{t["pays"]}/app/basal/id6793001641">
          <img src="/img/app-store-en.svg" alt="{t["apple"]}" width="132" height="44" loading="lazy">
        </a>
      </div>'''


def article(l, a):
    """a : dict(court, surtitre, h1, chapeau, publie, maj?, sommaire=[(id, titre)], corps) — corps en HTML."""
    t = L[l]
    maj = f'''
      <span aria-hidden="true">·</span>
      <span>{t["maj"]} <time datetime="{a["maj"]}">{_date(a["maj"], l)}</time></span>''' if a.get('maj') else ''
    sommaire = '\n'.join(f'        <li><a href="#{i}">{x}</a></li>' for i, x in a['sommaire'])
    return f'''<main id="contenu" class="wrap">
  <nav class="fil" aria-label="{t["fil"]}"><a href="{U["accueil"][l]}">{t["accueil"]}</a><span aria-hidden="true">›</span><a href="{U["guides"][l]}">{t["guides"]}</a><span aria-hidden="true">›</span>{a["court"]}</nav>
  <header class="article-tete">
    <p class="surtitre">{a["surtitre"]}</p>
    <h1>{a["h1"]}</h1>
    <p class="chapeau">{a["chapeau"]}</p>
    <div class="signature">
      <span class="avatar" aria-hidden="true">TS</span>
      <span>{t["par"]} <b>Théo Serrano</b>, {t["createur"]}</span>
      <span aria-hidden="true">·</span>
      <span>{t["publie"]} <time datetime="{a["publie"]}">{_date(a["publie"], l)}</time></span>{maj}
    </div>
  </header>

  <div class="article">
    <aside class="sommaire" aria-labelledby="sommaire-t">
      <p id="sommaire-t">{t["sommaire"]}</p>
      <ol>
{sommaire}
      </ol>
    </aside>

    <article class="corps">
{a["corps"]}
    </article>
  </div>

  <aside class="note-page">
    <p>{a.get("note", t["note"])}</p>
  </aside>
</main>'''


def ld_article(l, url, titre, description, court, publie, maj=None):
    t = L[l]
    return [
        {'@context': 'https://schema.org', '@type': 'Article', 'headline': titre, 'description': description, 'inLanguage': l,
         'url': f'https://basal-app.fr{url}', 'mainEntityOfPage': f'https://basal-app.fr{url}', 'image': 'https://basal-app.fr/img/og-en.png',
         'datePublished': publie, 'dateModified': maj or publie,
         'author': {'@type': 'Person', 'name': 'Théo Serrano', 'url': 'https://basal-app.fr/a-propos.html'}, 'publisher': {'@id': 'https://basal-app.fr/#organisation'}},
        {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': t['accueil'], 'item': f'https://basal-app.fr{U["accueil"][l]}'},
            {'@type': 'ListItem', 'position': 2, 'name': t['guides'], 'item': f'https://basal-app.fr{U["guides"][l]}'},
            {'@type': 'ListItem', 'position': 3, 'name': court, 'item': f'https://basal-app.fr{url}'}]},
    ]


def page(l, cle, a, tete):
    """Assemble l'entrée PAGES d'un guide. tete : dict(title, description, og_title, og_description)."""
    url = U[cle][l]
    return {'slug': url, 'tete': dict(**tete, locale=L[l]['locale'], og_type='article'), 'main': article(l, a),
            'ld': ld_article(l, url, a['h1'], tete['description'], a['court'], a['publie'], a.get('maj'))}


def recette(l, slug_fr):
    """(adresse, nom) d'une recette dans la langue l, lus dans les pages générées par l'app."""
    import glob, os, re
    racine = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../src/contenus/recettes', l)
    for f in glob.glob(os.path.join(racine, '*.html')):
        if f.endswith('.tete.html'):
            continue
        h = open(f, encoding='utf-8').read()
        if f'/img/recettes/{slug_fr}.webp" alt' in h:
            nom = re.search(r'<h1>(.*?)</h1>', h).group(1)
            return f'{U["recettes"][l]}{os.path.basename(f)}', nom
    raise SystemExit(f'recette introuvable : {l}/{slug_fr}')


def avis_traduction(l, fr_url):
    """Paragraphe des pages légales traduites : seule la version française fait foi."""
    a = f'<a href="{fr_url}" hreflang="fr" lang="fr">'
    return {'en': f'<p>This is a translation of the {a}French version</a>. If the two versions ever differ, only the French version is authoritative.</p>',
            'es': f'<p>Esta es una traducción de la {a}versión francesa</a>. Si las dos versiones difieren, solo la versión francesa da fe.</p>',
            'de': f'<p>Dies ist eine Übersetzung der {a}französischen Fassung</a>. Weichen die beiden Fassungen voneinander ab, ist allein die französische Fassung maßgeblich.</p>'}[l]


def legale(l, cle, titre, description, corps):
    """Entrée PAGES d'une page légale (gabarit .page, sans fil d'Ariane, comme la version française)."""
    return {'slug': U[cle][l], 'tete': dict(title=titre, description=description, og_title=titre, og_description=description, locale=L[l]['locale']),
            'main': f'<div class="page" role="main">\n{corps}\n</div>'}


# Libellés des articles écrits selon la méthode SEO du 18/11 (bloc situation, en bref, sources, pour aller plus loin).
M = {'en': dict(situation='Your situation', bref='In short', sources='Sources', plus='Further reading', guide='Guide', calc='Calculator',
                methode='The app’s exact rules are set out on the <a href="{u}">Method</a> page.'),
     'es': dict(situation='Tu situación', bref='En resumen', sources='Fuentes', plus='Para saber más', guide='Guía', calc='Calculadora',
                methode='Las reglas exactas de la aplicación se detallan en la página <a href="{u}">Método</a>.'),
     'de': dict(situation='Deine Situation', bref='Kurz gesagt', sources='Quellen', plus='Weiterlesen', guide='Ratgeber', calc='Rechner',
                methode='Die genauen Regeln der App stehen auf der Seite <a href="{u}">Methode</a>.')}


def article_seo(l, cle, a, campagne):
    """Entrée PAGES d'un article au format du lot 7 (FR : seo-2026-11/lot7_articles.py).
    a : dict(title, desc, court, surtitre, h1, chapeau, situation, bref, sections=[(id, h2, html)], appel=(titre, texte),
    sources=[...], plus=[(cle, surtitre ou None, h3, texte)], publie). title ≤ 60, desc ≤ 155."""
    assert len(a['title']) <= 60 and len(a['desc']) <= 155, (l, cle, len(a['title']), len(a['desc']))
    m = M[l]
    nl = '\n'
    cartes = nl.join(f'        <a class="guide" href="{U[c][l]}"><span class="surtitre" style="margin:0">{sur or m["guide"]}</span><h3>{h}</h3><p>{p}</p></a>' for c, sur, h, p in a['plus'])
    corps = f'''      <div class="en-bref">
        <p class="surtitre">{m["bref"]}</p>
        <p>{a["bref"]}</p>
      </div>

''' + (nl * 2).join(f'      <h2 id="{i}">{t}</h2>{nl}      {c}' for i, t, c in a['sections']) + f'''

      <div class="appel">
        <p class="appel-t">{a["appel"][0]}</p>
        <p>{a["appel"][1]}</p>
        {stores(l, campagne)}
      </div>

      <h2 id="sources">{m["sources"]}</h2>
      <ol class="sources">
''' + nl.join(f'        <li>{x}</li>' for x in a['sources']) + f'''
      </ol>
      <p>{m["methode"].format(u=U["methode"][l])}</p>

      <h2 style="font-size:1.5rem;margin-top:48px">{m["plus"]}</h2>
      <div class="guides" style="grid-template-columns:repeat(auto-fit,minmax(240px,1fr))">
{cartes}
      </div>'''
    art = dict(court=a['court'], surtitre=a['surtitre'], h1=a['h1'], chapeau=a['chapeau'], publie=a['publie'],
               sommaire=[(i, t) for i, t, _ in a['sections']] + [('sources', m['sources'])], corps=corps)
    p = page(l, cle, art, dict(title=a['title'], description=a['desc'], og_title=a['title'], og_description=a['desc']))
    bloc = f'''

  <div class="en-bref en-situation">
    <p class="surtitre">{m["situation"]}</p>
    <p>{a["situation"]}</p>
  </div>'''
    i = p['main'].index('</header>') + len('</header>')
    p['main'] = p['main'][:i] + bloc + p['main'][i:]
    # Liens entre articles écrits href="@cle" : résolus dans la langue de la page, via U.
    import re
    p['main'] = re.sub(r'href="@([a-z0-9-]+)"', lambda x: f'href="{U[x.group(1)][l]}"', p['main'])
    return p
