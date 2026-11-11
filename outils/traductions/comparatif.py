from commun import U, page, stores

FR = '/comparatif-applications-nutrition.html'
DATE = '2026-11-11'
C = 'comparatif'
IDS = ['what-each-does-best', 'what-is-free', 'prices', 'what-none-of-the-three-does', 'what-basal-does-not-do', 'how-to-choose', 'going-further']
PRIX = [('MyFitnessPal Premium', '9,99', '49,99'), ('Yazio Pro', '6,99', '44,99'), ('Foodvisor Premium', None, '59,99'), ('Basal Premium', '4,99', '39,99')]


def corps(l, t):
    li = lambda xs: '\n'.join(f'      <li>{x}</li>' for x in xs)
    cartes = lambda cs: '\n'.join(f'''        <div class="carte">
          <h3>{h}</h3>
          <p>{p}</p>
        </div>''' for h, p in cs)
    e = (lambda x: f'€{x.replace(",", ".")}') if l == 'en' else (lambda x: f'{x} €')
    prix = li([t['prix'](nom, e(m) if m else None, e(a), nom.startswith('Basal')) for nom, m, a in PRIX])
    s = t['s']
    return f'''      <div class="encadre">
        <p>{t["releve"]}</p>
      </div>

      <h2 id="{IDS[0]}">{s[0]}</h2>
      <div class="cartes">
{cartes(t["mieux"])}
      </div>

      <h2 id="{IDS[1]}">{s[1]}</h2>
      <p>{t["gratuit_intro"]}</p>
      <ul class="liste">
{li(t["gratuit"])}
      </ul>

      <h2 id="{IDS[2]}">{s[2]}</h2>
      <ul class="liste">
{prix}
      </ul>
      <p>{t["bougent"]}</p>

      <h2 id="{IDS[3]}">{s[3]}</h2>
      <p>{t["aucune"][0]}</p>
      <p>{t["aucune"][1]}</p>

      <h2 id="{IDS[4]}">{s[4]}</h2>
      <p>{t["basal_pas"]}</p>

      <h2 id="{IDS[5]}">{s[5]}</h2>
      <div class="cartes">
{cartes(t["choisir"])}
      </div>

      <h2 id="{IDS[6]}">{s[6]}</h2>
      <ul class="liste">
{li(t["plus"])}
      </ul>

      {stores(l, t["campagne"])}'''


def textes(l):
    u = lambda k: U[k][l]
    if l == 'en':
        return dict(
            s=['What each one does best', 'The real question is not the price, it is what is free', 'Prices', 'What none of the three does', 'And what Basal does not do', 'How to choose', 'Going further'],
            releve='<strong>Prices and features checked in October 2026</strong>, for France, in euros. These apps change their offers regularly, and prices differ from one country to another — if you read this page long afterwards, or outside France, check the stores directly before deciding.',
            mieux=[('MyFitnessPal', 'The largest food database on the market, built over more than fifteen years. Available in many languages, with a mature ecosystem of integrations. If you travel or scan products from all over, it is the one that will find the entry.'),
                   ('Yazio', 'A German product, very polished, with the most generous free version of the three — the barcode scanner is included. Good coverage of European supermarket products, and intermittent fasting far more developed than elsewhere.'),
                   ('Foodvisor', 'A French app, built around photo recognition: you photograph your plate and it estimates what is on it. It is the fastest logging of the lot when it works, and no one else has made it the core of their product.')],
            gratuit_intro='All these apps are “free” to download. The difference lies elsewhere: in what you can really do without paying, and above all in what has moved behind the subscription over the years.',
            gratuit=['<strong>MyFitnessPal</strong> moved its <strong>barcode scanner</strong> into the paid offer. It was the most used feature of its free version, and its move to Premium is largely what fuelled the search for alternatives.',
                     '<strong>Foodvisor</strong> keeps what makes it interesting for subscribers: photo recognition, recipes, courses. The free version is essentially limited to manual logging.',
                     '<strong>Yazio</strong> is the most generous of the three: the scanner stays free, and the free version is enough for many people.',
                     '<strong>Basal</strong> keeps all of the <strong>tracking</strong> free: calories, macros, scanner, weight, activity, steps, unlimited strength training, recipes, meal planning, shopping list and export. The subscription adds the <strong>analyses</strong> and three meal assistants.'],
            prix=lambda nom, m, a, basal: f'<strong>{nom}</strong> — {"" if basal else "around "}{m + " a month or " if m else ""}{a} a year.',
            bougent='These amounts change, and the stores sometimes show first-year promotions that make comparisons misleading. The number that matters is the renewal price, not the first bill.',
            aucune=['MyFitnessPal, Yazio and Foodvisor are <strong>nutrition</strong> apps. They sometimes record sessions, as calories burned — but none of them keeps a real strength-training log, and none links the two diaries.',
                    f'Three questions therefore go unanswered, whichever of the three you choose: how many sets each muscle group really gets over a week, what you eat on rest days compared with training days, and whether your lifts progress while your weight goes down. You need both diaries to answer them, and that is Basal’s reason for being. The details are on the <a href="{u("nutrition-musculation")}">nutrition and strength training</a> page.'],
            basal_pas='For this page to keep its value, the end of the list is needed too. Basal exists <strong>only in English, French, Spanish and German</strong>, has no photo recognition of meals, has no news feed or messaging (its Community is only for sharing recipes, routines and programmes), and cannot import a history from another app. Its food database combines ANSES’s Ciqual table for everyday foods and Open Food Facts, an open, collaborative database, for packaged products: very complete for common products in France, sparser for rare items and for products sold elsewhere.',
            choisir=[('If you do not do strength training', 'Yazio is probably the best features-to-price ratio of the four, and its free version is enough for many people.'),
                     ('If you hate logging your meals', 'Foodvisor, for the photo — provided you accept that most of it is behind the subscription.'),
                     ('If you scan products from all over the world', 'MyFitnessPal, for the size of its database, knowing that the scanner requires the subscription.'),
                     ('If you lift weights', 'Basal, because it is the only one of the four that also keeps the training log and links the two.')],
            plus=[f'<a href="{u("alternative-mfp")}">An alternative to MyFitnessPal, made in France</a> — the detailed comparison with Basal.',
                  f'<a href="{u("compteur-gratuit")}">A calorie counter that is really free</a> — what “free” means from one app to another.',
                  f'<a href="{u("tdee")}">Calculate your energy expenditure</a> — the calculator, with no sign-up.'],
            campagne='en-nutrition-apps-compared',
            marques='MyFitnessPal, Yazio and Foodvisor are trademarks of their respective owners. This page is neither affiliated with nor endorsed by these companies. Google Play and the Google Play logo are trademarks of Google LLC. Apple and the App Store logo are trademarks of Apple Inc., registered in the U.S. and other countries.',
        )
    if l == 'es':
        return dict(
            s=['Lo que cada una hace mejor', 'La verdadera pregunta no es el precio, sino lo que es gratis', 'Los precios', 'Lo que ninguna de las tres hace', 'Y lo que Basal no hace', 'Cómo elegir', 'Para saber más'],
            releve='<strong>Precios y funciones consultados en octubre de 2026</strong>, para Francia. Estas aplicaciones cambian sus ofertas con regularidad, y los precios varían de un país a otro: si lees esta página mucho tiempo después, o fuera de Francia, compruébalo directamente en las tiendas antes de decidir.',
            mieux=[('MyFitnessPal', 'La base de alimentos más grande del mercado, construida durante más de quince años. Disponible en muchos idiomas, con un ecosistema de integraciones maduro. Si viajas o escaneas productos de cualquier parte, es la que encontrará la ficha.'),
                   ('Yazio', 'Producto alemán, muy pulido, con la versión gratuita más generosa de las tres: el escáner de códigos de barras está incluido. Buena cobertura de productos de supermercado europeos, y un ayuno intermitente mucho más trabajado que en otras.'),
                   ('Foodvisor', 'Aplicación francesa, construida en torno al reconocimiento por foto: fotografías tu plato y estima lo que contiene. Es el registro más rápido del grupo cuando funciona, y nadie más lo ha convertido en el centro de su producto.')],
            gratuit_intro='Todas estas aplicaciones son «gratuitas» al descargarlas. La diferencia está en otra parte: en lo que puedes hacer de verdad sin pagar y, sobre todo, en lo que ha pasado detrás de la suscripción con los años.',
            gratuit=['<strong>MyFitnessPal</strong> pasó su <strong>escáner de códigos de barras</strong> a la oferta de pago. Era la función más usada de su versión gratuita, y su paso a Premium es en buena parte lo que alimentó la búsqueda de alternativas.',
                     '<strong>Foodvisor</strong> reserva a la suscripción lo que la hace interesante: el reconocimiento por foto, las recetas, los cursos. La versión gratuita se limita básicamente al registro manual.',
                     '<strong>Yazio</strong> es la más generosa de las tres: el escáner sigue siendo gratis, y la versión libre le basta a mucha gente.',
                     '<strong>Basal</strong> mantiene gratis todo el <strong>seguimiento</strong>: calorías, macros, escáner, peso, actividad, pasos, musculación ilimitada, recetas, planificación de comidas, lista de la compra y exportación. La suscripción añade los <strong>análisis</strong> y tres asistentes de comidas.'],
            prix=lambda nom, m, a, basal: f'<strong>{nom}</strong>: {"" if basal else "unos "}{m + " al mes o " if m else ""}{a} al año.',
            bougent='Estos importes cambian, y las tiendas muestran a veces promociones del primer año que hacen engañosas las comparaciones. La cifra que cuenta es la de la renovación, no la de la primera factura.',
            aucune=['MyFitnessPal, Yazio y Foodvisor son aplicaciones de <strong>nutrición</strong>. A veces registran sesiones, como gasto calórico, pero ninguna lleva un verdadero cuaderno de musculación, y ninguna cruza los dos diarios.',
                    f'Tres preguntas quedan, por tanto, sin respuesta, elijas la que elijas de las tres: cuántas series recibe de verdad cada grupo muscular en una semana, lo que comes los días de descanso frente a los de entrenamiento, y si tus cargas progresan mientras tu peso baja. Hacen falta los dos diarios para responderlas, y esa es la razón de ser de Basal. El detalle está en la página <a href="{u("nutrition-musculation")}">nutrición y fuerza</a>.'],
            basal_pas='Para que esta página conserve su valor, también hace falta el final de la lista. Basal existe <strong>solo en español, francés, inglés y alemán</strong>, no reconoce comidas por foto, no tiene muro de noticias ni mensajería (su Comunidad solo sirve para compartir recetas, rutinas y programas) y no permite importar un historial de otra aplicación. Su base de alimentos combina la tabla Ciqual de la ANSES para los alimentos corrientes y Open Food Facts, una base abierta y colaborativa, para los productos envasados: muy completa en productos corrientes en Francia, más escasa en referencias raras y en productos vendidos en otros países.',
            choisir=[('Si no haces musculación', 'Yazio es probablemente la mejor relación funciones-precio de las cuatro, y su versión gratuita le basta a mucha gente.'),
                     ('Si odias registrar tus comidas', 'Foodvisor, por la foto, siempre que aceptes que lo esencial está detrás de la suscripción.'),
                     ('Si escaneas productos de todo el mundo', 'MyFitnessPal, por el tamaño de su base, sabiendo que el escáner requiere la suscripción.'),
                     ('Si levantas pesas', 'Basal, porque es la única de las cuatro que también lleva el cuaderno de sesiones y cruza ambos.')],
            plus=[f'<a href="{u("alternative-mfp")}">Una alternativa a MyFitnessPal, hecha en Francia</a>: la comparación detallada con Basal.',
                  f'<a href="{u("compteur-gratuit")}">Un contador de calorías realmente gratis</a>: lo que «gratis» significa según la aplicación.',
                  f'<a href="{u("tdee")}">Calcular tu gasto energético</a>: la calculadora, sin registro.'],
            campagne='es-comparativa-apps-nutricion',
            marques='MyFitnessPal, Yazio y Foodvisor son marcas de sus respectivos titulares. Esta página no está afiliada a estas empresas ni aprobada por ellas. Google Play y el logotipo de Google Play son marcas de Google LLC. Apple y el logotipo de App Store son marcas de Apple Inc., registradas en EE. UU. y en otros países.',
        )
    return dict(
        s=['Was jede am besten kann', 'Die eigentliche Frage ist nicht der Preis, sondern was kostenlos ist', 'Die Preise', 'Was keine der drei kann', 'Und was Basal nicht kann', 'Wie wählen', 'Weiterlesen'],
        releve='<strong>Preise und Funktionen im Oktober 2026 erhoben</strong>, für Frankreich. Diese Apps ändern ihre Angebote regelmäßig, und die Preise unterscheiden sich von Land zu Land – wenn du diese Seite lange danach oder außerhalb Frankreichs liest, prüfe direkt in den Stores, bevor du dich entscheidest.',
        mieux=[('MyFitnessPal', 'Die größte Lebensmitteldatenbank auf dem Markt, über mehr als fünfzehn Jahre aufgebaut. In vielen Sprachen verfügbar, mit einem ausgereiften Ökosystem an Integrationen. Wenn du reist oder Produkte von überall scannst, findet sie den Eintrag.'),
               ('Yazio', 'Ein deutsches Produkt, sehr ausgereift, mit der großzügigsten Gratisversion der drei – der Barcode-Scanner ist enthalten. Gute Abdeckung europäischer Supermarktprodukte und ein deutlich ausgefeilteres Intervallfasten als anderswo.'),
               ('Foodvisor', 'Eine französische App, rund um Fotoerkennung gebaut: Du fotografierst deinen Teller, und sie schätzt, was darauf liegt. Wenn es klappt, ist das die schnellste Erfassung von allen, und niemand sonst hat das zum Kern seines Produkts gemacht.')],
        gratuit_intro='Alle diese Apps sind beim Herunterladen „kostenlos“. Der Unterschied liegt woanders: darin, was du ohne Bezahlung wirklich tun kannst, und vor allem darin, was im Lauf der Jahre hinter das Abo gewandert ist.',
        gratuit=['<strong>MyFitnessPal</strong> hat seinen <strong>Barcode-Scanner</strong> ins kostenpflichtige Angebot verschoben. Er war die meistgenutzte Funktion der Gratisversion, und sein Wechsel zu Premium hat die Suche nach Alternativen weitgehend befeuert.',
                 '<strong>Foodvisor</strong> behält dem Abo vor, was die App interessant macht: Fotoerkennung, Rezepte, Kurse. Die Gratisversion beschränkt sich im Wesentlichen auf manuelle Eingabe.',
                 '<strong>Yazio</strong> ist die großzügigste der drei: Der Scanner bleibt kostenlos, und die freie Version reicht vielen Menschen.',
                 '<strong>Basal</strong> lässt das gesamte <strong>Tracking</strong> kostenlos: Kalorien, Makros, Scanner, Gewicht, Aktivität, Schritte, unbegrenztes Krafttraining, Rezepte, Mahlzeitenplanung, Einkaufsliste und Export. Das Abo fügt die <strong>Analysen</strong> und drei Mahlzeiten-Assistenten hinzu.'],
        prix=lambda nom, m, a, basal: f'<strong>{nom}</strong> – {"" if basal else "etwa "}{m + " im Monat oder " if m else ""}{a} im Jahr.',
        bougent='Diese Beträge ändern sich, und die Stores zeigen manchmal Rabatte im ersten Jahr, die Vergleiche irreführend machen. Entscheidend ist der Preis bei der Verlängerung, nicht der der ersten Rechnung.',
        aucune=['MyFitnessPal, Yazio und Foodvisor sind <strong>Ernährungs</strong>-Apps. Sie erfassen manchmal Einheiten, als Kalorienverbrauch – aber keine führt ein echtes Trainingstagebuch, und keine verknüpft die beiden Tagebücher.',
                f'Drei Fragen bleiben deshalb offen, egal welche der drei du wählst: wie viele Sätze jede Muskelgruppe in einer Woche wirklich bekommt, was du an Ruhetagen im Vergleich zu Trainingstagen isst, und ob deine Gewichte steigen, während dein Körpergewicht sinkt. Um sie zu beantworten, braucht man beide Tagebücher, und das ist der Daseinszweck von Basal. Die Einzelheiten stehen auf der Seite <a href="{u("nutrition-musculation")}">Ernährung und Krafttraining</a>.'],
        basal_pas='Damit diese Seite ihren Wert behält, gehört auch das Ende der Liste dazu. Basal gibt es <strong>nur auf Deutsch, Französisch, Englisch und Spanisch</strong>, hat keine Fotoerkennung von Mahlzeiten, weder Newsfeed noch Nachrichten (die Community dient nur dazu, Rezepte, Routinen und Programme zu teilen), und erlaubt keinen Import eines Verlaufs aus einer anderen App. Die Lebensmitteldatenbank kombiniert die Ciqual-Tabelle der ANSES für alltägliche Lebensmittel und Open Food Facts, eine offene, gemeinschaftliche Datenbank, für verpackte Produkte: sehr vollständig bei gängigen Produkten in Frankreich, lückenhafter bei seltenen Artikeln und bei Produkten aus anderen Ländern.',
        choisir=[('Wenn du kein Krafttraining machst', 'Yazio hat wahrscheinlich das beste Verhältnis von Funktionen zu Preis der vier, und seine Gratisversion reicht vielen Menschen.'),
                 ('Wenn du es hasst, Mahlzeiten einzutragen', 'Foodvisor, wegen des Fotos – sofern du akzeptierst, dass das Wesentliche hinter dem Abo liegt.'),
                 ('Wenn du Produkte aus aller Welt scannst', 'MyFitnessPal, wegen der Größe seiner Datenbank, wohl wissend, dass der Scanner das Abo verlangt.'),
                 ('Wenn du Gewichte hebst', 'Basal, weil es als einzige der vier auch das Trainingstagebuch führt und beides verknüpft.')],
        plus=[f'<a href="{u("alternative-mfp")}">Eine Alternative zu MyFitnessPal, aus Frankreich</a> – der ausführliche Vergleich mit Basal.',
              f'<a href="{u("compteur-gratuit")}">Ein wirklich kostenloser Kalorienzähler</a> – was „kostenlos“ je nach App bedeutet.',
              f'<a href="{u("tdee")}">Deinen Energieverbrauch berechnen</a> – der Rechner, ohne Anmeldung.'],
        campagne='de-ernaehrungs-apps-vergleich',
        marques='MyFitnessPal, Yazio und Foodvisor sind Marken ihrer jeweiligen Inhaber. Diese Seite ist weder mit diesen Unternehmen verbunden noch von ihnen gebilligt. Google Play und das Google-Play-Logo sind Marken von Google LLC. Apple und das App-Store-Logo sind Marken von Apple Inc., eingetragen in den USA und anderen Ländern.',
    )


NOTE = {'en': 'This page is for information and written by the publisher of Basal. Basal is not a medical device and does not replace advice from a health professional.',
        'es': 'Esta página es informativa y la ha redactado el editor de Basal. Basal no es un dispositivo médico y no sustituye el consejo de un profesional sanitario.',
        'de': 'Diese Seite dient der Information und wurde vom Herausgeber von Basal verfasst. Basal ist kein Medizinprodukt und ersetzt nicht den Rat medizinischen Fachpersonals.'}

META = {
    'en': ('Nutrition apps compared', 'Choosing an app', 'Comparison: MyFitnessPal, Yazio, Foodvisor and Basal',
           'This page is written by the developer of Basal, so by someone with an interest in the answer. I wrote it anyway, trying to make it useful to someone who would not choose Basal: each app first gets what it does better than the others, and my own limits are listed like theirs.',
           dict(title='MyFitnessPal, Yazio, Foodvisor, Basal compared — Basal', description='What each nutrition app does best, what really stays free (barcode scanner, photo recognition), prices checked in October 2026, and how to choose according to your use.',
                og_title='Comparison: MyFitnessPal, Yazio, Foodvisor and Basal', og_description='What each one does best, what really stays free, prices, and how to choose.')),
    'es': ('Comparativa de aplicaciones', 'Elegir una aplicación', 'Comparativa: MyFitnessPal, Yazio, Foodvisor y Basal',
           'Esta página la escribe el desarrollador de Basal, es decir, alguien con interés en la respuesta. La he escrito igualmente, intentando que sea útil para alguien que no elegiría Basal: cada aplicación recibe primero lo que hace mejor que las demás, y mis límites se enumeran como los suyos.',
           dict(title='Comparativa: MyFitnessPal, Yazio, Foodvisor y Basal — Basal', description='Lo que cada aplicación de nutrición hace mejor, lo que de verdad sigue siendo gratis (escáner, reconocimiento por foto), precios consultados en octubre de 2026 y cómo elegir según tu uso.',
                og_title='Comparativa: MyFitnessPal, Yazio, Foodvisor y Basal', og_description='Lo que cada una hace mejor, lo que de verdad es gratis, los precios y cómo elegir.')),
    'de': ('Ernährungs-Apps im Vergleich', 'Eine App wählen', 'Vergleich: MyFitnessPal, Yazio, Foodvisor und Basal',
           'Diese Seite schreibt der Entwickler von Basal, also jemand, der ein Interesse an der Antwort hat. Ich habe sie trotzdem geschrieben und versucht, sie für jemanden nützlich zu machen, der Basal nicht wählen würde: Jede App bekommt zuerst, was sie besser kann als die anderen, und meine eigenen Grenzen stehen genauso da wie ihre.',
           dict(title='Vergleich: MyFitnessPal, Yazio, Foodvisor, Basal — Basal', description='Was jede Ernährungs-App am besten kann, was wirklich kostenlos bleibt (Barcode-Scanner, Fotoerkennung), Preise vom Oktober 2026 und wie du je nach Nutzung wählst.',
                og_title='Vergleich: MyFitnessPal, Yazio, Foodvisor und Basal', og_description='Was jede am besten kann, was wirklich kostenlos bleibt, die Preise und wie du wählst.')),
}

PAGES = {}
for l in ('en', 'es', 'de'):
    court, sur, h1, chap, tete = META[l]
    t = textes(l)
    PAGES[l] = page(l, C, dict(court=court, surtitre=sur, h1=h1, chapeau=chap, publie='2026-10-06', maj='2026-10-30',
                               note=f'{NOTE[l]}</p>\n    <p>{t["marques"]}', sommaire=list(zip(IDS, t['s'])), corps=corps(l, t)), tete)
