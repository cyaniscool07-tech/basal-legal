from commun import U, L

FR = '/a-propos.html'
DATE = '2026-11-11'
C = 'apropos'


def textes(l):
    u = lambda k: U[k][l]
    if l == 'en':
        return dict(
            court='About', h1='Who makes Basal', title='About Basal: who makes it and what it lives on',
            description='Basal is designed and developed by Théo Serrano, an independent developer in France. Its principles, its business model (optional Premium, no ads), its data sources and how to get in touch.',
            og_title='About Basal', og_description='Who makes Basal, its principles, its business model and its data sources.',
            chapeau='Basal is a nutrition, weight and strength-training tracking app. It is designed, developed and maintained by Théo Serrano, an independent developer in France.',
            s=['The publisher', 'The principles', 'What Basal lives on', 'Key facts', 'Sources and licences', 'Contact'],
            editeur=f'Théo Serrano publishes Basal as a sole trader (entrepreneur individuel), under the trade name Basal. He writes the app, this site and the articles on it, and answers messages himself. Full contact details are in the <a href="{u("mentions")}">legal notice</a>.',
            principes=[f'<strong>Start from a published formula, then correct it with your data.</strong> The starting expenditure comes from the Mifflin-St Jeor equation; the app then checks it against your meals and how your weight changes. All the calculations are detailed on the <a href="{u("methode")}">Method</a> page.',
                       '<strong>Say when we do not know.</strong> As long as the data is too thin, the app shows “not enough data” rather than a number that would look certain.',
                       '<strong>Keep the essentials free.</strong> Tracking meals, weight and sessions, and the recipes, require neither a subscription nor an account.',
                       '<strong>Do not use health as a selling point.</strong> Basal observes, calculates and explains; it is not a medical device, and the app says so.'],
            vit=f'An optional Premium subscription, sold through Google Play and the App Store, which adds analyses and assistants (see <a href="{u("compteur-gratuit")}">what is free and what is Premium</a>). Basal shows no ads and sells no data.',
            reperes=[('Platforms', 'iPhone and Android, in English, French, Spanish and German'), ('Foods', '3,304 foods from ANSES’s Ciqual table, plus Open Food Facts products by search and barcode'),
                     ('Strength training', '873 exercises'), ('Recipes', '50 recipes with values calculated from the Ciqual table'),
                     ('Account', 'Optional; if created, the data is hosted in Ireland (European Union)'), ('Site', 'Hosted by GitHub Pages, no cookies; audience measured by GoatCounter')],
            sources=['Nutritional values of generic foods: <a href="https://ciqual.anses.fr/">ANSES’s Ciqual 2025 table</a>, Etalab 2.0 open licence.',
                     'Branded products: <a href="https://world.openfoodfacts.org/">Open Food Facts</a>, a collaborative database under the Open Database License.',
                     'Recipe illustrations: AI-generated, for illustration only.', 'Site fonts: Inter and Instrument Serif, under the SIL Open Font License.'],
            contact=f'A question, a mistake in a calculation, a suggestion: <a href="mailto:contact@basal-app.fr">contact@basal-app.fr</a>. For your data, see the <a href="{u("confidentialite")}">privacy policy</a> and the <a href="{u("suppression")}">account deletion</a> page.',
            appel_t='Try Basal.', appel='Basic tracking is free, with no account and no ads.', telecharger='Download')
    if l == 'es':
        return dict(
            court='Sobre Basal', h1='Quién hace Basal', title='Sobre Basal: quién la hace y de qué vive',
            description='Basal la diseña y desarrolla Théo Serrano, desarrollador independiente en Francia. Sus principios, su modelo económico (Premium opcional, sin publicidad), sus fuentes de datos y cómo contactar.',
            og_title='Sobre Basal', og_description='Quién hace Basal, sus principios, su modelo económico y sus fuentes de datos.',
            chapeau='Basal es una aplicación de seguimiento nutricional, de peso y de musculación. La diseña, desarrolla y mantiene Théo Serrano, desarrollador independiente en Francia.',
            s=['El editor', 'Los principios', 'De qué vive Basal', 'Algunos datos', 'Fuentes y licencias', 'Contacto'],
            editeur=f'Théo Serrano edita Basal como empresario individual (entrepreneur individuel), con el nombre comercial Basal. Escribe la aplicación, este sitio y los artículos que contiene, y responde él mismo a los mensajes. Los datos de contacto completos figuran en el <a href="{u("mentions")}">aviso legal</a>.',
            principes=[f'<strong>Partir de una fórmula publicada y corregirla con tus datos.</strong> El gasto de partida viene de la ecuación de Mifflin-St Jeor; la aplicación la contrasta después con tus comidas y la evolución de tu peso. Todos los cálculos se detallan en la página <a href="{u("methode")}">Método</a>.',
                       '<strong>Decir cuándo no se sabe.</strong> Mientras los datos sean demasiado escasos, la aplicación muestra «datos insuficientes» en lugar de una cifra que parecería segura.',
                       '<strong>Mantener lo esencial gratis.</strong> El seguimiento de las comidas, del peso, de las sesiones y las recetas no piden ni suscripción ni cuenta.',
                       '<strong>No convertir la salud en argumento.</strong> Basal constata, calcula y explica; no es un dispositivo médico, y la aplicación lo recuerda.'],
            vit=f'De una suscripción Premium, opcional, vendida a través de Google Play y la App Store, que añade análisis y asistentes (ver <a href="{u("compteur-gratuit")}">lo que es gratis y lo que es Premium</a>). Basal no muestra publicidad y no vende ningún dato.',
            reperes=[('Plataformas', 'iPhone y Android, en español, francés, inglés y alemán'), ('Alimentos', '3.304 alimentos de la tabla Ciqual de la ANSES, más los productos de Open Food Facts por búsqueda y código de barras'),
                     ('Musculación', '873 ejercicios'), ('Recetas', '50 recetas con valores calculados con la tabla Ciqual'),
                     ('Cuenta', 'Opcional; si se crea, los datos se alojan en Irlanda (Unión Europea)'), ('Sitio', 'Alojado en GitHub Pages, sin cookies; audiencia medida con GoatCounter')],
            sources=['Valores nutricionales de los alimentos genéricos: <a href="https://ciqual.anses.fr/">tabla Ciqual 2025 de la ANSES</a>, licencia abierta Etalab 2.0.',
                     'Productos comerciales: <a href="https://world.openfoodfacts.org/">Open Food Facts</a>, base colaborativa con licencia Open Database License.',
                     'Ilustraciones de las recetas: generadas por IA, no contractuales.', 'Fuentes tipográficas del sitio: Inter e Instrument Serif, con licencia SIL Open Font License.'],
            contact=f'Una pregunta, un error en un cálculo, una sugerencia: <a href="mailto:contact@basal-app.fr">contact@basal-app.fr</a>. Para tus datos, consulta la <a href="{u("confidentialite")}">política de privacidad</a> y la página de <a href="{u("suppression")}">eliminación de cuenta</a>.',
            appel_t='Prueba Basal.', appel='El seguimiento básico es gratis, sin cuenta y sin publicidad.', telecharger='Descargar')
    return dict(
        court='Über Basal', h1='Wer Basal macht', title='Über Basal: wer die App macht und wovon sie lebt',
        description='Basal wird von Théo Serrano entworfen und entwickelt, einem unabhängigen Entwickler in Frankreich. Ihre Grundsätze, ihr Geschäftsmodell (optionales Premium, keine Werbung), ihre Datenquellen und Kontakt.',
        og_title='Über Basal', og_description='Wer Basal macht, ihre Grundsätze, ihr Geschäftsmodell und ihre Datenquellen.',
        chapeau='Basal ist eine App für Ernährungs-, Gewichts- und Krafttrainingstracking. Sie wird von Théo Serrano entworfen, entwickelt und gepflegt, einem unabhängigen Entwickler in Frankreich.',
        s=['Der Herausgeber', 'Die Grundsätze', 'Wovon Basal lebt', 'Eckdaten', 'Quellen und Lizenzen', 'Kontakt'],
        editeur=f'Théo Serrano gibt Basal als Einzelunternehmer (entrepreneur individuel) unter dem Handelsnamen Basal heraus. Er schreibt die App, diese Website und die Artikel darauf, und beantwortet Nachrichten selbst. Die vollständigen Kontaktdaten stehen im <a href="{u("mentions")}">Impressum</a>.',
        principes=[f'<strong>Von einer veröffentlichten Formel ausgehen und sie dann mit deinen Daten korrigieren.</strong> Der Ausgangsverbrauch stammt aus der Mifflin-St-Jeor-Gleichung; die App gleicht ihn dann mit deinen Mahlzeiten und der Entwicklung deines Gewichts ab. Alle Berechnungen stehen auf der Seite <a href="{u("methode")}">Methode</a>.',
                   '<strong>Sagen, wenn man es nicht weiß.</strong> Solange die Daten zu dünn sind, zeigt die App „nicht genug Daten“ an statt einer Zahl, die sicher aussähe.',
                   '<strong>Das Wesentliche kostenlos lassen.</strong> Das Erfassen von Mahlzeiten, Gewicht und Einheiten sowie die Rezepte verlangen weder ein Abo noch ein Konto.',
                   '<strong>Gesundheit nicht zum Verkaufsargument machen.</strong> Basal stellt fest, rechnet und erklärt; es ist kein Medizinprodukt, und die App weist darauf hin.'],
        vit=f'Von einem optionalen Premium-Abo, verkauft über Google Play und den App Store, das Analysen und Assistenten hinzufügt (siehe <a href="{u("compteur-gratuit")}">was kostenlos ist und was Premium</a>). Basal zeigt keine Werbung und verkauft keine Daten.',
        reperes=[('Plattformen', 'iPhone und Android, auf Deutsch, Französisch, Englisch und Spanisch'), ('Lebensmittel', '3.304 Lebensmittel aus der Ciqual-Tabelle der ANSES, dazu Produkte aus Open Food Facts per Suche und Barcode'),
                 ('Krafttraining', '873 Übungen'), ('Rezepte', '50 Rezepte mit aus der Ciqual-Tabelle berechneten Werten'),
                 ('Konto', 'Optional; wird es angelegt, liegen die Daten in Irland (Europäische Union)'), ('Website', 'Gehostet bei GitHub Pages, ohne Cookies; Reichweite gemessen mit GoatCounter')],
        sources=['Nährwerte allgemeiner Lebensmittel: <a href="https://ciqual.anses.fr/">Ciqual-2025-Tabelle der ANSES</a>, offene Lizenz Etalab 2.0.',
                 'Handelsprodukte: <a href="https://world.openfoodfacts.org/">Open Food Facts</a>, gemeinschaftliche Datenbank unter der Open Database License.',
                 'Rezeptbilder: KI-generiert, unverbindlich.', 'Schriften der Website: Inter und Instrument Serif, unter der SIL Open Font License.'],
        contact=f'Eine Frage, ein Fehler in einer Berechnung, ein Vorschlag: <a href="mailto:contact@basal-app.fr">contact@basal-app.fr</a>. Zu deinen Daten siehe die <a href="{u("confidentialite")}">Datenschutzerklärung</a> und die Seite <a href="{u("suppression")}">Konto löschen</a>.',
        appel_t='Probier Basal aus.', appel='Das Basis-Tracking ist kostenlos, ohne Konto und ohne Werbung.', telecharger='Herunterladen')


PAGES = {}
for l in ('en', 'es', 'de'):
    t = textes(l)
    s = t['s']
    li = '\n'.join(f'      <li>{x}</li>' for x in t['principes'])
    rows = '\n'.join(f'          <tr><th scope="row">{a}</th><td>{b}</td></tr>' for a, b in t['reperes'])
    src = '\n'.join(f'      <li>{x}</li>' for x in t['sources'])
    main = f'''<main id="contenu" class="wrap">
  <nav class="fil" aria-label="{L[l]["fil"]}"><a href="{U["accueil"][l]}">{L[l]["accueil"]}</a><span aria-hidden="true">›</span>{t["court"]}</nav>
  <header class="article-tete">
    <p class="surtitre">{t["court"]}</p>
    <h1>{t["h1"]}</h1>
    <p class="chapeau">{t["chapeau"]}</p>
  </header>

  <div class="corps" style="padding-top:44px">
    <h2>{s[0]}</h2>
    <p>{t["editeur"]}</p>

    <h2>{s[1]}</h2>
    <ul class="liste">
{li}
    </ul>

    <h2>{s[2]}</h2>
    <p>{t["vit"]}</p>

    <h2>{s[3]}</h2>
    <div class="tableau">
      <table>
        <tbody>
{rows}
        </tbody>
      </table>
    </div>

    <h2>{s[4]}</h2>
    <ul>
{src}
    </ul>

    <h2>{s[5]}</h2>
    <p>{t["contact"]}</p>

    <div class="appel-contexte">
      <div><strong>{t["appel_t"]}</strong><p>{t["appel"]}</p></div>
      <a class="bouton vif" href="{U["accueil"][l]}#download">{t["telecharger"]}</a>
    </div>
  </div>
</main>'''
    PAGES[l] = {'slug': U['apropos'][l], 'tete': dict(title=t['title'], description=t['description'], og_title=t['og_title'], og_description=t['og_description'], locale=L[l]['locale']), 'main': main}
