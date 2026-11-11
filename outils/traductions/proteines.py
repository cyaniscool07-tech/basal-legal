from commun import U, page

FR = '/proteines-par-jour.html'
DATE = '2026-11-11'
C = 'proteines'

SOURCES = '''      <h2 id="sources">{titre}</h2>
      <ol class="sources">
        <li>ANSES. <i>Actualisation des repères du PNNS : élaboration des références nutritionnelles</i>. 2016.</li>
        <li>EFSA Panel on Dietetic Products, Nutrition and Allergies. “Scientific Opinion on Dietary Reference Values for protein”. <i>EFSA Journal</i>, 2012, 10(2), 2557.</li>
        <li>Bauer J et al. “Evidence-based recommendations for optimal dietary protein intake in older people: a position paper from the PROT-AGE Study Group”. <i>Journal of the American Medical Directors Association</i>, 2013, 14(8), p. 542-559.</li>
        <li>Jäger R et al. “International Society of Sports Nutrition Position Stand: protein and exercise”. <i>Journal of the International Society of Sports Nutrition</i>, 2017, 14, 20.</li>
        <li>Morton RW et al. “A systematic review, meta-analysis and meta-regression of the effect of protein supplementation on resistance training-induced gains in muscle mass and strength in healthy adults”. <i>British Journal of Sports Medicine</i>, 2018, 52(6), p. 376-384.</li>
        <li>Helms ER et al. “A systematic review of dietary protein during caloric restriction in resistance trained lean athletes: a case for higher intakes”. <i>International Journal of Sport Nutrition and Exercise Metabolism</i>, 2014, 24(2), p. 127-138.</li>
        <li>Schoenfeld BJ, Aragon AA. “How much protein can the body use in a single meal for muscle-building? Implications for daily protein distribution”. <i>Journal of the International Society of Sports Nutrition</i>, 2018, 15, 10.</li>
        <li>ANSES. <a href="https://ciqual.anses.fr/">Ciqual 2025 food composition table</a>, Etalab 2.0 open licence.</li>
      </ol>'''


def table(cap, cols, lignes, source):
    th = ''.join(f'<th scope="col"{" class=\"n\"" if i else ""}>{c}</th>' for i, c in enumerate(cols))
    rows = '\n'.join('            <tr>' + ''.join(f'<td{" class=\"n\"" if i else ""}>{x}</td>' for i, x in enumerate(r)) + '</tr>' for r in lignes)
    return f'''      <div class="tableau">
        <table>
          <caption>{cap}</caption>
          <thead><tr>{th}</tr></thead>
          <tbody>
{rows}
          </tbody>
        </table>
        <p class="source">{source}</p>
      </div>'''


def corps(l, t):
    """t : textes de la langue. Structure identique dans les 3 langues."""
    ex = '\n'.join(f'        <div class="ligne"><span>{a}</span><b>{b}</b></div>' for a, b in t['exemples'])
    return f'''      <div class="en-bref">
        <p class="surtitre">{t["bref_t"]}</p>
        <p>{t["bref"]}</p>
      </div>

      <h2 id="minimum">{t["s"][0]}</h2>
      <p>{t["min1"]}</p>
      <p>{t["min2"]}</p>

      <h2 id="objectif">{t["s"][1]}</h2>
{table(t["t1_cap"], t["t1_cols"], t["t1"], t["t1_src"])}
      <p>{t["obj1"]}</p>
      <p>{t["obj2"]}</p>

      <h3>{t["grille_t"]}</h3>
      <p>{t["grille"]}</p>
{table(t["t2_cap"], t["t2_cols"], t["t2"], t["t2_src"])}

      <h2 id="poids-eleve">{t["s"][2]}</h2>
      <p>{t["pe1"]}</p>
      <p>{t["pe2"]}</p>
      <p class="formule"><code>{t["formule"]}</code></p>

      <h2 id="exemples">{t["s"][3]}</h2>
      <p>{t["ex_intro"]}</p>
      <div class="calcul" role="group" aria-label="{t["ex_label"]}">
        <div class="titre">{t["ex_titre"]}</div>
{ex}
      </div>
      <p>{t["ex_fin"]}</p>

      <h2 id="repartir">{t["s"][4]}</h2>
      <p>{t["rep1"]}</p>
      <p>{t["rep2"]}</p>

      <h2 id="aliments">{t["s"][5]}</h2>
{table(t["t3_cap"], t["t3_cols"], t["t3"], t["t3_src"])}
      <p>{t["recettes"]}</p>

      <h2 id="trop">{t["s"][6]}</h2>
      <p>{t["trop1"]}</p>
      <p>{t["trop2"]}</p>

      <h2 id="inconnu">{t["s"][7]}</h2>
      <div class="inconnu">
        <p><strong>{t["inc"][0][0]}</strong> {t["inc"][0][1]}</p>
        <p><strong>{t["inc"][1][0]}</strong> {t["inc"][1][1]}</p>
        <p style="margin:0"><strong>{t["inc"][2][0]}</strong> {t["inc"][2][1]}</p>
      </div>

      <div class="appel-contexte">
        <div><strong>{t["appel_t"]}</strong><p>{t["appel"]}</p></div>
        <a class="bouton vif" href="{U["accueil"][l]}#download">{t["dl"]}</a>
      </div>

{SOURCES.format(titre=t["s"][8])}

      <h2 style="font-size:1.5rem;margin-top:48px">{t["plus_t"]}</h2>
      <div class="guides" style="grid-template-columns:repeat(auto-fit,minmax(240px,1fr))">
        <a class="guide" href="{U["prise-de-masse"][l]}"><span class="surtitre" style="margin:0">{t["guide"]}</span><h3>{t["g1"][0]}</h3><p>{t["g1"][1]}</p></a>
        <a class="guide" href="{U["nutrition-musculation"][l]}"><span class="surtitre" style="margin:0">{t["guide"]}</span><h3>{t["g2"][0]}</h3><p>{t["g2"][1]}</p></a>
      </div>'''


IDS = ['minimum', 'objectif', 'poids-eleve', 'exemples', 'repartir', 'aliments', 'trop', 'inconnu', 'sources']

EN = dict(bref_t='In short',
    bref='Without particular sport, aim for about 0.83 g of protein per kilo a day (60 g at 72 kg). With strength training, 1.4 to 2 g per kilo. During weight loss with training, rather the top of the range, up to 2.2 g, to protect muscle. Above a BMI of 25, calculate on a reference weight rather than your total weight.',
    s=['The minimum for an adult', 'By goal', 'If your weight is high', 'Worked examples', 'Spreading it over the day', 'Where to find it', 'Too much protein, a risk?', 'What we do not know', 'Sources'],
    min1='ANSES (France) and EFSA use the same reference for a healthy adult: <strong>0.83 g of protein per kilo of body weight per day</strong>. This figure covers the needs of 97.5% of the population. It is a floor to avoid deficiency, not a target for building muscle.',
    min2='Older people are an exception: the PROT-AGE expert group recommends 1.0 to 1.2 g per kilo after 65, because muscle responds less well to protein with age.',
    t1_cap='Benchmarks in grams of protein per kilo of body weight per day', t1_cols=['Situation', 'g per kilo', 'Source'],
    t1=[['Adult with no particular sport', '0.83', 'ANSES, EFSA'], ['Over 65', '1.0 to 1.2', 'PROT-AGE'], ['Strength training, building muscle', '1.4 to 2.0', 'ISSN; Morton meta-analysis'], ['Weight loss with strength training', '1.6 to 2.2', 'ISSN; Helms']],
    t1_src='Full references are at the bottom of the page.',
    obj1='The most cited meta-analysis on strength training (Morton, 2018, 49 trials) finds that muscle gain stops increasing at around <strong>1.6 g per kilo</strong> on average. Its confidence interval goes up to 2.2 g, hence the advice to aim higher if you want to be sure you are not limited.',
    obj2=f'In a deficit, needs go up: the body draws more readily on muscle when energy is short. Reviews of lean athletes in calorie restriction put the useful intake higher than at maintenance, hence the top of the range during weight loss. The rest of the strategy is in the <a href="{U["deficit"]["en"]}">calorie deficit</a> guide.',
    grille_t='The Basal app’s grid', grille='Basal combines these benchmarks into a simple grid, applied to your reference weight:',
    t2_cap='Grams of protein per kilo of reference weight, in Basal', t2_cols=['Goal', 'Fewer than 3 sessions a week', '3 sessions or more'],
    t2=[['Lose weight', '1.8', '2.2'], ['Maintain', '1.4', '1.8'], ['Build muscle', '1.6', '2.0']],
    t2_src='Grid of the Basal app, version 1.4. It is meant for someone tracking their food to change weight or progress: so it starts above the 0.83 g minimum.',
    pe1='Protein needs follow lean mass (muscles, organs), not fat. Multiplying 2.2 g by 120 kg would give 264 g a day, over 1,000 kcal of protein: no recommendation supports such a figure.',
    pe2=f'The usual correction is the <strong>adjusted weight</strong>. Up to a BMI of 25, your actual weight is kept. Above it, the weight corresponding to a BMI of 25 is used, plus a quarter of the excess. That is what Basal does, and what the <a href="{U["calc-proteines"]["en"]}">protein calculator</a> does.',
    formule='reference weight = weight at BMI 25 + 0.25 × (weight − weight at BMI 25)',
    ex_intro='These results are calculated by the app’s own code: a test checks that they stay correct if a formula changes.', ex_label='Examples of protein needs', ex_titre='With the Basal grid',
    exemples=[('165 cm, 60 kg, maintenance, fewer than 3 sessions: 60 × 1.4', '84 g'), ('175 cm, 70 kg, maintenance, fewer than 3 sessions: 70 × 1.4', '98 g'),
              ('175 cm, 70 kg, muscle gain, 3 sessions or more: 70 × 2.0', '140 g'), ('175 cm, 70 kg, weight loss, 3 sessions or more: 70 × 2.2', '154 g'),
              ('165 cm, 85 kg, weight loss, 3 sessions or more: 72.3 × 2.2', '159 g')],
    ex_fin=f'For your own number, the <a href="{U["calc-proteines"]["en"]}">protein calculator</a> does the same calculation in seconds, without sending anything.',
    rep1='The day’s total matters more than the timing. A regular spread still helps: the review by Schoenfeld and Aragon (2018) suggests about <strong>0.4 g per kilo per meal</strong>, over at least four meals, to reach 1.6 g per kilo. At 70 kg, that is close to 30 g per meal.',
    rep2='In practice, a serving of protein at each meal is usually enough. The poorest meals are usually breakfast and snacks: that is where quark, eggs or skyr change the total most.',
    t3_cap='Protein per serving, from the Ciqual 2025 table', t3_cols=['Food', 'Serving', 'Protein'],
    t3=[['Skinless chicken breast, grilled', '120 g', '36 g'], ['Minced beef 5% fat, cooked', '100 g', '25.5 g'], ['Tuna in water, drained', '100 g', '24.8 g'], ['Green lentils, cooked', '200 g', '20.2 g'],
        ['Plain quark (fromage blanc) 0%', '200 g', '14.7 g'], ['Hard-boiled eggs (2 eggs)', '100 g', '13.5 g'], ['Plain tofu', '100 g', '13.4 g'], ['Semi-skimmed milk', '250 g', '8.7 g'],
        ['Emmental', '30 g', '8.4 g'], ['Rolled oats', '50 g', '5.3 g']],
    t3_src='Calculated from the <a href="https://ciqual.anses.fr/">Ciqual 2025 table (ANSES)</a>, Etalab 2.0 open licence. Servings are examples, not recommendations.',
    recettes=f'The <a href="{U["recettes"]["en"]}">calculated recipes</a> show their protein per serving, for example <a href="/en/recipes/chicken-rice-and-broccoli.html">chicken, rice and broccoli</a> or the <a href="/en/recipes/red-lentil-and-coconut-dhal.html">red lentil dhal</a>.',
    trop1='In healthy adults, EFSA considers intakes of up to twice the reference safe, about 1.7 g per kilo. It has not set an upper limit, for lack of sufficient data beyond. Sports ranges up to 2.2 g go beyond that benchmark: they rest on studies in healthy people, often lasting a few months.',
    trop2='Kidney disease changes everything: in that case, protein intake is decided with a doctor, not a calculator.',
    inc=[('Your exact need.', 'These ranges are group averages. Your real need depends on your lean mass, your training and your age, which no formula measures.'),
         ('The real gain beyond 1.6 g per kilo.', 'It is small and uncertain. Aiming higher mostly serves as a safety margin.'),
         ('The very long-term effects of high intakes.', 'Trials rarely last more than a year.')],
    appel_t='Your protein, meal by meal', appel='Basal calculates your target with this grid and tracks it at every meal. In Premium, it separates training and rest days. Tracking is free and needs no account.', dl='Download',
    plus_t='Going further', guide='Guide', g1=('Bulking', 'What surplus to choose, and how fast to gain weight.'), g2=('Nutrition for strength training', 'Sets per muscle, and protein on rest days.'))

ES = dict(bref_t='En resumen',
    bref='Sin un deporte concreto, apunta a unos 0,83 g de proteínas por kilo y día (60 g para 72 kg). Con entrenamiento de fuerza, de 1,4 a 2 g por kilo. Durante una pérdida de peso con entrenamiento, mejor la parte alta del rango, hasta 2,2 g, para proteger el músculo. Por encima de un IMC de 25, calcula sobre un peso de referencia en lugar de tu peso total.',
    s=['El mínimo para un adulto', 'Según tu objetivo', 'Si tu peso es elevado', 'Ejemplos con cifras', 'Repartirlas a lo largo del día', 'Dónde encontrarlas', '¿Demasiadas proteínas, un riesgo?', 'Lo que no se sabe', 'Fuentes'],
    min1='La ANSES (Francia) y la EFSA usan la misma referencia para un adulto sano: <strong>0,83 g de proteínas por kilo de peso corporal y día</strong>. Esta cifra cubre las necesidades del 97,5 % de la población. Es un mínimo para evitar carencias, no un objetivo para ganar músculo.',
    min2='Las personas mayores son una excepción: el grupo de expertos PROT-AGE recomienda de 1,0 a 1,2 g por kilo a partir de los 65 años, porque el músculo responde peor a las proteínas con la edad.',
    t1_cap='Referencias en gramos de proteínas por kilo de peso y día', t1_cols=['Situación', 'g por kilo', 'Fuente'],
    t1=[['Adulto sin actividad deportiva concreta', '0,83', 'ANSES, EFSA'], ['Más de 65 años', '1,0 a 1,2', 'PROT-AGE'], ['Entrenamiento de fuerza, ganar músculo', '1,4 a 2,0', 'ISSN; metaanálisis de Morton'], ['Pérdida de peso con entrenamiento de fuerza', '1,6 a 2,2', 'ISSN; Helms']],
    t1_src='Las referencias completas están al final de la página.',
    obj1='El metaanálisis más citado sobre entrenamiento de fuerza (Morton, 2018, 49 ensayos) encuentra que la ganancia muscular deja de aumentar hacia <strong>1,6 g por kilo</strong> de media. Su intervalo de confianza llega hasta 2,2 g, de ahí el consejo de apuntar más alto si quieres asegurarte de no quedarte corto.',
    obj2=f'En déficit, la necesidad sube: el cuerpo recurre más fácilmente al músculo cuando falta energía. Las revisiones sobre deportistas magros en restricción calórica sitúan el aporte útil más alto que en mantenimiento, de ahí la parte alta del rango durante una pérdida de peso. El resto de la estrategia está en la guía del <a href="{U["deficit"]["es"]}">déficit calórico</a>.',
    grille_t='La tabla de la aplicación Basal', grille='Basal combina estas referencias en una tabla sencilla, aplicada a tu peso de referencia:',
    t2_cap='Gramos de proteínas por kilo de peso de referencia, en Basal', t2_cols=['Objetivo', 'Menos de 3 sesiones por semana', '3 sesiones o más'],
    t2=[['Perder peso', '1,8', '2,2'], ['Mantener', '1,4', '1,8'], ['Ganar músculo', '1,6', '2,0']],
    t2_src='Tabla de la aplicación Basal, versión 1.4. Está pensada para quien sigue su alimentación para cambiar de peso o progresar: por eso parte por encima del mínimo de 0,83 g.',
    pe1='Las necesidades de proteínas siguen la masa magra (músculos, órganos), no la grasa. Multiplicar 2,2 g por 120 kg daría 264 g al día, más de 1.000 kcal de proteínas: ninguna recomendación respalda esa cifra.',
    pe2=f'La corrección habitual es el <strong>peso ajustado</strong>. Hasta un IMC de 25 se mantiene tu peso real. Por encima, se toma el peso que corresponde a un IMC de 25 más una cuarta parte del exceso. Es lo que hace Basal y lo que hace la <a href="{U["calc-proteines"]["es"]}">calculadora de proteínas</a>.',
    formule='peso de referencia = peso a IMC 25 + 0,25 × (peso − peso a IMC 25)',
    ex_intro='Estos resultados los calcula el propio código de la aplicación: una prueba automática comprueba que siguen siendo exactos si cambia una fórmula.', ex_label='Ejemplos de necesidades de proteínas', ex_titre='Con la tabla de Basal',
    exemples=[('165 cm, 60 kg, mantenimiento, menos de 3 sesiones: 60 × 1,4', '84 g'), ('175 cm, 70 kg, mantenimiento, menos de 3 sesiones: 70 × 1,4', '98 g'),
              ('175 cm, 70 kg, ganar músculo, 3 sesiones o más: 70 × 2,0', '140 g'), ('175 cm, 70 kg, pérdida de peso, 3 sesiones o más: 70 × 2,2', '154 g'),
              ('165 cm, 85 kg, pérdida de peso, 3 sesiones o más: 72,3 × 2,2', '159 g')],
    ex_fin=f'Para tu propia cifra, la <a href="{U["calc-proteines"]["es"]}">calculadora de proteínas</a> hace el mismo cálculo en unos segundos, sin enviar nada.',
    rep1='El total del día cuenta más que el momento. Aun así, un reparto regular ayuda: la revisión de Schoenfeld y Aragon (2018) propone unos <strong>0,4 g por kilo y comida</strong>, en al menos cuatro comidas, para llegar a 1,6 g por kilo. Para 70 kg, son casi 30 g por comida.',
    rep2='En la práctica, una ración de proteínas en cada comida suele bastar. Las comidas más pobres suelen ser el desayuno y la merienda: ahí es donde un queso fresco batido, unos huevos o un skyr cambian más el total.',
    t3_cap='Proteínas por ración, según la tabla Ciqual 2025', t3_cols=['Alimento', 'Ración', 'Proteínas'],
    t3=[['Pechuga de pollo sin piel, a la plancha', '120 g', '36 g'], ['Carne picada 5 % de grasa, cocinada', '100 g', '25,5 g'], ['Atún al natural, escurrido', '100 g', '24,8 g'], ['Lentejas verdes cocidas', '200 g', '20,2 g'],
        ['Queso fresco batido natural 0 %', '200 g', '14,7 g'], ['Huevos duros (2 huevos)', '100 g', '13,5 g'], ['Tofu natural', '100 g', '13,4 g'], ['Leche semidesnatada', '250 g', '8,7 g'],
        ['Emmental', '30 g', '8,4 g'], ['Copos de avena', '50 g', '5,3 g']],
    t3_src='Calculado a partir de la <a href="https://ciqual.anses.fr/">tabla Ciqual 2025 de la ANSES</a>, licencia abierta Etalab 2.0. Las raciones son ejemplos, no recomendaciones.',
    recettes=f'Las <a href="{U["recettes"]["es"]}">recetas calculadas</a> muestran sus proteínas por ración, por ejemplo el <a href="/es/recetas/pollo-arroz-y-brocoli.html">pollo, arroz y brócoli</a> o el <a href="/es/recetas/dahl-de-lentejas-rojas-con-leche-de-coco.html">dahl de lentejas rojas</a>.',
    trop1='En el adulto sano, la EFSA considera seguros aportes de hasta el doble de la referencia, unos 1,7 g por kilo. No ha fijado un límite superior por falta de datos suficientes más allá. Los rangos deportivos de hasta 2,2 g superan esa referencia: se basan en estudios con personas sanas, a menudo de pocos meses.',
    trop2='Una enfermedad renal lo cambia todo: en ese caso, el aporte de proteínas se decide con un médico, no con una calculadora.',
    inc=[('Tu necesidad exacta.', 'Estos rangos son medias de grupos. Tu necesidad real depende de tu masa magra, tu entrenamiento y tu edad, que ninguna fórmula mide.'),
         ('La ganancia real por encima de 1,6 g por kilo.', 'Es pequeña e incierta. Apuntar más alto sirve sobre todo como margen de seguridad.'),
         ('Los efectos a muy largo plazo de los aportes altos.', 'Los ensayos rara vez duran más de un año.')],
    appel_t='Tus proteínas, comida a comida', appel='Basal calcula tu objetivo con esta tabla y lo sigue en cada comida. En Premium, distingue los días de entrenamiento y de descanso. El seguimiento es gratis y sin cuenta.', dl='Descargar',
    plus_t='Para saber más', guide='Guía', g1=('Volumen muscular', 'Qué superávit elegir y a qué ritmo ganar peso.'), g2=('Nutrición y fuerza', 'Las series por músculo y las proteínas de los días de descanso.'))

DE = dict(bref_t='Kurz gesagt',
    bref='Ohne besonderen Sport reichen etwa 0,83 g Eiweiß pro Kilo und Tag (60 g bei 72 kg). Mit Krafttraining 1,4 bis 2 g pro Kilo. Beim Abnehmen mit Training eher das obere Ende, bis 2,2 g, um die Muskeln zu schützen. Über einem BMI von 25 rechnest du besser mit einem Referenzgewicht statt mit deinem Gesamtgewicht.',
    s=['Das Minimum für Erwachsene', 'Je nach Ziel', 'Wenn dein Gewicht hoch ist', 'Rechenbeispiele', 'Über den Tag verteilen', 'Wo du es findest', 'Zu viel Eiweiß, ein Risiko?', 'Was man nicht weiß', 'Quellen'],
    min1='Die ANSES (Frankreich) und die EFSA verwenden für gesunde Erwachsene denselben Referenzwert: <strong>0,83 g Eiweiß pro Kilo Körpergewicht und Tag</strong>. Dieser Wert deckt den Bedarf von 97,5 % der Bevölkerung. Er ist eine Untergrenze gegen Mangel, kein Ziel für Muskelaufbau.',
    min2='Ältere Menschen sind eine Ausnahme: Die Expertengruppe PROT-AGE empfiehlt ab 65 Jahren 1,0 bis 1,2 g pro Kilo, weil der Muskel mit dem Alter schlechter auf Eiweiß reagiert.',
    t1_cap='Richtwerte in Gramm Eiweiß pro Kilo Körpergewicht und Tag', t1_cols=['Situation', 'g pro Kilo', 'Quelle'],
    t1=[['Erwachsene ohne besonderen Sport', '0,83', 'ANSES, EFSA'], ['Über 65 Jahre', '1,0 bis 1,2', 'PROT-AGE'], ['Krafttraining, Muskelaufbau', '1,4 bis 2,0', 'ISSN; Metaanalyse von Morton'], ['Abnehmen mit Krafttraining', '1,6 bis 2,2', 'ISSN; Helms']],
    t1_src='Die vollständigen Quellen stehen am Ende der Seite.',
    obj1='Die meistzitierte Metaanalyse zum Krafttraining (Morton, 2018, 49 Studien) findet, dass der Muskelzuwachs im Mittel bei etwa <strong>1,6 g pro Kilo</strong> nicht weiter steigt. Ihr Konfidenzintervall reicht bis 2,2 g, daher der Rat, höher zu zielen, wenn du sicher nicht begrenzt sein willst.',
    obj2=f'Im Defizit steigt der Bedarf: Der Körper greift eher auf Muskeln zurück, wenn Energie fehlt. Übersichtsarbeiten zu schlanken Sportlern in Kalorienrestriktion setzen die sinnvolle Zufuhr höher an als beim Halten, daher das obere Ende beim Abnehmen. Der Rest der Strategie steht im Ratgeber zum <a href="{U["deficit"]["de"]}">Kaloriendefizit</a>.',
    grille_t='Die Tabelle der Basal-App', grille='Basal fasst diese Richtwerte in einer einfachen Tabelle zusammen, angewendet auf dein Referenzgewicht:',
    t2_cap='Gramm Eiweiß pro Kilo Referenzgewicht, in Basal', t2_cols=['Ziel', 'Weniger als 3 Einheiten pro Woche', '3 Einheiten oder mehr'],
    t2=[['Abnehmen', '1,8', '2,2'], ['Gewicht halten', '1,4', '1,8'], ['Muskeln aufbauen', '1,6', '2,0']],
    t2_src='Tabelle der Basal-App, Version 1.4. Sie richtet sich an Menschen, die ihre Ernährung tracken, um ihr Gewicht zu verändern oder Fortschritte zu machen: Sie liegt daher über dem Minimum von 0,83 g.',
    pe1='Der Eiweißbedarf folgt der fettfreien Masse (Muskeln, Organe), nicht dem Fett. 2,2 g mal 120 kg ergäben 264 g am Tag, über 1.000 kcal aus Eiweiß: Keine Empfehlung stützt eine solche Zahl.',
    pe2=f'Die übliche Korrektur ist das <strong>angepasste Gewicht</strong>. Bis zu einem BMI von 25 bleibt es bei deinem tatsächlichen Gewicht. Darüber nimmt man das Gewicht bei BMI 25 plus ein Viertel des Überschusses. So macht es Basal, und so macht es der <a href="{U["calc-proteines"]["de"]}">Proteinrechner</a>.',
    formule='Referenzgewicht = Gewicht bei BMI 25 + 0,25 × (Gewicht − Gewicht bei BMI 25)',
    ex_intro='Diese Ergebnisse berechnet der Code der App selbst: Ein Test prüft, dass sie stimmen, falls sich eine Formel ändert.', ex_label='Beispiele für den Eiweißbedarf', ex_titre='Mit der Tabelle von Basal',
    exemples=[('165 cm, 60 kg, Gewicht halten, weniger als 3 Einheiten: 60 × 1,4', '84 g'), ('175 cm, 70 kg, Gewicht halten, weniger als 3 Einheiten: 70 × 1,4', '98 g'),
              ('175 cm, 70 kg, Muskelaufbau, 3 Einheiten oder mehr: 70 × 2,0', '140 g'), ('175 cm, 70 kg, Abnehmen, 3 Einheiten oder mehr: 70 × 2,2', '154 g'),
              ('165 cm, 85 kg, Abnehmen, 3 Einheiten oder mehr: 72,3 × 2,2', '159 g')],
    ex_fin=f'Für deine eigene Zahl macht der <a href="{U["calc-proteines"]["de"]}">Proteinrechner</a> dieselbe Rechnung in Sekunden, ohne etwas zu senden.',
    rep1='Die Tagessumme zählt mehr als der Zeitpunkt. Eine gleichmäßige Verteilung hilft trotzdem: Die Übersicht von Schoenfeld und Aragon (2018) schlägt etwa <strong>0,4 g pro Kilo und Mahlzeit</strong> vor, auf mindestens vier Mahlzeiten, um 1,6 g pro Kilo zu erreichen. Bei 70 kg sind das knapp 30 g pro Mahlzeit.',
    rep2='In der Praxis reicht meist eine Portion Eiweiß zu jeder Mahlzeit. Die eiweißärmsten Mahlzeiten sind meist Frühstück und Snack: Dort verändern Quark, Eier oder Skyr die Summe am meisten.',
    t3_cap='Eiweiß pro Portion, nach der Ciqual-Tabelle 2025', t3_cols=['Lebensmittel', 'Portion', 'Eiweiß'],
    t3=[['Hähnchenbrust ohne Haut, gegrillt', '120 g', '36 g'], ['Rinderhack 5 % Fett, gegart', '100 g', '25,5 g'], ['Thunfisch naturell, abgetropft', '100 g', '24,8 g'], ['Grüne Linsen, gekocht', '200 g', '20,2 g'],
        ['Magerquark natur 0 %', '200 g', '14,7 g'], ['Hart gekochte Eier (2 Eier)', '100 g', '13,5 g'], ['Tofu natur', '100 g', '13,4 g'], ['Teilentrahmte Milch', '250 g', '8,7 g'],
        ['Emmentaler', '30 g', '8,4 g'], ['Haferflocken', '50 g', '5,3 g']],
    t3_src='Berechnet mit der <a href="https://ciqual.anses.fr/">Ciqual-Tabelle 2025 der ANSES</a>, offene Lizenz Etalab 2.0. Die Portionen sind Beispiele, keine Empfehlungen.',
    recettes=f'Die <a href="{U["recettes"]["de"]}">berechneten Rezepte</a> zeigen ihr Eiweiß pro Portion, zum Beispiel <a href="/de/rezepte/hahnchen-reis-und-brokkoli.html">Hähnchen, Reis und Brokkoli</a> oder das <a href="/de/rezepte/dal-aus-roten-linsen-mit-kokosmilch.html">Dal aus roten Linsen</a>.',
    trop1='Bei gesunden Erwachsenen hält die EFSA Zufuhren bis zum Doppelten des Referenzwerts für sicher, also etwa 1,7 g pro Kilo. Eine Obergrenze hat sie mangels ausreichender Daten darüber nicht festgelegt. Die sportlichen Bereiche bis 2,2 g gehen darüber hinaus: Sie beruhen auf Studien mit gesunden Menschen, oft über wenige Monate.',
    trop2='Eine Nierenerkrankung ändert alles: Dann wird die Eiweißzufuhr mit einem Arzt festgelegt, nicht mit einem Rechner.',
    inc=[('Dein genauer Bedarf.', 'Diese Bereiche sind Gruppendurchschnitte. Dein tatsächlicher Bedarf hängt von deiner fettfreien Masse, deinem Training und deinem Alter ab, die keine Formel misst.'),
         ('Der echte Nutzen über 1,6 g pro Kilo.', 'Er ist klein und unsicher. Höher zu zielen dient vor allem als Sicherheitsmarge.'),
         ('Die sehr langfristigen Wirkungen hoher Zufuhren.', 'Studien dauern selten länger als ein Jahr.')],
    appel_t='Dein Eiweiß, Mahlzeit für Mahlzeit', appel='Basal berechnet dein Ziel mit dieser Tabelle und verfolgt es bei jeder Mahlzeit. In Premium unterscheidet es Trainings- und Ruhetage. Das Tracking ist kostenlos und ohne Konto.', dl='Herunterladen',
    plus_t='Weiterlesen', guide='Ratgeber', g1=('Masseaufbau', 'Welcher Überschuss, und wie schnell zunehmen.'), g2=('Ernährung und Krafttraining', 'Sätze pro Muskel und Eiweiß an Ruhetagen.'))


def art(l, t, court, h1, chapeau):
    return dict(court=court, surtitre='Guide' if l != 'de' else 'Ratgeber', publie='2026-10-31', h1=h1, chapeau=chapeau,
                sommaire=list(zip(IDS, t['s'])), corps=corps(l, t))


PAGES = {
    'en': page('en', C, art('en', EN, 'Protein per day', 'How much protein per day?',
        'To cover an adult’s needs, 0.83 g per kilo of body weight is enough. With strength training, or during weight loss, the useful range rises to 1.4 to 2.2 g per kilo. Here is where those figures come from, how to apply them to your weight, and what we do not know.'),
        dict(title='How much protein per day? (by weight and goal) — Basal', description='How much protein a day for your weight and goal: the 0.83 g/kg minimum, 1.4 to 2.2 g/kg with strength training, worked examples and sources.',
             og_title='How much protein per day?', og_description='Where the figures come from, how to apply them to your weight, and what we do not know.')),
    'es': page('es', C, art('es', ES, 'Proteínas al día', '¿Cuántas proteínas al día?',
        'Para cubrir las necesidades de un adulto bastan 0,83 g por kilo de peso corporal. Con entrenamiento de fuerza, o durante una pérdida de peso, el rango útil sube a 1,4–2,2 g por kilo. De dónde salen estas cifras, cómo aplicarlas a tu peso y lo que no se sabe.'),
        dict(title='¿Cuántas proteínas al día? (según peso y objetivo) — Basal', description='Cuántas proteínas al día según tu peso y tu objetivo: el mínimo de 0,83 g/kg, de 1,4 a 2,2 g/kg con entrenamiento, ejemplos con cifras y fuentes.',
             og_title='¿Cuántas proteínas al día?', og_description='De dónde salen las cifras, cómo aplicarlas a tu peso y lo que no se sabe.')),
    'de': page('de', C, art('de', DE, 'Protein pro Tag', 'Wie viel Protein pro Tag?',
        'Um den Bedarf eines Erwachsenen zu decken, reichen 0,83 g pro Kilo Körpergewicht. Mit Krafttraining oder beim Abnehmen steigt der sinnvolle Bereich auf 1,4 bis 2,2 g pro Kilo. Woher diese Zahlen kommen, wie du sie auf dein Gewicht anwendest und was man nicht weiß.'),
        dict(title='Wie viel Protein pro Tag? (nach Gewicht und Ziel) — Basal', description='Wie viel Eiweiß pro Tag für dein Gewicht und Ziel: Minimum 0,83 g/kg, 1,4 bis 2,2 g/kg mit Krafttraining, Rechenbeispiele und Quellen.',
             og_title='Wie viel Protein pro Tag?', og_description='Woher die Zahlen kommen, wie du sie auf dein Gewicht anwendest und was man nicht weiß.')),
}
