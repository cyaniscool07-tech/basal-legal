FR = '/calculateurs/'
DATE = '2026-11-11'


def main(t):
    piliers = '\n'.join(f'      <div class="pilier"><span class="num">0{i + 1}</span><h3>{h}</h3><p>{p}</p><a href="{u}">{a}</a></div>' for i, (h, p, u, a) in enumerate(t['outils']))
    guides = ''
    if t.get('guides'):
        guides = f'''
  <h2 style="font-size:1.5rem;margin-top:48px">{t["guides_t"]}</h2>
  <div class="guides">
''' + '\n'.join(f'    <a class="guide" href="{u}"><span class="surtitre" style="margin:0">{s}</span><h3>{h}</h3><p>{p}</p></a>' for s, h, p, u in t['guides']) + '\n  </div>'
    return f'''<main id="contenu" class="wrap">
  <nav class="fil" aria-label="{t["fil"]}"><a href="{t["accueil_url"]}">{t["accueil"]}</a><span aria-hidden="true">›</span>{t["hub"]}</nav>
  <header class="article-tete">
    <p class="surtitre">{t["surtitre"]}</p>
    <h1>{t["h1"]}</h1>
    <p class="chapeau">{t["chapeau"]}</p>
  </header>

  <section class="hub-repas" aria-labelledby="t-outils">
    <h2 id="t-outils" class="visuellement-masque">{t["liste"]}</h2>
    <div class="piliers" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr))">
{piliers}
    </div>
  </section>

  <div class="appel-contexte">
    <div><strong>{t["appel_t"]}</strong><p>{t["appel"]}</p></div>
    <a class="bouton vif" href="{t["accueil_url"]}#download">{t["dl"]}</a>
  </div>
{guides}
</main>'''


def ld(nom, url, lang, accueil, n_accueil, n_hub):
    return [
        {'@context': 'https://schema.org', '@type': 'CollectionPage', 'name': nom, 'url': f'https://basal-app.fr{url}', 'inLanguage': lang, 'publisher': {'@id': 'https://basal-app.fr/#organisation'}},
        {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': n_accueil, 'item': f'https://basal-app.fr{accueil}'},
            {'@type': 'ListItem', 'position': 2, 'name': n_hub, 'item': f'https://basal-app.fr{url}'}]},
    ]


PAGES = {
    'en': {'slug': '/en/calculators/',
           'tete': dict(title='Free calculators: expenditure and macros | Basal', locale='en_GB',
                        description='Free calculators: expenditure, macros, protein, one-rep max and real expenditure from your weight. The Basal app’s formulas, no sign-up.',
                        og_title='Free calculators: expenditure and macros | Basal', og_description='The Basal app’s formulas, no sign-up, nothing is sent.'),
           'main': main(dict(fil='Breadcrumb', accueil='Home', accueil_url='/en/', hub='Calculators', surtitre='Free calculators', h1='Work out your expenditure and your macros',
               chapeau='The same formulas as the app, no sign-up: the calculation runs in your browser and nothing is sent.', liste='The calculators',
               outils=[('Basal metabolic rate and daily expenditure', 'The Mifflin-St Jeor equation and the activity factor, for a woman or a man, with the calculation in detail.', '/en/calorie-calculator.html', 'Work out my expenditure'),
                       ('Macros', 'Protein and fat anchored to body weight, carbs filling the rest, for your goal and activity.', '/en/macro-calculator.html', 'Work out my macros'),
                       ('Real expenditure', 'Your expenditure worked out from what you eat and how your weight changes, as in the app, compared with the formula.', '/en/real-expenditure-calculator.html', 'Work out my real expenditure'),
                       ('Protein', 'Your daily needs for your weight, goal and training, on a reference weight.', '/en/protein-calculator.html', 'Work out my protein'),
                       ('1RM', 'Your estimated maximum load from a set, and your loads from 1 to 12 reps.', '/en/one-rep-max-calculator.html', 'Work out my 1RM')],
               appel_t='A calculation that corrects itself', appel='These calculators give a starting point. In the app, Basal corrects it every week with your meals and weigh-ins.', dl='Download')),
           'ld': ld('Free calculators: expenditure and macros', '/en/calculators/', 'en', '/en/', 'Home', 'Calculators')},
    'es': {'slug': '/es/calculadoras/',
           'tete': dict(title='Calculadoras gratis: gasto y macros | Basal', locale='es_ES',
                        description='Calculadoras gratis: gasto, macros, proteínas, 1RM y gasto real deducido de tu peso. Las fórmulas de la aplicación Basal, sin registro.',
                        og_title='Calculadoras gratis: gasto y macros | Basal', og_description='Las fórmulas de la aplicación Basal, sin registro, no se envía nada.'),
           'main': main(dict(fil='Ruta de navegación', accueil='Inicio', accueil_url='/es/', hub='Calculadoras', surtitre='Calculadoras gratis', h1='Calcula tu gasto y tus macros',
               chapeau='Las mismas fórmulas que la aplicación, sin registro: el cálculo se hace en tu navegador y no se envía nada.', liste='Las calculadoras',
               outils=[('Metabolismo basal y gasto diario', 'La ecuación de Mifflin-St Jeor y el coeficiente de actividad, para mujer u hombre, con el detalle del cálculo.', '/es/calculadora-calorias.html', 'Calcular mi gasto'),
                       ('Macros', 'Proteínas y grasas ancladas al peso, hidratos para completar, según tu objetivo y tu actividad.', '/es/calculadora-macros.html', 'Calcular mis macros'),
                       ('Gasto real', 'Tu gasto deducido de lo que comes y de la evolución de tu peso, como en la aplicación, comparado con la fórmula.', '/es/gasto-real.html', 'Calcular mi gasto real'),
                       ('Proteínas', 'Tus necesidades diarias según tu peso, tu objetivo y tu entrenamiento, sobre un peso de referencia.', '/es/calculadora-proteinas.html', 'Calcular mis proteínas'),
                       ('1RM', 'Tu carga máxima estimada a partir de una serie, y tus cargas de 1 a 12 repeticiones.', '/es/calculadora-1rm.html', 'Calcular mi 1RM')],
               appel_t='Un cálculo que se corrige', appel='Estas calculadoras dan un punto de partida. En la aplicación, Basal lo corrige cada semana con tus comidas y tus pesadas.', dl='Descargar',
               guides_t='Para entender los resultados',
               guides=[('Calorías', '¿Cuántas calorías debo consumir al día?', 'Ejemplos con cifras según edad, sexo y actividad.', '/es/cuantas-calorias-al-dia.html'),
                       ('Metabolismo', 'Metabolismo basal', 'Qué es y qué lo hace variar.', '/es/metabolismo-basal.html'),
                       ('Perder peso', 'Déficit calórico', 'Cuánto restar y qué ritmo esperar.', '/es/deficit-calorico.html')])),
           'ld': ld('Calculadoras gratis: gasto y macros', '/es/calculadoras/', 'es', '/es/', 'Inicio', 'Calculadoras')},
    'de': {'slug': '/de/rechner/',
           'tete': dict(title='Kostenlose Rechner: Verbrauch und Makros | Basal', locale='de_DE',
                        description='Kostenlose Rechner: Verbrauch, Makros, Eiweiß, 1RM und tatsächlicher Verbrauch aus deinem Gewicht. Die Formeln der Basal-App, ohne Anmeldung.',
                        og_title='Kostenlose Rechner: Verbrauch und Makros | Basal', og_description='Die Formeln der Basal-App, ohne Anmeldung, es wird nichts gesendet.'),
           'main': main(dict(fil='Brotkrümelnavigation', accueil='Startseite', accueil_url='/de/', hub='Rechner', surtitre='Kostenlose Rechner', h1='Verbrauch und Makros berechnen',
               chapeau='Dieselben Formeln wie in der App, ohne Anmeldung: Die Berechnung läuft in deinem Browser, es wird nichts gesendet.', liste='Die Rechner',
               outils=[('Grundumsatz und Tagesverbrauch', 'Die Mifflin-St-Jeor-Gleichung und der Aktivitätsfaktor, für Frauen und Männer, mit der Berechnung im Detail.', '/de/kalorienrechner.html', 'Verbrauch berechnen'),
                       ('Makros', 'Eiweiß und Fett am Körpergewicht verankert, Kohlenhydrate für den Rest, nach Ziel und Aktivität.', '/de/makrorechner.html', 'Makros berechnen'),
                       ('Tatsächlicher Verbrauch', 'Dein Verbrauch aus dem, was du isst, und dem Verlauf deines Gewichts, wie in der App, im Vergleich zur Formel.', '/de/tatsaechlicher-verbrauch.html', 'Tatsächlichen Verbrauch berechnen'),
                       ('Eiweiß', 'Dein Tagesbedarf nach Gewicht, Ziel und Training, auf ein Referenzgewicht bezogen.', '/de/proteinrechner.html', 'Eiweiß berechnen'),
                       ('1RM', 'Dein geschätztes Maximalgewicht aus einem Satz und deine Gewichte für 1 bis 12 Wiederholungen.', '/de/1rm-rechner.html', '1RM berechnen')],
               appel_t='Eine Rechnung, die sich korrigiert', appel='Diese Rechner liefern einen Startwert. In der App korrigiert Basal ihn jede Woche mit deinen Mahlzeiten und deinem Gewicht.', dl='Herunterladen',
               guides_t='Die Ergebnisse verstehen',
               guides=[('Stoffwechsel', 'Grundumsatz', 'Was er ist und was ihn verändert.', '/de/grundumsatz.html')])),
           'ld': ld('Kostenlose Rechner: Verbrauch und Makros', '/de/rechner/', 'de', '/de/', 'Startseite', 'Rechner')},
}
