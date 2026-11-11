from commun import U, page, stores

FR = '/prise-de-masse.html'
DATE = '2026-11-11'
C = 'prise-de-masse'
SOM = ['combien', 'seche-ou-rapide', 'rythme', 'proteines', 'ajuster', 'pratique']


def corps(l, t):
    li = lambda xs: '\n'.join(f'      <li>{x}</li>' for x in xs)
    ex = '\n'.join(f'      <div class="ligne"><span>{a}</span><b>{b}</b></div>' for a, b in t['ex'])
    return f'''    <h2 id="combien">{t["s"][0]}</h2>
    <p>{t["p1"]}</p>
    <div class="encadre">
{ex}
    </div>

    <h2 id="seche-ou-rapide">{t["s"][1]}</h2>
    <p>{t["p2"]}</p>
    <p>{t["p3"]}</p>

    <h2 id="rythme">{t["s"][2]}</h2>
    <p>{t["p4"]}</p>
    <p>{t["p5"]}</p>

    <h2 id="proteines">{t["s"][3]}</h2>
    <p>{t["p6"]}</p>
    <p>{t["p7"]}</p>
    <div class="encadre">
      <p>{t["encadre"]}</p>
    </div>

    <h2 id="ajuster">{t["s"][4]}</h2>
    <ul>
{li(t["ajuster"])}
    </ul>

    <h2 id="pratique">{t["s"][5]}</h2>
    <ul>
{li(t["pratique"])}
    </ul>

    <div class="appel">
      <p class="appel-t">{t["appel_t"]}</p>
      <p>{t["appel"]}</p>
      {stores(l, t["campagne"])}
    </div>'''


EN = dict(s=['How many extra calories?', 'Lean or fast bulk?', 'How fast to gain weight?', 'How much protein?', 'When to adjust?', 'In practice'],
    p1=f'Start from your daily expenditure (estimate it with <a href="{U["tdee"]["en"]}">the calculator</a>) and add <strong>5 to 10%</strong>, usually 150 to 300 kcal a day. A bigger surplus does not build more muscle: the body has a limited building speed, and the excess goes to fat.',
    ex=[('Man, 30, 78 kg, moderately active (expenditure ≈ 2,710 kcal)', '2,850 to 2,980 kcal'), ('Woman, 30, 62 kg, moderately active (expenditure ≈ 2,080 kcal)', '2,180 to 2,290 kcal')],
    p2='A <strong>lean bulk</strong> aims for a moderate surplus, the one described above: you gain weight slowly, with little fat. A <strong>fast bulk</strong> pushes the surplus to 500 kcal or more: the scale climbs quickly, but a good part of it will have to be lost afterwards during a cut.',
    p3='For most lifters, the lean version pays off better: less fat to lose afterwards, so more time spent building.',
    p4='A common benchmark: <strong>0.25 to 0.5% of your weight a week</strong> if you are a beginner (at 78 kg, about 0.2 to 0.4 kg), and rather half that if you have been training for several years, because gains slow down with experience.',
    p5='As with weight loss, judge that pace on the two-to-three-week trend, not on a single weigh-in: water and carbs stored in muscle move weight from one day to the next.',
    p6=f'Meta-analyses commonly put the useful intake between <strong>1.6 and 2.2 g of protein per kilo of body weight per day</strong>. At 78 kg, that is about 125 to 170 g; at 62 kg, about 100 to 135 g. Beyond that, the benefit flattens. For your own number: <a href="{U["calc-proteines"]["en"]}">work out your protein needs</a>.',
    p7=f'The rest of the calories is shared between carbs, which fuel training, and fat, best kept above roughly 20% of total calories. For meal ideas, <a href="{U["recettes"]["en"]}">Basal’s recipes</a> show their protein per serving.',
    encadre=f'<strong>The surplus is useless without training that progresses.</strong> Load, reps or volume going up over the weeks is what gives the body a reason to build. For volume, see <a href="{U["series"]["en"]}">how many sets per muscle per week</a>.',
    ajuster=['Weight has not moved for three weeks: add 100 to 150 kcal.', 'Weight is rising clearly faster than planned and your waist follows: take off 100 to 150 kcal.',
             'Loads stall while weight goes up: look at sleep and your programme first, not calories.'],
    pratique=['Add 5 to 10% to your expenditure, 150 to 300 kcal a day.', 'Aim for 1.6 to 2.2 g of protein per kilo, spread over the day.',
              'Gain 0.25 to 0.5% of your weight a week, less if you are experienced.', 'Adjust in small steps based on the trend, never on a single weigh-in.'],
    appel_t='Your bulk, tracked from plate to bar', appel='Basal links your meals and your workouts: it follows your weight trend, your protein on training and rest days, and the progress of your loads. Tracking is free, ad-free and needs no account.',
    campagne='en-bulking')

ES = dict(s=['¿Cuántas calorías de más?', '¿Volumen limpio o rápido?', '¿A qué ritmo ganar peso?', '¿Cuántas proteínas?', '¿Cuándo ajustar?', 'En la práctica'],
    p1=f'Parte de tu gasto diario (estímalo con <a href="{U["tdee"]["es"]}">la calculadora</a>) y añade <strong>un 5 a 10 %</strong>, por lo general de 150 a 300 kcal al día. Un superávit mayor no construye más músculo: el cuerpo tiene una velocidad de construcción limitada y el sobrante se va a grasa.',
    ex=[('Hombre, 30 años, 78 kg, moderadamente activo (gasto ≈ 2.710 kcal)', '2.850 a 2.980 kcal'), ('Mujer, 30 años, 62 kg, moderadamente activa (gasto ≈ 2.080 kcal)', '2.180 a 2.290 kcal')],
    p2='Un <strong>volumen limpio</strong> busca un superávit moderado, el descrito arriba: se gana peso despacio, con poca grasa. Un <strong>volumen rápido</strong> («bulk» en el gimnasio) lleva el superávit a 500 kcal o más: la báscula sube rápido, pero buena parte habrá que perderla después en una definición.',
    p3='Para la mayoría, la versión limpia sale más a cuenta: menos grasa que perder después, y por tanto más tiempo construyendo.',
    p4='Una referencia habitual: <strong>del 0,25 al 0,5 % de tu peso por semana</strong> si empiezas (para 78 kg, unos 0,2 a 0,4 kg), y más bien la mitad si entrenas desde hace varios años, porque las ganancias se frenan con la experiencia.',
    p5='Como en una pérdida de peso, juzga ese ritmo por la tendencia de dos o tres semanas, no por una pesada aislada: el agua y los hidratos almacenados en los músculos hacen variar el peso de un día a otro.',
    p6=f'Los metaanálisis suelen situar el aporte útil entre <strong>1,6 y 2,2 g de proteínas por kilo de peso corporal y día</strong>. Para 78 kg son unos 125 a 170 g; para 62 kg, unos 100 a 135 g. Por encima, el beneficio se aplana. Para tu propia cifra: <a href="{U["calc-proteines"]["es"]}">calcula tus necesidades de proteínas</a>.',
    p7=f'El resto de las calorías se reparte entre los hidratos, que alimentan el entrenamiento, y las grasas, que conviene mantener por encima del 20 % de las calorías totales. Para ideas de comidas, las <a href="{U["recettes"]["es"]}">recetas de Basal</a> muestran sus proteínas por ración.',
    encadre=f'<strong>El superávit no sirve de nada sin un entrenamiento que progresa.</strong> La carga, las repeticiones o el volumen que aumentan semana a semana son lo que da al cuerpo una razón para construir. Para el volumen, mira <a href="{U["series"]["es"]}">cuántas series por músculo y por semana</a>.',
    ajuster=['El peso no se mueve desde hace tres semanas: añade de 100 a 150 kcal.', 'El peso sube claramente más rápido de lo previsto y la cintura también: quita de 100 a 150 kcal.',
             'Las cargas se estancan mientras el peso sube: mira primero el sueño y el programa, no las calorías.'],
    pratique=['Añade un 5 a 10 % a tu gasto, de 150 a 300 kcal al día.', 'Apunta a 1,6–2,2 g de proteínas por kilo, repartidas a lo largo del día.',
              'Gana del 0,25 al 0,5 % de tu peso por semana, menos si tienes experiencia.', 'Ajusta poco a poco según la tendencia, nunca según una pesada.'],
    appel_t='Tu volumen, seguido entre el plato y la barra', appel='Basal une tus comidas y tus entrenamientos: sigue la tendencia de tu peso, tus proteínas en días de entrenamiento y de descanso, y la progresión de tus cargas. El seguimiento es gratis, sin publicidad y sin cuenta.',
    campagne='es-volumen')

DE = dict(s=['Wie viele Kalorien zusätzlich?', 'Sauberer oder schneller Masseaufbau?', 'Wie schnell zunehmen?', 'Wie viel Eiweiß?', 'Wann anpassen?', 'In der Praxis'],
    p1=f'Geh von deinem Tagesverbrauch aus (schätze ihn mit <a href="{U["tdee"]["de"]}">dem Rechner</a>) und füge <strong>5 bis 10 %</strong> hinzu, meist 150 bis 300 kcal am Tag. Ein größerer Überschuss baut nicht mehr Muskeln auf: Der Körper hat ein begrenztes Aufbautempo, der Rest geht in Fett.',
    ex=[('Mann, 30 Jahre, 78 kg, mäßig aktiv (Verbrauch ≈ 2.710 kcal)', '2.850 bis 2.980 kcal'), ('Frau, 30 Jahre, 62 kg, mäßig aktiv (Verbrauch ≈ 2.080 kcal)', '2.180 bis 2.290 kcal')],
    p2='Ein <strong>sauberer Masseaufbau</strong> setzt auf einen moderaten Überschuss, den oben beschriebenen: Man nimmt langsam zu, mit wenig Fett. Ein <strong>schneller Masseaufbau</strong> („Bulk“ im Gym) treibt den Überschuss auf 500 kcal oder mehr: Die Waage steigt schnell, aber ein guter Teil muss danach in einer Diätphase wieder runter.',
    p3='Für die meisten lohnt sich die saubere Variante mehr: weniger Fett, das man danach verlieren muss, also mehr Zeit zum Aufbauen.',
    p4='Ein üblicher Richtwert: <strong>0,25 bis 0,5 % deines Gewichts pro Woche</strong>, wenn du Anfänger bist (bei 78 kg etwa 0,2 bis 0,4 kg), und eher die Hälfte, wenn du seit mehreren Jahren trainierst, weil die Zuwächse mit der Erfahrung langsamer werden.',
    p5='Wie beim Abnehmen beurteilst du das Tempo am Trend über zwei bis drei Wochen, nicht an einer einzelnen Wiegung: Wasser und in den Muskeln gespeicherte Kohlenhydrate lassen das Gewicht von Tag zu Tag schwanken.',
    p6=f'Metaanalysen setzen die sinnvolle Zufuhr meist zwischen <strong>1,6 und 2,2 g Eiweiß pro Kilo Körpergewicht und Tag</strong>. Bei 78 kg sind das etwa 125 bis 170 g, bei 62 kg etwa 100 bis 135 g. Darüber flacht der Nutzen ab. Für deine eigene Zahl: <a href="{U["calc-proteines"]["de"]}">berechne deinen Eiweißbedarf</a>.',
    p7=f'Der Rest der Kalorien verteilt sich auf Kohlenhydrate, die das Training befeuern, und Fett, das man besser über etwa 20 % der Gesamtkalorien hält. Für Mahlzeitenideen zeigen die <a href="{U["recettes"]["de"]}">Rezepte von Basal</a> ihr Eiweiß pro Portion.',
    encadre=f'<strong>Der Überschuss nützt nichts ohne ein Training, das sich steigert.</strong> Mehr Gewicht, Wiederholungen oder Volumen über die Wochen geben dem Körper einen Grund aufzubauen. Zum Volumen siehe <a href="{U["series"]["de"]}">wie viele Sätze pro Muskel und Woche</a>.',
    ajuster=['Das Gewicht bewegt sich seit drei Wochen nicht: 100 bis 150 kcal hinzufügen.', 'Das Gewicht steigt deutlich schneller als geplant und der Bauchumfang folgt: 100 bis 150 kcal abziehen.',
             'Die Trainingsgewichte stagnieren, während das Gewicht steigt: zuerst Schlaf und Trainingsplan prüfen, nicht die Kalorien.'],
    pratique=['Füge deinem Verbrauch 5 bis 10 % hinzu, also 150 bis 300 kcal am Tag.', 'Ziele auf 1,6 bis 2,2 g Eiweiß pro Kilo, über den Tag verteilt.',
              'Nimm 0,25 bis 0,5 % deines Gewichts pro Woche zu, weniger, wenn du erfahren bist.', 'Passe in kleinen Schritten nach dem Trend an, nie nach einer einzelnen Wiegung.'],
    appel_t='Dein Masseaufbau, zwischen Teller und Hantel verfolgt', appel='Basal verbindet deine Mahlzeiten und dein Training: Es verfolgt den Trend deines Gewichts, dein Eiweiß an Trainings- und Ruhetagen und den Fortschritt deiner Gewichte. Das Tracking ist kostenlos, werbefrei und braucht kein Konto.',
    campagne='de-masseaufbau')


def art(l, t, court, surtitre, h1, chapeau):
    return dict(court=court, surtitre=surtitre, publie='2026-10-20', maj='2026-10-30', h1=h1, chapeau=chapeau, sommaire=list(zip(SOM, t['s'])), corps=corps(l, t))


PAGES = {
    'en': page('en', C, art('en', EN, 'Bulking', 'Losing or gaining weight', 'Bulking: calories, protein and pace',
        'Building muscle takes a little more energy than you spend, enough protein and training that progresses. The hard part is not gaining weight: it is gaining it mostly as muscle.'),
        dict(title='Bulking: calories, protein and pace (lean or fast) — Basal', description='How many extra calories to build muscle, lean or fast bulk, how fast to gain weight and how much protein: worked figures.',
             og_title='Bulking: calories, protein and pace', og_description='What surplus to choose, how fast to gain, and when to adjust.')),
    'es': page('es', C, art('es', ES, 'Volumen muscular', 'Perder o ganar peso', 'Volumen muscular: calorías, proteínas y ritmo',
        'Ganar músculo pide un poco más de energía de la que gastas, suficientes proteínas y un entrenamiento que progresa. Lo difícil no es ganar peso: es ganarlo sobre todo en forma de músculo.'),
        dict(title='Volumen muscular: calorías, proteínas y ritmo — Basal', description='Cuántas calorías de más para ganar músculo, volumen limpio o rápido, a qué ritmo ganar peso y cuántas proteínas: cifras concretas.',
             og_title='Volumen muscular: calorías, proteínas y ritmo', og_description='Qué superávit elegir, a qué ritmo ganar peso y cuándo ajustar.')),
    'de': page('de', C, art('de', DE, 'Masseaufbau', 'Abnehmen oder zunehmen', 'Masseaufbau: Kalorien, Eiweiß und Tempo',
        'Muskelaufbau braucht etwas mehr Energie, als du verbrauchst, genug Eiweiß und ein Training, das sich steigert. Schwierig ist nicht das Zunehmen, sondern vor allem Muskeln zuzunehmen.'),
        dict(title='Masseaufbau: Kalorien, Eiweiß und Tempo — Basal', description='Wie viele zusätzliche Kalorien für Muskelaufbau, sauberer oder schneller Masseaufbau, wie schnell zunehmen und wie viel Eiweiß: konkrete Zahlen.',
             og_title='Masseaufbau: Kalorien, Eiweiß und Tempo', og_description='Welcher Überschuss, wie schnell zunehmen und wann anpassen.')),
}
