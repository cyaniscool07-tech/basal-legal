from commun import U, page, stores

FR = '/compteur-calories-gratuit.html'
DATE = '2026-11-11'
C = 'compteur-gratuit'
IDS = {
    'en': ['four-kinds-of-free', 'what-basal-keeps-free', 'so-what-is-paid', 'why-this-is-not-generosity', 'and-without-an-account', 'going-further'],
    'es': ['cuatro-formas-de-decir-gratis', 'lo-que-basal-mantiene-gratis', 'entonces-que-es-de-pago', 'por-que-no-es-generosidad', 'y-sin-cuenta', 'para-saber-mas'],
    'de': ['vier-arten-kostenlos', 'was-basal-kostenlos-laesst', 'was-kostet-also-geld', 'warum-das-keine-grosszuegigkeit-ist', 'und-ohne-konto', 'weiterlesen'],
}


def corps(l, t):
    i = IDS[l]
    li = lambda xs: '\n'.join(f'      <li>{x}</li>' for x in xs)
    return f'''      <h2 id="{i[0]}">{t["s"][0]}</h2>
      <p>{t["quatre_intro"]}</p>
      <ul class="liste">
{li(t["quatre"])}
      </ul>

      <div class="encadre">
        <p>{t["scanner"]}</p>
      </div>

      <h2 id="{i[1]}">{t["s"][1]}</h2>
      <p>{t["gratuit_intro"]}</p>
      <ul class="liste">
{li(t["gratuit"])}
      </ul>

      <h2 id="{i[2]}">{t["s"][2]}</h2>
      <p>{t["payant"]}</p>
      <p>{t["regle"]}</p>

      <h2 id="{i[3]}">{t["s"][3]}</h2>
      <p>{t["modele"]}</p>
      <p>{t["inconvenient"]}</p>

      <h2 id="{i[4]}">{t["s"][4]}</h2>
      <p>{t["compte"]}</p>

      <h2 id="{i[5]}">{t["s"][5]}</h2>
      <ul class="liste">
{li(t["plus"])}
      </ul>

      {stores(l, t["campagne"])}'''


EN = dict(
    s=['The four ways of saying “free”', 'What Basal keeps free', 'So what is paid', 'Why this is not generosity', 'And without an account', 'Going further'],
    quatre_intro='When an app presents itself as free, it usually covers one of these situations. They are not at all equal.',
    quatre=['<strong>Free with ads.</strong> You do not pay in money. The model assumes your attention is worth something, so the app tries to bring you back often, which is not always in your interest.',
            '<strong>Free with a quota.</strong> A number of foods per day, a number of recipes, a history limited to a few days. The app works until the exact moment it becomes useful to you.',
            '<strong>Free during the trial.</strong> Seven days, sometimes three. After that, it is a paid app that asked you to put your data in first.',
            '<strong>Free, except the core feature.</strong> The most effective of the four: everything stays open except the thing that made you install the app. The barcode scanner has become the textbook case.'],
    scanner='<strong>The scanner is the real test.</strong> Logging a meal by hand takes one to two minutes; the scanner takes three seconds. It decides whether you will keep going for a month or for three days. An app that puts it behind a subscription is not a free app with a paid option: it is a paid app with a demo.',
    gratuit_intro='No subscription, no trial that expires, no quota, and no ads:',
    gratuit=['calories and macronutrients — protein, carbohydrates, fat, fibre — split by meal;',
             'food search and the <strong>barcode scanner</strong>;',
             'weight tracking, with trends and the moving average;',
             'adaptive metabolism, which refines your expenditure from your real data;',
             'strength training, unlimited: over 870 exercises, sets, loads, reps, supersets, rest timer, records and routines;',
             'cardio sessions and steps, with the calories burned calculated for you;',
             'your own recipes, with their nutrition calculated per serving;',
             'a full export of your data, as JSON or CSV, at any time.'],
    payant='The <strong>analyses</strong> — the weekly review and its history, metabolism over time, volume per muscle group, protein on training days compared with rest days, advanced nutrition strategies — and three <strong>meal assistants</strong> that organise your meals, prepare your week and optimise it (each can be tried once for free). Recipes, meal planning and the shopping list stay free. €4.99 a month or €39.99 a year in the eurozone; the store shows the price in your currency.',
    regle='The split follows a simple rule: <strong>logging and cooking are free; understanding and automating are paid.</strong> If you never pay, you keep a complete log that does not degrade over time. Nothing locks after thirty days.',
    modele='To be direct: this model exists because it is sustainable, not out of philanthropy. An app without ads does not need to capture your attention, and an app that does not sell data does not need your profile. That leaves the subscription, which is only justified if what it unlocks has value in itself — hence the choice never to hold basic tracking to ransom.',
    inconvenient='The downside is real and it is mine: many people will use Basal for years without ever paying. That is the price of a model in which you do not have to be held hostage.',
    compte=f'You can use Basal fully without creating an account. In that case, your profile, your weight and your meals stay on your phone and are sent nowhere. The details, including what works offline, are in <a href="{U["sans-compte"]["en"]}">a calorie app without an account</a>. The account is optional and only serves to get your data back on another device; deleting it erases them from the server. The app is for adults only.',
    plus=[f'<a href="{U["comparatif"]["en"]}">Comparison: MyFitnessPal, Yazio, Foodvisor and Basal</a> — what each one keeps free, with prices.',
          f'<a href="{U["alternative-mfp"]["en"]}">A MyFitnessPal alternative</a>.',
          f'<a href="{U["tdee"]["en"]}">Calculate your energy expenditure</a> — no sign-up, nothing is sent.'],
    campagne='en-free-calorie-counter',
)

ES = dict(
    s=['Las cuatro formas de decir «gratis»', 'Lo que Basal mantiene gratis', 'Entonces, ¿qué es de pago?', 'Por qué no es generosidad', 'Y sin cuenta', 'Para saber más'],
    quatre_intro='Cuando una aplicación se presenta como gratuita, suele tratarse de una de estas situaciones. No valen lo mismo en absoluto.',
    quatre=['<strong>Gratis con publicidad.</strong> No pagas con dinero. El modelo da por hecho que tu atención vale algo, así que la aplicación intenta que vuelvas a menudo, lo que no siempre coincide con tu interés.',
            '<strong>Gratis con cupo.</strong> Un número de alimentos al día, un número de recetas, un historial limitado a unos pocos días. La aplicación funciona hasta el momento exacto en que te resulta útil.',
            '<strong>Gratis durante la prueba.</strong> Siete días, a veces tres. Pasado ese plazo, es una aplicación de pago que antes te pidió que metieras tus datos.',
            '<strong>Gratis, salvo la función principal.</strong> La más eficaz de las cuatro: todo queda abierto excepto lo que te hizo instalar la aplicación. El escáner de códigos de barras se ha convertido en el caso de manual.'],
    scanner='<strong>El escáner es la verdadera prueba.</strong> Registrar una comida a mano lleva uno o dos minutos; el escáner, tres segundos. Es él quien decide si aguantarás un mes o tres días. Una aplicación que lo pone tras una suscripción no es una aplicación gratuita con una opción de pago: es una aplicación de pago con una demostración.',
    gratuit_intro='Sin suscripción, sin prueba que caduque, sin cupo y sin publicidad:',
    gratuit=['las calorías y los macronutrientes — proteínas, hidratos, grasas, fibra — repartidos por comida;',
             'la búsqueda de alimentos y el <strong>escáner de códigos de barras</strong>;',
             'el seguimiento del peso, con las tendencias y la media móvil;',
             'el metabolismo adaptativo, que afina tu gasto a partir de tus datos reales;',
             'la musculación, ilimitada: más de 870 ejercicios, series, cargas, repeticiones, superseries, temporizador de descanso, récords y rutinas;',
             'las sesiones de cardio y los pasos, con las calorías gastadas calculadas por ti;',
             'tus recetas personales, con su cálculo nutricional por ración;',
             'la exportación completa de tus datos, en JSON o CSV, en cualquier momento.'],
    payant='Los <strong>análisis</strong> — el balance semanal y su historial, el metabolismo a lo largo del tiempo, el volumen por grupo muscular, las proteínas de los días de entrenamiento frente a los de descanso, las estrategias nutricionales avanzadas — y tres <strong>asistentes de comidas</strong> que organizan tus comidas, preparan tu semana y la optimizan (cada uno se puede probar una vez gratis). Las recetas, la planificación y la lista de la compra siguen siendo gratuitas. 4,99 € al mes o 39,99 € al año.',
    regle='El reparto sigue una regla sencilla: <strong>registrar y cocinar es gratis; entender y automatizar es de pago.</strong> Si nunca pagas, conservas un diario completo que no se degrada con el tiempo. Nada se bloquea a los treinta días.',
    modele='Seamos directos: este modelo existe porque es sostenible, no por filantropía. Una aplicación sin publicidad no necesita captar tu atención, y una aplicación que no revende datos no necesita tu perfil. Queda la suscripción, que solo se justifica si lo que desbloquea tiene valor por sí mismo; de ahí la decisión de no pedir nunca rescate por el seguimiento básico.',
    inconvenient='El inconveniente es real y es para mí: mucha gente usará Basal durante años sin pagar nunca. Es el precio de un modelo en el que no hace falta tenerte de rehén.',
    compte=f'Puedes usar Basal por completo sin crear una cuenta. En ese caso, tu perfil, tu peso y tus comidas se quedan en tu teléfono y no se envían a ninguna parte. El detalle, incluido lo que funciona sin conexión, está en <a href="{U["sans-compte"]["es"]}">una app de calorías sin cuenta</a>. La cuenta es opcional y solo sirve para recuperar tus datos en otro dispositivo; eliminarla los borra del servidor. La aplicación está reservada a personas mayores de edad.',
    plus=[f'<a href="{U["comparatif"]["es"]}">Comparativa: MyFitnessPal, Yazio, Foodvisor y Basal</a>: lo que cada una deja gratis, con precios.',
          f'<a href="{U["alternative-mfp"]["es"]}">Una alternativa a MyFitnessPal</a>.',
          f'<a href="{U["tdee"]["es"]}">Calcular tu gasto energético</a>: sin registro, no se envía nada.'],
    campagne='es-contador-calorias-gratis',
)

DE = dict(
    s=['Vier Arten, „kostenlos“ zu sagen', 'Was Basal kostenlos lässt', 'Was kostet also Geld?', 'Warum das keine Großzügigkeit ist', 'Und ohne Konto', 'Weiterlesen'],
    quatre_intro='Wenn sich eine App als kostenlos bezeichnet, steckt meist eine dieser Situationen dahinter. Sie sind ganz und gar nicht gleichwertig.',
    quatre=['<strong>Kostenlos mit Werbung.</strong> Du zahlst nicht mit Geld. Das Modell geht davon aus, dass deine Aufmerksamkeit etwas wert ist, also versucht die App, dich oft zurückzuholen – was nicht immer in deinem Interesse liegt.',
            '<strong>Kostenlos mit Kontingent.</strong> Eine Anzahl Lebensmittel pro Tag, eine Anzahl Rezepte, ein auf wenige Tage begrenzter Verlauf. Die App funktioniert genau bis zu dem Moment, in dem sie dir nützlich wird.',
            '<strong>Kostenlos während des Tests.</strong> Sieben Tage, manchmal drei. Danach ist es eine kostenpflichtige App, die dich vorher deine Daten hat eingeben lassen.',
            '<strong>Kostenlos, außer der Kernfunktion.</strong> Die wirksamste der vier: Alles bleibt offen außer dem, wofür du die App installiert hast. Der Barcode-Scanner ist zum Paradebeispiel geworden.'],
    scanner='<strong>Der Scanner ist der eigentliche Test.</strong> Eine Mahlzeit von Hand einzutragen dauert ein bis zwei Minuten, der Scanner drei Sekunden. Er entscheidet, ob du einen Monat durchhältst oder drei Tage. Eine App, die ihn hinter ein Abo stellt, ist keine kostenlose App mit kostenpflichtiger Option, sondern eine kostenpflichtige App mit einer Demo.',
    gratuit_intro='Ohne Abo, ohne ablaufenden Test, ohne Kontingent und ohne Werbung:',
    gratuit=['Kalorien und Makronährstoffe – Eiweiß, Kohlenhydrate, Fett, Ballaststoffe – nach Mahlzeit aufgeteilt;',
             'die Lebensmittelsuche und der <strong>Barcode-Scanner</strong>;',
             'das Gewichtstracking, mit Trends und gleitendem Durchschnitt;',
             'der adaptive Stoffwechsel, der deinen Verbrauch aus deinen echten Daten verfeinert;',
             'Krafttraining ohne Limit: über 870 Übungen, Sätze, Gewichte, Wiederholungen, Supersätze, Pausentimer, Rekorde und Routinen;',
             'Cardio-Einheiten und Schritte, mit den verbrannten Kalorien für dich berechnet;',
             'deine eigenen Rezepte, mit ihren Nährwerten pro Portion;',
             'der vollständige Export deiner Daten, als JSON oder CSV, jederzeit.'],
    payant='Die <strong>Analysen</strong> – der Wochenrückblick und sein Verlauf, der Stoffwechsel über die Zeit, das Volumen pro Muskelgruppe, das Eiweiß an Trainingstagen im Vergleich zu Ruhetagen, die fortgeschrittenen Ernährungsstrategien – und drei <strong>Mahlzeiten-Assistenten</strong>, die deine Mahlzeiten organisieren, deine Woche vorbereiten und sie optimieren (jeder lässt sich einmal kostenlos ausprobieren). Rezepte, Planung und Einkaufsliste bleiben kostenlos. 4,99 € im Monat oder 39,99 € im Jahr.',
    regle='Die Aufteilung folgt einer einfachen Regel: <strong>Erfassen und Kochen sind kostenlos, Verstehen und Automatisieren kosten Geld.</strong> Wenn du nie zahlst, behältst du ein vollständiges Tagebuch, das mit der Zeit nicht schlechter wird. Nach dreißig Tagen wird nichts gesperrt.',
    modele='Um es offen zu sagen: Dieses Modell gibt es, weil es tragfähig ist, nicht aus Menschenfreundlichkeit. Eine App ohne Werbung muss deine Aufmerksamkeit nicht einfangen, und eine App, die keine Daten verkauft, braucht dein Profil nicht. Bleibt das Abo, das sich nur rechtfertigt, wenn das, was es freischaltet, einen eigenen Wert hat – daher die Entscheidung, das Basis-Tracking nie als Druckmittel zu verwenden.',
    inconvenient='Der Nachteil ist real, und er liegt bei mir: Viele Menschen werden Basal jahrelang nutzen, ohne je zu zahlen. Das ist der Preis eines Modells, in dem man dich nicht als Geisel nehmen muss.',
    compte=f'Du kannst Basal vollständig ohne Konto nutzen. Dann bleiben dein Profil, dein Gewicht und deine Mahlzeiten auf deinem Handy und werden nirgendwohin gesendet. Die Einzelheiten, auch was offline funktioniert, stehen in <a href="{U["sans-compte"]["de"]}">Kalorien-App ohne Konto</a>. Das Konto ist freiwillig und dient nur dazu, deine Daten auf einem anderen Gerät wiederzufinden; wenn du es löschst, werden sie vom Server entfernt. Die App ist nur für Volljährige.',
    plus=[f'<a href="{U["comparatif"]["de"]}">Vergleich: MyFitnessPal, Yazio, Foodvisor und Basal</a> – was jede kostenlos lässt, mit Preisen.',
          f'<a href="{U["alternative-mfp"]["de"]}">Eine Alternative zu MyFitnessPal</a>.',
          f'<a href="{U["tdee"]["de"]}">Deinen Energieverbrauch berechnen</a> – ohne Anmeldung, nichts wird gesendet.'],
    campagne='de-kalorienzaehler-kostenlos',
)

META = {
    'en': ('Free calorie counter', 'Choosing an app', 'A free calorie app, with no subscription',
           'Every nutrition tracking app is free to download. So the word no longer says much. What does say something is the list of what you can do without paying — and that list has shrunk almost everywhere in recent years.',
           'This page is for information and written by the publisher of Basal. Basal is not a medical device and does not replace advice from a health professional.',
           dict(title='Free calorie counter app, no subscription — Basal',
                description='A free calorie app: what “free” means elsewhere (paid scanner, quotas, trials that expire) and what Basal keeps free, with no time limit.',
                og_title='A free calorie app, with no subscription',
                og_description='Paid scanner, daily quotas, trials that expire: what “free” really covers, and what Basal keeps open.')),
    'es': ('Contador de calorías gratis', 'Elegir una aplicación', 'Una aplicación de calorías gratis y sin suscripción',
           'Todas las aplicaciones de seguimiento nutricional son gratuitas al descargarlas. Así que la palabra ya no dice gran cosa. Lo que sí lo dice es la lista de lo que se puede hacer sin pagar, y esa lista se ha acortado casi en todas partes estos últimos años.',
           'Esta página es informativa y la ha redactado el editor de Basal. Basal no es un dispositivo médico y no sustituye el consejo de un profesional sanitario.',
           dict(title='Contador de calorías gratis, sin suscripción — Basal',
                description='Una aplicación de calorías gratis: lo que «gratis» significa en otras (escáner de pago, cupos, pruebas que caducan) y lo que Basal mantiene gratis, sin límite de tiempo.',
                og_title='Una aplicación de calorías gratis y sin suscripción',
                og_description='Escáner de pago, cupos diarios, pruebas que caducan: lo que «gratis» cubre de verdad, y lo que Basal deja abierto.')),
    'de': ('Kalorienzähler kostenlos', 'Eine App wählen', 'Eine kostenlose Kalorien-App, ohne Abo',
           'Alle Ernährungstracking-Apps sind kostenlos herunterzuladen. Das Wort sagt also nicht mehr viel. Was etwas sagt, ist die Liste dessen, was man ohne Bezahlung tun kann – und diese Liste ist in den letzten Jahren fast überall kürzer geworden.',
           'Diese Seite dient der Information und wurde vom Herausgeber von Basal verfasst. Basal ist kein Medizinprodukt und ersetzt nicht den Rat medizinischen Fachpersonals.',
           dict(title='Kalorienzähler kostenlos, ohne Abo — Basal',
                description='Eine kostenlose Kalorien-App: was „kostenlos“ anderswo bedeutet (Scanner kostenpflichtig, Kontingente, ablaufende Tests) und was Basal ohne Zeitlimit kostenlos lässt.',
                og_title='Eine kostenlose Kalorien-App, ohne Abo',
                og_description='Kostenpflichtiger Scanner, Tageskontingente, ablaufende Tests: was „kostenlos“ wirklich heißt, und was Basal offen lässt.')),
}

PAGES = {}
for l, t in (('en', EN), ('es', ES), ('de', DE)):
    court, sur, h1, chap, note, tete = META[l]
    PAGES[l] = page(l, C, dict(court=court, surtitre=sur, h1=h1, chapeau=chap, note=note, publie='2026-10-06', maj='2026-10-31',
                               sommaire=list(zip(IDS[l], t['s'])), corps=corps(l, t)), tete)
