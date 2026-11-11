from commun import U, page, stores

FR = '/variations-de-poids.html'
DATE = '2026-11-11'
C = 'variations'
SOM = ['arithmetique', 'ecart', 'regarder', 'reperes', 'basal', 'plus-loin']


def corps(l, t):
    p = lambda xs: '\n'.join(f'    <p>{x}</p>' for x in xs)
    li = lambda xs: '\n'.join(f'      <li><strong>{a}</strong> {b}</li>' for a, b in xs)
    plus = '\n'.join(f'      <li>{x}</li>' for x in t['plus'])
    return f'''      <div class="en-bref">
        <p class="surtitre">{t["bref_t"]}</p>
        <p>{t["bref"]}</p>
      </div>

    <h2 id="arithmetique">{t["s"][0]}</h2>
{p(t["a"])}

    <h2 id="ecart">{t["s"][1]}</h2>
    <ul class="liste">
{li(t["causes"])}
    </ul>
    <div class="encadre">
      <p>{t["enc"]}</p>
    </div>

    <h2 id="regarder">{t["s"][2]}</h2>
{p(t["c"])}

    <h2 id="reperes">{t["s"][3]}</h2>
    <ul class="liste">
{li(t["reperes"])}
    </ul>

    <h2 id="basal">{t["s"][4]}</h2>
{p(t["d"])}

    <h2 id="plus-loin">{t["s"][5]}</h2>
    <ul class="liste">
{plus}
    </ul>
    {stores(l, t["campagne"])}'''


EN = dict(bref_t='In short',
    bref='One extra kilo overnight is almost never fat: you would have to eat about 7,700 kcal too many to gain one. The gap comes from water (glycogen, salt, training, cycle), from what is still being digested and from weighing conditions. Weight therefore varies by 1 to 2 kg every day: weigh yourself under the same conditions and read the seven-day average.',
    s=['Let’s start with the arithmetic', 'Where the gap really comes from', 'What to look at instead', 'A few reading tips', 'What Basal does', 'Going further'],
    a=['One kilogram of fat tissue represents around <strong>7,700 kcal</strong>. To really gain a kilo of fat in one day, you would therefore have to eat about 7,700 kcal <em>above</em> your expenditure — for most people, nearly three times their daily needs, in a single day.',
       'It is not impossible, but it is rare, and above all: it is not what happened if the scale moved by a kilo overnight. The number comes from somewhere else.'],
    causes=[('Glycogen and its water.', 'Your muscles and liver store glycogen, and each gram stored holds about three grams of water. Between full and depleted stores, the difference is counted in kilos — without a gram of fat having moved.'),
            ('Sodium.', 'A salty meal increases water retention for one to two days. The effect is mechanical and temporary.'),
            ('Gut content.', 'Part of what you ate and drank is still in your system. It is real weight, but it is not <em>you</em>.'),
            ('Recent training.', 'A hard session causes local inflammation and water retention in the muscles worked, which shows on the scale for a day or two.'),
            ('The menstrual cycle,', 'which produces regular, perfectly normal fluid shifts over several days.'),
            ('Weighing conditions.', 'Before or after the toilet, dressed or not, morning or evening: the gap between two readings on the same day commonly reaches one to two kilos.')],
    enc='<strong>A single weigh-in mostly measures noise.</strong> It is not a fault of your scale or your discipline: it is the nature of the signal. Body weight varies by one to two kilos around its real value, every day, for everyone.',
    c=['The solution is not to weigh yourself less often — it is the opposite. The more data points you have, the more reliable the average becomes. What needs to change is the number you <em>look at</em>.',
       'A <strong>seven-day rolling average</strong> absorbs shifts in water, salt and digestion, because they cancel out over a week, whereas a change in fat mass does not. The average curve goes up or down when something real happens, and stays flat when nothing does.',
       'Weigh yourself every day and only read the average: it is the routine that asks the most regularity and the least interpretation.'],
    reperes=[('One week is not enough to conclude.', 'It usually takes two to three weeks of averages to tell a trend from a fluctuation.'),
             ('A plateau is not a stop.', 'Fluid shifts can mask several weeks of real change, then clear all at once — the scale then “catches up” abruptly.'),
             ('Weigh yourself under the same conditions:', 'on waking, after the toilet, before eating or drinking. What matters is not the condition you choose, it is that it is always the same.')],
    d=[f'Weight tracking shows the trend and the rolling average rather than just the last weigh-in, over the period of your choice. Over the weeks, the app also compares what you log with how your weight actually changes, to refine your energy expenditure — it is explained on the <a href="{U["metabolisme-adaptatif"]["en"]}">adaptive metabolism</a> page.',
       f'A point of method that matters as much as the numbers: Basal observes, it does not prescribe. A day above your target is never presented as a failure, and the current day is never counted as failed before it is over. Weight tracking is <a href="{U["compteur-gratuit"]["en"]}">free and unlimited</a>.'],
    plus=[f'<a href="{U["metabolisme-adaptatif"]["en"]}">Adaptive metabolism</a> — why a fixed formula is wrong, and how to refine it with your data.',
          f'<a href="{U["series"]["en"]}">How many sets per muscle per week</a>.', f'<a href="{U["tdee"]["en"]}">Work out your energy expenditure</a> — no sign-up.'],
    campagne='en-weight-fluctuations')

ES = dict(bref_t='En resumen',
    bref='Un kilo más de un día para otro casi nunca es grasa: habría que comer unas 7.700 kcal de más para ganar un kilo. La diferencia viene del agua (glucógeno, sal, entrenamiento, ciclo), de lo que aún está en digestión y de las condiciones de la pesada. El peso varía así de 1 a 2 kg cada día: pésate en las mismas condiciones y lee la media de siete días.',
    s=['Empecemos por la aritmética', 'De dónde viene realmente la diferencia', 'Qué mirar en su lugar', 'Algunas claves de lectura', 'Lo que hace Basal', 'Para saber más'],
    a=['Un kilo de tejido graso representa unas <strong>7.700 kcal</strong>. Para ganar de verdad un kilo de grasa en un día, habría que comer unas 7.700 kcal <em>por encima</em> de tu gasto — para la mayoría de la gente, casi el triple de sus necesidades diarias, en un solo día.',
       'No es imposible, pero es raro y, sobre todo, no es lo que ha pasado si la báscula se ha movido un kilo en una noche. La cifra viene de otro sitio.'],
    causes=[('El glucógeno y su agua.', 'Tus músculos y tu hígado almacenan glucógeno, y cada gramo almacenado retiene unos tres gramos de agua. Entre unas reservas llenas y unas reservas a medias, la diferencia se cuenta en kilos — sin que se haya movido un gramo de grasa.'),
            ('El sodio.', 'Una comida salada aumenta la retención de agua durante uno o dos días. El efecto es mecánico y pasajero.'),
            ('El contenido digestivo.', 'Parte de lo que has comido y bebido sigue en tu sistema. Es peso real, pero no eres <em>tú</em>.'),
            ('El entrenamiento reciente.', 'Una sesión intensa provoca inflamación local y retención de agua en los músculos trabajados, que se ve en la báscula durante uno o dos días.'),
            ('El ciclo menstrual,', 'que produce variaciones de líquidos regulares y perfectamente normales durante varios días.'),
            ('Las condiciones de la pesada.', 'Antes o después de ir al baño, vestido o no, por la mañana o por la noche: la diferencia entre dos medidas del mismo día llega con frecuencia a uno o dos kilos.')],
    enc='<strong>Una pesada aislada mide sobre todo ruido.</strong> No es un fallo de tu báscula ni de tu disciplina: es la naturaleza de la señal. El peso corporal varía de uno a dos kilos alrededor de su valor real, todos los días, en todo el mundo.',
    c=['La solución no es pesarse menos — es lo contrario. Cuantos más puntos de medida tienes, más fiable es la media. Lo que tiene que cambiar es la cifra que <em>miras</em>.',
       'Una <strong>media móvil de siete días</strong> absorbe las variaciones de agua, sal y digestión, porque se compensan en una semana, mientras que un cambio de masa grasa no se compensa. La curva de medias sube o baja cuando ocurre algo real y se queda plana cuando no pasa nada.',
       'Pesarse todos los días y leer solo la media: es la rutina que pide más regularidad y menos interpretación.'],
    reperes=[('Una semana no basta para concluir.', 'Suelen hacer falta dos o tres semanas de medias para distinguir una tendencia de una fluctuación.'),
             ('Una meseta no es un parón.', 'Las variaciones de líquidos pueden ocultar varias semanas de cambio real y luego desaparecer de golpe — la báscula «recupera» entonces de repente.'),
             ('Pésate en las mismas condiciones:', 'al despertar, después de ir al baño, antes de comer o beber. Lo que importa no es la condición elegida, sino que sea siempre la misma.')],
    d=[f'El seguimiento del peso muestra la tendencia y la media móvil en lugar de la última pesada sola, en el periodo que elijas. Con las semanas, la aplicación compara además lo que registras con la evolución real de tu peso para afinar tu gasto energético — se explica en la página del <a href="{U["metabolisme-adaptatif"]["es"]}">metabolismo adaptativo</a>.',
       f'Un punto de método que importa tanto como las cifras: Basal constata, no prescribe. Un día por encima de tu objetivo nunca se presenta como un fracaso, y el día en curso nunca se cuenta como fallido antes de terminar. El seguimiento del peso es <a href="{U["compteur-gratuit"]["es"]}">gratuito y sin límite</a>.'],
    plus=[f'<a href="{U["metabolisme-adaptatif"]["es"]}">El metabolismo adaptativo</a> — por qué una fórmula fija se equivoca y cómo afinarla con tus datos.',
          f'<a href="{U["series"]["es"]}">Cuántas series por músculo y por semana</a>.', f'<a href="{U["tdee"]["es"]}">Calcula tu gasto energético</a> — sin registro.'],
    campagne='es-variaciones-peso')

DE = dict(bref_t='Kurz gesagt',
    bref='Ein Kilo mehr über Nacht ist fast nie Fett: Man müsste etwa 7.700 kcal zu viel essen, um ein Kilo zuzunehmen. Der Unterschied kommt von Wasser (Glykogen, Salz, Training, Zyklus), von dem, was noch verdaut wird, und von den Wiegebedingungen. Das Gewicht schwankt so jeden Tag um 1 bis 2 kg: Wiege dich unter gleichen Bedingungen und lies den Sieben-Tage-Durchschnitt.',
    s=['Beginnen wir mit der Rechnung', 'Woher der Unterschied wirklich kommt', 'Worauf du stattdessen schauen solltest', 'Einige Lesehilfen', 'Was Basal macht', 'Weiterlesen'],
    a=['Ein Kilogramm Fettgewebe entspricht etwa <strong>7.700 kcal</strong>. Um an einem Tag wirklich ein Kilo Fett zuzunehmen, müsste man also etwa 7.700 kcal <em>über</em> seinem Verbrauch essen — für die meisten Menschen fast das Dreifache ihres Tagesbedarfs, an einem einzigen Tag.',
       'Das ist nicht unmöglich, aber selten, und vor allem: Es ist nicht das, was passiert ist, wenn die Waage über Nacht um ein Kilo gestiegen ist. Die Zahl kommt woanders her.'],
    causes=[('Glykogen und sein Wasser.', 'Muskeln und Leber speichern Glykogen, und jedes gespeicherte Gramm bindet etwa drei Gramm Wasser. Zwischen vollen und angebrochenen Speichern liegen Kilos — ohne dass sich ein Gramm Fett bewegt hat.'),
            ('Natrium.', 'Eine salzige Mahlzeit erhöht die Wassereinlagerung für ein bis zwei Tage. Der Effekt ist mechanisch und vorübergehend.'),
            ('Der Darminhalt.', 'Ein Teil dessen, was du gegessen und getrunken hast, ist noch in deinem System. Das ist echtes Gewicht, aber nicht <em>du</em>.'),
            ('Das letzte Training.', 'Eine harte Einheit verursacht lokale Entzündung und Wassereinlagerung in den beanspruchten Muskeln, die ein bis zwei Tage auf der Waage sichtbar ist.'),
            ('Der Menstruationszyklus,', 'der über mehrere Tage regelmäßige, völlig normale Flüssigkeitsschwankungen erzeugt.'),
            ('Die Wiegebedingungen.', 'Vor oder nach der Toilette, angezogen oder nicht, morgens oder abends: Der Unterschied zwischen zwei Messungen am selben Tag erreicht oft ein bis zwei Kilo.')],
    enc='<strong>Eine einzelne Wiegung misst vor allem Rauschen.</strong> Das ist kein Fehler deiner Waage oder deiner Disziplin, sondern die Natur des Signals. Das Körpergewicht schwankt täglich um ein bis zwei Kilo um seinen echten Wert, bei allen Menschen.',
    c=['Die Lösung ist nicht, sich seltener zu wiegen — sondern das Gegenteil. Je mehr Messpunkte du hast, desto zuverlässiger wird der Durchschnitt. Ändern muss sich die Zahl, auf die du <em>schaust</em>.',
       'Ein <strong>gleitender Sieben-Tage-Durchschnitt</strong> schluckt Schwankungen von Wasser, Salz und Verdauung, weil sie sich über eine Woche ausgleichen, eine Veränderung der Fettmasse dagegen nicht. Die Durchschnittskurve steigt oder fällt, wenn etwas Echtes passiert, und bleibt flach, wenn nichts passiert.',
       'Täglich wiegen und nur den Durchschnitt lesen: Das ist die Routine, die am meisten Regelmäßigkeit und am wenigsten Deutung verlangt.'],
    reperes=[('Eine Woche reicht nicht für ein Urteil.', 'Meist braucht es zwei bis drei Wochen Durchschnittswerte, um einen Trend von einer Schwankung zu unterscheiden.'),
             ('Ein Plateau ist kein Stillstand.', 'Flüssigkeitsschwankungen können mehrere Wochen echter Veränderung verdecken und sich dann auf einmal auflösen — die Waage „holt“ dann plötzlich auf.'),
             ('Wiege dich unter gleichen Bedingungen:', 'nach dem Aufstehen, nach der Toilette, vor dem Essen und Trinken. Wichtig ist nicht die gewählte Bedingung, sondern dass sie immer gleich ist.')],
    d=[f'Das Gewichtstracking zeigt den Trend und den gleitenden Durchschnitt statt nur der letzten Wiegung, über den Zeitraum deiner Wahl. Über die Wochen vergleicht die App außerdem deine Einträge mit der tatsächlichen Entwicklung deines Gewichts, um deinen Energieverbrauch zu verfeinern — erklärt auf der Seite zur <a href="{U["metabolisme-adaptatif"]["de"]}">metabolischen Anpassung</a>.',
       f'Ein Punkt der Methode, der so viel zählt wie die Zahlen: Basal stellt fest, es schreibt nicht vor. Ein Tag über deinem Ziel wird nie als Misserfolg dargestellt, und der laufende Tag zählt nie als verpatzt, bevor er vorbei ist. Das Gewichtstracking ist <a href="{U["compteur-gratuit"]["de"]}">kostenlos und unbegrenzt</a>.'],
    plus=[f'<a href="{U["metabolisme-adaptatif"]["de"]}">Metabolische Anpassung</a> — warum eine feste Formel danebenliegt und wie du sie mit deinen Daten verfeinerst.',
          f'<a href="{U["series"]["de"]}">Wie viele Sätze pro Muskel und Woche</a>.', f'<a href="{U["tdee"]["de"]}">Berechne deinen Energieverbrauch</a> — ohne Anmeldung.'],
    campagne='de-gewichtsschwankungen')


def art(l, t, court, surtitre, h1, chapeau):
    return dict(court=court, surtitre=surtitre, publie='2026-10-06', maj='2026-11-02', h1=h1, chapeau=chapeau, sommaire=list(zip(SOM, t['s'])), corps=corps(l, t))


PAGES = {
    'en': page('en', C, art('en', EN, 'Weight fluctuations', 'Calories and expenditure', 'Why your weight changes from one day to the next',
        'The scale shows a kilo more than yesterday. It is an accurate measurement, and yet it says almost nothing about what you care about. A scale weighs a <em>total</em>: bones, muscle, fat, water, blood, and everything still passing through your system. The total moves constantly, and its most volatile parts have nothing to do with fat.'),
        dict(title='Why your weight changes from one day to the next — Basal', description='One extra kilo overnight is almost never fat: water, glycogen, salt, digestion and weighing conditions. How to read your weight with a seven-day average.',
             og_title='Why your weight changes from one day to the next', og_description='What really moves the scale, and what to look at instead.')),
    'es': page('es', C, art('es', ES, 'Variaciones de peso', 'Calorías y gasto', 'Por qué tu peso cambia de un día para otro',
        'La báscula marca un kilo más que ayer. Es una medida exacta y, sin embargo, no dice casi nada de lo que te interesa. Una báscula pesa un <em>total</em>: huesos, músculos, grasa, agua, sangre y todo lo que aún está en tránsito en tu cuerpo. El total se mueve sin parar, y sus componentes más volátiles no tienen nada que ver con la grasa.'),
        dict(title='Por qué tu peso cambia de un día para otro — Basal', description='Un kilo más de un día para otro casi nunca es grasa: agua, glucógeno, sal, digestión y condiciones de pesada. Cómo leer tu peso con una media de siete días.',
             og_title='Por qué tu peso cambia de un día para otro', og_description='Lo que de verdad mueve la báscula, y qué mirar en su lugar.')),
    'de': page('de', C, art('de', DE, 'Gewichtsschwankungen', 'Kalorien und Verbrauch', 'Warum dein Gewicht von Tag zu Tag schwankt',
        'Die Waage zeigt ein Kilo mehr als gestern. Das ist eine genaue Messung und sagt doch fast nichts über das, was dich interessiert. Eine Waage wiegt eine <em>Summe</em>: Knochen, Muskeln, Fett, Wasser, Blut und alles, was noch durch deinen Körper wandert. Die Summe bewegt sich ständig, und ihre flüchtigsten Teile haben nichts mit Fett zu tun.'),
        dict(title='Warum dein Gewicht von Tag zu Tag schwankt — Basal', description='Ein Kilo mehr über Nacht ist fast nie Fett: Wasser, Glykogen, Salz, Verdauung und Wiegebedingungen. So liest du dein Gewicht mit einem Sieben-Tage-Durchschnitt.',
             og_title='Warum dein Gewicht von Tag zu Tag schwankt', og_description='Was die Waage wirklich bewegt und worauf du stattdessen schauen solltest.')),
}
