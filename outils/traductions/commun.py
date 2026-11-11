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
    'methode': {'en': '/en/method.html', 'es': '/es/metodo.html', 'de': '/de/methode.html'},
    'faq': {'en': '/en/faq.html', 'es': '/es/preguntas-frecuentes.html', 'de': '/de/haeufige-fragen.html'},
    'apropos': {'en': '/en/about.html', 'es': '/es/sobre-basal.html', 'de': '/de/ueber-basal.html'},
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
    <p>{t["note"]}</p>
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
