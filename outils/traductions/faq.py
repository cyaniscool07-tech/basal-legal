import re
from commun import U, L

FR = '/questions-frequentes.html'
DATE = '2026-11-11'
C = 'faq'


def questions(l):
    u = lambda k: U[k][l]
    if l == 'en':
        return [
            ('gratuit', 'Is Basal really free?', '<p>Yes, for the most part, with no time limit and no ads: meal and macro tracking, barcode scanner, weight and trend, adaptive expenditure, strength sessions, recipes, the Community and step sync.</p><p>An optional Premium subscription adds eight features: the weekly review, volume per muscle group, protein on training and rest days, the advanced metabolism layer, advanced strategies, and three meal assistants (organise, prepare and optimise the week). The review and each assistant can be tried once for free.</p>'),
            ('appareils', 'Which devices does Basal work on?', '<p>On iPhone (App Store) and Android (Google Play). There is no version designed for iPad and no web version. The app is in English, French, Spanish and German, following the phone’s language.</p>'),
            ('compte', 'Do I need to create an account?', f'<p>No. The whole app works without an account, without an email and without signing up: your data stays on your phone.</p><p>An optional account is for getting your data back on another phone (it is then synced to a server hosted in Ireland) and for posting in the Community. The details are in <a href="{u("sans-compte")}">a calorie app without an account</a>.</p>'),
            ('programme', 'Can Basal create a strength programme for me?', f'<p>Not automatically: Basal does not generate programmes. You can build your routines yourself, exercise by exercise, or pick up routines and programmes shared in the Community, sorted by level.</p><p>To get started, the guide <a href="{u("series")}">how many sets per muscle per week</a> gives the orders of magnitude.</p>'),
            ('montre', 'Does Basal work with a smartwatch?', '<p>There is no Apple Watch app, and no direct connection to Garmin, Fitbit or Samsung. Basal does, however, read your <strong>step count</strong> from Apple Health (iPhone) or Health Connect (Android), for free: if your watch sends its steps there, Basal picks them up. It reads and writes nothing else.</p>'),
            ('photo', 'Can I add a meal by taking a photo of it?', f'<p>No, Basal does not recognise dishes from photos: these estimates often get the quantities wrong, and quantities make up most of the calories. The camera is for reading the <strong>barcode</strong> of packaged products, live or from a sharp photo when live reading fails.</p><p>For a home-made dish, food search and the <a href="{u("recettes")}">calculated recipes</a> give more reliable values.</p>'),
            ('aliments', 'Is the food database reliable?', '<p>Basal includes <a href="https://ciqual.anses.fr/">ANSES’s Ciqual 2025 table</a>, over 3,300 foods analysed and published by the French health agency. Scanned products come from Open Food Facts, a collaborative database: their values are those on the labels, entered by contributors, so sometimes incomplete.</p><p>On top of that come the menus of six fast-food chains and an estimate per type of restaurant dish.</p>'),
            ('objectif', 'How is my calorie target calculated?', f'<p>Basal starts from the Mifflin-St Jeor formula (age, sex, height, weight), multiplies it by your activity level, then applies your goal. After that, it compares what you eat with how your weight actually changes to correct this estimate, in small steps.</p><p>All the formulas and their limits are on the <a href="{u("methode")}">Method</a> page, and you can try them with the <a href="{u("tdee")}">expenditure calculator</a>.</p>'),
            ('1rm', 'What is the estimated 1RM?', f'<p>It is the maximum load you could lift just once, estimated from a set of several reps, without having to attempt it. Basal uses the Epley formula: <code>load × (1 + reps ÷ 30)</code>. It is used to track your progress from one session to the next.</p><p>The <a href="{u("1rm")}">1RM calculator</a> does the same calculation and gives the loads by percentage.</p>'),
            ('exercices', 'Can I add my own exercises?', '<p>Yes. The library has 873 exercises, and you can create your own from the exercise selection screen: they are then available in your routines like the others.</p>'),
            ('sauvegarde', 'Is my data backed up?', f'<p>It is stored on your phone. So as not to lose it when you change device, you have two options:</p><ul><li>create an account, which syncs your data automatically;</li><li>create a backup file (Settings, then My data), to restore on the new phone.</li></ul><p>Exporting as JSON or CSV is for reading your data elsewhere: it cannot be imported back. The details are in the <a href="{u("confidentialite")}">privacy policy</a>.</p>'),
            ('hors-ligne', 'Does the app work without the internet?', '<p>Yes, for the most part: tracking, weight, sessions, recipes and searching the Ciqual foods work offline. You need a connection to read a barcode, search Open Food Facts, use the Community, sync an account or subscribe to Premium.</p>'),
            ('donnees', 'Does Basal sell my data?', f'<p>No. Basal does not sell, rent or share any data for advertising purposes, and the app contains no ads and no ad trackers. The only third-party services are there to make it work (sync, subscription, crash detection) and are listed in the <a href="{u("confidentialite")}">privacy policy</a>.</p>'),
        ]
    if l == 'es':
        return [
            ('gratuit', '¿Basal es realmente gratis?', '<p>Sí en lo esencial, sin límite de tiempo y sin publicidad: seguimiento de comidas y macros, escáner de códigos de barras, peso y tendencia, gasto adaptativo, sesiones de musculación, recetas, Comunidad y sincronización de pasos.</p><p>Una suscripción Premium, opcional, añade ocho funciones: el balance semanal, el volumen por grupo muscular, las proteínas de los días de entrenamiento y de descanso, la capa avanzada del metabolismo, las estrategias avanzadas y tres asistentes de comidas (organizar, preparar y optimizar la semana). El balance y cada asistente se pueden probar una vez gratis.</p>'),
            ('appareils', '¿En qué dispositivos funciona Basal?', '<p>En iPhone (App Store) y en Android (Google Play). No hay versión diseñada para iPad ni versión web. La aplicación está en español, francés, inglés y alemán, según el idioma del teléfono.</p>'),
            ('compte', '¿Hay que crear una cuenta?', f'<p>No. Toda la aplicación funciona sin cuenta, sin correo ni registro: tus datos se quedan en tu teléfono.</p><p>Una cuenta, opcional, sirve para recuperar tus datos en otro teléfono (se sincronizan entonces en un servidor alojado en Irlanda) y para publicar en la Comunidad. El detalle está en <a href="{u("sans-compte")}">una app de calorías sin cuenta</a>.</p>'),
            ('programme', '¿Puede Basal crearme un programa de musculación?', f'<p>No automáticamente: Basal no genera programas. Puedes construir tus rutinas tú mismo, ejercicio a ejercicio, o retomar rutinas y programas compartidos en la Comunidad, clasificados por nivel.</p><p>Para empezar bien, la guía <a href="{u("series")}">cuántas series por músculo y por semana</a> da los órdenes de magnitud.</p>'),
            ('montre', '¿Basal funciona con un reloj inteligente?', '<p>No hay aplicación para Apple Watch ni conexión directa con Garmin, Fitbit o Samsung. En cambio, Basal lee tu <strong>número de pasos</strong> en Salud (iPhone) o Health Connect (Android), gratis: si tu reloj envía allí sus pasos, Basal los recoge. No lee ni escribe nada más.</p>'),
            ('photo', '¿Se puede añadir una comida haciéndole una foto?', f'<p>No, Basal no reconoce platos en foto: esas estimaciones suelen equivocarse en las cantidades, que son la mayor parte de las calorías. La cámara sirve para leer el <strong>código de barras</strong> de los productos envasados, en directo o desde una foto nítida cuando la lectura directa falla.</p><p>Para un plato casero, la búsqueda de alimentos y las <a href="{u("recettes")}">recetas calculadas</a> dan valores más fiables.</p>'),
            ('aliments', '¿Es fiable la base de alimentos?', '<p>Basal incluye la <a href="https://ciqual.anses.fr/">tabla Ciqual 2025 de la ANSES</a>, más de 3.300 alimentos analizados y publicados por la agencia sanitaria francesa. Los productos escaneados vienen de Open Food Facts, una base colaborativa: sus valores son los de las etiquetas, introducidos por colaboradores, y por eso a veces están incompletos.</p><p>Se suman los menús de seis cadenas de comida rápida y una estimación por tipo de plato de restaurante.</p>'),
            ('objectif', '¿Cómo se calcula mi objetivo calórico?', f'<p>Basal parte de la fórmula de Mifflin-St Jeor (edad, sexo, altura, peso), la multiplica por tu nivel de actividad y aplica tu objetivo. Después compara lo que comes con la evolución real de tu peso para corregir esa estimación, poco a poco.</p><p>Todas las fórmulas y sus límites están en la página <a href="{u("methode")}">Método</a>, y puedes probarlas con la <a href="{u("tdee")}">calculadora de gasto</a>.</p>'),
            ('1rm', '¿Qué es el 1RM estimado?', f'<p>Es la carga máxima que podrías levantar una sola vez, estimada a partir de una serie de varias repeticiones, sin tener que intentarlo. Basal usa la fórmula de Epley: <code>carga × (1 + repeticiones ÷ 30)</code>. Sirve para seguir tu progresión de una sesión a otra.</p><p>La <a href="{u("1rm")}">calculadora de 1RM</a> hace el mismo cálculo y da las cargas por porcentaje.</p>'),
            ('exercices', '¿Puedo añadir mis propios ejercicios?', '<p>Sí. La biblioteca tiene 873 ejercicios, y puedes crear los tuyos desde la pantalla de elección de ejercicio: después están disponibles en tus rutinas como los demás.</p>'),
            ('sauvegarde', '¿Se guardan mis datos?', f'<p>Se guardan en tu teléfono. Para no perderlos al cambiar de dispositivo, tienes dos opciones:</p><ul><li>crear una cuenta, que sincroniza tus datos automáticamente;</li><li>crear un archivo de copia de seguridad (Ajustes, luego Mis datos), para restaurarlo en el teléfono nuevo.</li></ul><p>La exportación en JSON o CSV sirve para leer tus datos en otro sitio: no se vuelve a importar. El detalle está en la <a href="{u("confidentialite")}">política de privacidad</a>.</p>'),
            ('hors-ligne', '¿La aplicación funciona sin internet?', '<p>Sí en lo esencial: el seguimiento, el peso, las sesiones, las recetas y la búsqueda entre los alimentos Ciqual funcionan sin conexión. Hace falta conexión para leer un código de barras, buscar en Open Food Facts, usar la Comunidad, sincronizar una cuenta o suscribirse a Premium.</p>'),
            ('donnees', '¿Basal vende mis datos?', f'<p>No. Basal no vende, ni alquila, ni comparte ningún dato con fines publicitarios, y la aplicación no contiene publicidad ni rastreadores publicitarios. Los únicos servicios externos sirven para el funcionamiento (sincronización, suscripción, detección de fallos) y se enumeran en la <a href="{u("confidentialite")}">política de privacidad</a>.</p>'),
        ]
    return [
        ('gratuit', 'Ist Basal wirklich kostenlos?', '<p>Im Wesentlichen ja, ohne Zeitlimit und ohne Werbung: Erfassen von Mahlzeiten und Makros, Barcode-Scanner, Gewicht und Trend, adaptiver Verbrauch, Krafttrainingseinheiten, Rezepte, Community und Schritt-Synchronisierung.</p><p>Ein freiwilliges Premium-Abo fügt acht Funktionen hinzu: den Wochenrückblick, das Volumen pro Muskelgruppe, das Eiweiß an Trainings- und Ruhetagen, die erweiterte Stoffwechselebene, die fortgeschrittenen Strategien und drei Mahlzeiten-Assistenten (die Woche organisieren, vorbereiten und optimieren). Der Rückblick und jeder Assistent lassen sich einmal kostenlos ausprobieren.</p>'),
        ('appareils', 'Auf welchen Geräten läuft Basal?', '<p>Auf dem iPhone (App Store) und auf Android (Google Play). Es gibt keine fürs iPad gestaltete Version und keine Web-Version. Die App ist auf Deutsch, Französisch, Englisch und Spanisch, je nach Sprache des Handys.</p>'),
        ('compte', 'Muss ich ein Konto anlegen?', f'<p>Nein. Die ganze App funktioniert ohne Konto, ohne E-Mail und ohne Anmeldung: Deine Daten bleiben auf deinem Handy.</p><p>Ein freiwilliges Konto dient dazu, deine Daten auf einem anderen Handy wiederzufinden (sie werden dann mit einem Server in Irland synchronisiert), und um in der Community zu veröffentlichen. Die Einzelheiten stehen in <a href="{u("sans-compte")}">Kalorien-App ohne Konto</a>.</p>'),
        ('programme', 'Kann Basal mir einen Trainingsplan erstellen?', f'<p>Nicht automatisch: Basal erzeugt keine Pläne. Du kannst deine Routinen selbst zusammenstellen, Übung für Übung, oder in der Community geteilte Routinen und Programme übernehmen, nach Niveau sortiert.</p><p>Für den Einstieg gibt der Ratgeber <a href="{u("series")}">wie viele Sätze pro Muskel und Woche</a> die Größenordnungen an.</p>'),
        ('montre', 'Funktioniert Basal mit einer Smartwatch?', '<p>Es gibt keine Apple-Watch-App und keine direkte Verbindung zu Garmin, Fitbit oder Samsung. Basal liest dafür deine <strong>Schrittzahl</strong> aus Apple Health (iPhone) oder Health Connect (Android), kostenlos: Wenn deine Uhr ihre Schritte dorthin schickt, übernimmt Basal sie. Es liest und schreibt nichts anderes.</p>'),
        ('photo', 'Kann man eine Mahlzeit per Foto hinzufügen?', f'<p>Nein, Basal erkennt keine Gerichte auf Fotos: Solche Schätzungen liegen bei den Mengen oft daneben, und die Mengen machen den Großteil der Kalorien aus. Die Kamera dient dazu, den <strong>Barcode</strong> verpackter Produkte zu lesen, live oder aus einem scharfen Foto, wenn das Live-Lesen scheitert.</p><p>Für ein selbst gekochtes Gericht liefern die Lebensmittelsuche und die <a href="{u("recettes")}">berechneten Rezepte</a> verlässlichere Werte.</p>'),
        ('aliments', 'Ist die Lebensmitteldatenbank verlässlich?', '<p>Basal enthält die <a href="https://ciqual.anses.fr/">Ciqual-2025-Tabelle der ANSES</a>, über 3.300 Lebensmittel, analysiert und veröffentlicht von der französischen Gesundheitsbehörde. Gescannte Produkte stammen aus Open Food Facts, einer gemeinschaftlichen Datenbank: Ihre Werte sind die der Etiketten, von Mitwirkenden eingegeben, und daher manchmal unvollständig.</p><p>Hinzu kommen die Menüs von sechs Fast-Food-Ketten und eine Schätzung pro Art von Restaurantgericht.</p>'),
        ('objectif', 'Wie wird mein Kalorienziel berechnet?', f'<p>Basal geht von der Mifflin-St-Jeor-Formel aus (Alter, Geschlecht, Größe, Gewicht), multipliziert sie mit deinem Aktivitätsniveau und wendet dann dein Ziel an. Danach vergleicht es, was du isst, mit der tatsächlichen Entwicklung deines Gewichts, um diese Schätzung in kleinen Schritten zu korrigieren.</p><p>Alle Formeln und ihre Grenzen stehen auf der Seite <a href="{u("methode")}">Methode</a>, und du kannst sie mit dem <a href="{u("tdee")}">Verbrauchsrechner</a> ausprobieren.</p>'),
        ('1rm', 'Was ist das geschätzte 1RM?', f'<p>Es ist das maximale Gewicht, das du ein einziges Mal heben könntest, geschätzt aus einem Satz mit mehreren Wiederholungen, ohne es versuchen zu müssen. Basal verwendet die Epley-Formel: <code>Gewicht × (1 + Wiederholungen ÷ 30)</code>. Sie dient dazu, deinen Fortschritt von Einheit zu Einheit zu verfolgen.</p><p>Der <a href="{u("1rm")}">1RM-Rechner</a> macht dieselbe Rechnung und gibt die Gewichte nach Prozentsatz an.</p>'),
        ('exercices', 'Kann ich eigene Übungen hinzufügen?', '<p>Ja. Die Bibliothek umfasst 873 Übungen, und du kannst eigene im Bildschirm zur Übungsauswahl anlegen: Sie stehen dann in deinen Routinen wie die anderen zur Verfügung.</p>'),
        ('sauvegarde', 'Werden meine Daten gesichert?', f'<p>Sie werden auf deinem Handy gespeichert. Damit du sie beim Gerätewechsel nicht verlierst, hast du zwei Möglichkeiten:</p><ul><li>ein Konto anlegen, das deine Daten automatisch synchronisiert;</li><li>eine Sicherungsdatei erstellen (Einstellungen, dann Meine Daten) und sie auf dem neuen Handy wiederherstellen.</li></ul><p>Der Export als JSON oder CSV dient dazu, deine Daten anderswo zu lesen: Er lässt sich nicht wieder importieren. Die Einzelheiten stehen in der <a href="{u("confidentialite")}">Datenschutzerklärung</a>.</p>'),
        ('hors-ligne', 'Funktioniert die App ohne Internet?', '<p>Im Wesentlichen ja: Tracking, Gewicht, Einheiten, Rezepte und die Suche in den Ciqual-Lebensmitteln funktionieren offline. Eine Verbindung brauchst du, um einen Barcode zu lesen, in Open Food Facts zu suchen, die Community zu nutzen, ein Konto zu synchronisieren oder Premium abzuschließen.</p>'),
        ('donnees', 'Verkauft Basal meine Daten?', f'<p>Nein. Basal verkauft, vermietet und teilt keine Daten zu Werbezwecken, und die App enthält weder Werbung noch Werbe-Tracker. Die einzigen Drittanbieterdienste dienen dem Betrieb (Synchronisierung, Abo, Absturzerkennung) und sind in der <a href="{u("confidentialite")}">Datenschutzerklärung</a> aufgeführt.</p>'),
    ]


T = {
    'en': dict(h1='Frequently asked questions', court='FAQ', surtitre='Help', chapeau='What Basal does, what it does not do, and what stays free. The answers describe version 1.4 of the app. Another question: <a href="mailto:contact@basal-app.fr">contact@basal-app.fr</a>.',
               appel_t='Try it without signing up', appel='Tracking is free, has no ads and needs no account.', telecharger='Download',
               tete=dict(title='Frequently asked questions — Basal', description='Is Basal free, does it need an account, does it work offline or with a watch, where does the food data come from: the answers, for version 1.4 of the app.',
                         og_title='Frequently asked questions — Basal', og_description='Free, account, offline, watch, food database: the answers about Basal.')),
    'es': dict(h1='Preguntas frecuentes', court='Preguntas frecuentes', surtitre='Ayuda', chapeau='Lo que hace Basal, lo que no hace y lo que sigue siendo gratis. Las respuestas describen la versión 1.4 de la aplicación. ¿Otra pregunta?: <a href="mailto:contact@basal-app.fr">contact@basal-app.fr</a>.',
               appel_t='Pruébala sin registrarte', appel='El seguimiento es gratis, sin publicidad y no pide ninguna cuenta.', telecharger='Descargar',
               tete=dict(title='Preguntas frecuentes — Basal', description='¿Basal es gratis?, ¿pide cuenta?, ¿funciona sin conexión o con un reloj?, ¿de dónde vienen los datos de los alimentos?: las respuestas, para la versión 1.4 de la app.',
                         og_title='Preguntas frecuentes — Basal', og_description='Gratis, cuenta, sin conexión, reloj, base de alimentos: las respuestas sobre Basal.')),
    'de': dict(h1='Häufige Fragen', court='Häufige Fragen', surtitre='Hilfe', chapeau='Was Basal kann, was es nicht kann und was kostenlos bleibt. Die Antworten beschreiben Version 1.4 der App. Eine andere Frage: <a href="mailto:contact@basal-app.fr">contact@basal-app.fr</a>.',
               appel_t='Ohne Anmeldung ausprobieren', appel='Das Tracking ist kostenlos, ohne Werbung und braucht kein Konto.', telecharger='Herunterladen',
               tete=dict(title='Häufige Fragen — Basal', description='Ist Basal kostenlos, braucht es ein Konto, funktioniert es offline oder mit einer Uhr, woher kommen die Lebensmitteldaten: die Antworten, für Version 1.4 der App.',
                         og_title='Häufige Fragen — Basal', og_description='Kostenlos, Konto, offline, Uhr, Lebensmitteldatenbank: die Antworten zu Basal.')),
}


def texte(h):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', h.replace('<li>', ' '))).strip()


PAGES = {}
for l, t in T.items():
    qs = questions(l)
    details = '\n'.join(f'''    <details class="faq-q" id="{i}">
      <summary>{q}</summary>
      <div class="faq-r">{r}</div>
    </details>''' for i, q, r in qs)
    url = U['faq'][l]
    main = f'''<main id="contenu" class="wrap">
  <nav class="fil" aria-label="{L[l]["fil"]}"><a href="{U["accueil"][l]}">{L[l]["accueil"]}</a><span aria-hidden="true">›</span>{t["court"]}</nav>
  <header class="article-tete">
    <p class="surtitre">{t["surtitre"]}</p>
    <h1>{t["h1"]}</h1>
    <p class="chapeau">{t["chapeau"]}</p>
  </header>

  <div class="faq">
{details}
  </div>
  <div class="appel-contexte">
    <div><strong>{t["appel_t"]}</strong><p>{t["appel"]}</p></div>
    <a class="bouton vif" href="{U["accueil"][l]}#download">{t["telecharger"]}</a>
  </div>
</main>'''
    ld = [{'@context': 'https://schema.org', '@type': 'FAQPage', 'inLanguage': l, 'url': f'https://basal-app.fr{url}',
           'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': texte(r)}} for _, q, r in qs]},
          {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
              {'@type': 'ListItem', 'position': 1, 'name': L[l]['accueil'], 'item': f'https://basal-app.fr{U["accueil"][l]}'},
              {'@type': 'ListItem', 'position': 2, 'name': t['court'], 'item': f'https://basal-app.fr{url}'}]}]
    PAGES[l] = {'slug': url, 'tete': dict(**t['tete'], locale=L[l]['locale']), 'main': main, 'ld': ld}
