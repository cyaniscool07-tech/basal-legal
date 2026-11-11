from commun import U, page, stores

FR = '/nutrition-musculation.html'
DATE = '2026-11-11'
C = 'nutrition-musculation'
SOM = ['deux-carnets', 'series', 'repos', 'signe', 'limites', 'pratique']


def corps(l, t):
    p = lambda xs: '\n'.join(f'    <p>{x}</p>' for x in xs)
    li = '\n'.join(f'      <li>{x}</li>' for x in t['pratique'])
    return f'''    <h2 id="deux-carnets">{t["s"][0]}</h2>
{p(t["a"])}

    <h2 id="series">{t["s"][1]}</h2>
{p(t["b"])}
    <div class="encadre">
      <p>{t["b_enc"]}</p>
    </div>

    <h2 id="repos">{t["s"][2]}</h2>
{p(t["c"])}

    <h2 id="signe">{t["s"][3]}</h2>
{p(t["d"])}
    <div class="encadre">
      <p>{t["d_enc"]}</p>
    </div>

    <h2 id="limites">{t["s"][4]}</h2>
{p(t["e"])}

    <h2 id="pratique">{t["s"][5]}</h2>
    <ul>
{li}
    </ul>

    <div class="appel">
      <p class="appel-t">{t["appel_t"]}</p>
      <p>{t["appel"]}</p>
      {stores(l, t["campagne"])}
    </div>

    <p>{t["lire"]}</p>'''


EN = dict(s=['Two logs, no conversation', '1. How many sets each muscle really gets', '2. Rest days, the blind spot', '3. The one accessible sign you are not losing muscle', 'What cross-checking cannot tell you', 'In practice'],
    a=['A nutrition app knows what you eat and ignores what you lift. A strength-training app knows what you lift and ignores what you eat. Each answers half of the question perfectly, and the missing half is exactly where the interesting answers are.',
       'Three observations need both logs at once. None is spectacular. All can be checked on your own numbers.'],
    b=['Ask someone how many weekly sets their shoulders get and they will give a number. Count them in their log and the gap is often a factor of two. Sessions look alike, exercises repeat, and some muscle groups quietly drop out of the programme without anyone noticing.',
       'This count is not trivial. A bench press works the chest, but also the triceps and front delts. Counting the set once for each muscle involved inflates the total artificially; counting it only for the chest erases the rest. The common practice is to count one set for the main muscle and half a set for each secondary muscle. It is a convention, not a truth — but it has the merit of being consistent from week to week, which is exactly what you ask of a benchmark.'],
    b_enc='<strong>Per-muscle totals do not add up to the number of sets in the session.</strong> It is confusing the first time: a 20-set session can produce 34 “sets per muscle” spread over six groups. The two numbers measure different things, and only the second says what each muscle received.',
    c=['The most common mistake is not eating too little on training days. It is eating markedly less on rest days, without having decided to. The day is organised differently, hunger drops, the post-workout snack disappears — and the protein with it.',
       'Yet muscle protein synthesis stays elevated well after the session. Rest days are not days without needs; they are the days when building happens. Comparing your intake between the two categories is instructive precisely because you do not expect a gap.',
       'Meta-analyses commonly put useful intakes for strength training around <strong>1.6 to 2.2 g of protein per kilogram of body weight per day</strong>, with returns flattening beyond. It is not a magic threshold, and the range is wide because the studies are too. It serves to place an order of magnitude, not to judge a single day.'],
    d=['During weight loss, the real question is not how many kilos have gone, but what they were made of. A scale will never tell you: it weighs a total, not a composition.',
       f'There is one clue anyone can read: <strong>if your weight goes down while your loads go up</strong>, the loss is probably not coming out of muscle. The reverse deserves attention — weight dropping while loads collapse, over several weeks, is the clearest signal that a deficit is too aggressive or that protein is not keeping up. To compare sessions with different reps, the <a href="{U["1rm"]["en"]}">estimated 1RM</a> puts your loads on the same scale.'],
    d_enc='<strong>Beware of enthusiasm.</strong> In a beginner, loads go up for months for purely neural reasons, without a gram of extra muscle. The signal is useful in someone who has been training for a while and whose progress has already slowed; in a beginner losing weight, it does not prove much.',
    e=['It measures no body composition. It does not replace bioimpedance, skinfolds or DEXA — and those three have their own margins of error anyway.',
       'It depends entirely on what you log. Half-logged sessions make volume that really happened disappear; forgotten meals make intake look lower than it is. The conclusion will be wrong in the direction that hurts you.',
       'It needs weeks. One week of volume says nothing about a neglected muscle: you need at least two weeks of data for a gap to become a trend rather than a scheduling accident. Same for protein, where a few days are enough to shift an average.'],
    pratique=['Count your sets per muscle over the week, not per session: that is the unit a programme is steered by.', 'Look at your rest-day protein separately from your training-day protein. That is where the gap hides.',
              'Only call a muscle “neglected” after two weeks of data, never on one.', 'If your weight and your loads both go down over three weeks, raise your calories before raising your motivation.', 'Log the weeks that go wrong. They are what explain the month’s numbers.'],
    appel_t='These three cross-checks, without doing them by hand',
    appel='Basal knows both your meals and your workouts: it counts your sets per muscle group, compares your protein on training days with rest days, and shows “not enough data” rather than a number until it has enough to back it up. Tracking is free and needs no account.',
    campagne='en-nutrition-strength',
    lire=f'Also read: <a href="{U["prise-de-masse"]["en"]}">bulking</a> (calories, protein and pace) and <a href="{U["deficit"]["en"]}">the calorie deficit</a> to lose fat without losing muscle.')

ES = dict(s=['Dos cuadernos, ninguna conversación', '1. Cuántas series recibe de verdad cada músculo', '2. Los días de descanso, el punto ciego', '3. La única señal accesible de que no pierdes músculo', 'Lo que este cruce no puede decirte', 'En la práctica'],
    a=['Una aplicación de nutrición sabe lo que comes e ignora lo que levantas. Una aplicación de entrenamiento sabe lo que levantas e ignora lo que comes. Cada una responde perfectamente a la mitad de la pregunta, y la mitad que falta es justo donde están las respuestas interesantes.',
       'Tres observaciones necesitan los dos diarios a la vez. Ninguna es espectacular. Todas se comprueban con tus propias cifras.'],
    b=['Pregunta a alguien cuántas series semanales reciben sus hombros y te dará una cifra. Cuéntalas en su cuaderno y la diferencia suele ser del doble. Las sesiones se parecen, los ejercicios se repiten y algunos grupos musculares desaparecen tranquilamente del programa sin que nadie lo note.',
       'Este recuento no es trivial. Un press de banca trabaja el pectoral, pero también el tríceps y el deltoides anterior. Contar la serie una vez por cada músculo implicado infla el total; contarla solo para el pectoral borra el resto. Lo habitual es contar una serie para el músculo principal y media serie para cada músculo secundario. Es una convención, no una verdad — pero tiene la ventaja de ser constante de una semana a otra, que es justo lo que se pide a una referencia.'],
    b_enc='<strong>Los totales por músculo no suman el número de series de la sesión.</strong> Desconcierta la primera vez: una sesión de 20 series puede dar 34 «series por músculo» repartidas en seis grupos. Las dos cifras miden cosas distintas, y solo la segunda dice lo que ha recibido cada músculo.',
    c=['El error más extendido no es comer poco los días de entrenamiento. Es comer bastante menos los días de descanso sin haberlo decidido. El día se organiza de otra forma, el hambre baja, desaparece el tentempié de después del entrenamiento — y las proteínas con él.',
       'Sin embargo, la síntesis proteica sigue elevada mucho después de la sesión. Los días de descanso no son días sin necesidades; son los días en que se construye. Comparar lo que comes entre las dos categorías es instructivo precisamente porque no se espera ninguna diferencia.',
       'Los metaanálisis suelen situar los aportes útiles en entrenamiento de fuerza en torno a <strong>1,6–2,2 g de proteínas por kilo de peso corporal y día</strong>, con beneficios que se aplanan por encima. No es un umbral mágico, y el rango es amplio porque los estudios también lo son. Sirve para situar un orden de magnitud, no para juzgar un día.'],
    d=['Durante una pérdida de peso, la verdadera pregunta no es cuántos kilos se han ido, sino de qué estaban hechos. Una báscula no lo dirá nunca: pesa un total, no una composición.',
       f'Hay un indicio que cualquiera puede leer: <strong>si tu peso baja mientras tus cargas suben</strong>, la pérdida probablemente no se hace a costa del músculo. Lo contrario merece atención — un peso que baja mientras las cargas se hunden, durante varias semanas, es la señal más clara de que un déficit es demasiado agresivo o de que las proteínas no acompañan. Para comparar sesiones con repeticiones distintas, el <a href="{U["1rm"]["es"]}">1RM estimado</a> pone tus cargas en la misma escala.'],
    d_enc='<strong>Cuidado con el entusiasmo.</strong> En un principiante, las cargas suben durante meses por razones puramente nerviosas, sin un gramo más de músculo. La señal es útil en alguien que entrena desde hace tiempo y cuya progresión ya se ha calmado; en un principiante que pierde peso, no demuestra gran cosa.',
    e=['No mide ninguna composición corporal. No sustituye a una bioimpedancia, a los pliegues cutáneos ni a una DEXA — que, por cierto, tienen sus propios márgenes de error.',
       'Depende por completo de lo que registras. Sesiones anotadas a medias hacen desaparecer volumen que sí existió; comidas olvidadas hacen creer en aportes más bajos de lo que son. La conclusión será falsa en el sentido que te perjudica.',
       'Necesita semanas. Una semana de volumen no dice nada de un músculo olvidado: hacen falta al menos dos semanas de datos para que una carencia sea una tendencia y no un imprevisto de agenda. Lo mismo con las proteínas, donde unos pocos días bastan para mover una media.'],
    pratique=['Cuenta tus series por músculo en la semana, no por sesión: es la unidad con la que se dirige un programa.', 'Mira tus proteínas de los días de descanso por separado de las de los días de entrenamiento. Ahí se esconde la diferencia.',
              'Considera un músculo «olvidado» solo tras dos semanas de datos, nunca con una.', 'Si tu peso baja y tus cargas también durante tres semanas, sube tus calorías antes que tu motivación.', 'Registra las semanas malas. Son las que explican las cifras del mes.'],
    appel_t='Estos tres cruces, sin hacerlos a mano',
    appel='Basal conoce a la vez tus comidas y tus entrenamientos: cuenta tus series por grupo muscular, compara tus proteínas de los días de entrenamiento con las de los días de descanso y muestra «datos insuficientes» en lugar de una cifra mientras no tiene con qué respaldarla. El seguimiento es gratis y no pide ninguna cuenta.',
    campagne='es-nutricion-fuerza',
    lire=f'Lee también: <a href="{U["prise-de-masse"]["es"]}">el volumen muscular</a> (calorías, proteínas y ritmo) y <a href="{U["deficit"]["es"]}">el déficit calórico</a> para perder grasa sin perder músculo.')

DE = dict(s=['Zwei Tagebücher, kein Gespräch', '1. Wie viele Sätze jeder Muskel wirklich bekommt', '2. Ruhetage, der blinde Fleck', '3. Das einzige zugängliche Zeichen, dass du keine Muskeln verlierst', 'Was dieser Abgleich nicht sagen kann', 'In der Praxis'],
    a=['Eine Ernährungs-App weiß, was du isst, und ignoriert, was du hebst. Eine Trainings-App weiß, was du hebst, und ignoriert, was du isst. Jede beantwortet die Hälfte der Frage perfekt, und die fehlende Hälfte ist genau die, in der die interessanten Antworten liegen.',
       'Drei Beobachtungen brauchen beide Tagebücher gleichzeitig. Keine ist spektakulär. Alle lassen sich an deinen eigenen Zahlen prüfen.'],
    b=['Frag jemanden, wie viele Sätze pro Woche seine Schultern bekommen, und er nennt eine Zahl. Zähl sie in seinem Trainingstagebuch, und der Unterschied ist oft ein Faktor zwei. Die Einheiten ähneln sich, die Übungen wiederholen sich, und manche Muskelgruppen verschwinden still aus dem Plan, ohne dass es jemand merkt.',
       'Diese Zählung ist nicht trivial. Bankdrücken trainiert die Brust, aber auch Trizeps und vordere Schulter. Den Satz für jeden beteiligten Muskel einmal zu zählen, bläht die Summe künstlich auf; ihn nur für die Brust zu zählen, löscht den Rest. Üblich ist, für den Hauptmuskel einen Satz und für jeden Hilfsmuskel einen halben Satz zu zählen. Das ist eine Konvention, keine Wahrheit — aber sie ist von Woche zu Woche gleich, und genau das verlangt man von einem Richtwert.'],
    b_enc='<strong>Die Summen pro Muskel ergeben nicht die Satzzahl der Einheit.</strong> Das verwirrt beim ersten Mal: Eine Einheit mit 20 Sätzen kann 34 „Sätze pro Muskel“ auf sechs Gruppen ergeben. Die beiden Zahlen messen Verschiedenes, und nur die zweite sagt, was jeder Muskel bekommen hat.',
    c=['Der häufigste Fehler ist nicht, an Trainingstagen zu wenig zu essen. Es ist, an Ruhetagen deutlich weniger zu essen, ohne es beschlossen zu haben. Der Tag läuft anders, der Hunger sinkt, der Snack nach dem Training fällt weg — und das Eiweiß mit ihm.',
       'Dabei bleibt die Proteinsynthese lange nach der Einheit erhöht. Ruhetage sind keine Tage ohne Bedarf; an ihnen wird aufgebaut. Die Zufuhr zwischen beiden Tagesarten zu vergleichen ist gerade deshalb aufschlussreich, weil man keinen Unterschied erwartet.',
       'Metaanalysen setzen die sinnvolle Zufuhr im Krafttraining meist bei etwa <strong>1,6 bis 2,2 g Eiweiß pro Kilogramm Körpergewicht und Tag</strong> an, mit abflachendem Nutzen darüber. Das ist keine magische Schwelle, und der Bereich ist breit, weil die Studien es auch sind. Er dient zur Einordnung einer Größenordnung, nicht zur Bewertung eines Tages.'],
    d=['Beim Abnehmen ist die eigentliche Frage nicht, wie viele Kilo weg sind, sondern woraus sie bestanden. Eine Waage sagt das nie: Sie wiegt eine Summe, keine Zusammensetzung.',
       f'Es gibt ein Indiz, das jeder lesen kann: <strong>Sinkt dein Gewicht, während deine Trainingsgewichte steigen</strong>, geht der Verlust wahrscheinlich nicht zulasten der Muskeln. Das Umgekehrte verdient Aufmerksamkeit — ein sinkendes Gewicht bei einbrechenden Trainingsgewichten über mehrere Wochen ist das klarste Signal, dass ein Defizit zu aggressiv ist oder das Eiweiß nicht mithält. Um Einheiten mit unterschiedlichen Wiederholungen zu vergleichen, bringt das <a href="{U["1rm"]["de"]}">geschätzte 1RM</a> deine Gewichte auf dieselbe Skala.'],
    d_enc='<strong>Vorsicht vor Begeisterung.</strong> Bei Anfängern steigen die Gewichte monatelang aus rein neuronalen Gründen, ohne ein Gramm Muskel mehr. Das Signal ist bei jemandem nützlich, der schon länger trainiert und dessen Fortschritt sich bereits beruhigt hat; bei einem abnehmenden Anfänger beweist es wenig.',
    e=['Er misst keine Körperzusammensetzung. Er ersetzt weder Bioimpedanz noch Hautfaltenmessung noch DEXA — und diese drei haben übrigens eigene Fehlerspannen.',
       'Er hängt vollständig von deinen Einträgen ab. Halb eingetragene Einheiten lassen Volumen verschwinden, das stattgefunden hat; vergessene Mahlzeiten lassen die Zufuhr niedriger erscheinen. Die Schlussfolgerung wird in die Richtung falsch, die dir schadet.',
       'Er braucht Wochen. Eine Woche Volumen sagt nichts über einen vernachlässigten Muskel: Es braucht mindestens zwei Wochen Daten, damit eine Lücke ein Trend wird und kein Terminzufall. Gleiches gilt fürs Eiweiß, wo wenige Tage reichen, um einen Durchschnitt zu verschieben.'],
    pratique=['Zähle deine Sätze pro Muskel über die Woche, nicht pro Einheit: Das ist die Einheit, nach der ein Plan gesteuert wird.', 'Schau dir dein Eiweiß an Ruhetagen getrennt von dem an Trainingstagen an. Dort versteckt sich der Unterschied.',
              'Nenne einen Muskel erst nach zwei Wochen Daten „vernachlässigt“, nie nach einer.', 'Sinken über drei Wochen Gewicht und Trainingsgewichte, erhöhe deine Kalorien, bevor du deine Motivation erhöhst.', 'Trage die misslungenen Wochen ein. Sie erklären die Zahlen des Monats.'],
    appel_t='Diese drei Abgleiche, ohne sie von Hand zu führen',
    appel='Basal kennt deine Mahlzeiten und dein Training zugleich: Es zählt deine Sätze pro Muskelgruppe, vergleicht dein Eiweiß an Trainings- und Ruhetagen und zeigt „zu wenige Daten“ statt einer Zahl, solange es sie nicht belegen kann. Das Tracking ist kostenlos und braucht kein Konto.',
    campagne='de-ernaehrung-krafttraining',
    lire=f'Lies auch: <a href="{U["prise-de-masse"]["de"]}">Masseaufbau</a> (Kalorien, Eiweiß und Tempo) und <a href="{U["deficit"]["de"]}">das Kaloriendefizit</a>, um Fett zu verlieren, ohne Muskeln zu verlieren.')


def art(l, t, court, surtitre, h1, chapeau):
    return dict(court=court, surtitre=surtitre, publie='2026-08-08', maj='2026-10-30', h1=h1, chapeau=chapeau, sommaire=list(zip(SOM, t['s'])), corps=corps(l, t))


PAGES = {
    'en': page('en', C, art('en', EN, 'Nutrition and strength training', 'Strength training', 'Are you eating enough for what you lift?',
        'The question sounds simple. Answering it takes two logs that almost never talk to each other: the gym one and the food one.'),
        dict(title='Nutrition and strength training: are you eating enough? — Basal', description='Sets per muscle, protein on rest days and the one sign you are not losing muscle: what you learn by cross-checking your meals with your workouts.',
             og_title='Are you eating enough for what you lift?', og_description='Three observations that need both your food log and your training log.')),
    'es': page('es', C, art('es', ES, 'Nutrición y fuerza', 'Entrenamiento de fuerza', '¿Comes lo suficiente para lo que levantas?',
        'La pregunta parece sencilla. Responderla requiere dos cuadernos que casi nunca se hablan: el del gimnasio y el de las comidas.'),
        dict(title='Nutrición y entrenamiento de fuerza: ¿comes lo suficiente? — Basal', description='Series por músculo, proteínas en días de descanso y la única señal de que no pierdes músculo: lo que se aprende cruzando comidas y entrenamientos.',
             og_title='¿Comes lo suficiente para lo que levantas?', og_description='Tres observaciones que necesitan tu diario de comidas y tu diario de entrenamiento.')),
    'de': page('de', C, art('de', DE, 'Ernährung und Krafttraining', 'Krafttraining', 'Isst du genug für das, was du hebst?',
        'Die Frage klingt einfach. Sie zu beantworten braucht zwei Tagebücher, die fast nie miteinander reden: das vom Gym und das vom Essen.'),
        dict(title='Ernährung und Krafttraining: Isst du genug? — Basal', description='Sätze pro Muskel, Eiweiß an Ruhetagen und das einzige Zeichen, dass du keine Muskeln verlierst: was der Abgleich von Mahlzeiten und Training zeigt.',
             og_title='Isst du genug für das, was du hebst?', og_description='Drei Beobachtungen, die dein Ernährungs- und dein Trainingstagebuch brauchen.')),
}
