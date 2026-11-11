from commun import U, page

FR = '/appli-calories-sans-compte.html'
DATE = '2026-11-11'
C = 'sans-compte'
IDS = ['why', 'without-account', 'offline', 'data', 'check', 'limits']
VERSION = {'en': 'App version 1.4', 'es': 'Aplicación versión 1.4', 'de': 'App-Version 1.4'}


def corps(l, t):
    li = lambda xs, ind='        ': '\n'.join(f'{ind}<li>{x}</li>' for x in xs)
    rows = '\n'.join(f'            <tr><td>{a}</td><td>{t["oui"] if b else t["non"]}</td></tr>' for a, b in t['tab'])
    s = t['s']
    return f'''      <div class="en-bref">
        <p class="surtitre">{t["bref_t"]}</p>
        <p>{t["bref"]}</p>
      </div>

      <h2 id="why">{s[0]}</h2>
      <p>{t["pourquoi"][0]}</p>
      <p>{t["pourquoi"][1]}</p>

      <h2 id="without-account">{s[1]}</h2>
      <p>{t["tout"]}</p>
      <ul>
{li(t["liste"])}
      </ul>
      <p>{t["compte"]}</p>

      <h2 id="offline">{s[2]}</h2>
      <div class="tableau">
        <table>
          <caption>{t["cap"]}</caption>
          <thead><tr><th scope="col">{t["th"][0]}</th><th scope="col">{t["th"][1]}</th></tr></thead>
          <tbody>
{rows}
          </tbody>
        </table>
        <p class="source">{t["src"]}</p>
      </div>
      <p>{t["pratique"]}</p>

      <h2 id="data">{s[3]}</h2>
      <p>{t["perdre"]}</p>
      <ul>
{li(t["solutions"])}
      </ul>
      <p>{t["export"]}</p>

      <h2 id="check">{s[4]}</h2>
      <p>{t["verif"]}</p>
      <ol>
{li(t["etapes"])}
      </ol>
      <p>{t["conf"]}</p>

      <h2 id="limits">{s[5]}</h2>
      <div class="inconnu">
        <p>{t["lim"][0]}</p>
        <p>{t["lim"][1]}</p>
        <p style="margin:0">{t["lim"][2]}</p>
      </div>
      <p>{t["autres"]}</p>

      <div class="appel-contexte">
        <div><strong>{t["appel_t"]}</strong><p>{t["appel"]}</p></div>
        <a class="bouton vif" href="{U["accueil"][l]}#download">{t["telecharger"]}</a>
      </div>'''


def textes(l):
    u = lambda k: U[k][l]
    if l == 'en':
        return dict(
            s=['Why so many apps ask for an account', 'What Basal does without an account', 'What works offline', 'Not losing your data', 'Checking an app yourself', 'What Basal does not do'],
            bref_t='In short',
            bref='Basal installs and works entirely without an account, without an email and without signing up, for free and with no ads. Tracking meals, weight and sessions works offline. You only need the internet to read a barcode, search Open Food Facts, the Community and the Premium subscription. To lose nothing when you change phone, a backup file is enough.',
            pourquoi=['An account has real uses: getting your data back on another phone, sharing a subscription between devices. But it also serves other purposes: sending marketing emails, linking your usage to your identity, and making it harder to leave for another app.',
                      'To track what you eat, none of that is needed. A calorie counter can calculate everything on the phone: the food table, expenditure, targets and history fit in the device’s memory.'],
            tout='Everything, except two things. Without creating an account, without an email and without signing up, you get:',
            liste=['meal, calorie and macro tracking, with ANSES’s Ciqual table (over 3,300 foods);', 'the barcode scanner;',
                   f'weight, its trend and the expenditure recalculated from your data (<a href="{u("metabolisme-adaptatif")}">adaptive metabolism</a>);',
                   'strength sessions, routines and estimated 1RM;', 'calculated recipes, meal planning and the shopping list;',
                   'steps, read from Apple Health or Health Connect;', 'the Premium subscription, which can also be bought without an account.'],
            compte='The account, which is optional, is only for two things: syncing your data so you can get it back on another phone, and posting in the Community.',
            cap='Basal without an internet connection', th=['Feature', 'Offline'], oui='Yes', non='No',
            tab=[('Adding a meal from the Ciqual table', 1), ('Calories, macros, targets and history', 1), ('Weight, trend and recalculated expenditure', 1), ('Sessions, routines and exercises', 1),
                 ('Recipes, meal planning and shopping list', 1), ('Reading a barcode (Open Food Facts product page)', 0), ('Searching for a branded product in Open Food Facts', 0), ('Community, sync, buying Premium', 0)],
            src='Behaviour of the Basal app, version 1.4. Offline, search is limited to the built-in foods, and a banner says so.',
            pratique='In practice, at the gym with no signal or when travelling, you can log everything. A packaged product can be caught up later, once connected, or added by hand with the values on the label.',
            perdre='That is the trade-off: without an account, your data lives only on your phone. If you lose it or change it, the data does not follow you on its own. Two solutions:',
            solutions=['<strong>A backup file</strong>: in Settings, then My data, “Create a backup” produces a file you keep wherever you like, and “Restore a backup” loads it onto the new phone. Still without an account.',
                       f'<strong>An account</strong>, if you would rather sync happens on its own. It can be deleted at any time, with its data (<a href="{u("suppression")}">account deletion</a>).'],
            export='Exporting as JSON or CSV is different: it is for reading your data in a spreadsheet or another app, and it cannot be imported back.',
            verif='“No account” and “offline” are easy to write on a store listing. Four checks take five minutes, on any app:',
            etapes=['<strong>The first launch.</strong> If a sign-up screen blocks access, or if “continue without an account” leads to a cut-down version, the promise does not hold.',
                    '<strong>Airplane mode.</strong> Turn it on, then add an everyday food (an apple, rice). If the search returns nothing, the food database is not on the phone.',
                    '<strong>The store listing.</strong> The App Store (“App Privacy”) and Google Play (“Data safety”) list the data collected and the data linked to your identity.',
                    '<strong>The privacy policy.</strong> Look for the words “advertising”, “partners” and “sale”: an app with no ads has no reason to share your data with ad networks.'],
            conf=f'For Basal, the <a href="{u("confidentialite")}">privacy policy</a> lists every third-party service and its role.',
            lim=['<strong>No photo recognition of dishes</strong>: the camera reads barcodes, not plates.', '<strong>No watch app</strong>: only steps come through, via Apple Health or Health Connect.',
                 '<strong>No iPad or web version</strong>: Basal is an app for iPhone and Android.'],
            autres=f'The other answers are in the <a href="{u("faq")}">FAQ</a>, and what stays free in <a href="{u("compteur-gratuit")}">a free calorie app, with no subscription</a>.',
            appel_t='Install, open, log your first meal', appel='No email, no sign-up, no ads. Tracking is free, and your data stays on your phone.', telecharger='Download',
        )
    if l == 'es':
        return dict(
            s=['Por qué tantas apps piden una cuenta', 'Lo que Basal hace sin cuenta', 'Lo que funciona sin conexión', 'No perder tus datos', 'Comprobar una app por ti mismo', 'Lo que Basal no hace'],
            bref_t='En resumen',
            bref='Basal se instala y se usa por completo sin cuenta, sin correo electrónico y sin registro, gratis y sin publicidad. El seguimiento de las comidas, del peso y de las sesiones funciona sin conexión. Solo hace falta internet para leer un código de barras, buscar en Open Food Facts, la Comunidad y la suscripción Premium. Para no perder nada al cambiar de teléfono, basta con un archivo de copia de seguridad.',
            pourquoi=['Una cuenta tiene utilidades reales: recuperar tus datos en otro teléfono, compartir una suscripción entre dispositivos. Pero también sirve para otras cosas: enviar correos de marketing, vincular tu uso a tu identidad y hacer más difícil irse a otra aplicación.',
                      'Para seguir tu alimentación, nada de eso es necesario. Un contador de calorías puede calcularlo todo en el teléfono: la tabla de alimentos, el gasto, los objetivos y el historial caben en la memoria del dispositivo.'],
            tout='Todo, salvo dos cosas. Sin crear cuenta, sin correo y sin registro, tienes:',
            liste=['el seguimiento de comidas, calorías y macros, con la tabla Ciqual de la ANSES (más de 3.300 alimentos);', 'el escáner de códigos de barras;',
                   f'el peso, su tendencia y el gasto recalculado a partir de tus datos (<a href="{u("metabolisme-adaptatif")}">el metabolismo adaptativo</a>);',
                   'las sesiones de musculación, las rutinas y el 1RM estimado;', 'las recetas calculadas, la planificación y la lista de la compra;',
                   'los pasos, leídos de Salud o Health Connect;', 'la suscripción Premium, que también se compra sin cuenta.'],
            compte='La cuenta, opcional, solo sirve para dos cosas: sincronizar tus datos para recuperarlos en otro teléfono y publicar en la Comunidad.',
            cap='Basal sin conexión a internet', th=['Función', 'Sin conexión'], oui='Sí', non='No',
            tab=[('Añadir una comida desde la tabla Ciqual', 1), ('Calorías, macros, objetivos e historial', 1), ('Peso, tendencia y gasto recalculado', 1), ('Sesiones, rutinas y ejercicios', 1),
                 ('Recetas, planificación y lista de la compra', 1), ('Leer un código de barras (ficha de Open Food Facts)', 0), ('Buscar un producto de marca en Open Food Facts', 0), ('Comunidad, sincronización, compra de Premium', 0)],
            src='Comportamiento de la aplicación Basal, versión 1.4. Sin conexión, la búsqueda se limita a los alimentos integrados, y un aviso lo indica.',
            pratique='En la práctica, en el gimnasio sin cobertura o de viaje, puedes anotarlo todo. Un producto envasado se recupera después, ya con conexión, o se añade a mano con los valores de la etiqueta.',
            perdre='Es la contrapartida: sin cuenta, tus datos solo viven en tu teléfono. Si lo pierdes o lo cambias, no te siguen solos. Dos soluciones:',
            solutions=['<strong>Un archivo de copia de seguridad</strong>: en Ajustes, luego Mis datos, «Crear una copia de seguridad» genera un archivo que guardas donde quieras, y «Restaurar una copia de seguridad» lo carga en el teléfono nuevo. Siempre sin cuenta.',
                       f'<strong>Una cuenta</strong>, si prefieres que la sincronización se haga sola. Se puede eliminar en cualquier momento, con sus datos (<a href="{u("suppression")}">eliminación de cuenta</a>).'],
            export='La exportación en JSON o CSV es distinta: sirve para leer tus datos en una hoja de cálculo u otra aplicación, y no se vuelve a importar.',
            verif='«Sin cuenta» y «sin conexión» son fáciles de escribir en una ficha. Cuatro comprobaciones llevan cinco minutos, en cualquier aplicación:',
            etapes=['<strong>El primer arranque.</strong> Si una pantalla de registro bloquea el acceso, o si «continuar sin cuenta» lleva a una versión recortada, la promesa no se cumple.',
                    '<strong>El modo avión.</strong> Actívalo y añade una comida corriente (una manzana, arroz). Si la búsqueda no devuelve nada, la base de alimentos no está en el teléfono.',
                    '<strong>La ficha de la tienda.</strong> El App Store («Privacidad de la app») y Google Play («Seguridad de los datos») enumeran los datos recogidos y los vinculados a tu identidad.',
                    '<strong>La política de privacidad.</strong> Busca las palabras «publicidad», «socios» y «venta»: una aplicación sin publicidad no tiene motivo para compartir tus datos con redes publicitarias.'],
            conf=f'En el caso de Basal, la <a href="{u("confidentialite")}">política de privacidad</a> enumera cada servicio externo y su función.',
            lim=['<strong>No reconoce platos en foto</strong>: la cámara lee códigos de barras, no platos.', '<strong>No hay app para reloj</strong>: solo pasan los pasos, a través de Salud o Health Connect.',
                 '<strong>No hay versión para iPad ni web</strong>: Basal es una aplicación para iPhone y Android.'],
            autres=f'Las demás respuestas están en las <a href="{u("faq")}">preguntas frecuentes</a>, y lo que sigue siendo gratis en <a href="{u("compteur-gratuit")}">una aplicación de calorías gratis y sin suscripción</a>.',
            appel_t='Instala, abre y anota tu primera comida', appel='Sin correo, sin registro, sin publicidad. El seguimiento es gratis y tus datos se quedan en tu teléfono.', telecharger='Descargar',
        )
    return dict(
        s=['Warum so viele Apps ein Konto verlangen', 'Was Basal ohne Konto kann', 'Was offline funktioniert', 'Keine Daten verlieren', 'Eine App selbst prüfen', 'Was Basal nicht kann'],
        bref_t='Kurz gesagt',
        bref='Basal lässt sich vollständig ohne Konto, ohne E-Mail und ohne Anmeldung installieren und nutzen, kostenlos und ohne Werbung. Das Erfassen von Mahlzeiten, Gewicht und Einheiten funktioniert offline. Internet brauchst du nur, um einen Barcode zu lesen, in Open Food Facts zu suchen, für die Community und das Premium-Abo. Damit beim Handywechsel nichts verloren geht, reicht eine Sicherungsdatei.',
        pourquoi=['Ein Konto hat echten Nutzen: deine Daten auf einem anderen Handy wiederfinden, ein Abo zwischen Geräten teilen. Es dient aber auch anderen Zwecken: Marketing-E-Mails verschicken, deine Nutzung mit deiner Identität verknüpfen und den Wechsel zu einer anderen App erschweren.',
                  'Um deine Ernährung zu erfassen, ist nichts davon nötig. Ein Kalorienzähler kann alles auf dem Handy berechnen: Die Lebensmitteltabelle, der Verbrauch, die Ziele und der Verlauf passen in den Speicher des Geräts.'],
        tout='Alles, bis auf zwei Dinge. Ohne Konto, ohne E-Mail und ohne Anmeldung hast du:',
        liste=['das Erfassen von Mahlzeiten, Kalorien und Makros, mit der Ciqual-Tabelle der ANSES (über 3.300 Lebensmittel);', 'den Barcode-Scanner;',
               f'das Gewicht, seinen Trend und den aus deinen Daten neu berechneten Verbrauch (<a href="{u("metabolisme-adaptatif")}">die metabolische Anpassung</a>);',
               'Krafttrainingseinheiten, Routinen und das geschätzte 1RM;', 'berechnete Rezepte, die Planung und die Einkaufsliste;',
               'die Schritte, aus Apple Health oder Health Connect gelesen;', 'das Premium-Abo, das sich ebenfalls ohne Konto kaufen lässt.'],
        compte='Das freiwillige Konto dient nur zwei Dingen: deine Daten zu synchronisieren, um sie auf einem anderen Handy wiederzufinden, und in der Community zu veröffentlichen.',
        cap='Basal ohne Internetverbindung', th=['Funktion', 'Offline'], oui='Ja', non='Nein',
        tab=[('Eine Mahlzeit aus der Ciqual-Tabelle hinzufügen', 1), ('Kalorien, Makros, Ziele und Verlauf', 1), ('Gewicht, Trend und neu berechneter Verbrauch', 1), ('Einheiten, Routinen und Übungen', 1),
             ('Rezepte, Planung und Einkaufsliste', 1), ('Einen Barcode lesen (Open-Food-Facts-Eintrag)', 0), ('Ein Markenprodukt in Open Food Facts suchen', 0), ('Community, Synchronisierung, Premium-Kauf', 0)],
        src='Verhalten der App Basal, Version 1.4. Offline beschränkt sich die Suche auf die integrierten Lebensmittel, und ein Hinweis zeigt das an.',
        pratique='In der Praxis kannst du im Fitnessstudio ohne Netz oder auf Reisen alles eintragen. Ein verpacktes Produkt lässt sich später nachholen, sobald du verbunden bist, oder von Hand mit den Werten auf dem Etikett hinzufügen.',
        perdre='Das ist die Kehrseite: Ohne Konto leben deine Daten nur auf deinem Handy. Wenn du es verlierst oder wechselst, folgen sie dir nicht von selbst. Zwei Lösungen:',
        solutions=['<strong>Eine Sicherungsdatei</strong>: In Einstellungen, dann Meine Daten, erzeugt „Sicherung erstellen“ eine Datei, die du aufbewahrst, wo du willst, und „Sicherung wiederherstellen“ lädt sie auf das neue Handy. Weiterhin ohne Konto.',
                   f'<strong>Ein Konto</strong>, wenn dir eine automatische Synchronisierung lieber ist. Es kann jederzeit gelöscht werden, mitsamt seinen Daten (<a href="{u("suppression")}">Konto löschen</a>).'],
        export='Der Export als JSON oder CSV ist etwas anderes: Er dient dazu, deine Daten in einer Tabellenkalkulation oder einer anderen App zu lesen, und lässt sich nicht wieder importieren.',
        verif='„Ohne Konto“ und „offline“ lassen sich leicht in einen Store-Eintrag schreiben. Vier Prüfungen dauern fünf Minuten, bei jeder App:',
        etapes=['<strong>Der erste Start.</strong> Wenn ein Anmeldebildschirm den Zugang sperrt oder „ohne Konto fortfahren“ zu einer abgespeckten Version führt, hält das Versprechen nicht.',
                '<strong>Der Flugmodus.</strong> Schalte ihn ein und füge ein alltägliches Lebensmittel hinzu (einen Apfel, Reis). Liefert die Suche nichts, liegt die Lebensmitteldatenbank nicht auf dem Handy.',
                '<strong>Der Store-Eintrag.</strong> Der App Store („App-Datenschutz“) und Google Play („Datensicherheit“) listen die erhobenen Daten und die mit deiner Identität verknüpften Daten auf.',
                '<strong>Die Datenschutzerklärung.</strong> Suche nach den Wörtern „Werbung“, „Partner“ und „Verkauf“: Eine App ohne Werbung hat keinen Grund, deine Daten mit Werbenetzwerken zu teilen.'],
        conf=f'Für Basal listet die <a href="{u("confidentialite")}">Datenschutzerklärung</a> jeden Drittanbieterdienst und seine Rolle auf.',
        lim=['<strong>Keine Erkennung von Gerichten per Foto</strong>: Die Kamera liest Barcodes, keine Teller.', '<strong>Keine Uhr-App</strong>: Nur die Schritte kommen an, über Apple Health oder Health Connect.',
             '<strong>Keine iPad- oder Web-Version</strong>: Basal ist eine App für iPhone und Android.'],
        autres=f'Die übrigen Antworten stehen in den <a href="{u("faq")}">häufigen Fragen</a>, und was kostenlos bleibt, in <a href="{u("compteur-gratuit")}">eine kostenlose Kalorien-App, ohne Abo</a>.',
        appel_t='Installieren, öffnen, erste Mahlzeit eintragen', appel='Keine E-Mail, keine Anmeldung, keine Werbung. Das Tracking ist kostenlos, und deine Daten bleiben auf deinem Handy.', telecharger='Herunterladen',
    )


META = {
    'en': ('Calorie app without an account', 'Choosing an app', 'A calorie app without an account, that works offline',
           'Counting calories without giving your email, without signing up and without a permanent connection is possible. Here is what that changes, what really works offline, how not to lose your data, and how to check that an app keeps its promises.',
           dict(title='Calorie app with no account, no sign-up, offline — Basal', description='Counting calories with no account, no email and no connection: what Basal does without signing up, what works offline, how to back up your data, and how to check an app.',
                og_title='A calorie app without an account, that works offline', og_description='No email, no sign-up: what works offline, how not to lose your data, and how to check an app.')),
    'es': ('App de calorías sin cuenta', 'Elegir una aplicación', 'Una app de calorías sin cuenta, que funciona sin conexión',
           'Contar calorías sin dar tu correo, sin registrarte y sin conexión permanente es posible. Esto es lo que cambia, lo que de verdad funciona sin conexión, cómo no perder tus datos y cómo comprobar que una aplicación cumple lo que promete.',
           dict(title='App de calorías sin cuenta, sin registro y sin conexión — Basal', description='Contar calorías sin cuenta, sin correo y sin conexión: lo que hace Basal sin registro, lo que funciona sin conexión, cómo guardar tus datos y cómo comprobar una app.',
                og_title='Una app de calorías sin cuenta, que funciona sin conexión', og_description='Sin correo ni registro: lo que funciona sin conexión, cómo no perder tus datos y cómo comprobar una app.')),
    'de': ('Kalorien-App ohne Konto', 'Eine App wählen', 'Eine Kalorien-App ohne Konto, die offline funktioniert',
           'Kalorien zählen, ohne deine E-Mail anzugeben, ohne Anmeldung und ohne ständige Verbindung, ist möglich. Hier steht, was das ändert, was offline wirklich funktioniert, wie du keine Daten verlierst und wie du prüfst, ob eine App hält, was sie verspricht.',
           dict(title='Kalorien-App ohne Konto, ohne Anmeldung, offline — Basal', description='Kalorien zählen ohne Konto, ohne E-Mail und ohne Verbindung: was Basal ohne Anmeldung kann, was offline funktioniert, wie du deine Daten sicherst und wie du eine App prüfst.',
                og_title='Eine Kalorien-App ohne Konto, die offline funktioniert', og_description='Ohne E-Mail und ohne Anmeldung: was offline funktioniert, wie du keine Daten verlierst und wie du eine App prüfst.')),
}

PAGES = {}
for l in ('en', 'es', 'de'):
    court, sur, h1, chap, tete = META[l]
    t = textes(l)
    p = page(l, C, dict(court=court, surtitre=sur, h1=h1, chapeau=chap, publie='2026-10-31', sommaire=list(zip(IDS, t['s'])), corps=corps(l, t)), tete)
    p['main'] = p['main'].replace('</time></span>\n    </div>', f'</time></span>\n      <span aria-hidden="true">·</span>\n      <span>{VERSION[l]}</span>\n    </div>', 1)
    PAGES[l] = p
