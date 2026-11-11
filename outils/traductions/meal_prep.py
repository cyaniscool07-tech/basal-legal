from commun import U, page, recette, stores

FR = '/preparer-sa-semaine.html'
DATE = '2026-11-11'
C = 'meal-prep'
SOM = ['recettes-qui-tiennent', 'conservation', 'organiser', 'recettes', 'application', 'sources']

# (recettes, note) : une ligne de la liste ; les noms viennent des pages traduites par l'app.
LIGNES = [(['poulet-riz-brocoli'], 'riz'), (['chili-con-carne', 'chili-sin-carne'], None), (['dahl-lentilles-corail'], None), (['curry-poulet-coco'], None),
          (['pates-bolognaise'], None), (['couscous-poulet'], None), (['hachis-parmentier'], None), (['ratatouille'], None), (['quiche-lorraine', 'tortilla-espagnole'], None),
          (['taboule-quinoa', 'salade-lentilles'], None), (['soupe-poireaux', 'veloute-butternut'], None), (['muffins-oeufs-legumes'], 'petit-dej'),
          (['houmous-carottes', 'energy-balls', 'banana-bread'], 'collations')]

SOURCES = '''    <ul>
      <li><a href="https://www.anses.fr/en/news/good-practices-preventing-foodborne-infections-during-lockdown">ANSES (2020)</a></li>
      <li><a href="https://www.anses.fr/en/article/refrigerator-and-food-hygiene">ANSES, refrigerator and food hygiene</a></li>
      <li><a href="https://www.mangerbouger.fr/manger-mieux/se-faire-plaisir-en-mangeant-equilibre/cuisiner-maison/petit-guide-de-la-conservation-des-aliments-et-regles-d-hygiene">Manger Bouger – Santé publique France (2022)</a></li>
      <li><a href="https://www.canada.ca/en/services/health/publications/food-nutrition/infographic-leftovers.html">Health Canada (2024), leftovers</a></li>
      <li><a href="https://foodstandards.gov.scot/consumers/food-safety/at-home/rice">Food Standards Scotland, rice</a></li>
    </ul>'''


def liste(l, t):
    lignes = []
    for slugs, note in LIGNES:
        liens = [f'<a href="{u}">{n}</a>' for u, n in (recette(l, s) for s in slugs)]
        texte = liens[0] if len(liens) == 1 else (', '.join(liens[:-1]) + f' {t["et"]} ' + liens[-1])
        lignes.append(f'      <li>{texte}{t["notes"][note] if note else ""}</li>')
    return '\n'.join(lignes)


def corps(l, t):
    p = lambda xs: '\n'.join(f'    <p>{x}</p>' for x in xs)
    li = lambda xs: '\n'.join(f'      <li>{x}</li>' for x in xs)
    return f'''    <h2 id="recettes-qui-tiennent">{t["s"][0]}</h2>
{p(t["a"])}

    <h2 id="conservation">{t["s"][1]}</h2>
    <p>{t["b"]}</p>
    <ul>
{li(t["durees"])}
    </ul>
    <p>{t["regles_t"]}</p>
    <ul>
{li(t["regles"])}
    </ul>

    <h2 id="organiser">{t["s"][2]}</h2>
    <p>{t["c"]}</p>
    <ul>
{li(t["facons"])}
    </ul>
{p(t["c2"])}

    <h2 id="recettes">{t["s"][3]}</h2>
    <p>{t["d"]}</p>
    <ul class="liste">
{liste(l, t)}
    </ul>

    <h2 id="application">{t["s"][4]}</h2>
    <p>{t["e"]}</p>
    {stores(l, t["campagne"])}

    <h2 id="sources">{t["s"][5]}</h2>
{SOURCES}'''


EN = dict(et='and', notes={'riz': ' — the classic, to eat within 24 h (rice)', 'petit-dej': ', for breakfasts', 'collations': ', for snacks'},
    s=['Choosing recipes that keep', 'How long it keeps', 'Organising the week', '19 recipes you can make ahead', 'In the app', 'Sources'],
    a=['Not all recipes age the same way. Those best suited to cooking ahead have three things in common: they <strong>reheat without spoiling</strong> (stews, curries, sauces, pulses), they <strong>portion easily</strong> into boxes, and their ingredients <strong>do not go watery</strong> after two days. Fried food, dressed leafy salads and overcooked pasta, on the other hand, do not take the wait well.',
       'Nutrition-wise, a weekly prep is also a chance to lock in your <strong>protein</strong>: by choosing a rich base (chicken, lentils, fish, eggs), each box brings a known serving, instead of a day-to-day guess.'],
    b='These are <strong>indicative guidelines</strong> from health authorities, at 4 °C at most, for dishes chilled quickly — never a guarantee:',
    durees=['<strong>Home-cooked dishes</strong> (meat, poultry, fish, vegetables, cooked eggs): <strong>3 days</strong> in the fridge (ANSES, Santé publique France).',
            '<strong>Soups</strong>: <strong>2 days</strong> (Health Canada, lower bound).',
            '<strong>Dishes with cooked rice</strong>: <strong>24 hours</strong>. Rice can carry spores of <em>Bacillus cereus</em>, which survive cooking (Food Standards Scotland; ANSES describes the same risk).',
            '<strong>Raw-egg preparations</strong> (chocolate mousse): 24 hours, do not freeze.',
            '<strong>In the freezer</strong>, a home-made dish keeps its quality for <strong>2 to 3 months</strong> (Health Canada); a soup, about 4 months.'],
    regles_t='Four rules apply to everything made ahead:',
    regles=['put it in the fridge <strong>within 2 hours</strong> of cooking;', 'a fridge at <strong>4 °C at most</strong>, dishes stored in the coldest zone;',
            'reheat <strong>all the way through</strong> (70 °C), until steam comes out;', 'thaw <strong>in the fridge</strong>, never at room temperature, and never refreeze.'],
    c='The practical consequence of the times above: <strong>one Sunday session does not cover seven days in the fridge</strong>. Two ways to go about it, to combine:',
    facons=['<strong>Two short sessions</strong>, for example Sunday and Wednesday, each for three days.', '<strong>Freeze on cooking day</strong> the portions planned beyond three days, and move them to the fridge the day before the meal.'],
    c2=['Eat first what keeps least (rice, soups), keep what holds best for the end of the period, and write the cooking date on each box.',
        f'To count a serving accurately, weigh the whole dish once cooked and divide: details in the guide <a href="{U["peser"]["en"]}">weighing raw or cooked</a>.'],
    d='Each recipe gives the ingredients to the gram, the steps, and the calories and macros per serving.',
    e='In Basal, these recipes are tagged “Meal prep” in the Meals tab, and their storage times follow exactly the guidelines above. The <strong>“Prep my week”</strong> assistant (Premium, with one free use to try it) picks the recipes, spreads the meals over the days, plans what to freeze and fills the shopping list. The meal plan and the shopping list stay free.',
    campagne='en-meal-prep')

ES = dict(et='y', notes={'riz': ' — el clásico, para comer en 24 h (arroz)', 'petit-dej': ', para los desayunos', 'collations': ', para las meriendas'},
    s=['Elegir recetas que aguanten', 'Cuánto tiempo se conservan', 'Organizar la semana', '19 recetas para preparar con antelación', 'En la aplicación', 'Fuentes'],
    a=['No todas las recetas envejecen igual. Las que mejor se prestan a prepararse con antelación tienen tres puntos en común: se <strong>recalientan sin estropearse</strong> (guisos, currys, salsas, legumbres), se <strong>reparten fácilmente</strong> en táperes y sus ingredientes <strong>no sueltan agua</strong> a los dos días. En cambio, los fritos, las ensaladas de hoja ya aliñadas y la pasta demasiado cocida soportan mal la espera.',
       'En cuanto a nutrición, preparar la semana es también una ocasión para fijar tus <strong>proteínas</strong>: eligiendo una base rica (pollo, lentejas, pescado, huevos), cada táper aporta una ración conocida en lugar de una estimación diaria.'],
    b='Son <strong>referencias orientativas</strong> de las autoridades sanitarias, a 4 °C como máximo, para platos enfriados rápido — nunca una garantía:',
    durees=['<strong>Platos caseros</strong> (carne, aves, pescado, verduras, huevos cocidos): <strong>3 días</strong> en la nevera (ANSES, Santé publique France).',
            '<strong>Sopas y cremas</strong>: <strong>2 días</strong> (Health Canada, límite bajo).',
            '<strong>Platos con arroz cocido</strong>: <strong>24 horas</strong>. El arroz puede llevar esporas de <em>Bacillus cereus</em>, que resisten la cocción (Food Standards Scotland; la ANSES describe el mismo riesgo).',
            '<strong>Preparaciones con huevo crudo</strong> (mousse de chocolate): 24 horas, no congelar.',
            '<strong>En el congelador</strong>, un plato casero conserva su calidad <strong>2 o 3 meses</strong> (Health Canada); una sopa, unos 4 meses.'],
    regles_t='Cuatro reglas valen para todo lo que se prepara con antelación:',
    regles=['meter en la nevera <strong>en las 2 horas</strong> siguientes a la cocción;', 'una nevera a <strong>4 °C como máximo</strong>, con los platos en la zona más fría;',
            'recalentar <strong>bien por dentro</strong> (70 °C), hasta que salga vapor;', 'descongelar <strong>en la nevera</strong>, nunca a temperatura ambiente, y no volver a congelar nunca.'],
    c='La consecuencia práctica de los plazos anteriores: <strong>una sesión el domingo no cubre siete días en la nevera</strong>. Dos maneras de hacerlo, combinables:',
    facons=['<strong>Dos sesiones</strong> cortas, por ejemplo domingo y miércoles, cada una para tres días.', '<strong>Congelar el mismo día de la cocción</strong> las raciones previstas más allá de tres días, y pasarlas a la nevera la víspera de la comida.'],
    c2=['Come primero lo que menos aguanta (arroz, sopas), deja para el final lo que mejor se conserva y apunta la fecha de preparación en cada táper.',
        f'Para contar una ración justa, pesa el plato entero ya cocinado y divide: el detalle está en la guía <a href="{U["peser"]["es"]}">pesar crudo o cocinado</a>.'],
    d='Cada ficha da los ingredientes al gramo, los pasos y las calorías y macros por ración.',
    e='En Basal, estas recetas llevan la etiqueta «Meal prep» en la pestaña Comidas, y sus plazos de conservación siguen exactamente las referencias de arriba. El asistente <strong>«Prepara mi semana»</strong> (Premium, con un uso gratis para probarlo) elige las recetas, reparte las comidas en los días, prevé lo que hay que congelar y rellena la lista de la compra. La planificación y la lista de la compra siguen siendo gratis.',
    campagne='es-meal-prep')

DE = dict(et='und', notes={'riz': ' — der Klassiker, innerhalb von 24 h essen (Reis)', 'petit-dej': ', fürs Frühstück', 'collations': ', für Snacks'},
    s=['Rezepte wählen, die halten', 'Wie lange es sich hält', 'Die Woche organisieren', '19 Rezepte zum Vorkochen', 'In der App', 'Quellen'],
    a=['Nicht alle Rezepte altern gleich. Die, die sich am besten zum Vorkochen eignen, haben drei Dinge gemeinsam: Sie lassen sich <strong>aufwärmen, ohne zu leiden</strong> (Schmorgerichte, Currys, Saucen, Hülsenfrüchte), sie lassen sich <strong>leicht portionieren</strong>, und ihre Zutaten <strong>ziehen nach zwei Tagen kein Wasser</strong>. Frittiertes, angemachter Blattsalat und zu weich gekochte Nudeln vertragen das Warten dagegen schlecht.',
       'Für die Ernährung ist das Vorkochen auch eine Gelegenheit, dein <strong>Eiweiß</strong> festzulegen: Mit einer eiweißreichen Basis (Hähnchen, Linsen, Fisch, Eier) bringt jede Box eine bekannte Portion statt einer täglichen Schätzung.'],
    b='Das sind <strong>Richtwerte</strong> der Gesundheitsbehörden, bei höchstens 4 °C, für schnell gekühlte Gerichte — nie eine Garantie:',
    durees=['<strong>Selbst gekochte Gerichte</strong> (Fleisch, Geflügel, Fisch, Gemüse, gegarte Eier): <strong>3 Tage</strong> im Kühlschrank (ANSES, Santé publique France).',
            '<strong>Suppen</strong>: <strong>2 Tage</strong> (Health Canada, untere Grenze).',
            '<strong>Gerichte mit gekochtem Reis</strong>: <strong>24 Stunden</strong>. Reis kann Sporen von <em>Bacillus cereus</em> tragen, die das Kochen überstehen (Food Standards Scotland; die ANSES beschreibt dasselbe Risiko).',
            '<strong>Zubereitungen mit rohen Eiern</strong> (Mousse au Chocolat): 24 Stunden, nicht einfrieren.',
            '<strong>Im Gefrierschrank</strong> behält ein selbst gekochtes Gericht seine Qualität <strong>2 bis 3 Monate</strong> (Health Canada), eine Suppe etwa 4 Monate.'],
    regles_t='Vier Regeln gelten für alles, was vorgekocht wird:',
    regles=['<strong>innerhalb von 2 Stunden</strong> nach dem Kochen in den Kühlschrank;', 'ein Kühlschrank mit <strong>höchstens 4 °C</strong>, Gerichte in der kältesten Zone;',
            '<strong>vollständig durcherhitzen</strong> (70 °C), bis Dampf austritt;', '<strong>im Kühlschrank</strong> auftauen, nie bei Raumtemperatur, und nie wieder einfrieren.'],
    c='Die praktische Folge der Zeiten oben: <strong>Eine Kochsession am Sonntag deckt keine sieben Tage im Kühlschrank ab</strong>. Zwei Wege, kombinierbar:',
    facons=['<strong>Zwei kurze Sessions</strong>, zum Beispiel Sonntag und Mittwoch, jeweils für drei Tage.', '<strong>Am Kochtag einfrieren</strong>, was über drei Tage hinaus geplant ist, und es am Vortag der Mahlzeit in den Kühlschrank legen.'],
    c2=['Iss zuerst, was sich am kürzesten hält (Reis, Suppen), heb das Haltbarste fürs Ende auf und schreib das Zubereitungsdatum auf jede Box.',
        f'Um eine Portion genau zu zählen, wiege das ganze gegarte Gericht und teile es: Details im Ratgeber <a href="{U["peser"]["de"]}">roh oder gekocht wiegen</a>.'],
    d='Jedes Rezept nennt die Zutaten aufs Gramm, die Schritte sowie Kalorien und Makros pro Portion.',
    e='In Basal sind diese Rezepte im Tab Mahlzeiten mit „Meal Prep“ markiert, und ihre Haltbarkeiten folgen genau den Richtwerten oben. Der Assistent <strong>„Plane meine Woche“</strong> (Premium, mit einer kostenlosen Nutzung zum Testen) wählt die Rezepte, verteilt die Mahlzeiten auf die Tage, plant, was eingefroren werden muss, und füllt die Einkaufsliste. Wochenplan und Einkaufsliste bleiben kostenlos.',
    campagne='de-meal-prep')


def art(l, t, court, surtitre, h1, chapeau):
    return dict(court=court, surtitre=surtitre, publie='2026-10-18', maj='2026-10-30', h1=h1, chapeau=chapeau, sommaire=list(zip(SOM, t['s'])), corps=corps(l, t))


PAGES = {
    'en': page('en', C, art('en', EN, 'Meal prep', 'Meals', 'Meal prep: recipes and planning to prepare your week',
        'Cook once, eat for several days. The principle of <em>meal prep</em> (or <em>batch cooking</em>) is simple; what makes it succeed or fail are three choices: the recipes, the storage calendar, and what you freeze from the start.'),
        dict(title='Meal prep: recipes and planning for your week — Basal', description='Which recipes keep, how long food keeps in the fridge and freezer (health authority guidelines), how to organise the week, and 19 make-ahead recipes with their macros.',
             og_title='Meal prep: recipes and planning to prepare your week', og_description='Recipes that keep, storage times, and how to organise your week.')),
    'es': page('es', C, art('es', ES, 'Meal prep', 'Comidas', 'Meal prep: recetas y organización para preparar tu semana',
        'Cocinar una vez, comer varios días. El principio del <em>meal prep</em> (o <em>batch cooking</em>) es sencillo; lo que lo hace funcionar o fracasar son tres elecciones: las recetas, el calendario de conservación y lo que se congela desde el principio.'),
        dict(title='Meal prep: recetas y organización para tu semana — Basal', description='Qué recetas aguantan, cuánto se conservan en nevera y congelador (referencias sanitarias), cómo organizar la semana y 19 recetas para preparar con antelación con sus macros.',
             og_title='Meal prep: recetas y organización para preparar tu semana', og_description='Recetas que aguantan, plazos de conservación y cómo organizar la semana.')),
    'de': page('de', C, art('de', DE, 'Meal Prep', 'Mahlzeiten', 'Meal Prep: Rezepte und Planung für deine Woche',
        'Einmal kochen, mehrere Tage essen. Das Prinzip von <em>Meal Prep</em> (oder <em>Batch Cooking</em>) ist einfach; ob es klappt, entscheiden drei Dinge: die Rezepte, der Haltbarkeitskalender und das, was man von Anfang an einfriert.'),
        dict(title='Meal Prep: Rezepte und Planung für die Woche — Basal', description='Welche Rezepte halten, wie lange sich Essen im Kühl- und Gefrierschrank hält (Richtwerte der Behörden), wie man die Woche plant und 19 Rezepte zum Vorkochen mit Makros.',
             og_title='Meal Prep: Rezepte und Planung für deine Woche', og_description='Rezepte, die halten, Haltbarkeiten und wie man die Woche organisiert.')),
}
