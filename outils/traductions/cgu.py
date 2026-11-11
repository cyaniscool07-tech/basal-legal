from commun import U, legale, avis_traduction

FR = '/cgu.html'
DATE = '2026-11-11'
C = 'cgu'


def corps(l):
    u = lambda k: U[k][l]
    av = avis_traduction(l, FR)
    conf, ment, supp = u('confidentialite'), u('mentions'), u('suppression')
    if l == 'en':
        return f'''  <h1 id="contenu">Terms of use — Basal</h1>
  <p class="updated">Last updated: 7 November 2026</p>

  {av}

  <p>These terms of use govern access to and use of the <strong>Basal</strong> mobile app, published by Théo Serrano (see the <a href="{ment}">legal notice</a> for the publisher’s full identity). Basal is a nutrition, weight and physical activity tracking app.</p>

  <h2>1. Acceptance</h2>
  <p>Installing and using the app implies full acceptance of these terms of use, as well as of the <a href="{conf}">privacy policy</a>. If you do not accept these terms, you must not use the app.</p>

  <h2>2. Minimum age</h2>
  <p>The app is for people aged <strong>18 and over</strong> — see the privacy policy, section 11, for the details of this choice, which is deliberately stricter than the law requires. By using the app, you declare that you are at least 18.</p>

  <h2>3. Access to the app and account</h2>
  <p>The app can be used <strong>entirely without creating an account</strong>: the tracking features (calories, weight, activity, strength training, targets) then remain available, with the data kept only on your device.</p>
  <p>Creating an account is <strong>optional</strong> and lets you back up your data on a server to get it back on another device, and carry a Premium subscription from one platform to another. The details (creation, sign-in with Google/Apple, deletion) are described in the <a href="{conf}">privacy policy</a>, section 3.</p>
  <p>You are responsible for keeping the means of access to your account (password, signed-in device) confidential, and for any activity resulting from them.</p>

  <h2>4. Premium subscription</h2>
  <p class="note">At the time of writing, the Premium offer is not yet enabled in the app — this section describes how it works for when it is.</p>
  <p>Some advanced features of the app may be offered as part of a paid <strong>Premium</strong> subscription, in addition to the free features, which remain available with no time limit.</p>
  <ul>
    <li><strong>Sale and billing</strong>: purchases and subscriptions are handled exclusively by the platform from which you installed the app (Apple App Store or Google Play), using the payment methods you have registered there. The price shown on the subscription page at the time of purchase is authoritative; it is not reproduced in this document to avoid any gap with the actual price.</li>
    <li><strong>Automatic renewal</strong>: unless cancelled before the end of the current period, a subscription renews automatically at the chosen frequency (monthly, yearly, or a one-off lifetime purchase depending on the plans offered), and the corresponding amount is charged by the platform.</li>
    <li><strong>Free trial</strong>: when a trial is offered, its length and the price applied afterwards are shown before purchase, and the platform decides whether you are eligible. Unless cancelled at least 24 hours before it ends, the subscription then starts automatically and the stated amount is charged by the platform.</li>
    <li><strong>Cancellation</strong>: you can cancel a subscription at any time from your Apple or Google account settings — the publisher cannot cancel a subscription for you, nor change its price or frequency. Cancellation takes effect at the end of the period already paid for; the publisher makes no pro-rata refund.</li>
    <li><strong>Refunds</strong>: any refund request falls exclusively under Apple’s or Google’s policy, as they alone are authorised to handle this type of request for a purchase made on their platform.</li>
    <li><strong>Scope</strong>: a subscription bought on one platform (e.g. Google Play) is not automatically transferable to the other (e.g. the App Store); getting it back on another device or platform requires a Basal account, as explained in section 3.</li>
    <li><strong>Loss of access</strong>: uninstalling the app or deleting the Basal account does <strong>not</strong> cancel an ongoing subscription, which remains managed by the platform — see <a href="{supp}">account deletion</a> for what is erased and what is not.</li>
  </ul>

  <h2>5. Health warning</h2>
  <p>Basal provides estimates (calorie needs, basal metabolic rate, energy expenditure, macronutrients) calculated from recognised scientific formulas and the data you enter. These estimates are provided <strong>for information only</strong> and in no way constitute medical advice, a diagnosis or a prescription.</p>
  <p>The app does not replace consulting a health professional (doctor, dietitian, nutritionist), in particular in the case of an eating disorder, an existing condition, pregnancy, or before making a major change to your diet or physical activity. Théo Serrano cannot be held liable for the consequences of using the app as a substitute for appropriate medical follow-up.</p>

  <h2>6. Intellectual property</h2>
  <p>The content of the app (name, logo, interface, texts, code) is protected and remains the property of the publisher — see the <a href="{ment}">legal notice</a> for details, including the third-party content included under its own licence (in particular Open Food Facts).</p>
  <p>The data you record in the app yourself (meals, personal recipes, sessions, targets) belongs to you: the export provided for in the privacy policy (section 8) lets you retrieve it at any time in an open format.</p>

  <h2>6a. Community and published content</h2>
  <p><strong>Rules.</strong> The Community rules, shown in the app and accepted before any first post, form part of these terms of use. They describe what can be posted and what is refused or removed.</p>
  <p><strong>What you guarantee.</strong> You post your own creations, or content you have the right to share, and accurate information. You remain responsible for what you post.</p>
  <p><strong>Licence.</strong> By posting, you grant the publisher and the other people using Basal a <strong>free, non-exclusive, worldwide</strong> permission, for as long as the post stays up: to host and display your content in the app, to let it be imported, and to let everyone <strong>edit their own copy</strong>. You remain the owner of your content. Removing a post ends the permission for the future; copies already imported stay with those who made them.</p>
  <p><strong>Moderation.</strong> Every post, and every new version, is reviewed before it becomes visible. A refusal, hiding or suspension is <strong>always explained</strong> and communicated in the app; you can ask for a <strong>review</strong> once per decision. An account that breaks the rules seriously or repeatedly may be suspended from the Community; its personal tracking is never affected.</p>
  <p><strong>Reporting content.</strong> From the content’s page (“Report”), or at <a href="mailto:contact@basal-app.fr">contact@basal-app.fr</a> — including without an account, in particular for content you believe is <strong>illegal</strong> or that reuses your work without your consent. Give the link or code of the content, the reason, and your contact details. You are informed of what action is taken.</p>
  <p><strong>No medical advice.</strong> Shared recipes and routines do not replace the advice of a health professional (see section 5). The publisher checks posts but guarantees neither their accuracy nor their suitability for your situation.</p>

  <h2>7. Availability and changes to the service</h2>
  <p>The publisher strives to ensure continuous access to the app and, for features requiring an account, to the backup service, without guaranteeing absolute availability (maintenance, outage, force majeure).</p>
  <p>The app’s features may change (addition, modification or removal); significant changes affecting your personal data are announced in advance in accordance with the privacy policy, section 13.</p>

  <h2>8. Termination</h2>
  <p>You can stop using the app at any time by uninstalling it. If you created an account, you can delete it from Settings → Account, which erases your data from the server as described on the <a href="{supp}">dedicated page</a>. An ongoing Premium subscription follows its own cancellation rules (see section 4).</p>
  <p>The publisher reserves the right to suspend or close an account in the event of use clearly contrary to these terms of use or to the law.</p>

  <h2>9. Changes to the terms of use</h2>
  <p>These terms of use may be changed to reflect a change in the app, its offer or the applicable regulations. The version in force is the one published at this address; in the event of a substantial change, notice will be given in the app.</p>

  <h2>10. Applicable law and disputes</h2>
  <p>These terms of use are governed by French law. In the event of a dispute and failing an amicable resolution, the competent French courts shall have sole jurisdiction, subject to the mandatory provisions applicable to consumers.</p>

  <h2>11. Contact</h2>
  <div class="contact">
    <p style="margin:0">For any question about these terms of use, write to <strong>contact@basal-app.fr</strong>, or use the app’s page in the store where you downloaded it.</p>
  </div>'''
    if l == 'es':
        return f'''  <h1 id="contenu">Condiciones generales de uso — Basal</h1>
  <p class="updated">Última actualización: 7 de noviembre de 2026</p>

  {av}

  <p>Las presentes condiciones generales de uso rigen el acceso a la aplicación móvil <strong>Basal</strong> y su uso. La edita Théo Serrano (ver el <a href="{ment}">aviso legal</a> para la identidad completa del editor). Basal es una aplicación de seguimiento nutricional, de peso y de actividad física.</p>

  <h2>1. Aceptación</h2>
  <p>La instalación y el uso de la aplicación implican la aceptación plena de las presentes condiciones, así como de la <a href="{conf}">política de privacidad</a>. Si no aceptas estas condiciones, no debes usar la aplicación.</p>

  <h2>2. Edad mínima</h2>
  <p>La aplicación está reservada a personas de <strong>18 años o más</strong>: ver la política de privacidad, sección 11, para el detalle de esta decisión, que es deliberadamente más estricta que lo que exige la ley. Al usar la aplicación, declaras tener al menos 18 años.</p>

  <h2>3. Acceso a la aplicación y cuenta</h2>
  <p>La aplicación se puede usar <strong>por completo sin crear una cuenta</strong>: las funciones de seguimiento (calorías, peso, actividad, musculación, objetivos) siguen entonces disponibles, con los datos guardados únicamente en tu dispositivo.</p>
  <p>Crear una cuenta es <strong>opcional</strong> y permite guardar tus datos en un servidor para recuperarlos en otro dispositivo, así como llevar una suscripción Premium de una plataforma a otra. Las modalidades (creación, inicio de sesión con Google/Apple, eliminación) se describen en detalle en la <a href="{conf}">política de privacidad</a>, sección 3.</p>
  <p>Eres responsable de la confidencialidad de los medios de acceso a tu cuenta (contraseña, dispositivo conectado) y de toda actividad derivada de ellos.</p>

  <h2>4. Suscripción Premium</h2>
  <p class="note">En la fecha de redacción, la oferta Premium aún no está activada en la aplicación: esta sección describe su funcionamiento para cuando lo esté.</p>
  <p>Algunas funciones avanzadas de la aplicación pueden ofrecerse dentro de una suscripción de pago <strong>Premium</strong>, como complemento de las funciones gratuitas, que siguen disponibles sin límite de tiempo.</p>
  <ul>
    <li><strong>Venta y facturación</strong>: las compras y suscripciones las gestiona exclusivamente la plataforma desde la que instalaste la aplicación (Apple App Store o Google Play), con los medios de pago que hayas registrado en ella. El precio que aparece en la ficha de la suscripción en el momento de la compra es el que da fe; no se reproduce en este documento para evitar cualquier diferencia con el precio real.</li>
    <li><strong>Renovación automática</strong>: salvo cancelación antes del final del periodo en curso, una suscripción se renueva automáticamente según la periodicidad elegida (mensual, anual o una compra única de por vida según las fórmulas ofrecidas), y la plataforma cobra el importe correspondiente.</li>
    <li><strong>Prueba gratuita</strong>: cuando se ofrece una prueba, su duración y el precio aplicado después se muestran antes de la compra, y la plataforma decide si tienes derecho a ella. Salvo cancelación al menos 24 horas antes de su fin, la suscripción empieza entonces automáticamente y la plataforma cobra el importe indicado.</li>
    <li><strong>Cancelación</strong>: puedes cancelar una suscripción en cualquier momento desde los ajustes de tu cuenta de Apple o Google; el editor no puede cancelar una suscripción por ti, ni modificar su precio o su periodicidad. La cancelación surte efecto al final del periodo ya pagado; el editor no realiza ningún reembolso prorrateado.</li>
    <li><strong>Reembolso</strong>: toda solicitud de reembolso depende exclusivamente de la política de Apple o de Google, únicos habilitados para tramitar este tipo de solicitud para una compra realizada en su plataforma.</li>
    <li><strong>Alcance</strong>: una suscripción comprada en una plataforma (por ejemplo, Google Play) no se transfiere automáticamente a la otra (por ejemplo, la App Store); recuperarla en otro dispositivo u otra plataforma requiere una cuenta de Basal, como se explica en la sección 3.</li>
    <li><strong>Pérdida de acceso</strong>: desinstalar la aplicación o eliminar la cuenta de Basal <strong>no</strong> cancela una suscripción en curso, que sigue gestionada por la plataforma; ver la <a href="{supp}">eliminación de cuenta</a> para saber lo que se borra y lo que no.</li>
  </ul>

  <h2>5. Advertencia relativa a la salud</h2>
  <p>Basal ofrece estimaciones (necesidades calóricas, metabolismo basal, gasto energético, macronutrientes) calculadas a partir de fórmulas científicas reconocidas y de los datos que introduces. Estas estimaciones se ofrecen <strong>a título informativo</strong> y en ningún caso constituyen un consejo médico, un diagnóstico ni una prescripción.</p>
  <p>La aplicación no sustituye la consulta con un profesional sanitario (médico, dietista, nutricionista), en particular en caso de trastorno de la conducta alimentaria, enfermedad existente, embarazo, o antes de emprender un cambio importante de alimentación o de actividad física. Théo Serrano no se hace responsable de las consecuencias de usar la aplicación en sustitución de un seguimiento médico adecuado.</p>

  <h2>6. Propiedad intelectual</h2>
  <p>El contenido de la aplicación (nombre, logotipo, interfaz, textos, código) está protegido y sigue siendo propiedad del editor: ver el <a href="{ment}">aviso legal</a> para el detalle, incluidos los contenidos de terceros integrados con su propia licencia (en particular Open Food Facts).</p>
  <p>Los datos que registras tú mismo en la aplicación (comidas, recetas personales, sesiones, objetivos) te pertenecen: la exportación prevista en la política de privacidad (sección 8) te permite recuperarlos en cualquier momento en un formato abierto.</p>

  <h2>6 bis. Comunidad y contenidos publicados</h2>
  <p><strong>Normas.</strong> Las normas de la Comunidad, mostradas en la aplicación y aceptadas antes de cualquier primera publicación, forman parte de las presentes condiciones. Describen lo que se puede publicar y lo que se rechaza o se retira.</p>
  <p><strong>Lo que garantizas.</strong> Publicas tus propias creaciones, o contenidos que tienes derecho a compartir, e información exacta. Sigues siendo responsable de lo que publicas.</p>
  <p><strong>Licencia.</strong> Al publicar, concedes al editor y a las demás personas que usan Basal una autorización <strong>gratuita, no exclusiva y mundial</strong>, durante el tiempo que dure la publicación: alojar y mostrar tu contenido en la aplicación, permitir que se importe, y permitir que cada cual <strong>modifique su propia copia</strong>. Sigues siendo propietario de tu contenido. Retirar una publicación pone fin a la autorización para el futuro; las copias ya importadas quedan en manos de quienes las hicieron.</p>
  <p><strong>Moderación.</strong> Cada publicación, y cada nueva versión, se examina antes de ser visible. Un rechazo, una ocultación o una suspensión <strong>siempre se motiva</strong> y se comunica en la aplicación; puedes pedir un <strong>nuevo examen</strong> una vez por decisión. Una cuenta que infrinja las normas de forma grave o reiterada puede ser suspendida de la Comunidad; su seguimiento personal nunca se ve afectado.</p>
  <p><strong>Denunciar un contenido.</strong> Desde la ficha del contenido («Denunciar») o en <a href="mailto:contact@basal-app.fr">contact@basal-app.fr</a>, incluso sin cuenta, en particular para un contenido que te parezca <strong>ilícito</strong> o que reproduzca tu obra sin tu consentimiento. Indica el enlace o el código del contenido, el motivo y tus datos de contacto. Se te informa del curso dado.</p>
  <p><strong>Sin consejo médico.</strong> Las recetas y rutinas compartidas no sustituyen el consejo de un profesional sanitario (ver la sección 5). El editor revisa las publicaciones, pero no garantiza ni su exactitud ni su adecuación a tu situación.</p>

  <h2>7. Disponibilidad y evolución del servicio</h2>
  <p>El editor se esfuerza por garantizar un acceso continuo a la aplicación y, para las funciones que requieren cuenta, al servicio de copia de seguridad, sin garantizar una disponibilidad absoluta (mantenimiento, avería, fuerza mayor).</p>
  <p>Las funciones de la aplicación pueden cambiar (incorporación, modificación o retirada); los cambios significativos que afecten a tus datos personales se anuncian con antelación conforme a la política de privacidad, sección 13.</p>

  <h2>8. Resolución</h2>
  <p>Puedes dejar de usar la aplicación en cualquier momento desinstalándola. Si has creado una cuenta, puedes eliminarla desde Ajustes → Cuenta, lo que borra tus datos del servidor según lo descrito en la <a href="{supp}">página dedicada</a>. Una suscripción Premium en curso sigue sus propias reglas de cancelación (ver la sección 4).</p>
  <p>El editor se reserva el derecho de suspender o cerrar una cuenta en caso de un uso manifiestamente contrario a las presentes condiciones o a la ley.</p>

  <h2>9. Modificación de las condiciones</h2>
  <p>Las presentes condiciones pueden modificarse para reflejar una evolución de la aplicación, de su oferta o de la normativa aplicable. La versión vigente es la publicada en esta dirección; en caso de cambio sustancial, se informará en la aplicación.</p>

  <h2>10. Legislación aplicable y litigios</h2>
  <p>Las presentes condiciones se rigen por la legislación francesa. En caso de litigio y a falta de resolución amistosa, solo serán competentes los tribunales franceses, sin perjuicio de las disposiciones imperativas aplicables a los consumidores.</p>

  <h2>11. Contacto</h2>
  <div class="contact">
    <p style="margin:0">Para cualquier pregunta sobre estas condiciones, escribe a <strong>contact@basal-app.fr</strong>, o usa la ficha de la aplicación en la tienda donde la descargaste.</p>
  </div>'''
    return f'''  <h1 id="contenu">Nutzungsbedingungen — Basal</h1>
  <p class="updated">Zuletzt aktualisiert: 7. November 2026</p>

  {av}

  <p>Diese Nutzungsbedingungen regeln den Zugang zur mobilen App <strong>Basal</strong> und ihre Nutzung. Herausgeber ist Théo Serrano (siehe das <a href="{ment}">Impressum</a> für die vollständige Identität des Herausgebers). Basal ist eine App für Ernährungs-, Gewichts- und Aktivitätstracking.</p>

  <h2>1. Annahme</h2>
  <p>Mit der Installation und Nutzung der App erkennst du diese Nutzungsbedingungen sowie die <a href="{conf}">Datenschutzerklärung</a> vollständig an. Wenn du diese Bedingungen nicht annimmst, darfst du die App nicht nutzen.</p>

  <h2>2. Mindestalter</h2>
  <p>Die App ist Personen ab <strong>18 Jahren</strong> vorbehalten – siehe die Datenschutzerklärung, Abschnitt 11, zu den Gründen dieser Entscheidung, die bewusst strenger ist als gesetzlich vorgeschrieben. Mit der Nutzung der App erklärst du, mindestens 18 Jahre alt zu sein.</p>

  <h2>3. Zugang zur App und Konto</h2>
  <p>Die App ist <strong>vollständig ohne Konto</strong> nutzbar: Die Tracking-Funktionen (Kalorien, Gewicht, Aktivität, Krafttraining, Ziele) bleiben dann verfügbar, wobei die Daten nur auf deinem Gerät gespeichert werden.</p>
  <p>Ein Konto anzulegen ist <strong>freiwillig</strong> und ermöglicht es, deine Daten auf einem Server zu sichern, um sie auf einem anderen Gerät wiederzufinden, sowie ein Premium-Abo von einer Plattform zur anderen mitzunehmen. Die Einzelheiten (Anlegen, Anmeldung über Google/Apple, Löschen) beschreibt die <a href="{conf}">Datenschutzerklärung</a>, Abschnitt 3.</p>
  <p>Du bist für die Vertraulichkeit der Zugangsmittel zu deinem Konto (Passwort, angemeldetes Gerät) und für jede daraus folgende Aktivität verantwortlich.</p>

  <h2>4. Premium-Abo</h2>
  <p class="note">Zum Zeitpunkt der Abfassung ist das Premium-Angebot in der App noch nicht aktiviert – dieser Abschnitt beschreibt seine Funktionsweise für den Zeitpunkt, an dem es aktiviert wird.</p>
  <p>Einige erweiterte Funktionen der App können im Rahmen eines kostenpflichtigen <strong>Premium</strong>-Abos angeboten werden, zusätzlich zu den kostenlosen Funktionen, die ohne Zeitlimit verfügbar bleiben.</p>
  <ul>
    <li><strong>Verkauf und Abrechnung</strong>: Käufe und Abos werden ausschließlich von der Plattform abgewickelt, über die du die App installiert hast (Apple App Store oder Google Play), mit den dort hinterlegten Zahlungsmitteln. Maßgeblich ist der zum Kaufzeitpunkt auf der Abo-Seite angezeigte Preis; er wird in diesem Dokument nicht wiedergegeben, um jede Abweichung vom tatsächlichen Preis zu vermeiden.</li>
    <li><strong>Automatische Verlängerung</strong>: Sofern nicht vor Ende des laufenden Zeitraums gekündigt, verlängert sich ein Abo automatisch im gewählten Rhythmus (monatlich, jährlich oder ein einmaliger Kauf auf Lebenszeit, je nach angebotenen Tarifen), und der entsprechende Betrag wird von der Plattform abgebucht.</li>
    <li><strong>Kostenloser Test</strong>: Wird ein Test angeboten, werden seine Dauer und der danach geltende Preis vor dem Kauf angezeigt, und die Plattform entscheidet, ob du Anspruch darauf hast. Sofern nicht mindestens 24 Stunden vor seinem Ende gekündigt, beginnt das Abo dann automatisch, und der angegebene Betrag wird von der Plattform abgebucht.</li>
    <li><strong>Kündigung</strong>: Du kannst ein Abo jederzeit in den Einstellungen deines Apple- oder Google-Kontos kündigen – der Herausgeber kann ein Abo weder für dich kündigen noch seinen Preis oder Rhythmus ändern. Die Kündigung wird zum Ende des bereits bezahlten Zeitraums wirksam; der Herausgeber erstattet nichts anteilig.</li>
    <li><strong>Erstattung</strong>: Jeder Erstattungsantrag unterliegt ausschließlich den Richtlinien von Apple oder Google, die allein befugt sind, solche Anträge für einen Kauf auf ihrer Plattform zu bearbeiten.</li>
    <li><strong>Geltungsbereich</strong>: Ein auf einer Plattform gekauftes Abo (z. B. Google Play) ist nicht automatisch auf die andere übertragbar (z. B. den App Store); um es auf einem anderen Gerät oder einer anderen Plattform wiederzufinden, ist ein Basal-Konto nötig, wie in Abschnitt 3 erklärt.</li>
    <li><strong>Verlust des Zugangs</strong>: Das Deinstallieren der App oder das Löschen des Basal-Kontos kündigt ein laufendes Abo <strong>nicht</strong>, da es weiterhin von der Plattform verwaltet wird – siehe <a href="{supp}">Konto löschen</a> dazu, was gelöscht wird und was nicht.</li>
  </ul>

  <h2>5. Gesundheitshinweis</h2>
  <p>Basal liefert Schätzungen (Kalorienbedarf, Grundumsatz, Energieverbrauch, Makronährstoffe), berechnet aus anerkannten wissenschaftlichen Formeln und den Daten, die du eingibst. Diese Schätzungen dienen <strong>nur der Information</strong> und stellen in keinem Fall eine medizinische Beratung, Diagnose oder Verordnung dar.</p>
  <p>Die App ersetzt nicht die Beratung durch medizinisches Fachpersonal (Ärztin oder Arzt, Diätassistenz, Ernährungsberatung), insbesondere bei einer Essstörung, einer bestehenden Erkrankung, einer Schwangerschaft oder vor einer wesentlichen Änderung der Ernährung oder der körperlichen Aktivität. Théo Serrano haftet nicht für die Folgen einer Nutzung der App als Ersatz für eine angemessene medizinische Betreuung.</p>

  <h2>6. Geistiges Eigentum</h2>
  <p>Der Inhalt der App (Name, Logo, Oberfläche, Texte, Code) ist geschützt und bleibt Eigentum des Herausgebers – siehe das <a href="{ment}">Impressum</a> für Einzelheiten, einschließlich der unter eigener Lizenz integrierten Inhalte Dritter (insbesondere Open Food Facts).</p>
  <p>Die Daten, die du selbst in der App erfasst (Mahlzeiten, eigene Rezepte, Einheiten, Ziele), gehören dir: Der in der Datenschutzerklärung (Abschnitt 8) vorgesehene Export ermöglicht es dir, sie jederzeit in einem offenen Format abzurufen.</p>

  <h2>6a. Community und veröffentlichte Inhalte</h2>
  <p><strong>Regeln.</strong> Die Community-Regeln, die in der App angezeigt und vor jeder ersten Veröffentlichung akzeptiert werden, sind Bestandteil dieser Nutzungsbedingungen. Sie beschreiben, was veröffentlicht werden kann und was abgelehnt oder entfernt wird.</p>
  <p><strong>Was du garantierst.</strong> Du veröffentlichst eigene Werke oder Inhalte, die du teilen darfst, und zutreffende Informationen. Du bleibst für das verantwortlich, was du veröffentlichst.</p>
  <p><strong>Lizenz.</strong> Mit der Veröffentlichung räumst du dem Herausgeber und den anderen Nutzerinnen und Nutzern von Basal eine <strong>unentgeltliche, nicht ausschließliche, weltweite</strong> Erlaubnis für die Dauer der Veröffentlichung ein: deinen Inhalt in der App zu hosten und anzuzeigen, ihn importieren zu lassen und jeden <strong>seine eigene Kopie bearbeiten</strong> zu lassen. Du bleibst Eigentümer deines Inhalts. Das Zurückziehen einer Veröffentlichung beendet die Erlaubnis für die Zukunft; bereits importierte Kopien bleiben bei denen, die sie gemacht haben.</p>
  <p><strong>Moderation.</strong> Jede Veröffentlichung und jede neue Fassung wird geprüft, bevor sie sichtbar wird. Eine Ablehnung, Ausblendung oder Sperre wird <strong>immer begründet</strong> und in der App mitgeteilt; du kannst einmal pro Entscheidung eine <strong>erneute Prüfung</strong> verlangen. Ein Konto, das schwer oder wiederholt gegen die Regeln verstößt, kann von der Community gesperrt werden; sein persönliches Tracking ist davon nie betroffen.</p>
  <p><strong>Einen Inhalt melden.</strong> Über die Seite des Inhalts („Melden“) oder an <a href="mailto:contact@basal-app.fr">contact@basal-app.fr</a> – auch ohne Konto, insbesondere bei einem Inhalt, der dir <strong>rechtswidrig</strong> erscheint oder dein Werk ohne deine Zustimmung übernimmt. Gib den Link oder Code des Inhalts, den Grund und deine Kontaktdaten an. Du wirst über das weitere Vorgehen informiert.</p>
  <p><strong>Keine medizinische Beratung.</strong> Geteilte Rezepte und Routinen ersetzen nicht den Rat medizinischen Fachpersonals (siehe Abschnitt 5). Der Herausgeber prüft die Veröffentlichungen, garantiert aber weder ihre Richtigkeit noch ihre Eignung für deine Situation.</p>

  <h2>7. Verfügbarkeit und Weiterentwicklung des Dienstes</h2>
  <p>Der Herausgeber bemüht sich, einen ununterbrochenen Zugang zur App und, für Funktionen mit Konto, zum Sicherungsdienst zu gewährleisten, ohne eine absolute Verfügbarkeit zu garantieren (Wartung, Ausfall, höhere Gewalt).</p>
  <p>Die Funktionen der App können sich ändern (Hinzufügen, Ändern oder Entfernen); wesentliche Änderungen, die deine personenbezogenen Daten betreffen, werden gemäß der Datenschutzerklärung, Abschnitt 13, vorab angekündigt.</p>

  <h2>8. Beendigung</h2>
  <p>Du kannst die Nutzung der App jederzeit beenden, indem du sie deinstallierst. Wenn du ein Konto angelegt hast, kannst du es unter Einstellungen → Konto löschen, wodurch deine Daten wie auf der <a href="{supp}">entsprechenden Seite</a> beschrieben vom Server entfernt werden. Ein laufendes Premium-Abo folgt seinen eigenen Kündigungsregeln (siehe Abschnitt 4).</p>
  <p>Der Herausgeber behält sich vor, ein Konto bei einer Nutzung, die offensichtlich gegen diese Nutzungsbedingungen oder das Gesetz verstößt, zu sperren oder zu schließen.</p>

  <h2>9. Änderung der Nutzungsbedingungen</h2>
  <p>Diese Nutzungsbedingungen können geändert werden, um eine Weiterentwicklung der App, ihres Angebots oder der anwendbaren Vorschriften abzubilden. Gültig ist die unter dieser Adresse veröffentlichte Fassung; bei einer wesentlichen Änderung wird in der App darauf hingewiesen.</p>

  <h2>10. Anwendbares Recht und Streitigkeiten</h2>
  <p>Diese Nutzungsbedingungen unterliegen französischem Recht. Im Streitfall und mangels gütlicher Einigung sind ausschließlich die zuständigen französischen Gerichte zuständig, vorbehaltlich der zwingenden Verbraucherschutzvorschriften.</p>

  <h2>11. Kontakt</h2>
  <div class="contact">
    <p style="margin:0">Für alle Fragen zu diesen Nutzungsbedingungen schreibe an <strong>contact@basal-app.fr</strong> oder nutze die Seite der App im Store, aus dem du sie heruntergeladen hast.</p>
  </div>'''


META = {'en': ('Terms of use — Basal', 'Terms of use of the Basal app (nutrition, weight, metabolism and activity tracking).'),
        'es': ('Condiciones generales de uso — Basal', 'Condiciones generales de uso de la aplicación Basal (seguimiento nutricional, peso, metabolismo y actividad).'),
        'de': ('Nutzungsbedingungen — Basal', 'Nutzungsbedingungen der App Basal (Ernährungs-, Gewichts-, Stoffwechsel- und Aktivitätstracking).')}

PAGES = {l: legale(l, C, *META[l], corps(l)) for l in META}
