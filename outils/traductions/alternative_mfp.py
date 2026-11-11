from commun import U, page, stores

FR = '/alternative-myfitnesspal.html'
DATE = '2026-11-11'
C = 'alternative-mfp'
IDS = ['what-basal-does-less-well', 'what-basal-does-differently', 'and-the-tone', 'in-short']


def corps(l, t):
    li = lambda xs: '\n'.join(f'      <li>{x}</li>' for x in xs)
    sous = '\n\n'.join(f'      <h3>{h}</h3>\n' + '\n'.join(f'      <p>{p}</p>' for p in ps) for h, ps in t['autrement'])
    s = t['s']
    return f'''      <h2 id="{IDS[0]}">{s[0]}</h2>
      <p>{t["base"]}</p>
      <ul class="liste">
{li(t["moins"])}
      </ul>
      <p>{t["bloque"]}</p>

      <h2 id="{IDS[1]}">{s[1]}</h2>

{sous}

      <h2 id="{IDS[2]}">{s[2]}</h2>
      <p>{t["ton"]}</p>
      <div class="encadre">
        <p>{t["constate"]}</p>
      </div>
      <p>{t["adultes"]}</p>

      <h2 id="{IDS[3]}">{s[3]}</h2>
      <div class="cartes">
        <div class="carte">
          <h3>{t["choisis"][0]}</h3>
          <p>{t["choisis"][1]}</p>
        </div>
        <div class="carte">
          <h3>{t["reste"][0]}</h3>
          <p>{t["reste"][1]}</p>
        </div>
      </div>

      <p>{t["essayer"]}</p>

      {stores(l, t["campagne"])}'''


def textes(l):
    u = lambda k: U[k][l]
    if l == 'en':
        return dict(
            s=['Let’s start with what Basal will not do as well', 'What Basal does differently', 'And the tone', 'In short'],
            base='A food database is built over time and with its users. Apps installed for fifteen years have a head start that nothing catches up in a few months, and for an obscure processed product, they will find an entry where Basal will not.',
            moins=['<strong>Basal exists in English, French, Spanish and German, no further.</strong> And its food database is designed for France: if you live elsewhere, some of the products in your supermarket will not be in it.',
                   '<strong>No iPad layout</strong>: on a tablet, the app runs in iPhone compatibility mode.',
                   '<strong>Two food databases, each with its limit.</strong> Everyday foods come from ANSES’s Ciqual table (over 3,000 foods, French reference values); packaged products come from Open Food Facts, an open database fed by volunteers, whose quality varies from one product to another.',
                   '<strong>No news feed, no messaging, no conversational coach.</strong> Basal’s Community is only for sharing recipes, routines and programmes. If you are looking for a social network, Basal will disappoint you.',
                   '<strong>No import from another app.</strong> You start from a blank page: your history stays where it is.'],
            bloque='If one of these points is a deal-breaker, the rest will not change anything, and you might as well know now.',
            autrement=[('Tracking is free, complete and has no time limit', [
                            'Calories, macronutrients, barcode scanner, weight tracking, activity, steps, unlimited strength training, personal recipes, exporting your data: all of it is free. There is no trial that expires, no daily food quota, and no scanner reserved for subscribers.',
                            'The Premium subscription — €4.99 a month or €39.99 a year in the eurozone, shown in your currency in the store — adds the <strong>analyses</strong> (the weekly review and its history, metabolism over time, volume per muscle group, protein on training days compared with rest days, advanced nutrition strategies) and three <strong>meal assistants</strong> that organise your meals, prepare your week and optimise it. Recipes, meal planning and the shopping list stay free. If you never pay, you keep a whole tracking app.']),
                       ('No ads, no selling of data', ['There is no banner, no interstitial, no video to watch, and your data is sold to no one. This is not a sales promise, it is a consequence of the model: an app that lives on a subscription needs neither your attention nor your profile.']),
                       ('No mandatory account', ['You can install Basal and use it fully without ever creating an account. In that case, your profile, your weight and your meals stay on your phone and are sent nowhere. The account exists, it is optional, and it is for getting your data back on another device — the data then goes to a server located in Ireland, in the European Union, and deleting the account erases it.']),
                       ('Nutrition and strength training talk to each other', [
                            'This is the difference that motivated the app. A strength-training log ignores what you eat; a nutrition app ignores what you lift. Basal knows both, so it can answer questions neither category handles alone: how many sets each muscle group really gets over the week, what you eat on rest days compared with training days, and whether your lifts go up while your weight goes down.',
                            f'The details of these three analyses are on the <a href="{u("nutrition-musculation")}">nutrition and strength training</a> page.']),
                       ('A metabolism that learns, not a fixed formula', [f'Many apps calculate your expenditure once at sign-up, with an equation and an activity factor picked from a list, then never come back to it. Basal starts from the same equation, then compares what you log with how your weight actually changes to refine your expenditure over the weeks. It is explained on the <a href="{u("metabolisme-adaptatif")}">adaptive metabolism</a> page, and you can do the starting calculation yourself with the <a href="{u("tdee")}">calculator</a>.'])],
            ton='It is hard to put in a comparison table, yet it is what comes up most often among people who leave a tracking app.',
            constate='<strong>Basal observes, it does not prescribe.</strong> A day above your target is never presented as a failure, and the current day is never counted as missed before it is over. A missed day triggers no guilt-inducing reminder. The weekly review states how reliable your data is before stating any numbers: with three days logged out of seven, it tells you so, instead of passing noise off as fact.',
            adultes='The app is for adults only. Calorie tracking in teenagers is a documented risk factor for eating disorders, and that is why the rating is set at 18+ in both stores.',
            choisis=('Choose Basal if', 'you want free, unlimited tracking, in English, French, Spanish or German, that links your eating and your training sessions, with no ads and no forced account.'),
            reste=('Stay where you are if', 'you need another language, a very large food database (especially outside France), a social network with a news feed, or to bring over an existing history.'),
            essayer='Since tracking is free and needs no account, trying it requires no sign-up. If it does not suit you, uninstall it: nothing has gone anywhere else.',
            campagne='en-myfitnesspal-alternative',
        )
    if l == 'es':
        return dict(
            s=['Empecemos por lo que Basal no hará tan bien', 'Lo que Basal hace de otra manera', 'Y el tono', 'En resumen'],
            base='Una base de alimentos se construye con el tiempo y con sus usuarios. Las aplicaciones instaladas desde hace quince años tienen una ventaja que nada recupera en unos meses, y con un producto industrial poco conocido encontrarán una ficha donde Basal no la tendrá.',
            moins=['<strong>Basal existe en español, francés, inglés y alemán, nada más.</strong> Y su base de alimentos está pensada para Francia: si vives en otro país, parte de los productos de tu supermercado no estarán.',
                   '<strong>Sin diseño para iPad</strong>: en tableta, la aplicación funciona en modo de compatibilidad con iPhone.',
                   '<strong>Dos bases de alimentos, cada una con su límite.</strong> Los alimentos corrientes vienen de la tabla Ciqual de la ANSES (más de 3.000 alimentos, valores de referencia franceses); los productos envasados vienen de Open Food Facts, una base abierta alimentada por voluntarios, cuya calidad es desigual según el producto.',
                   '<strong>Ningún muro de noticias, ninguna mensajería, ningún coach conversacional.</strong> La Comunidad de Basal solo sirve para compartir recetas, rutinas y programas. Si buscas una red social, Basal te decepcionará.',
                   '<strong>No se puede importar desde otra aplicación.</strong> Empiezas de cero: tu historial se queda donde está.'],
            bloque='Si alguno de estos puntos te frena, lo que sigue no cambiará nada, y más vale saberlo ahora.',
            autrement=[('El seguimiento es gratis, completo y sin límite de tiempo', [
                            'Calorías, macronutrientes, escáner de códigos de barras, seguimiento del peso, actividad, pasos, musculación ilimitada, recetas personales, exportación de tus datos: todo eso es gratis. No hay periodo de prueba que caduque, ni cupo de alimentos al día, ni escáner reservado a suscriptores.',
                            'La suscripción Premium — 4,99 € al mes o 39,99 € al año — añade los <strong>análisis</strong> (el balance semanal y su historial, el metabolismo a lo largo del tiempo, el volumen por grupo muscular, las proteínas de los días de entrenamiento frente a los de descanso, las estrategias nutricionales avanzadas) y tres <strong>asistentes de comidas</strong> que organizan tus comidas, preparan tu semana y la optimizan. Las recetas, la planificación y la lista de la compra siguen siendo gratis. Si nunca pagas, conservas una aplicación de seguimiento completa.']),
                       ('Sin publicidad y sin venta de datos', ['No hay banners, ni intersticiales, ni vídeos que ver, y tus datos no se venden a nadie. No es una promesa comercial, es la consecuencia del modelo: una aplicación que vive de una suscripción no necesita ni tu atención ni tu perfil.']),
                       ('Ninguna cuenta obligatoria', ['Puedes instalar Basal y usarlo por completo sin crear nunca una cuenta. En ese caso, tu perfil, tu peso y tus comidas se quedan en tu teléfono y no se envían a ninguna parte. La cuenta existe, es opcional y sirve para recuperar tus datos en otro dispositivo; entonces se envían a un servidor situado en Irlanda, en la Unión Europea, y eliminar la cuenta los borra.']),
                       ('La nutrición y la musculación se hablan', [
                            'Es la diferencia que motivó la aplicación. Un cuaderno de musculación ignora lo que comes; una aplicación de nutrición ignora lo que levantas. Basal conoce ambas cosas, y por eso puede responder a preguntas que ninguna de las dos categorías trata por separado: cuántas series recibe de verdad cada grupo muscular en la semana, lo que comes los días de descanso frente a los de entrenamiento, y si tus cargas suben mientras tu peso baja.',
                            f'El detalle de estos tres análisis está en la página <a href="{u("nutrition-musculation")}">nutrición y fuerza</a>.']),
                       ('Un metabolismo aprendido, no una fórmula fija', [f'Muchas aplicaciones calculan tu gasto una vez al registrarte, con una ecuación y un coeficiente de actividad elegido de una lista, y no vuelven a tocarlo. Basal parte de la misma ecuación y luego compara lo que registras con la evolución real de tu peso para afinar tu gasto con las semanas. Se explica en la página <a href="{u("metabolisme-adaptatif")}">metabolismo adaptativo</a>, y puedes hacer el cálculo de partida tú mismo con la <a href="{u("tdee")}">calculadora</a>.'])],
            ton='Es difícil de meter en una tabla comparativa, y sin embargo es lo que más se repite entre quienes dejan una aplicación de seguimiento.',
            constate='<strong>Basal constata, no prescribe.</strong> Un día por encima de tu objetivo nunca se presenta como un fracaso, y el día en curso nunca se cuenta como fallido antes de que termine. Un día sin registrar no dispara ningún recordatorio culpabilizador. El balance semanal indica la fiabilidad de tus datos antes de dar cifras: con tres días registrados de siete, te lo dice, en lugar de hacer pasar ruido por un hecho.',
            adultes='La aplicación está reservada a adultos. El seguimiento calórico en adolescentes es un factor de riesgo documentado de trastornos de la conducta alimentaria, y por eso la clasificación está fijada en mayores de 18 años en ambas tiendas.',
            choisis=('Elige Basal si', 'quieres un seguimiento gratis y sin límite, en español, francés, inglés o alemán, que cruce tu alimentación y tus sesiones, sin publicidad ni cuenta impuesta.'),
            reste=('Quédate donde estás si', 'necesitas otro idioma, una base de alimentos muy amplia (sobre todo fuera de Francia), una red social con muro de noticias, o recuperar un historial existente.'),
            essayer='Como el seguimiento es gratis y sin cuenta, probarlo no requiere registro. Si no te convence, desinstálalo: nada se ha ido a otra parte.',
            campagne='es-alternativa-myfitnesspal',
        )
    return dict(
        s=['Zuerst, was Basal nicht so gut kann', 'Was Basal anders macht', 'Und der Ton', 'Kurz gesagt'],
        base='Eine Lebensmitteldatenbank entsteht mit der Zeit und mit ihren Nutzern. Apps, die seit fünfzehn Jahren installiert werden, haben einen Vorsprung, den in ein paar Monaten nichts aufholt, und bei einem wenig bekannten Industrieprodukt finden sie einen Eintrag, wo Basal keinen hat.',
        moins=['<strong>Basal gibt es auf Deutsch, Französisch, Englisch und Spanisch, nicht darüber hinaus.</strong> Und seine Lebensmitteldatenbank ist für Frankreich gedacht: Wenn du anderswo lebst, fehlt ein Teil der Produkte aus deinem Supermarkt.',
               '<strong>Kein iPad-Layout</strong>: Auf dem Tablet läuft die App im iPhone-Kompatibilitätsmodus.',
               '<strong>Zwei Lebensmitteldatenbanken, jede mit ihrer Grenze.</strong> Alltägliche Lebensmittel stammen aus der Ciqual-Tabelle der ANSES (über 3.000 Lebensmittel, französische Referenzwerte); verpackte Produkte stammen aus Open Food Facts, einer offenen Datenbank, die von Freiwilligen gepflegt wird und deren Qualität je nach Produkt schwankt.',
               '<strong>Kein Newsfeed, keine Nachrichten, kein Chat-Coach.</strong> Die Community von Basal dient nur dazu, Rezepte, Routinen und Programme zu teilen. Wenn du ein soziales Netzwerk suchst, wird Basal dich enttäuschen.',
               '<strong>Kein Import aus einer anderen App.</strong> Du fängst bei null an: Dein Verlauf bleibt, wo er ist.'],
        bloque='Wenn einer dieser Punkte für dich ein Ausschlusskriterium ist, ändert der Rest nichts daran, und das weißt du besser gleich.',
        autrement=[('Das Tracking ist kostenlos, vollständig und zeitlich unbegrenzt', [
                        'Kalorien, Makronährstoffe, Barcode-Scanner, Gewichtstracking, Aktivität, Schritte, unbegrenztes Krafttraining, eigene Rezepte, Export deiner Daten: All das ist kostenlos. Es gibt keinen ablaufenden Testzeitraum, kein Tageskontingent an Lebensmitteln und keinen Scanner nur für Abonnenten.',
                        'Das Premium-Abo – 4,99 € im Monat oder 39,99 € im Jahr – fügt die <strong>Analysen</strong> hinzu (den Wochenrückblick und seinen Verlauf, den Stoffwechsel über die Zeit, das Volumen pro Muskelgruppe, das Eiweiß an Trainingstagen im Vergleich zu Ruhetagen, die fortgeschrittenen Ernährungsstrategien) sowie drei <strong>Mahlzeiten-Assistenten</strong>, die deine Mahlzeiten organisieren, deine Woche vorbereiten und sie optimieren. Rezepte, Planung und Einkaufsliste bleiben kostenlos. Wenn du nie zahlst, behältst du eine vollständige Tracking-App.']),
                   ('Keine Werbung, kein Datenverkauf', ['Es gibt kein Banner, keine Einblendung, kein Video zum Ansehen, und deine Daten werden an niemanden verkauft. Das ist kein Werbeversprechen, sondern eine Folge des Modells: Eine App, die von einem Abo lebt, braucht weder deine Aufmerksamkeit noch dein Profil.']),
                   ('Kein Pflichtkonto', ['Du kannst Basal installieren und vollständig nutzen, ohne je ein Konto anzulegen. Dann bleiben dein Profil, dein Gewicht und deine Mahlzeiten auf deinem Handy und werden nirgendwohin gesendet. Das Konto gibt es, es ist freiwillig und dient dazu, deine Daten auf einem anderen Gerät wiederzufinden – sie gehen dann auf einen Server in Irland, in der Europäischen Union, und das Löschen des Kontos entfernt sie.']),
                   ('Ernährung und Krafttraining reden miteinander', [
                        'Das ist der Unterschied, der die App ausgelöst hat. Ein Trainingstagebuch weiß nicht, was du isst; eine Ernährungs-App weiß nicht, was du hebst. Basal kennt beides und kann deshalb Fragen beantworten, die keine der beiden Kategorien allein behandelt: wie viele Sätze jede Muskelgruppe in der Woche wirklich bekommt, was du an Ruhetagen im Vergleich zu Trainingstagen isst, und ob deine Gewichte steigen, während dein Körpergewicht sinkt.',
                        f'Die Einzelheiten dieser drei Analysen stehen auf der Seite <a href="{u("nutrition-musculation")}">Ernährung und Krafttraining</a>.']),
                   ('Ein gelernter Stoffwechsel statt einer starren Formel', [f'Viele Apps berechnen deinen Verbrauch einmal bei der Anmeldung, mit einer Gleichung und einem aus einer Liste gewählten Aktivitätsfaktor, und kommen nie wieder darauf zurück. Basal geht von derselben Gleichung aus und vergleicht dann, was du erfasst, mit der tatsächlichen Entwicklung deines Gewichts, um deinen Verbrauch über die Wochen zu verfeinern. Das erklärt die Seite <a href="{u("metabolisme-adaptatif")}">metabolische Anpassung</a>, und die Ausgangsrechnung kannst du selbst mit dem <a href="{u("tdee")}">Rechner</a> machen.'])],
        ton='Das lässt sich schwer in eine Vergleichstabelle packen, und doch ist es das, was Menschen, die eine Tracking-App verlassen, am häufigsten nennen.',
        constate='<strong>Basal stellt fest, es schreibt nicht vor.</strong> Ein Tag über deinem Ziel wird nie als Misserfolg dargestellt, und der laufende Tag zählt nie als verpasst, bevor er vorbei ist. Ein ausgelassener Tag löst keine Erinnerung aus, die ein schlechtes Gewissen macht. Der Wochenrückblick nennt die Verlässlichkeit deiner Daten, bevor er Zahlen nennt: Bei drei erfassten Tagen von sieben sagt er dir das, statt Rauschen als Tatsache auszugeben.',
        adultes='Die App ist nur für Erwachsene. Kalorientracking bei Jugendlichen ist ein belegter Risikofaktor für Essstörungen, und deshalb ist die Altersfreigabe in beiden Stores auf 18+ festgelegt.',
        choisis=('Wähle Basal, wenn', 'du ein kostenloses, unbegrenztes Tracking willst, auf Deutsch, Französisch, Englisch oder Spanisch, das deine Ernährung und deine Einheiten verknüpft, ohne Werbung und ohne Kontozwang.'),
        reste=('Bleib, wo du bist, wenn', 'du eine andere Sprache brauchst, eine sehr große Lebensmitteldatenbank (vor allem außerhalb Frankreichs), ein soziales Netzwerk mit Newsfeed oder einen bestehenden Verlauf übernehmen willst.'),
        essayer='Da das Tracking kostenlos und ohne Konto ist, braucht das Ausprobieren keine Anmeldung. Wenn es dir nicht passt, deinstalliere es: Nichts ist woanders hingegangen.',
        campagne='de-myfitnesspal-alternative',
    )


MARQUE = {'en': 'MyFitnessPal is a trademark of MyFitnessPal, Inc. This page is neither affiliated with nor endorsed by its owners.',
          'es': 'MyFitnessPal es una marca de MyFitnessPal, Inc. Esta página no está afiliada a sus titulares ni aprobada por ellos.',
          'de': 'MyFitnessPal ist eine Marke von MyFitnessPal, Inc. Diese Seite ist weder mit den Inhabern verbunden noch von ihnen gebilligt.'}
NOTE = {'en': 'This page is for information and written by the publisher of Basal. Basal is not a medical device and does not replace advice from a health professional.',
        'es': 'Esta página es informativa y la ha redactado el editor de Basal. Basal no es un dispositivo médico y no sustituye el consejo de un profesional sanitario.',
        'de': 'Diese Seite dient der Information und wurde vom Herausgeber von Basal verfasst. Basal ist kein Medizinprodukt und ersetzt nicht den Rat medizinischen Fachpersonals.'}

META = {
    'en': ('MyFitnessPal alternative', 'Choosing an app', 'An alternative to MyFitnessPal, made in France',
           'This page is written by the developer of Basal. So I am both judge and party, and the most useful comparison I can offer is not to speak ill of an app that millions of people use very well — it is to say precisely what mine does differently, and what it does not do at all.',
           dict(title='An alternative to MyFitnessPal, made in France — Basal', description='What Basal does less well than MyFitnessPal, what it does differently (free tracking with no time limit, no ads, no mandatory account, nutrition and strength training together), and who should stay where they are.',
                og_title='An alternative to MyFitnessPal, made in France', og_description='What Basal does less well, what it does differently, and who should stay where they are.')),
    'es': ('Alternativa a MyFitnessPal', 'Elegir una aplicación', 'Una alternativa a MyFitnessPal, hecha en Francia',
           'Esta página la escribe el desarrollador de Basal. Soy, por tanto, juez y parte, y la comparación más útil que puedo ofrecer no es hablar mal de una aplicación que millones de personas usan muy bien, sino decir con precisión lo que la mía hace de otra manera, y lo que no hace en absoluto.',
           dict(title='Una alternativa a MyFitnessPal, hecha en Francia — Basal', description='Lo que Basal hace peor que MyFitnessPal, lo que hace de otra manera (seguimiento gratis sin límite de tiempo, sin publicidad, sin cuenta obligatoria, nutrición y musculación juntas) y a quién le conviene quedarse donde está.',
                og_title='Una alternativa a MyFitnessPal, hecha en Francia', og_description='Lo que Basal hace peor, lo que hace de otra manera y a quién le conviene quedarse donde está.')),
    'de': ('MyFitnessPal-Alternative', 'Eine App wählen', 'Eine Alternative zu MyFitnessPal, aus Frankreich',
           'Diese Seite schreibt der Entwickler von Basal. Ich bin also Richter und Partei zugleich, und der nützlichste Vergleich, den ich bieten kann, ist nicht, schlecht über eine App zu reden, die Millionen Menschen sehr gut nutzen – sondern genau zu sagen, was meine anders macht und was sie gar nicht macht.',
           dict(title='Eine Alternative zu MyFitnessPal, aus Frankreich — Basal', description='Was Basal schlechter kann als MyFitnessPal, was es anders macht (kostenloses Tracking ohne Zeitlimit, keine Werbung, kein Pflichtkonto, Ernährung und Krafttraining zusammen) und wer besser bleibt, wo er ist.',
                og_title='Eine Alternative zu MyFitnessPal, aus Frankreich', og_description='Was Basal schlechter kann, was es anders macht und wer besser bleibt, wo er ist.')),
}

PAGES = {}
for l in ('en', 'es', 'de'):
    court, sur, h1, chap, tete = META[l]
    t = textes(l)
    PAGES[l] = page(l, C, dict(court=court, surtitre=sur, h1=h1, chapeau=chap, publie='2026-10-06', maj='2026-10-30',
                               note=f'{NOTE[l]}</p>\n    <p>{MARQUE[l]}', sommaire=list(zip(IDS, t['s'])), corps=corps(l, t)), tete)
