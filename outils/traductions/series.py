from commun import U, page, stores

FR = '/series-par-muscle.html'
DATE = '2026-11-11'
C = 'series'
SOM = ['total-seance', 'compter', 'ordre-de-grandeur', 'meme-sens', 'a-la-main', 'plus-loin']


def corps(l, t):
    p = lambda xs: '\n'.join(f'    <p>{x}</p>' for x in xs)
    pieges = '\n'.join(f'      <li><strong>{a}</strong> {b}</li>' for a, b in t['pieges'])
    plus = '\n'.join(f'      <li>{x}</li>' for x in t['plus'])
    return f'''      <div class="en-bref">
        <p class="surtitre">{t["bref_t"]}</p>
        <p>{t["bref"]}</p>
      </div>

    <h2 id="total-seance">{t["s"][0]}</h2>
{p(t["a"])}

    <h2 id="compter">{t["s"][1]}</h2>
{p(t["b"])}
    <div class="encadre">
      <p>{t["b_enc"]}</p>
    </div>
    <p>{t["b2"]}</p>

    <h2 id="ordre-de-grandeur">{t["s"][2]}</h2>
{p(t["c"])}

    <h2 id="meme-sens">{t["s"][3]}</h2>
    <ul class="liste">
{pieges}
    </ul>

    <h2 id="a-la-main">{t["s"][4]}</h2>
{p(t["d"])}

    <h2 id="plus-loin">{t["s"][5]}</h2>
    <ul class="liste">
{plus}
    </ul>
    {stores(l, t["campagne"])}'''


EN = dict(bref_t='In short',
    bref='Aim for roughly 10 to 20 sets per muscle group per week: that is the range the hypertrophy literature most often points to, with gains flattening at the top. Count a full set for the main muscle and half a set for each secondary muscle. If you are progressing with less, nothing forces you to do more.',
    s=['Why a session total says nothing', 'How to count a set', 'What order of magnitude', 'Why we always get it wrong the same way', 'Doing it by hand, or not', 'Going further'],
    a=['“I did twenty sets today” is information about your fatigue, not about your programme. It says neither which muscles worked, nor in what proportion, nor how it adds up with the session the day before yesterday.',
       'The muscle, for its part, does not know about sessions. It receives volume, recovers, receives more. The window that makes sense for it is the <strong>week</strong>, and the unit is the <strong>muscle group</strong>, not the movement.'],
    b=['This is the point that stumps everyone, because an exercise almost never works a single muscle. A bench press works the chest, but also the triceps and front delts. If you count the set once for every muscle involved, you inflate your totals artificially. If you count it only for the chest, you erase the rest.'],
    b_enc='<strong>The most common convention: a full set for the main muscle, half a set for each secondary muscle.</strong> It is not a physiological truth, it is a judgement call. Its merit is being consistent from week to week, which is exactly what you ask of a benchmark: it does not need to be exact, it needs to be stable.',
    b2='A confusing consequence the first time: <strong>per-muscle totals do not add up to the number of sets in the session.</strong> A 20-set session can produce 34 “sets per muscle” spread over six groups. The two numbers measure different things, and only the second says what each muscle received.',
    c=['The hypertrophy literature commonly puts the useful range at around <strong>ten to twenty weekly sets per muscle group</strong>, with returns flattening at the top of the range and large individual variability.',
       'The range is wide because the studies are: populations, training levels and even the definition of an “effective” set vary from one protocol to the next. It serves to place an order of magnitude, not to judge a week. Someone on eight sets who is progressing has no reason to change anything.',
       'What the number reveals best is not the total, it is the <strong>distribution</strong>. Imbalances always sit in the same place: lots of chest and biceps, little back, and legs that quietly drop out of the programme when the week gets busy.'],
    pieges=[('Sessions look alike.', 'You think you are varying, the log says you have repeated the same four movements for three months.'),
            ('Secondary muscles are invisible.', 'Nobody counts the triceps in a press or the biceps in a row, although they often make up half the real volume of those groups.'),
            ('You remember the hard sessions, not the missed ones.', 'A week where leg day was skipped looks like a normal week in memory.'),
            ('Warm-ups get mixed in with working sets', 'depending on your mood, and the total becomes impossible to compare from week to week.')],
    d=['Nothing stops you from counting yourself: go back over your last seven days, give each set to its main muscle and half a set to each secondary, add up by group. For one week it takes a quarter of an hour. The problem is not the first calculation, it is redoing it every week — that is where everyone gives up.',
       f'Basal does it from your workout log, over the period of your choice. It is a Premium feature; the training log itself, with its 870+ exercises, sets, loads and routines, stays <a href="{U["compteur-gratuit"]["en"]}">free and unlimited</a>.'],
    plus=[f'<a href="{U["nutrition-musculation"]["en"]}">Are you eating enough for what you lift?</a> — volume per muscle, protein on rest days, and the sign that weight loss is not costing muscle.',
          f'<a href="{U["variations"]["en"]}">Why your weight changes from one day to the next</a>.', f'<a href="{U["tdee"]["en"]}">Work out your energy expenditure</a>.'],
    campagne='en-sets-per-muscle')

ES = dict(bref_t='En resumen',
    bref='Apunta a unas 10 a 20 series por grupo muscular y por semana: es la zona que la literatura sobre hipertrofia señala con más frecuencia, con ganancias que se aplanan por arriba. Cuenta una serie completa para el músculo principal y media serie para cada músculo secundario. Si progresas con menos, nada te obliga a hacer más.',
    s=['Por qué el total de una sesión no dice nada', 'Cómo contar una serie', 'Qué orden de magnitud', 'Por qué siempre nos equivocamos en el mismo sentido', 'Hacerlo a mano, o no', 'Para saber más'],
    a=['«Hoy he hecho veinte series» es una información sobre tu cansancio, no sobre tu programa. No dice qué músculos han trabajado, ni en qué proporción, ni cómo se suma a la sesión de anteayer.',
       'El músculo no conoce las sesiones. Recibe un volumen, se recupera, recibe otro. La ventana que tiene sentido para él es la <strong>semana</strong>, y la unidad es el <strong>grupo muscular</strong>, no el movimiento.'],
    b=['Es el punto que bloquea a todo el mundo, porque un ejercicio casi nunca trabaja un solo músculo. Un press de banca trabaja el pectoral, pero también el tríceps y el deltoides anterior. Si cuentas la serie una vez por cada músculo implicado, inflas tus totales. Si solo la cuentas para el pectoral, borras el resto.'],
    b_enc='<strong>La convención más habitual: una serie completa para el músculo principal y media serie para cada músculo secundario.</strong> No es una verdad fisiológica, es un criterio. Su ventaja es ser constante de una semana a otra, que es justo lo que se pide a una referencia: no necesita ser exacta, necesita ser estable.',
    b2='Consecuencia desconcertante la primera vez: <strong>los totales por músculo no suman el número de series de la sesión.</strong> Una sesión de 20 series puede dar 34 «series por músculo» repartidas en seis grupos. Las dos cifras miden cosas distintas, y solo la segunda dice lo que ha recibido cada músculo.',
    c=['La literatura sobre hipertrofia suele situar la zona útil en torno a <strong>diez a veinte series semanales por grupo muscular</strong>, con beneficios que se aplanan en la parte alta del rango y una gran variabilidad individual.',
       'El rango es amplio porque los estudios también lo son: las poblaciones, el nivel de entrenamiento y hasta la definición de una serie «efectiva» cambian de un protocolo a otro. Sirve para situar un orden de magnitud, no para juzgar una semana. Alguien con ocho series que progresa no tiene ningún motivo para cambiar nada.',
       'Lo que mejor revela la cifra no es el total, sino el <strong>reparto</strong>. Los desequilibrios siempre están en el mismo sitio: mucho pectoral y bíceps, poca espalda, y unas piernas que desaparecen discretamente del programa cuando la semana se complica.'],
    pieges=[('Las sesiones se parecen.', 'Crees que varías, el cuaderno dice que repites los mismos cuatro movimientos desde hace tres meses.'),
            ('Los músculos secundarios son invisibles.', 'Nadie cuenta el tríceps de un press ni el bíceps de un remo, aunque suelen suponer la mitad del volumen real de esos grupos.'),
            ('Recordamos las sesiones duras, no las que faltaron.', 'Una semana en la que se saltó el día de pierna parece en la memoria una semana normal.'),
            ('Los calentamientos se mezclan con las series efectivas', 'según el humor del momento, y el total deja de ser comparable de una semana a otra.')],
    d=['Nada te impide contar tú mismo: repasa tus últimos siete días, asigna cada serie a su músculo principal y media serie a cada secundario, y suma por grupo. Para una semana, lleva un cuarto de hora. El problema no es el primer cálculo, es repetirlo cada semana — ahí es donde todo el mundo abandona.',
       f'Basal lo hace a partir de tu cuaderno de entrenamiento, en el periodo que elijas. Es una función de Premium; el cuaderno de entrenamiento en sí, con sus más de 870 ejercicios, series, cargas y rutinas, sigue siendo <a href="{U["compteur-gratuit"]["es"]}">gratuito y sin límite</a>.'],
    plus=[f'<a href="{U["nutrition-musculation"]["es"]}">¿Comes lo suficiente para lo que levantas?</a> — el volumen por músculo, las proteínas de los días de descanso y la señal de que una pérdida de peso no cuesta músculo.',
          f'<a href="{U["variations"]["es"]}">Por qué tu peso cambia de un día para otro</a>.', f'<a href="{U["tdee"]["es"]}">Calcula tu gasto energético</a>.'],
    campagne='es-series-por-musculo')

DE = dict(bref_t='Kurz gesagt',
    bref='Ziele auf etwa 10 bis 20 Sätze pro Muskelgruppe und Woche: Das ist der Bereich, den die Hypertrophie-Literatur am häufigsten nennt, mit abflachenden Zuwächsen nach oben. Zähle einen vollen Satz für den Hauptmuskel und einen halben Satz für jeden Hilfsmuskel. Wenn du mit weniger Fortschritte machst, zwingt dich nichts zu mehr.',
    s=['Warum die Summe einer Einheit nichts sagt', 'Wie man einen Satz zählt', 'Welche Größenordnung', 'Warum man sich immer in dieselbe Richtung irrt', 'Von Hand zählen, oder nicht', 'Weiterlesen'],
    a=['„Ich habe heute zwanzig Sätze gemacht“ ist eine Information über deine Müdigkeit, nicht über deinen Plan. Sie sagt weder, welche Muskeln gearbeitet haben, noch in welchem Verhältnis, noch wie sich das mit der Einheit von vorgestern summiert.',
       'Der Muskel kennt keine Einheiten. Er bekommt ein Volumen, erholt sich, bekommt das nächste. Das sinnvolle Zeitfenster für ihn ist die <strong>Woche</strong>, und die Einheit ist die <strong>Muskelgruppe</strong>, nicht die Bewegung.'],
    b=['Das ist der Punkt, an dem alle hängen bleiben, denn eine Übung trainiert fast nie nur einen Muskel. Bankdrücken trainiert die Brust, aber auch Trizeps und vordere Schulter. Zählst du den Satz für jeden beteiligten Muskel einmal, blähst du deine Summen künstlich auf. Zählst du ihn nur für die Brust, löschst du den Rest.'],
    b_enc='<strong>Die verbreitetste Konvention: ein voller Satz für den Hauptmuskel, ein halber Satz für jeden Hilfsmuskel.</strong> Das ist keine physiologische Wahrheit, sondern eine Abwägung. Ihr Vorteil ist, dass sie von Woche zu Woche gleich bleibt, und genau das verlangt man von einem Richtwert: Er muss nicht exakt sein, er muss stabil sein.',
    b2='Beim ersten Mal verwirrend: <strong>Die Summen pro Muskel ergeben nicht die Satzzahl der Einheit.</strong> Eine Einheit mit 20 Sätzen kann 34 „Sätze pro Muskel“ auf sechs Gruppen ergeben. Die beiden Zahlen messen Verschiedenes, und nur die zweite sagt, was jeder Muskel bekommen hat.',
    c=['Die Hypertrophie-Literatur setzt den sinnvollen Bereich meist bei etwa <strong>zehn bis zwanzig Sätzen pro Muskelgruppe und Woche</strong> an, mit abflachendem Nutzen im oberen Bereich und großer individueller Streuung.',
       'Der Bereich ist breit, weil die Studien es sind: Bevölkerungsgruppen, Trainingsniveau und sogar die Definition eines „effektiven“ Satzes unterscheiden sich von Protokoll zu Protokoll. Er dient zur Einordnung, nicht zur Bewertung einer Woche. Wer mit acht Sätzen Fortschritte macht, hat keinen Grund, etwas zu ändern.',
       'Am meisten verrät die Zahl übrigens nicht über die Summe, sondern über die <strong>Verteilung</strong>. Ungleichgewichte sitzen immer an derselben Stelle: viel Brust und Bizeps, wenig Rücken, und Beine, die still aus dem Plan verschwinden, wenn die Woche voll wird.'],
    pieges=[('Die Einheiten ähneln sich.', 'Man glaubt zu variieren, das Tagebuch sagt, dass man seit drei Monaten dieselben vier Bewegungen wiederholt.'),
            ('Hilfsmuskeln sind unsichtbar.', 'Niemand zählt den Trizeps beim Drücken oder den Bizeps beim Rudern, obwohl sie oft die Hälfte des tatsächlichen Volumens dieser Gruppen ausmachen.'),
            ('Man erinnert sich an harte Einheiten, nicht an ausgefallene.', 'Eine Woche, in der der Beintag ausfiel, sieht in der Erinnerung wie eine normale Woche aus.'),
            ('Aufwärmsätze mischen sich unter die Arbeitssätze,', 'je nach Laune, und die Summe ist von Woche zu Woche nicht mehr vergleichbar.')],
    d=['Nichts hindert dich, selbst zu zählen: Geh deine letzten sieben Tage durch, ordne jeden Satz seinem Hauptmuskel zu und jedem Hilfsmuskel einen halben, addiere pro Gruppe. Für eine Woche dauert das eine Viertelstunde. Das Problem ist nicht die erste Rechnung, sondern sie jede Woche zu wiederholen — da geben alle auf.',
       f'Basal macht das aus deinem Trainingstagebuch, über den Zeitraum deiner Wahl. Das ist eine Premium-Funktion; das Trainingstagebuch selbst, mit über 870 Übungen, Sätzen, Gewichten und Routinen, bleibt <a href="{U["compteur-gratuit"]["de"]}">kostenlos und unbegrenzt</a>.'],
    plus=[f'<a href="{U["nutrition-musculation"]["de"]}">Isst du genug für das, was du hebst?</a> — Volumen pro Muskel, Eiweiß an Ruhetagen und das Zeichen, dass Abnehmen keine Muskeln kostet.',
          f'<a href="{U["variations"]["de"]}">Warum dein Gewicht von Tag zu Tag schwankt</a>.', f'<a href="{U["tdee"]["de"]}">Berechne deinen Energieverbrauch</a>.'],
    campagne='de-saetze-pro-muskel')


def art(l, t, court, surtitre, h1, chapeau):
    return dict(court=court, surtitre=surtitre, publie='2026-10-06', maj='2026-11-02', h1=h1, chapeau=chapeau, sommaire=list(zip(SOM, t['s'])), corps=corps(l, t))


PAGES = {
    'en': page('en', C, art('en', EN, 'Sets per muscle', 'Strength training', 'How many sets per muscle per week',
        'Ask someone how many weekly sets their shoulders get, and they will give a number without hesitating. Count them in their log, and the gap is often a factor of two. It is not a memory problem: the unit we think in — the session — is not the one the muscle works in.'),
        dict(title='How many sets per muscle per week? — Basal', description='10 to 20 sets per muscle group per week, how to count a set (main and secondary muscles), and why we always get the count wrong the same way.',
             og_title='How many sets per muscle per week', og_description='The right unit, how to count, and what order of magnitude to aim for.')),
    'es': page('es', C, art('es', ES, 'Series por músculo', 'Entrenamiento de fuerza', 'Cuántas series por músculo y por semana',
        'Pregunta a alguien cuántas series semanales reciben sus hombros y te dará una cifra sin dudar. Cuéntalas en su cuaderno y la diferencia suele ser del doble. No es un problema de memoria: la unidad en la que pensamos — la sesión — no es la unidad en la que trabaja el músculo.'),
        dict(title='¿Cuántas series por músculo a la semana? — Basal', description='De 10 a 20 series por grupo muscular y semana, cómo contar una serie (músculo principal y secundarios) y por qué siempre nos equivocamos en el mismo sentido.',
             og_title='Cuántas series por músculo y por semana', og_description='La unidad correcta, cómo contar y qué orden de magnitud buscar.')),
    'de': page('de', C, art('de', DE, 'Sätze pro Muskel', 'Krafttraining', 'Wie viele Sätze pro Muskel und Woche',
        'Frag jemanden, wie viele Sätze pro Woche seine Schultern bekommen, und er nennt ohne Zögern eine Zahl. Zähl sie in seinem Tagebuch, und der Unterschied ist oft ein Faktor zwei. Das ist kein Gedächtnisproblem: Die Einheit, in der man denkt — die Trainingseinheit —, ist nicht die, in der der Muskel arbeitet.'),
        dict(title='Wie viele Sätze pro Muskel pro Woche? — Basal', description='10 bis 20 Sätze pro Muskelgruppe und Woche, wie man einen Satz zählt (Haupt- und Hilfsmuskeln) und warum man sich beim Zählen immer gleich irrt.',
             og_title='Wie viele Sätze pro Muskel und Woche', og_description='Die richtige Einheit, wie man zählt und welche Größenordnung sinnvoll ist.')),
}
