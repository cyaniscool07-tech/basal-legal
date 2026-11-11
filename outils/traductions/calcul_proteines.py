from calcul_macros import ld  # noqa: E402  (même structure JSON-LD)

FR = '/calcul-proteines.html'
DATE = '2026-11-11'


def main(t):
    return f'''<main id="contenu" class="wrap">
  <nav class="fil" aria-label="{t["fil"]}"><a href="{t["accueil_url"]}">{t["accueil"]}</a><span aria-hidden="true">›</span><a href="{t["hub_url"]}">{t["hub"]}</a><span aria-hidden="true">›</span>{t["court"]}</nav>
  <header class="article-tete" style="border:0;padding-bottom:0">
    <p class="surtitre">{t["surtitre"]}</p>
    <h1>{t["h1"]}</h1>
    <p class="chapeau">{t["chapeau"]}</p>
  </header>

  <div class="outil">
    <form class="carte" id="calc" novalidate>
      <div class="champs">
        <div class="champ"><label for="poids">{t["poids"]}</label><input id="poids" type="number" inputmode="decimal" step="0.1" min="30" max="300" placeholder="70"></div>
        <div class="champ"><label for="taille">{t["taille"]}</label><input id="taille" type="number" inputmode="numeric" min="120" max="230" placeholder="175"></div>
        <div class="champ">
          <label for="objectif">{t["objectif"]}</label>
          <select id="objectif">
            <option value="perte">{t["perte"]}</option>
            <option value="maintien" selected>{t["maintien"]}</option>
            <option value="prise">{t["prise"]}</option>
          </select>
        </div>
        <div class="champ large">
          <span id="sport-t" style="font-weight:600;font-size:.9rem">{t["entrainement"]}</span>
          <div class="segment" role="radiogroup" aria-labelledby="sport-t">
            <input type="radio" name="sport" id="peu" value="0" checked><label for="peu">{t["moins3"]}</label>
            <input type="radio" name="sport" id="sportif" value="1"><label for="sportif">{t["plus3"]}</label>
          </div>
        </div>
      </div>
    </form>

    <section class="carte resultat" aria-live="polite" aria-labelledby="res-t">
      <p class="surtitre" id="res-t">{t["res"]}</p>
      <div class="grand"><span id="total" data-flottant="{t["flottant"]}">—</span><small>{t["parjour"]}</small></div>
      <p id="message" style="margin:14px 0 0">{t["vide"]}</p>
      <div id="sortie" hidden>
        <div class="sous">
          <div><b id="s-gkg">—</b><span>{t["gkg"]}</span></div>
          <div><b id="s-kcal">—</b><span>{t["kcal"]}</span></div>
        </div>
        <p id="reference" style="margin:0"></p>
      </div>
    </section>
  </div>

  <div class="article" style="grid-template-columns:minmax(0,1fr);padding-top:56px">
    <div class="corps">
{t["corps"]}
      <div class="appel-contexte">
        <div><strong>{t["appel_t"]}</strong><p>{t["appel"]}</p></div>
        <a class="bouton vif" href="{t["accueil_url"]}#download">{t["dl"]}</a>
      </div>
    </div>
  </div>

  <aside class="note-page">
    <p>{t["note"]}</p>
  </aside>
</main>'''


def script(locale, vide, bornes, reel, ref_a, ref_b, ref_c):
    return [
        ("'Renseigne ton poids et ta taille pour voir le résultat.'", repr(vide)),
        ("'Vérifie les valeurs : poids de 30 à 300 kg, taille de 120 à 230 cm.'", repr(bornes)),
        ("'Poids de référence : ton poids réel (IMC de 25 ou moins).'", repr(reel)),
        ("'Poids de référence : ' + dec(reference) + ' kg. Au-delà d’un IMC de 25 (' + dec(seuil) + ' kg pour ta taille), seul un quart de l’excédent compte.'",
         f"{ref_a!r} + dec(reference) + {ref_b!r} + dec(seuil) + {ref_c!r}"),
        ("'fr-FR'", repr(locale)),
    ]


PAGES = {
    'en': {
        'slug': '/en/protein-calculator.html',
        'tete': dict(title='Protein calculator: how much protein per day | Basal', locale='en_GB',
                     description='How much protein a day for your weight, goal and training: the grid used by the Basal app. Free, no sign-up, nothing is sent.',
                     og_title='Protein calculator: how much protein per day', og_description='For your weight, goal and training, with the grid used by the Basal app.'),
        'main': main(dict(fil='Breadcrumb', accueil='Home', accueil_url='/en/', hub='Calculators', hub_url='/en/calculators/', court='Protein',
            surtitre='Free calculator', h1='Work out your daily protein needs',
            chapeau='Based on your weight, goal and training, with the grid the Basal app uses. It applies to a reference weight, which avoids overestimating needs when weight is high. Nothing is sent.',
            poids='Weight (kg)', taille='Height (cm)', objectif='Goal', perte='Lose weight', maintien='Maintain', prise='Build muscle', entrainement='Training',
            moins3='Fewer than 3 sessions a week', plus3='3 sessions or more', res='Your protein needs', flottant='Protein', parjour='g / day',
            vide='Enter your weight and height to see the result.', gkg='g per kg of reference weight', kcal='kcal supplied (4 kcal per gram)',
            corps='''      <h2>The grid used</h2>
      <p class="formule"><code>protein (g) = reference weight × grams per kilo</code></p>
      <div class="tableau">
        <table>
          <caption>Grams of protein per kilo of reference weight</caption>
          <thead><tr><th scope="col">Goal</th><th scope="col" class="n">Fewer than 3 sessions a week</th><th scope="col" class="n">3 sessions or more</th></tr></thead>
          <tbody>
            <tr><td>Lose weight</td><td class="n">1.8</td><td class="n">2.2</td></tr>
            <tr><td>Maintain</td><td class="n">1.4</td><td class="n">1.8</td></tr>
            <tr><td>Build muscle</td><td class="n">1.6</td><td class="n">2.0</td></tr>
          </tbody>
        </table>
        <p class="source">The grid of the Basal app (version 1.4). Needs go up in a deficit, where protein protects muscle mass.</p>
      </div>
      <div class="calcul" role="group" aria-label="Examples">
        <div class="titre">Examples, for 175 cm</div>
        <div class="ligne"><span>70 kg, weight loss, 3 sessions or more: 70 × 2.2</span><b>154 g</b></div>
        <div class="ligne"><span>70 kg, maintenance, fewer than 3 sessions: 70 × 1.4</span><b>98 g</b></div>
        <div class="ligne"><span>120 kg, weight loss, 3 sessions or more: 87.4 × 2.2</span><b>192 g</b></div>
      </div>

      <h2>Why a reference weight</h2>
      <p>Protein needs follow lean mass, not total weight. Applying 2.2 g per kilo at 120 kg would give 264 g a day, over 1,000 kcal before counting anything else: no recommendation supports such a figure. Up to a BMI of 25, the reference weight is therefore your actual weight; above it, only a quarter of the excess counts. This is the adjusted-weight formula, the standard approximation when lean mass is not measured.</p>

      <h2>And the rest of the plate</h2>
      <p>Protein is only part of the calculation. The <a href="/en/macro-calculator.html">macro calculator</a> adds fat and carbs, with the same rules, and the <a href="/en/recipes/">calculated recipes</a> show their protein per serving.</p>

      <h2>What this calculation does not know</h2>
      <div class="inconnu">
        <p><strong>It is an order of magnitude.</strong> It rests on the usual ranges in sports nutrition, not on a measurement of your body composition.</p>
        <p style="margin:0"><strong>Some situations call for a health professional</strong>: kidney disease, pregnancy, a prescribed diet, an eating disorder.</p>
      </div>
''', appel_t='Your protein target, every day',
            appel='Basal calculates your protein with this grid and tracks it meal by meal, with separate protein for training and rest days in Premium.',
            dl='Download', note='This tool is for information only. Basal is not a medical device and does not replace advice from a health professional.')),
        'script': script('en-GB', 'Enter your weight and height to see the result.', 'Check the values: weight from 30 to 300 kg, height from 120 to 230 cm.',
                         'Reference weight: your actual weight (BMI of 25 or less).', 'Reference weight: ', ' kg. Above a BMI of 25 (', ' kg for your height), only a quarter of the excess counts.'),
        'ld': ld('Protein calculator: how much protein per day', '/en/protein-calculator.html', 'Daily protein needs from weight, goal and training, on a reference weight.', 'en',
                 '/en/', 'Home', '/en/calculators/', 'Calculators', 'Protein'),
    },
    'es': {
        'slug': '/es/calculadora-proteinas.html',
        'tete': dict(title='Calculadora de proteínas: cuántas proteínas al día | Basal', locale='es_ES',
                     description='Cuántas proteínas al día según tu peso, tu objetivo y tu entrenamiento: la tabla de la aplicación Basal. Gratis, sin registro, no se envía nada.',
                     og_title='Calculadora de proteínas: cuántas proteínas al día', og_description='Según tu peso, tu objetivo y tu entrenamiento, con la tabla de la aplicación Basal.'),
        'main': main(dict(fil='Ruta de navegación', accueil='Inicio', accueil_url='/es/', hub='Calculadoras', hub_url='/es/calculadoras/', court='Proteínas',
            surtitre='Calculadora gratis', h1='Calcula tus necesidades de proteínas al día',
            chapeau='Según tu peso, tu objetivo y tu entrenamiento, con la tabla que usa la aplicación Basal. Se aplica a un peso de referencia, que evita sobrestimar las necesidades cuando el peso es alto. No se envía nada.',
            poids='Peso (kg)', taille='Altura (cm)', objectif='Objetivo', perte='Perder peso', maintien='Mantener', prise='Ganar músculo', entrainement='Entrenamiento',
            moins3='Menos de 3 sesiones por semana', plus3='3 sesiones o más', res='Tus necesidades de proteínas', flottant='Proteínas', parjour='g / día',
            vide='Indica tu peso y tu altura para ver el resultado.', gkg='g por kg de peso de referencia', kcal='kcal aportadas (4 kcal por gramo)',
            corps='''      <h2>La tabla utilizada</h2>
      <p class="formule"><code>proteínas (g) = peso de referencia × gramos por kilo</code></p>
      <div class="tableau">
        <table>
          <caption>Gramos de proteínas por kilo de peso de referencia</caption>
          <thead><tr><th scope="col">Objetivo</th><th scope="col" class="n">Menos de 3 sesiones por semana</th><th scope="col" class="n">3 sesiones o más</th></tr></thead>
          <tbody>
            <tr><td>Perder peso</td><td class="n">1,8</td><td class="n">2,2</td></tr>
            <tr><td>Mantener</td><td class="n">1,4</td><td class="n">1,8</td></tr>
            <tr><td>Ganar músculo</td><td class="n">1,6</td><td class="n">2,0</td></tr>
          </tbody>
        </table>
        <p class="source">La tabla de la aplicación Basal (versión 1.4). La necesidad sube en déficit, cuando las proteínas protegen la masa muscular.</p>
      </div>
      <div class="calcul" role="group" aria-label="Ejemplos">
        <div class="titre">Ejemplos, para 175 cm</div>
        <div class="ligne"><span>70 kg, pérdida de peso, 3 sesiones o más: 70 × 2,2</span><b>154 g</b></div>
        <div class="ligne"><span>70 kg, mantenimiento, menos de 3 sesiones: 70 × 1,4</span><b>98 g</b></div>
        <div class="ligne"><span>120 kg, pérdida de peso, 3 sesiones o más: 87,4 × 2,2</span><b>192 g</b></div>
      </div>

      <h2>Por qué un peso de referencia</h2>
      <p>Las necesidades de proteínas siguen la masa magra, no el peso total. Aplicar 2,2 g por kilo a 120 kg daría 264 g al día, más de 1.000 kcal antes de contar el resto: ninguna recomendación respalda esa cifra. Hasta un IMC de 25, el peso de referencia es por tanto tu peso real; por encima, solo cuenta una cuarta parte del exceso. Es la fórmula del peso ajustado, la aproximación habitual cuando no se mide la masa magra.</p>

      <h2>Y el resto del plato</h2>
      <p>Las proteínas son solo una parte del cálculo. La <a href="/es/calculadora-macros.html">calculadora de macros</a> añade las grasas y los hidratos, con las mismas reglas, y las <a href="/es/recetas/">recetas calculadas</a> muestran sus proteínas por ración.</p>

      <h2>Lo que este cálculo no sabe</h2>
      <div class="inconnu">
        <p><strong>Es un orden de magnitud.</strong> Se basa en los rangos habituales en nutrición deportiva, no en una medición de tu composición corporal.</p>
        <p style="margin:0"><strong>Algunas situaciones requieren un profesional sanitario</strong>: enfermedad renal, embarazo, dieta prescrita, trastorno de la conducta alimentaria.</p>
      </div>
''', appel_t='Tu objetivo de proteínas, cada día',
            appel='Basal calcula tus proteínas con esta tabla y las sigue comida a comida, con proteínas distintas para días de entrenamiento y de descanso en Premium.',
            dl='Descargar', note='Esta herramienta es informativa. Basal no es un dispositivo médico y no sustituye el consejo de un profesional sanitario.')),
        'script': script('es-ES', 'Indica tu peso y tu altura para ver el resultado.', 'Revisa los valores: peso de 30 a 300 kg, altura de 120 a 230 cm.',
                         'Peso de referencia: tu peso real (IMC de 25 o menos).', 'Peso de referencia: ', ' kg. Por encima de un IMC de 25 (', ' kg para tu altura), solo cuenta una cuarta parte del exceso.'),
        'ld': ld('Calculadora de proteínas: cuántas proteínas al día', '/es/calculadora-proteinas.html', 'Necesidades diarias de proteínas según peso, objetivo y entrenamiento, sobre un peso de referencia.', 'es',
                 '/es/', 'Inicio', '/es/calculadoras/', 'Calculadoras', 'Proteínas'),
    },
    'de': {
        'slug': '/de/proteinrechner.html',
        'tete': dict(title='Proteinrechner: Proteinbedarf pro Tag berechnen | Basal', locale='de_DE',
                     description='Wie viel Eiweiß pro Tag für dein Gewicht, dein Ziel und dein Training: die Tabelle der Basal-App. Kostenlos, ohne Anmeldung, es wird nichts gesendet.',
                     og_title='Proteinrechner: Proteinbedarf pro Tag berechnen', og_description='Für dein Gewicht, dein Ziel und dein Training, mit der Tabelle der Basal-App.'),
        'main': main(dict(fil='Brotkrümelnavigation', accueil='Startseite', accueil_url='/de/', hub='Rechner', hub_url='/de/rechner/', court='Eiweiß',
            surtitre='Kostenloser Rechner', h1='Proteinbedarf pro Tag berechnen',
            chapeau='Nach deinem Gewicht, deinem Ziel und deinem Training, mit der Tabelle der Basal-App. Sie gilt für ein Referenzgewicht, das den Bedarf bei hohem Gewicht nicht überschätzt. Es wird nichts gesendet.',
            poids='Gewicht (kg)', taille='Größe (cm)', objectif='Ziel', perte='Abnehmen', maintien='Gewicht halten', prise='Muskeln aufbauen', entrainement='Training',
            moins3='Weniger als 3 Einheiten pro Woche', plus3='3 Einheiten oder mehr', res='Dein Eiweißbedarf', flottant='Eiweiß', parjour='g / Tag',
            vide='Gib Gewicht und Größe ein, um das Ergebnis zu sehen.', gkg='g pro kg Referenzgewicht', kcal='kcal geliefert (4 kcal pro Gramm)',
            corps='''      <h2>Die verwendete Tabelle</h2>
      <p class="formule"><code>Eiweiß (g) = Referenzgewicht × Gramm pro Kilo</code></p>
      <div class="tableau">
        <table>
          <caption>Gramm Eiweiß pro Kilo Referenzgewicht</caption>
          <thead><tr><th scope="col">Ziel</th><th scope="col" class="n">Weniger als 3 Einheiten pro Woche</th><th scope="col" class="n">3 Einheiten oder mehr</th></tr></thead>
          <tbody>
            <tr><td>Abnehmen</td><td class="n">1,8</td><td class="n">2,2</td></tr>
            <tr><td>Gewicht halten</td><td class="n">1,4</td><td class="n">1,8</td></tr>
            <tr><td>Muskeln aufbauen</td><td class="n">1,6</td><td class="n">2,0</td></tr>
          </tbody>
        </table>
        <p class="source">Die Tabelle der Basal-App (Version 1.4). Der Bedarf steigt im Defizit, wo Eiweiß die Muskelmasse schützt.</p>
      </div>
      <div class="calcul" role="group" aria-label="Beispiele">
        <div class="titre">Beispiele, für 175 cm</div>
        <div class="ligne"><span>70 kg, Abnehmen, 3 Einheiten oder mehr: 70 × 2,2</span><b>154 g</b></div>
        <div class="ligne"><span>70 kg, Gewicht halten, weniger als 3 Einheiten: 70 × 1,4</span><b>98 g</b></div>
        <div class="ligne"><span>120 kg, Abnehmen, 3 Einheiten oder mehr: 87,4 × 2,2</span><b>192 g</b></div>
      </div>

      <h2>Warum ein Referenzgewicht</h2>
      <p>Der Eiweißbedarf folgt der fettfreien Masse, nicht dem Gesamtgewicht. 2,2 g pro Kilo bei 120 kg ergäben 264 g pro Tag, über 1.000 kcal, bevor der Rest überhaupt zählt: Keine Empfehlung stützt eine solche Zahl. Bis zu einem BMI von 25 ist das Referenzgewicht daher dein tatsächliches Gewicht; darüber zählt nur ein Viertel des Überschusses. Das ist die Formel des angepassten Gewichts, die übliche Näherung, wenn die fettfreie Masse nicht gemessen wird.</p>

      <h2>Und der Rest auf dem Teller</h2>
      <p>Eiweiß ist nur ein Teil der Rechnung. Der <a href="/de/makrorechner.html">Makrorechner</a> ergänzt Fett und Kohlenhydrate nach denselben Regeln, und die <a href="/de/rezepte/">berechneten Rezepte</a> zeigen ihr Eiweiß pro Portion.</p>

      <h2>Was diese Berechnung nicht weiß</h2>
      <div class="inconnu">
        <p><strong>Es ist eine Größenordnung.</strong> Sie beruht auf den üblichen Bereichen der Sporternährung, nicht auf einer Messung deiner Körperzusammensetzung.</p>
        <p style="margin:0"><strong>Manche Situationen gehören in fachliche Hände</strong>: Nierenerkrankung, Schwangerschaft, verordnete Diät, Essstörung.</p>
      </div>
''', appel_t='Dein Eiweißziel, jeden Tag',
            appel='Basal berechnet dein Eiweiß mit dieser Tabelle und verfolgt es Mahlzeit für Mahlzeit, mit eigenem Eiweißziel für Trainings- und Ruhetage in Premium.',
            dl='Herunterladen', note='Dieses Werkzeug dient nur der Information. Basal ist kein Medizinprodukt und ersetzt nicht den Rat medizinischen Fachpersonals.')),
        'script': script('de-DE', 'Gib Gewicht und Größe ein, um das Ergebnis zu sehen.', 'Prüfe die Werte: Gewicht von 30 bis 300 kg, Größe von 120 bis 230 cm.',
                         'Referenzgewicht: dein tatsächliches Gewicht (BMI von 25 oder weniger).', 'Referenzgewicht: ', ' kg. Über einem BMI von 25 (', ' kg für deine Größe) zählt nur ein Viertel des Überschusses.'),
        'ld': ld('Proteinrechner: Proteinbedarf pro Tag berechnen', '/de/proteinrechner.html', 'Täglicher Eiweißbedarf nach Gewicht, Ziel und Training, auf ein Referenzgewicht bezogen.', 'de',
                 '/de/', 'Startseite', '/de/rechner/', 'Rechner', 'Eiweiß'),
    },
}
