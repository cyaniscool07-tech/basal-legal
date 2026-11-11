FR = '/calcul-macros.html'
DATE = '2026-11-11'


def stores(l, campagne, play_alt, apple_alt, pays):
    return f'''<div class="cta">
          <a class="store-badge play" data-goatcounter-click="store-play-{campagne}" href="https://play.google.com/store/apps/details?id=com.reqquiem07.calorietracker&amp;hl={l}&amp;referrer=utm_source%3Dbasal-app.fr%26utm_medium%3Dsite%26utm_campaign%3D{campagne}">
            <img src="/img/google-play-en.png" alt="{play_alt}" width="148" height="44" loading="lazy">
          </a>
          <a class="store-badge apple" data-goatcounter-click="store-apple-{campagne}" href="https://apps.apple.com/{pays}/app/basal/id6793001641">
            <img src="/img/app-store-en.svg" alt="{apple_alt}" width="132" height="44" loading="lazy">
          </a>
        </div>'''


def ld(nom, url, desc, lang, accueil, n_accueil, hub, n_hub, court):
    return [
        {'@context': 'https://schema.org', '@type': 'WebApplication', 'name': nom, 'applicationCategory': 'HealthApplication', 'operatingSystem': 'All',
         'url': f'https://basal-app.fr{url}', 'inLanguage': lang, 'description': desc, 'offers': {'@type': 'Offer', 'price': '0', 'priceCurrency': 'EUR'},
         'publisher': {'@id': 'https://basal-app.fr/#organisation'}},
        {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': n_accueil, 'item': f'https://basal-app.fr{accueil}'},
            {'@type': 'ListItem', 'position': 2, 'name': n_hub, 'item': f'https://basal-app.fr{hub}'},
            {'@type': 'ListItem', 'position': 3, 'name': court, 'item': f'https://basal-app.fr{url}'}]},
    ]


def formulaire(t):
    """Le formulaire est identique dans les 3 langues : seuls les libellés changent."""
    return f'''  <div class="outil">
    <form class="carte" id="f" novalidate>
      <div class="champs">
            <div class="champ">
              <label for="sexe">{t["sexe"]}</label>
              <select id="sexe">
                <option value="male">{t["homme"]}</option>
                <option value="female">{t["femme"]}</option>
              </select>
            </div>
            <div class="champ">
              <label for="age">{t["age"]}</label>
              <input id="age" type="number" inputmode="numeric" min="18" max="100" placeholder="31">
            </div>
            <div class="champ">
              <label for="taille">{t["taille"]}</label>
              <input id="taille" type="number" inputmode="numeric" min="120" max="230" placeholder="178">
            </div>
            <div class="champ">
              <label for="poids">{t["poids"]}</label>
              <input id="poids" type="number" inputmode="decimal" min="30" max="300" step="0.1" placeholder="75">
            </div>
            <div class="champ large">
              <label for="activite">{t["activite"]}</label>
              <select id="activite">
{chr(10).join(f'                <option value="{v}"{" selected" if v == "1.55" else ""}>{x}</option>' for v, x in zip(["1.2", "1.375", "1.55", "1.725", "1.9"], t["niveaux"]))}
              </select>
            </div>
            <div class="champ">
              <label for="objectif">{t["objectif"]}</label>
              <select id="objectif">
                <option value="lose">{t["perte"]}</option>
                <option value="maintain" selected>{t["maintien"]}</option>
                <option value="gain">{t["prise"]}</option>
              </select>
            </div>
            <div class="champ">
              <label for="rythme">{t["rythme"]}</label>
              <select id="rythme"></select>
            </div>
          </div>
    </form>

    <section class="carte resultat" aria-live="polite">
          <p class="vide" id="vide">{t["vide"]}</p>
          <div id="sortie" hidden>
            <div class="ligne total">
              <span>{t["kcal"]}</span><b id="kcal" data-flottant="{t["flottant"]}">—</b>
            </div>
            <div class="ligne">
              <span>{t["prot"]} <em id="protDetail"></em></span><b id="prot">—</b>
            </div>
            <div class="ligne">
              <span>{t["gluc"]}</span><b id="gluc">—</b>
            </div>
            <div class="ligne">
              <span>{t["lip"]} <em id="lipDetail"></em></span><b id="lip">—</b>
            </div>
            <div class="ligne">
              <span>{t["fib"]}</span><b id="fib">—</b>
            </div>
            <p class="note" id="plancher" hidden></p>
          </div>
        </section>
  </div>'''


def script(locale, paliers, maintien, majeur, plancher_app, part, note_a, note_b):
    return [
        ("'Douce — ≈10 % sous ta dépense'", repr(paliers[0])), ("'Modérée — ≈15 % sous ta dépense'", repr(paliers[1])), ("'Intense — ≈20 % sous ta dépense'", repr(paliers[2])),
        ("'Maintien — à ta dépense'", repr(maintien)),
        ("'Douce — ≈5 % au-dessus de ta dépense'", repr(paliers[3])), ("'Modérée — ≈10 % au-dessus de ta dépense'", repr(paliers[4])), ("'Intense — ≈15 % au-dessus de ta dépense'", repr(paliers[5])),
        ("'Basal est réservée aux personnes majeures et ne calcule pas de besoins caloriques avant 18 ans : à cet âge, ils se déterminent avec un professionnel de santé.'", repr(majeur)),
        ("'— plancher appliqué'", repr(plancher_app)), ("'— 30 % des calories'", repr(part)),
        ("'Le rythme choisi descendrait sous ton métabolisme de base (' +", repr(note_a) + ' +'),
        ("""' kcal). L’objectif a été relevé à ce seuil : ' +
        'un déficit en dessous ne se tient pas dans la durée.'""", repr(note_b)),
        ("'fr-FR'", repr(locale)),
    ]


PAGES = {
    'en': {
        'slug': '/en/macro-calculator.html',
        'tete': dict(title='Macro calculator: protein, carbs and fat — Basal', locale='en_GB',
                     description='Work out your macros: protein and fat anchored to body weight, carbs filling the rest. Free, no sign-up, nothing is sent.',
                     og_title='Macro calculator: protein, carbs and fat', og_description='Protein and fat anchored to body weight, carbs filling the rest — and why a simple percentage of the total gets it wrong.'),
        'main': f'''<main id="contenu" class="wrap">
  <nav class="fil" aria-label="Breadcrumb"><a href="/en/">Home</a><span aria-hidden="true">›</span><a href="/en/calculators/">Calculators</a><span aria-hidden="true">›</span>Macros</nav>
  <header class="article-tete" style="border:0;padding-bottom:0">
    <p class="surtitre">Free calculator</p>
    <h1>Work out your macros</h1>
    <p class="chapeau">The same rules as the app: protein and fat anchored to your body weight, carbs filling
    the rest. Nothing is sent anywhere — the calculation runs in your browser.</p>
  </header>

{formulaire(dict(sexe='Sex', homme='Male', femme='Female', age='Age', taille='Height (cm)', poids='Weight (kg)', activite='Activity level',
    niveaux=['Sedentary — little or no exercise · under 5,000 steps/day', 'Lightly active — 1 to 3 sessions a week · 5,000 to 7,500 steps/day',
             'Moderately active — 3 to 5 sessions a week · 7,500 to 10,000 steps/day', 'Active — 6 to 7 sessions a week · 10,000 to 12,500 steps/day',
             'Very active — physical job or training twice a day · 12,500+ steps/day'],
    objectif='Goal', perte='Weight loss', maintien='Maintenance', prise='Muscle gain', rythme='Pace',
    vide='Fill in the four number fields to see the result.', kcal='Calorie target', flottant='Target', prot='Protein', gluc='Carbs', lip='Fat', fib='Fibre'))}

  <div class="article" style="grid-template-columns:minmax(0,1fr);padding-top:56px">
    <div class="corps">
      <div class="encadre">
        <p>
          <strong>These are starting points, not a prescription.</strong> The calculation rests on an
          estimate of expenditure that validation studies commonly report as about 10% off — that is
          250 kcal a day on an expenditure of 2,500. Your macros inherit that uncertainty. What corrects
          them is not a finer formula, it is watching your own data over several weeks.
        </p>
      </div>

      <h2>Why not a simple percentage</h2>
      <p>
        The most common method splits calories into fixed shares — for example 30% protein, 40% carbs,
        30% fat. It has a flaw that only shows in the cases where it matters most: <strong>it makes your
        needs depend on your calorie target</strong>, when they depend on your body.
      </p>
      <p>
        On a low target, 30% of 1,100 kcal gives about 82 g of protein and 37 g of fat. Both are too low,
        and they become too low precisely when they matter most — during weight loss, when the aim is to
        keep muscle and hormonal balance.
      </p>
      <p>
        Hence the order used here: protein and fat are set first, from body weight. Carbs take what is left.
      </p>

      <h2>The calculation in detail</h2>

      <h3>Protein</h3>
      <p>
        In grams per kilogram, depending on the goal, with a top-up from three sessions a week — the point
        at which training creates a real extra need.
      </p>
      <ul class="liste">
        <li><strong>Loss</strong> — 1.8 g/kg, or 2.2 g/kg if you train.</li>
        <li><strong>Maintenance</strong> — 1.4 g/kg, or 1.8 g/kg if you train.</li>
        <li><strong>Muscle gain</strong> — 1.6 g/kg, or 2.0 g/kg if you train.</li>
      </ul>
      <p>
        These values sit within the range the resistance-training literature commonly reports, 1.6 to
        2.2 g/kg, with returns that flatten beyond it.
      </p>

      <h3>Reference weight, and why it is not always your weight</h3>
      <p>
        Multiplying by total weight becomes a problem above a certain build: excess fat tissue does not
        have the same protein needs as the rest of the body. The calculation therefore uses your actual
        weight up to a BMI of 25, then counts only <strong>a quarter of the excess</strong> above it.
      </p>
      <p>
        That is the factor of the clinical adjusted-weight formula, used exactly where total weight would
        distort a prescription. The threshold sits at the <em>top</em> of the so-called normal range, not in
        the middle: a low threshold would trim protein for people who have nothing to trim. In practice, a
        person of ordinary build sees no difference.
      </p>

      <h3>Fat</h3>
      <p>
        The larger of two values is used: <strong>0.8 g per kilogram of reference weight</strong>, or
        <strong>30% of calories</strong>. The first is a floor that does not depend on the calorie total —
        below it, the risk of essential fatty acid deficiency and hormonal disruption is documented,
        whatever the goal.
      </p>

      <h3>Carbs and fibre</h3>
      <p>
        Carbs take what remains once protein and fat are covered, without ever going below zero: in an
        extreme case — very high weight and very low target — the priority goes to the safety of the other
        two rather than to the exact total. Fibre follows the standard recommendation of 14 g per 1,000 kcal.
      </p>

      <h3>The calorie floor</h3>
      <p>
        The calorie target never goes below your basal metabolic rate, nor below 800 kcal. It is not an
        arbitrary minimum: it is an individual physiological threshold, calculated from your sex, age, weight
        and height. If the pace you chose would take you lower, the calculator tells you instead of quietly
        correcting it.
      </p>

      <div class="appel">
        <p class="appel-t">Track these macros day to day</p>
        <p>
          Basal applies exactly these rules, then corrects the calorie target as it compares what you log
          with how your weight actually changes. Tracking calories, macros, weight and workouts is free,
          unlimited and needs no account.
        </p>
        {stores('en', 'en-macro-calculator', 'Get it on Google Play', 'Download on the App Store', 'gb')}
      </div>

      <h2>Going further</h2>
      <ul class="liste">
        <li><a href="/en/calorie-calculator.html">Work out your energy expenditure</a> — the number everything
        else comes from.</li>
        <li><a href="/en/protein-calculator.html">How much protein you need</a>.</li>
        <li><a href="/en/recipes/">Recipes with their calories and macros</a>.</li>
      </ul>
    </div>
  </div>

  <aside class="note-page">
    <p>This tool is for information only. Basal is not a medical device and does not replace advice
    from a health professional. For adults only.</p>
  </aside>
</main>''',
        'script': script('en-GB', ['Gentle — ≈10% below your expenditure', 'Moderate — ≈15% below your expenditure', 'Aggressive — ≈20% below your expenditure',
                                   'Gentle — ≈5% above your expenditure', 'Moderate — ≈10% above your expenditure', 'Aggressive — ≈15% above your expenditure'],
                         'Maintenance — at your expenditure',
                         'Basal is for adults only and does not calculate calorie needs under 18: at that age, they should be set with a health professional.',
                         '— floor applied', '— 30% of calories', 'The pace you chose would go below your basal metabolic rate (',
                         ' kcal). The target has been raised to that threshold: a deficit below it cannot be sustained.'),
        'ld': ld('Macro calculator: protein, carbs and fat', '/en/macro-calculator.html',
                 'Macronutrients from energy expenditure: protein and fat anchored to body weight, carbs filling the rest.', 'en',
                 '/en/', 'Home', '/en/calculators/', 'Calculators', 'Macros'),
    },
    'es': {
        'slug': '/es/calculadora-macros.html',
        'tete': dict(title='Calculadora de macros: proteínas, hidratos y grasas — Basal', locale='es_ES',
                     description='Calcula tus macros: proteínas y grasas ancladas al peso corporal, hidratos para completar. Gratis, sin registro, no se envía nada.',
                     og_title='Calculadora de macros: proteínas, hidratos y grasas', og_description='Proteínas y grasas ancladas al peso, hidratos para completar — y por qué un simple porcentaje del total se equivoca.'),
        'main': f'''<main id="contenu" class="wrap">
  <nav class="fil" aria-label="Ruta de navegación"><a href="/es/">Inicio</a><span aria-hidden="true">›</span><a href="/es/calculadoras/">Calculadoras</a><span aria-hidden="true">›</span>Macros</nav>
  <header class="article-tete" style="border:0;padding-bottom:0">
    <p class="surtitre">Calculadora gratis</p>
    <h1>Calcula tus macros</h1>
    <p class="chapeau">Las mismas reglas que la aplicación: proteínas y grasas ancladas a tu peso corporal, los
    hidratos para completar. No se envía nada — el cálculo se hace en tu navegador.</p>
  </header>

{formulaire(dict(sexe='Sexo', homme='Hombre', femme='Mujer', age='Edad', taille='Altura (cm)', poids='Peso (kg)', activite='Nivel de actividad',
    niveaux=['Sedentario — poco o ningún deporte · menos de 5.000 pasos/día', 'Ligeramente activo — 1 a 3 sesiones por semana · 5.000 a 7.500 pasos/día',
             'Moderadamente activo — 3 a 5 sesiones por semana · 7.500 a 10.000 pasos/día', 'Activo — 6 a 7 sesiones por semana · 10.000 a 12.500 pasos/día',
             'Muy activo — trabajo físico o doble entrenamiento · más de 12.500 pasos/día'],
    objectif='Objetivo', perte='Perder peso', maintien='Mantenimiento', prise='Ganar músculo', rythme='Ritmo',
    vide='Rellena los cuatro campos numéricos para ver el resultado.', kcal='Objetivo calórico', flottant='Objetivo', prot='Proteínas', gluc='Hidratos', lip='Grasas', fib='Fibra'))}

  <div class="article" style="grid-template-columns:minmax(0,1fr);padding-top:56px">
    <div class="corps">
      <div class="encadre">
        <p>
          <strong>Son puntos de partida, no una receta médica.</strong> El cálculo se apoya en una
          estimación del gasto cuyos estudios de validación suelen indicar un 10 % de desviación — es
          decir, 250 kcal al día sobre un gasto de 2.500. Tus macros heredan esa incertidumbre. Lo que
          los corrige no es una fórmula más fina, sino observar tus datos durante varias semanas.
        </p>
      </div>

      <h2>Por qué no un simple porcentaje</h2>
      <p>
        El método más extendido reparte las calorías en partes fijas — por ejemplo 30 % de proteínas,
        40 % de hidratos y 30 % de grasas. Tiene un defecto que solo se ve en los casos donde de verdad
        importa: <strong>hace depender tus necesidades de tu objetivo calórico</strong>, cuando dependen de tu cuerpo.
      </p>
      <p>
        Con un objetivo bajo, el 30 % de 1.100 kcal da unos 82 g de proteínas y 37 g de grasas. Las dos
        cifras se quedan cortas, y justo en el momento en que más importan — durante una pérdida de peso,
        cuando se trata de conservar la masa muscular y el equilibrio hormonal.
      </p>
      <p>
        De ahí el orden que se sigue aquí: las proteínas y las grasas se fijan primero, a partir del peso
        corporal. Los hidratos ocupan lo que queda.
      </p>

      <h2>El detalle del cálculo</h2>

      <h3>Las proteínas</h3>
      <p>
        En gramos por kilo, según el objetivo, con un suplemento a partir de tres sesiones por semana —
        umbral a partir del cual el entrenamiento crea una necesidad adicional real.
      </p>
      <ul class="liste">
        <li><strong>Pérdida</strong> — 1,8 g/kg, o 2,2 g/kg si entrenas.</li>
        <li><strong>Mantenimiento</strong> — 1,4 g/kg, o 1,8 g/kg si entrenas.</li>
        <li><strong>Ganar músculo</strong> — 1,6 g/kg, o 2,0 g/kg si entrenas.</li>
      </ul>
      <p>
        Estos valores están dentro del rango que suele indicar la literatura sobre entrenamiento de fuerza,
        de 1,6 a 2,2 g/kg, con beneficios que se aplanan por encima.
      </p>

      <h3>El peso de referencia, y por qué no siempre es tu peso</h3>
      <p>
        Multiplicar por el peso total plantea un problema a partir de cierta corpulencia: el tejido graso
        sobrante no tiene las mismas necesidades de proteínas que el resto del cuerpo. El cálculo usa por
        tanto el peso real hasta un IMC de 25 y, por encima, solo cuenta <strong>la cuarta parte del exceso</strong>.
      </p>
      <p>
        Es el factor de la fórmula clínica del peso ajustado, que se usa justo cuando el peso total
        falsearía una pauta. El umbral está en la parte <em>alta</em> del rango llamado normal, no en medio:
        un umbral bajo recortaría las proteínas de personas a las que no hay nada que recortar. En la
        práctica, una persona de complexión normal no ve ninguna diferencia.
      </p>

      <h3>Las grasas</h3>
      <p>
        Se toma el mayor de dos valores: <strong>0,8 g por kilo de peso de referencia</strong>, o
        <strong>el 30 % de las calorías</strong>. El primero es un mínimo independiente del total calórico —
        por debajo, el riesgo de carencia de ácidos grasos esenciales y de alteración hormonal está
        documentado, sea cual sea el objetivo.
      </p>

      <h3>Los hidratos y la fibra</h3>
      <p>
        Los hidratos ocupan lo que queda una vez cubiertas las proteínas y las grasas, sin bajar nunca de
        cero: en un caso extremo — peso muy alto y objetivo muy bajo — la prioridad es la seguridad de las
        otras dos antes que la exactitud del total. La fibra sigue la recomendación habitual de 14 g por cada 1.000 kcal.
      </p>

      <h3>El mínimo calórico</h3>
      <p>
        El objetivo calórico nunca baja de tu metabolismo basal, ni de 800 kcal. No es un mínimo
        arbitrario: es un umbral fisiológico individual, calculado a partir de tu sexo, tu edad, tu peso y
        tu altura. Si el ritmo elegido te llevara más abajo, la calculadora te lo dice en lugar de corregirlo
        en silencio.
      </p>

      <div class="appel">
        <p class="appel-t">Sigue estos macros a diario</p>
        <p>
          Basal aplica exactamente estas reglas y luego corrige el objetivo calórico a medida que compara lo
          que registras con la evolución real de tu peso. El seguimiento de calorías, macros, peso y
          entrenamientos es gratis, sin límite y sin cuenta obligatoria.
        </p>
        {stores('es', 'es-calculadora-macros', 'Disponible en Google Play', 'Descargar en la App Store', 'es')}
      </div>

      <h2>Para saber más</h2>
      <ul class="liste">
        <li><a href="/es/calculadora-calorias.html">Calcula tu gasto energético</a> — la cifra de la que sale todo lo demás.</li>
        <li><a href="/es/calculadora-proteinas.html">Cuántas proteínas necesitas</a>.</li>
        <li><a href="/es/recetas/">Recetas con sus calorías y sus macros</a>.</li>
      </ul>
    </div>
  </div>

  <aside class="note-page">
    <p>Esta herramienta es informativa. Basal no es un dispositivo médico y no sustituye el consejo de
    un profesional sanitario. Reservada a personas mayores de edad.</p>
  </aside>
</main>''',
        'script': script('es-ES', ['Suave — ≈10 % por debajo de tu gasto', 'Moderado — ≈15 % por debajo de tu gasto', 'Intenso — ≈20 % por debajo de tu gasto',
                                   'Suave — ≈5 % por encima de tu gasto', 'Moderado — ≈10 % por encima de tu gasto', 'Intenso — ≈15 % por encima de tu gasto'],
                         'Mantenimiento — igual a tu gasto',
                         'Basal está reservada a personas mayores de edad y no calcula necesidades calóricas antes de los 18 años: a esa edad se determinan con un profesional de la salud.',
                         '— mínimo aplicado', '— 30 % de las calorías', 'El ritmo elegido bajaría de tu metabolismo basal (',
                         ' kcal). El objetivo se ha subido a ese umbral: un déficit por debajo no se sostiene en el tiempo.'),
        'ld': ld('Calculadora de macros: proteínas, hidratos y grasas', '/es/calculadora-macros.html',
                 'Cálculo de los macronutrientes a partir del gasto energético: proteínas y grasas ancladas al peso corporal, hidratos para completar.', 'es',
                 '/es/', 'Inicio', '/es/calculadoras/', 'Calculadoras', 'Macros'),
    },
    'de': {
        'slug': '/de/makrorechner.html',
        'tete': dict(title='Makrorechner: Eiweiß, Kohlenhydrate und Fett — Basal', locale='de_DE',
                     description='Berechne deine Makros: Eiweiß und Fett am Körpergewicht verankert, Kohlenhydrate für den Rest. Kostenlos, ohne Anmeldung, es wird nichts gesendet.',
                     og_title='Makrorechner: Eiweiß, Kohlenhydrate und Fett', og_description='Eiweiß und Fett am Körpergewicht verankert, Kohlenhydrate für den Rest — und warum ein fester Prozentsatz danebenliegt.'),
        'main': f'''<main id="contenu" class="wrap">
  <nav class="fil" aria-label="Brotkrümelnavigation"><a href="/de/">Startseite</a><span aria-hidden="true">›</span><a href="/de/rechner/">Rechner</a><span aria-hidden="true">›</span>Makros</nav>
  <header class="article-tete" style="border:0;padding-bottom:0">
    <p class="surtitre">Kostenloser Rechner</p>
    <h1>Berechne deine Makros</h1>
    <p class="chapeau">Dieselben Regeln wie in der App: Eiweiß und Fett am Körpergewicht verankert,
    Kohlenhydrate für den Rest. Es wird nichts gesendet — die Berechnung läuft in deinem Browser.</p>
  </header>

{formulaire(dict(sexe='Geschlecht', homme='Mann', femme='Frau', age='Alter', taille='Größe (cm)', poids='Gewicht (kg)', activite='Aktivitätsniveau',
    niveaux=['Sitzend — wenig oder kein Sport · unter 5.000 Schritte/Tag', 'Leicht aktiv — 1 bis 3 Einheiten pro Woche · 5.000 bis 7.500 Schritte/Tag',
             'Mäßig aktiv — 3 bis 5 Einheiten pro Woche · 7.500 bis 10.000 Schritte/Tag', 'Aktiv — 6 bis 7 Einheiten pro Woche · 10.000 bis 12.500 Schritte/Tag',
             'Sehr aktiv — körperliche Arbeit oder zweimal täglich Training · über 12.500 Schritte/Tag'],
    objectif='Ziel', perte='Abnehmen', maintien='Gewicht halten', prise='Muskelaufbau', rythme='Tempo',
    vide='Fülle die vier Zahlenfelder aus, um das Ergebnis zu sehen.', kcal='Kalorienziel', flottant='Ziel', prot='Eiweiß', gluc='Kohlenhydrate', lip='Fett', fib='Ballaststoffe'))}

  <div class="article" style="grid-template-columns:minmax(0,1fr);padding-top:56px">
    <div class="corps">
      <div class="encadre">
        <p>
          <strong>Das sind Startwerte, keine Verordnung.</strong> Die Berechnung beruht auf einer
          Schätzung des Verbrauchs, für die Validierungsstudien üblicherweise etwa 10 % Abweichung
          angeben — also 250 kcal pro Tag bei einem Verbrauch von 2.500. Deine Makros erben diese
          Unsicherheit. Korrigiert werden sie nicht durch eine feinere Formel, sondern durch den Blick
          auf deine Daten über mehrere Wochen.
        </p>
      </div>

      <h2>Warum kein fester Prozentsatz</h2>
      <p>
        Die verbreitetste Methode teilt die Kalorien in feste Anteile auf — zum Beispiel 30 % Eiweiß,
        40 % Kohlenhydrate, 30 % Fett. Sie hat einen Fehler, der genau dort auffällt, wo es darauf
        ankommt: <strong>Sie macht deinen Bedarf von deinem Kalorienziel abhängig</strong>, obwohl er von
        deinem Körper abhängt.
      </p>
      <p>
        Bei einem niedrigen Ziel ergeben 30 % von 1.100 kcal etwa 82 g Eiweiß und 37 g Fett. Beides ist
        zu wenig, und zwar genau dann, wenn es am meisten zählt — beim Abnehmen, wenn Muskelmasse und
        hormonelles Gleichgewicht erhalten bleiben sollen.
      </p>
      <p>
        Daher die Reihenfolge hier: Eiweiß und Fett werden zuerst festgelegt, ausgehend vom Körpergewicht.
        Die Kohlenhydrate bekommen den Rest.
      </p>

      <h2>Die Berechnung im Detail</h2>

      <h3>Eiweiß</h3>
      <p>
        In Gramm pro Kilogramm, je nach Ziel, mit einem Zuschlag ab drei Einheiten pro Woche — ab dieser
        Schwelle erzeugt das Training einen echten Mehrbedarf.
      </p>
      <ul class="liste">
        <li><strong>Abnehmen</strong> — 1,8 g/kg, oder 2,2 g/kg, wenn du trainierst.</li>
        <li><strong>Gewicht halten</strong> — 1,4 g/kg, oder 1,8 g/kg, wenn du trainierst.</li>
        <li><strong>Muskelaufbau</strong> — 1,6 g/kg, oder 2,0 g/kg, wenn du trainierst.</li>
      </ul>
      <p>
        Diese Werte liegen in dem Bereich, den die Literatur zum Krafttraining üblicherweise nennt,
        1,6 bis 2,2 g/kg, mit abflachendem Nutzen darüber.
      </p>

      <h3>Das Referenzgewicht, und warum es nicht immer dein Gewicht ist</h3>
      <p>
        Mit dem Gesamtgewicht zu multiplizieren wird ab einer gewissen Statur zum Problem: überschüssiges
        Fettgewebe hat nicht denselben Eiweißbedarf wie der Rest des Körpers. Die Berechnung nutzt deshalb
        das tatsächliche Gewicht bis zu einem BMI von 25 und zählt darüber nur <strong>ein Viertel des Überschusses</strong>.
      </p>
      <p>
        Das ist der Faktor der klinischen Formel für das angepasste Gewicht, die genau dort verwendet wird,
        wo das Gesamtgewicht eine Empfehlung verfälschen würde. Die Schwelle liegt am <em>oberen</em> Ende des
        sogenannten Normalbereichs, nicht in der Mitte: Eine niedrige Schwelle würde Menschen Eiweiß
        streichen, bei denen es nichts zu streichen gibt. In der Praxis sieht eine Person mit
        durchschnittlicher Statur keinen Unterschied.
      </p>

      <h3>Fett</h3>
      <p>
        Verwendet wird der größere von zwei Werten: <strong>0,8 g pro Kilogramm Referenzgewicht</strong>
        oder <strong>30 % der Kalorien</strong>. Der erste ist eine Untergrenze, unabhängig von der
        Kaloriensumme — darunter ist das Risiko eines Mangels an essenziellen Fettsäuren und hormoneller
        Störungen belegt, unabhängig vom Ziel.
      </p>

      <h3>Kohlenhydrate und Ballaststoffe</h3>
      <p>
        Die Kohlenhydrate bekommen, was nach Eiweiß und Fett übrig bleibt, ohne je unter null zu fallen:
        In einem Extremfall — sehr hohes Gewicht und sehr niedriges Ziel — hat die Sicherheit der beiden
        anderen Vorrang vor der genauen Summe. Ballaststoffe folgen der üblichen Empfehlung von 14 g pro 1.000 kcal.
      </p>

      <h3>Die Kalorienuntergrenze</h3>
      <p>
        Das Kalorienziel liegt nie unter deinem Grundumsatz und nie unter 800 kcal. Das ist kein
        willkürliches Minimum, sondern eine individuelle physiologische Schwelle, berechnet aus
        Geschlecht, Alter, Gewicht und Größe. Würde das gewählte Tempo dich darunter bringen, sagt dir der
        Rechner das, statt still zu korrigieren.
      </p>

      <div class="appel">
        <p class="appel-t">Diese Makros im Alltag verfolgen</p>
        <p>
          Basal wendet genau diese Regeln an und korrigiert das Kalorienziel dann, indem es deine Einträge
          mit der tatsächlichen Entwicklung deines Gewichts vergleicht. Das Tracking von Kalorien, Makros,
          Gewicht und Training ist kostenlos, unbegrenzt und braucht kein Konto.
        </p>
        {stores('de', 'de-makrorechner', 'Jetzt bei Google Play', 'Laden im App Store', 'de')}
      </div>

      <h2>Weiterlesen</h2>
      <ul class="liste">
        <li><a href="/de/kalorienrechner.html">Berechne deinen Energieverbrauch</a> — die Zahl, aus der alles andere folgt.</li>
        <li><a href="/de/proteinrechner.html">Wie viel Eiweiß du brauchst</a>.</li>
        <li><a href="/de/rezepte/">Rezepte mit Kalorien und Makros</a>.</li>
      </ul>
    </div>
  </div>

  <aside class="note-page">
    <p>Dieses Werkzeug dient nur der Information. Basal ist kein Medizinprodukt und ersetzt nicht den
    Rat medizinischen Fachpersonals. Nur für Volljährige.</p>
  </aside>
</main>''',
        'script': script('de-DE', ['Sanft — ≈10 % unter deinem Verbrauch', 'Moderat — ≈15 % unter deinem Verbrauch', 'Intensiv — ≈20 % unter deinem Verbrauch',
                                   'Sanft — ≈5 % über deinem Verbrauch', 'Moderat — ≈10 % über deinem Verbrauch', 'Intensiv — ≈15 % über deinem Verbrauch'],
                         'Gewicht halten — entspricht deinem Verbrauch',
                         'Basal ist Volljährigen vorbehalten und berechnet vor 18 Jahren keinen Kalorienbedarf: In diesem Alter bestimmt man ihn mit medizinischem Fachpersonal.',
                         '— Untergrenze angewendet', '— 30 % der Kalorien', 'Das gewählte Tempo läge unter deinem Grundumsatz (',
                         ' kcal). Das Ziel wurde auf diese Schwelle angehoben: Ein Defizit darunter lässt sich nicht durchhalten.'),
        'ld': ld('Makrorechner: Eiweiß, Kohlenhydrate und Fett', '/de/makrorechner.html',
                 'Berechnung der Makronährstoffe aus dem Energieverbrauch: Eiweiß und Fett am Körpergewicht verankert, Kohlenhydrate für den Rest.', 'de',
                 '/de/', 'Startseite', '/de/rechner/', 'Rechner', 'Makros'),
    },
}
