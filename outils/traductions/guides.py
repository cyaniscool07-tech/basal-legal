"""Hub des guides. Une carte n'apparaît que si sa page existe déjà dans la langue (relancer après chaque lot)."""
import os
from commun import U

FR = '/guides/'
DATE = '2026-11-11'
RACINE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../src/contenus')


def existe(url):
    if url in U['recettes'].values():  # générées par l'app, dans src/contenus/recettes/<lang>/
        return True
    rel = url.lstrip('/')
    return os.path.exists(os.path.join(RACINE, rel + 'index.html' if rel.endswith('/') else rel))


def main(l, t):
    sections = []
    for i, (titre, cartes) in enumerate(t['sections']):
        cartes = [(U[c][l], h, p) for c, h, p in cartes if existe(U[c][l])]
        if not cartes:
            continue
        sections.append(f'''  <section class="hub-repas" aria-labelledby="t-{i}">
    <h2 id="t-{i}">{titre}</h2>
    <div class="guides">
''' + '\n'.join(f'      <a class="guide" href="{u}"><h3>{h}</h3><p>{p}</p></a>' for u, h, p in cartes) + '''
    </div>
  </section>''')
    return f'''<main id="contenu" class="wrap">
  <nav class="fil" aria-label="{t["fil"]}"><a href="{U["accueil"][l]}">{t["accueil"]}</a><span aria-hidden="true">›</span>{t["guides"]}</nav>
  <header class="article-tete">
    <p class="surtitre">{t["guides"]}</p>
    <h1>{t["h1"]}</h1>
    <p class="chapeau">{t["chapeau"]}</p>
  </header>
''' + '\n'.join(sections) + f'''
  <div class="appel-contexte">
    <div><strong>{t["outils_t"]}</strong><p>{t["outils"]}</p></div>
    <a class="bouton vif" href="{U["calculateurs"][l]}">{t["calcs"]}</a>
  </div>
</main>'''


def ld(l, t):
    url = U['guides'][l]
    return [{'@context': 'https://schema.org', '@type': 'CollectionPage', 'name': t['h1'], 'url': f'https://basal-app.fr{url}', 'inLanguage': l, 'publisher': {'@id': 'https://basal-app.fr/#organisation'}},
            {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
                {'@type': 'ListItem', 'position': 1, 'name': t['accueil'], 'item': f'https://basal-app.fr{U["accueil"][l]}'},
                {'@type': 'ListItem', 'position': 2, 'name': t['guides'], 'item': f'https://basal-app.fr{url}'}]}]


EN = dict(fil='Breadcrumb', accueil='Home', guides='Guides', h1='Understand before you count',
    chapeau='Guides that show their calculations, cite their sources and say what we do not know. The formulas they use are the app’s own.',
    outils_t='The tools that go with them', outils='Work out your expenditure and macros with the same formulas as the app.', calcs='The calculators',
    sections=[('Calories and expenditure', [('combien', 'How many calories a day?', 'For a woman or a man, by age and activity: worked examples, and how to calculate your own need.'),
                                            ('metabolisme-de-base', 'Basal metabolic rate: what it is and what changes it', 'Its share of your expenditure, the formula, and why lean mass counts more than age.'),
                                            ('metabolisme-adaptatif', 'Adaptive metabolism: why a formula is not enough', 'Why the Mifflin-St Jeor estimate is wrong, and how to correct it with your data.'),
                                            ('variations', 'Why your weight changes from one day to the next', 'Water, sodium, glycogen, digestion: why only the seven-day average is readable.')]),
              ('Losing or gaining weight', [('deficit', 'Calorie deficit: how to calculate it, what pace', 'How many calories to cut, what loss to expect each week, and why too big a deficit ends up stalling.'),
                                            ('prise-de-masse', 'Bulking: calories, protein and pace', 'What surplus to choose, how much protein, and how fast to gain weight.')]),
              ('Strength training', [('proteines', 'How much protein per day?', 'The minimum, the range for athletes and diets, the case of high body weight, and the foods that provide it.'),
                                     ('nutrition-musculation', 'Are you eating enough for what you lift?', 'The sets each muscle gets, protein on rest days, and the sign that weight loss is not costing muscle.'),
                                     ('series', 'How many sets per muscle per week', 'How to count your sets per muscle group, and what order of magnitude to aim for.')]),
              ('Meals', [('meal-prep', 'Meal prep: prepare your week', 'Which recipes to choose, how many days they keep, what to freeze.'),
                         ('peser', 'Weighing food raw or cooked', 'Raw and cooked values from the Ciqual table, and the logging mistake that doubles calories.'),
                         ('recettes', 'Calculated recipes', 'Everyday recipes with their calories and macros per serving, calculated from the Ciqual table.')]),
              ('Choosing an app', [('comparatif', 'Compared: MyFitnessPal, Yazio, Foodvisor and Basal', 'What is free in each, what is paid, and what none of them can do.'),
                                   ('alternative-mfp', 'A MyFitnessPal alternative', 'Free, unlimited tracking, no ads and no required account. With its limits.'),
                                   ('sans-compte', 'A calorie app with no account, that works offline', 'No email, no sign-up: what works offline, how to back up, and how to check an app.'),
                                   ('compteur-gratuit', 'A free calorie app, no subscription', 'What “free” means elsewhere, and what Basal keeps free.')])])

ES = dict(fil='Ruta de navegación', accueil='Inicio', guides='Guías', h1='Entender antes de contar',
    chapeau='Guías que muestran sus cálculos, citan sus fuentes y dicen lo que no se sabe. Las fórmulas que usan son las de la aplicación.',
    outils_t='Las herramientas que las acompañan', outils='Calcula tu gasto y tus macros con las mismas fórmulas que la aplicación.', calcs='Las calculadoras',
    sections=[('Calorías y gasto', [('combien', '¿Cuántas calorías debo consumir al día?', 'Para mujer u hombre, según la edad y la actividad: ejemplos con cifras y cómo calcular tu propia necesidad.'),
                                    ('metabolisme-de-base', 'Metabolismo basal: qué es y qué lo hace variar', 'Su parte en tu gasto, la fórmula y por qué la masa magra cuenta más que la edad.'),
                                    ('metabolisme-adaptatif', 'El metabolismo adaptativo: por qué una fórmula no basta', 'Por qué la estimación de Mifflin-St Jeor se equivoca y cómo corregirla con tus datos.'),
                                    ('variations', 'Por qué tu peso cambia de un día para otro', 'Agua, sodio, glucógeno, digestión: por qué solo la media de siete días es legible.')]),
              ('Perder o ganar peso', [('deficit', 'Déficit calórico: cálculo, ritmo y errores que evitar', 'Cuántas calorías restar, qué pérdida esperar por semana y por qué un déficit demasiado fuerte acaba estancándose.'),
                                       ('prise-de-masse', 'Volumen muscular: calorías, proteínas y ritmo', 'Qué superávit elegir, cuántas proteínas y a qué ritmo ganar peso.')]),
              ('Entrenamiento de fuerza', [('proteines', '¿Cuántas proteínas al día?', 'El mínimo, el rango de deportistas y dietas, el caso del peso elevado y los alimentos que las aportan.'),
                                           ('nutrition-musculation', '¿Comes lo suficiente para lo que levantas?', 'Las series que recibe cada músculo, las proteínas de los días de descanso y la señal de que una pérdida de peso no cuesta músculo.'),
                                           ('series', 'Cuántas series por músculo y por semana', 'Cómo contar tus series por grupo muscular y qué orden de magnitud buscar.')]),
              ('Comidas', [('meal-prep', 'Meal prep: prepara tu semana', 'Qué recetas elegir, cuántos días se conservan, qué congelar.'),
                           ('peser', 'Pesar los alimentos crudos o cocinados', 'Los valores crudos y cocidos de la tabla Ciqual, y el error de registro que duplica las calorías.'),
                           ('recettes', 'Recetas calculadas', 'Recetas del día a día con sus calorías y macros por ración, calculadas con la tabla Ciqual.')]),
              ('Elegir una aplicación', [('comparatif', 'Comparativa: MyFitnessPal, Yazio, Foodvisor y Basal', 'Lo que es gratis en cada una, lo que es de pago y lo que ninguna sabe hacer.'),
                                         ('alternative-mfp', 'Una alternativa a MyFitnessPal', 'Seguimiento gratis y sin límite, sin publicidad ni cuenta obligatoria. Con sus límites.'),
                                         ('sans-compte', 'Una app de calorías sin cuenta, que funciona sin conexión', 'Sin correo ni registro: lo que funciona sin conexión, cómo hacer copia de seguridad y cómo comprobar una app.'),
                                         ('compteur-gratuit', 'Una app de calorías gratis, sin suscripción', 'Lo que significa «gratis» en otras apps y lo que Basal mantiene gratis.')])])

DE = dict(fil='Brotkrümelnavigation', accueil='Startseite', guides='Ratgeber', h1='Verstehen, bevor man zählt',
    chapeau='Ratgeber, die ihre Rechnungen zeigen, ihre Quellen nennen und sagen, was man nicht weiß. Die Formeln darin sind die der App.',
    outils_t='Die passenden Werkzeuge', outils='Berechne deinen Verbrauch und deine Makros mit denselben Formeln wie in der App.', calcs='Die Rechner',
    sections=[('Kalorien und Verbrauch', [('combien', 'Wie viele Kalorien am Tag?', 'Für Frauen und Männer, nach Alter und Aktivität: Rechenbeispiele und wie du deinen eigenen Bedarf berechnest.'),
                                          ('metabolisme-de-base', 'Grundumsatz: was er ist und was ihn verändert', 'Sein Anteil am Verbrauch, die Formel und warum fettfreie Masse mehr zählt als das Alter.'),
                                          ('metabolisme-adaptatif', 'Metabolische Anpassung: Warum eine Formel nicht reicht', 'Warum die Mifflin-St-Jeor-Schätzung danebenliegt und wie du sie mit deinen Daten korrigierst.'),
                                          ('variations', 'Warum dein Gewicht von Tag zu Tag schwankt', 'Wasser, Natrium, Glykogen, Verdauung: warum nur der Sieben-Tage-Durchschnitt aussagekräftig ist.')]),
              ('Abnehmen oder zunehmen', [('deficit', 'Kaloriendefizit: Berechnung, Tempo und Fehler', 'Wie viele Kalorien du einsparen solltest, welche Abnahme pro Woche du erwarten kannst und warum ein zu starkes Defizit stagniert.'),
                                          ('prise-de-masse', 'Masseaufbau: Kalorien, Eiweiß und Tempo', 'Welcher Überschuss, wie viel Eiweiß und wie schnell zunehmen.')]),
              ('Krafttraining', [('proteines', 'Wie viel Protein pro Tag?', 'Das Minimum, der Bereich für Sportler und Diäten, der Fall eines hohen Gewichts und die Lebensmittel, die es liefern.'),
                                 ('nutrition-musculation', 'Isst du genug für das, was du hebst?', 'Die Sätze, die jeder Muskel bekommt, Eiweiß an Ruhetagen und das Zeichen, dass Abnehmen keine Muskeln kostet.'),
                                 ('series', 'Wie viele Sätze pro Muskel und Woche', 'Wie du deine Sätze pro Muskelgruppe zählst und welche Größenordnung sinnvoll ist.')]),
              ('Mahlzeiten', [('meal-prep', 'Meal Prep: deine Woche vorbereiten', 'Welche Rezepte, wie viele Tage sie halten, was einfrieren.'),
                              ('peser', 'Lebensmittel roh oder gekocht wiegen', 'Roh- und Garwerte der Ciqual-Tabelle und der Eingabefehler, der die Kalorien verdoppelt.'),
                              ('recettes', 'Berechnete Rezepte', 'Alltagsrezepte mit Kalorien und Makros pro Portion, berechnet mit der Ciqual-Tabelle.')]),
              ('Eine App wählen', [('comparatif', 'Vergleich: MyFitnessPal, Yazio, Foodvisor und Basal', 'Was bei jeder kostenlos ist, was kostet und was keine kann.'),
                                   ('alternative-mfp', 'Eine Alternative zu MyFitnessPal', 'Kostenloses, unbegrenztes Tracking ohne Werbung und ohne Kontopflicht. Mit seinen Grenzen.'),
                                   ('sans-compte', 'Eine Kalorien-App ohne Konto, die offline funktioniert', 'Ohne E-Mail und Anmeldung: was offline geht, wie man sichert und wie man eine App prüft.'),
                                   ('compteur-gratuit', 'Eine kostenlose Kalorien-App ohne Abo', 'Was „kostenlos“ anderswo heißt und was Basal kostenlos lässt.')])])

PAGES = {}
for l, t, titre, desc in [('en', EN, 'Guides: calories, protein and strength training | Basal', 'Guides that show their calculations and sources: calories per day, basal metabolic rate, deficit, protein, sets per muscle, meal prep.'),
                          ('es', ES, 'Guías: calorías, proteínas y entrenamiento de fuerza | Basal', 'Guías que muestran sus cálculos y sus fuentes: calorías al día, metabolismo basal, déficit, proteínas, series por músculo, meal prep.'),
                          ('de', DE, 'Ratgeber: Kalorien, Eiweiß und Krafttraining | Basal', 'Ratgeber, die ihre Rechnungen und Quellen zeigen: Kalorien pro Tag, Grundumsatz, Defizit, Eiweiß, Sätze pro Muskel, Meal Prep.')]:
    PAGES[l] = {'slug': U['guides'][l], 'tete': dict(title=titre, description=desc, og_title=t['h1'], og_description=desc, locale={'en': 'en_GB', 'es': 'es_ES', 'de': 'de_DE'}[l]),
                'main': main(l, t), 'ld': ld(l, t)}
