from commun import U, legale, avis_traduction

FR = '/mentions-legales.html'
DATE = '2026-11-11'
C = 'mentions'

CIQUAL = '<a href="https://www.etalab.gouv.fr/licence-ouverte-open-licence/">Licence Ouverte / Etalab 2.0</a>'
ODBL = '<a href="https://opendatacommons.org/licenses/odbl/">Open Database License</a>'


def corps(l):
    u = lambda k: U[k][l]
    av = avis_traduction(l, FR)
    if l == 'en':
        return f'''  <h1 id="contenu">Legal notice — Basal</h1>
  <p class="updated">Last updated: 7 August 2026</p>

  {av}

  <h2>1. Publisher of the app</h2>
  <p>The <strong>Basal</strong> app is published by:</p>
  <ul>
    <li><strong>Théo Serrano</strong>, sole trader (entrepreneur individuel, EI), trading under the name <strong>Basal</strong></li>
    <li>Address: 958 route de Saint Abdon, 69390 Charly, France</li>
    <li>SIRET: 943 668 137 000 12 — SIREN: 943 668 137</li>
    <li>Contact: <a href="mailto:contact@basal-app.fr">contact@basal-app.fr</a></li>
  </ul>
  <p><strong>Publication director</strong>: Théo Serrano, as publisher.</p>

  <h2>2. Hosting</h2>
  <h3>App data (accounts and backup)</h3>
  <p>When an account is created in the app (see the <a href="{u("confidentialite")}">privacy policy</a>, section 3), the associated data is hosted by <strong>Supabase</strong>, on servers located in <strong>Ireland (European Union)</strong>. Without an account, no personal data is sent to a server.</p>
  <h3>Legal pages (this document and the privacy policy)</h3>
  <p>The public versions of these pages are hosted by <strong>GitHub, Inc.</strong> (GitHub Pages) — 88 Colin P Kelly Jr St, San Francisco, CA 94107, United States.</p>
  <h3>The app itself</h3>
  <p>The app is not a website but a mobile app distributed exclusively through:</p>
  <ul>
    <li><strong>Apple App Store</strong>, operated by Apple Inc. (One Apple Park Way, Cupertino, CA 95014, United States);</li>
    <li><strong>Google Play</strong>, operated by Google LLC (1600 Amphitheatre Parkway, Mountain View, CA 94043, United States).</li>
  </ul>
  <p>Each platform applies its own terms of use for distributing the app and handling payments, independently of the publisher (see the <a href="{u("cgu")}">Terms of use</a>, section 4).</p>

  <h2>3. Intellectual property</h2>
  <p>All the elements making up the Basal app — name, logo, interface, texts, source code, structure of the food and exercise database, except for the third-party content mentioned below — are the property of Théo Serrano, unless otherwise stated, and are protected by applicable copyright and trademark law.</p>
  <p>Any reproduction, representation, modification or use, in whole or in part, without prior permission, is prohibited and may constitute infringement within the meaning of articles L.335-2 et seq. of the French Intellectual Property Code.</p>
  <p>Some built-in content comes from third-party sources and remains subject to its own licences:</p>
  <ul>
    <li>nutritional values of generic foods from ANSES’s <strong>Ciqual 2025 food composition table</strong> ({CIQUAL});</li>
    <li>food data from <strong>Open Food Facts</strong> (collaborative database under the {ODBL});</li>
    <li>the open-source libraries and software components used to build the app, each under its own licence.</li>
  </ul>

  <h2>4. Liability</h2>
  <p>Théo Serrano does everything possible to ensure the accuracy and updating of the information and calculations provided by the app, without any guarantee of results. The publisher cannot be held liable for errors, omissions, temporary unavailability of the service, or any damage resulting from use of the app that does not match its purpose — see also the <a href="{u("cgu")}">Terms of use</a>, section 5, for the health warning.</p>

  <h2>5. Applicable law</h2>
  <p>This legal notice is governed by French law. In the event of a dispute and failing an amicable agreement, the competent French courts shall have sole jurisdiction.</p>

  <h2>6. Contact</h2>
  <div class="contact">
    <p style="margin:0">For any question about this legal notice, write to <strong>contact@basal-app.fr</strong>.</p>
  </div>'''
    if l == 'es':
        return f'''  <h1 id="contenu">Aviso legal — Basal</h1>
  <p class="updated">Última actualización: 7 de agosto de 2026</p>

  {av}

  <h2>1. Editor de la aplicación</h2>
  <p>La aplicación <strong>Basal</strong> la edita:</p>
  <ul>
    <li><strong>Théo Serrano</strong>, empresario individual (entrepreneur individuel, EI), que opera con el nombre comercial <strong>Basal</strong></li>
    <li>Dirección: 958 route de Saint Abdon, 69390 Charly, Francia</li>
    <li>SIRET: 943 668 137 000 12 — SIREN: 943 668 137</li>
    <li>Contacto: <a href="mailto:contact@basal-app.fr">contact@basal-app.fr</a></li>
  </ul>
  <p><strong>Director de la publicación</strong>: Théo Serrano, en calidad de editor.</p>

  <h2>2. Alojamiento</h2>
  <h3>De los datos de la aplicación (cuentas y copia de seguridad)</h3>
  <p>Cuando se crea una cuenta en la aplicación (ver la <a href="{u("confidentialite")}">política de privacidad</a>, sección 3), los datos asociados los aloja <strong>Supabase</strong>, en servidores situados en <strong>Irlanda (Unión Europea)</strong>. Sin cuenta, no se transmite ningún dato personal a un servidor.</p>
  <h3>De las páginas legales (este documento y la política de privacidad)</h3>
  <p>Las versiones públicas de estas páginas las aloja <strong>GitHub, Inc.</strong> (GitHub Pages) — 88 Colin P Kelly Jr St, San Francisco, CA 94107, Estados Unidos.</p>
  <h3>De la propia aplicación</h3>
  <p>La aplicación no es un sitio web, sino una aplicación móvil distribuida exclusivamente a través de:</p>
  <ul>
    <li><strong>Apple App Store</strong>, explotada por Apple Inc. (One Apple Park Way, Cupertino, CA 95014, Estados Unidos);</li>
    <li><strong>Google Play</strong>, explotada por Google LLC (1600 Amphitheatre Parkway, Mountain View, CA 94043, Estados Unidos).</li>
  </ul>
  <p>Cada plataforma aplica sus propias condiciones de uso para la distribución de la aplicación y la gestión de los pagos, con independencia del editor (ver las <a href="{u("cgu")}">Condiciones de uso</a>, sección 4).</p>

  <h2>3. Propiedad intelectual</h2>
  <p>Todos los elementos que componen la aplicación Basal —nombre, logotipo, interfaz, textos, código fuente, estructura de la base de alimentos y de ejercicios, salvo los contenidos de terceros mencionados más abajo— son propiedad de Théo Serrano, salvo indicación contraria, y están protegidos por la normativa aplicable sobre derechos de autor y marcas.</p>
  <p>Queda prohibida cualquier reproducción, representación, modificación o explotación, total o parcial, sin autorización previa, que podría constituir una falsificación en el sentido de los artículos L.335-2 y siguientes del Código de la Propiedad Intelectual francés.</p>
  <p>Algunos contenidos integrados proceden de fuentes de terceros y siguen sujetos a sus propias licencias:</p>
  <ul>
    <li>los valores nutricionales de los alimentos genéricos de la <strong>Tabla de composición nutricional de los alimentos Ciqual 2025</strong> de la ANSES ({CIQUAL});</li>
    <li>los datos de alimentos de <strong>Open Food Facts</strong> (base colaborativa con licencia {ODBL});</li>
    <li>las bibliotecas y componentes de software de código abierto utilizados para construir la aplicación, cada uno con su propia licencia.</li>
  </ul>

  <h2>4. Responsabilidad</h2>
  <p>Théo Serrano hace todo lo posible por garantizar la exactitud y la actualización de la información y los cálculos que ofrece la aplicación, sin garantía de resultado. El editor no se hace responsable de errores, omisiones, interrupciones temporales del servicio ni de daños derivados de un uso de la aplicación no conforme a su finalidad; ver también las <a href="{u("cgu")}">Condiciones de uso</a>, sección 5, para la advertencia relativa a la salud.</p>

  <h2>5. Legislación aplicable</h2>
  <p>El presente aviso legal se rige por la legislación francesa. En caso de litigio y a falta de acuerdo amistoso, solo serán competentes los tribunales franceses.</p>

  <h2>6. Contacto</h2>
  <div class="contact">
    <p style="margin:0">Para cualquier pregunta sobre este aviso legal, escribe a <strong>contact@basal-app.fr</strong>.</p>
  </div>'''
    return f'''  <h1 id="contenu">Impressum — Basal</h1>
  <p class="updated">Zuletzt aktualisiert: 7. August 2026</p>

  {av}

  <h2>1. Herausgeber der App</h2>
  <p>Die App <strong>Basal</strong> wird herausgegeben von:</p>
  <ul>
    <li><strong>Théo Serrano</strong>, Einzelunternehmer (entrepreneur individuel, EI), tätig unter dem Handelsnamen <strong>Basal</strong></li>
    <li>Anschrift: 958 route de Saint Abdon, 69390 Charly, Frankreich</li>
    <li>SIRET: 943 668 137 000 12 — SIREN: 943 668 137</li>
    <li>Kontakt: <a href="mailto:contact@basal-app.fr">contact@basal-app.fr</a></li>
  </ul>
  <p><strong>Verantwortlich für den Inhalt</strong>: Théo Serrano, als Herausgeber.</p>

  <h2>2. Hosting</h2>
  <h3>Der App-Daten (Konten und Sicherung)</h3>
  <p>Wenn in der App ein Konto angelegt wird (siehe die <a href="{u("confidentialite")}">Datenschutzerklärung</a>, Abschnitt 3), werden die zugehörigen Daten von <strong>Supabase</strong> auf Servern in <strong>Irland (Europäische Union)</strong> gehostet. Ohne Konto werden keine personenbezogenen Daten an einen Server übertragen.</p>
  <h3>Der rechtlichen Seiten (dieses Dokument und die Datenschutzerklärung)</h3>
  <p>Die öffentlichen Fassungen dieser Seiten werden von <strong>GitHub, Inc.</strong> (GitHub Pages) gehostet – 88 Colin P Kelly Jr St, San Francisco, CA 94107, Vereinigte Staaten.</p>
  <h3>Der App selbst</h3>
  <p>Die App ist keine Website, sondern eine mobile App, die ausschließlich vertrieben wird über:</p>
  <ul>
    <li>den <strong>Apple App Store</strong>, betrieben von Apple Inc. (One Apple Park Way, Cupertino, CA 95014, Vereinigte Staaten);</li>
    <li><strong>Google Play</strong>, betrieben von Google LLC (1600 Amphitheatre Parkway, Mountain View, CA 94043, Vereinigte Staaten).</li>
  </ul>
  <p>Jede Plattform wendet für den Vertrieb der App und die Abwicklung der Zahlungen ihre eigenen Nutzungsbedingungen an, unabhängig vom Herausgeber (siehe die <a href="{u("cgu")}">Nutzungsbedingungen</a>, Abschnitt 4).</p>

  <h2>3. Geistiges Eigentum</h2>
  <p>Alle Bestandteile der App Basal – Name, Logo, Oberfläche, Texte, Quellcode, Struktur der Lebensmittel- und Übungsdatenbank, mit Ausnahme der unten genannten Inhalte Dritter – sind, sofern nicht anders angegeben, Eigentum von Théo Serrano und durch das anwendbare Urheber- und Markenrecht geschützt.</p>
  <p>Jede vollständige oder teilweise Vervielfältigung, Darstellung, Änderung oder Verwertung ohne vorherige Genehmigung ist untersagt und kann eine Verletzung im Sinne der Artikel L.335-2 ff. des französischen Gesetzbuchs über geistiges Eigentum darstellen.</p>
  <p>Einige integrierte Inhalte stammen aus Quellen Dritter und unterliegen weiterhin deren eigenen Lizenzen:</p>
  <ul>
    <li>die Nährwerte allgemeiner Lebensmittel aus der <strong>Nährwerttabelle Ciqual 2025</strong> der ANSES ({CIQUAL});</li>
    <li>die Lebensmitteldaten aus <strong>Open Food Facts</strong> (gemeinschaftliche Datenbank unter der {ODBL});</li>
    <li>die Open-Source-Bibliotheken und Softwarekomponenten, mit denen die App gebaut wird, jeweils unter ihrer eigenen Lizenz.</li>
  </ul>

  <h2>4. Haftung</h2>
  <p>Théo Serrano tut alles, um die Richtigkeit und Aktualität der Informationen und Berechnungen der App sicherzustellen, ohne Erfolgsgarantie. Der Herausgeber haftet nicht für Fehler, Auslassungen, vorübergehende Nichtverfügbarkeit des Dienstes oder Schäden, die aus einer nicht bestimmungsgemäßen Nutzung der App entstehen – siehe auch die <a href="{u("cgu")}">Nutzungsbedingungen</a>, Abschnitt 5, für den Gesundheitshinweis.</p>

  <h2>5. Anwendbares Recht</h2>
  <p>Dieses Impressum unterliegt französischem Recht. Im Streitfall und mangels gütlicher Einigung sind ausschließlich die zuständigen französischen Gerichte zuständig.</p>

  <h2>6. Kontakt</h2>
  <div class="contact">
    <p style="margin:0">Für alle Fragen zu diesem Impressum schreibe an <strong>contact@basal-app.fr</strong>.</p>
  </div>'''


META = {'en': ('Legal notice — Basal', 'Legal notice of the Basal app (nutrition, weight, metabolism and activity tracking): publisher, hosting, intellectual property.'),
        'es': ('Aviso legal — Basal', 'Aviso legal de la aplicación Basal (seguimiento nutricional, peso, metabolismo y actividad): editor, alojamiento, propiedad intelectual.'),
        'de': ('Impressum — Basal', 'Impressum der App Basal (Ernährungs-, Gewichts-, Stoffwechsel- und Aktivitätstracking): Herausgeber, Hosting, geistiges Eigentum.')}

PAGES = {l: legale(l, C, *META[l], corps(l)) for l in META}
