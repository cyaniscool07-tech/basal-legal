from commun import U, legale, avis_traduction

FR = '/suppression-compte.html'
DATE = '2026-11-11'
C = 'suppression'


def corps(l):
    u = lambda k: U[k][l]
    av = avis_traduction(l, FR)
    if l == 'en':
        return f'''  <h1 id="contenu">Delete your account — Basal</h1>
  <p class="updated">Last updated: 7 August 2026</p>

  {av}

  <p>This page explains how to delete your <strong>Basal</strong> account (nutrition, weight, metabolism and activity tracking) and the data linked to it. There are two ways: from the app, or by email if you no longer have it.</p>

  <div class="note">
    Worth remembering: <strong>you do not need an account to use Basal.</strong> If you never created one, there is nothing to delete — none of your data has left your phone, and uninstalling the app erases it.
  </div>

  <h2>1. From the app (immediate)</h2>
  <ol>
    <li>Open Basal.</li>
    <li>Go to <strong>Settings</strong> (the gear at the top right of any tab).</li>
    <li>Open <strong>Account</strong> (“Account, backup and Premium status”).</li>
    <li>Scroll down to <strong>“Delete my account”</strong>.</li>
    <li>Confirm.</li>
  </ol>
  <p>Deletion is <strong>immediate and permanent</strong>. No request to send, no waiting period, no approval on our side.</p>

  <h2>2. By email (if you no longer have the app)</h2>
  <p>If you have uninstalled Basal or changed phone, write to <strong>contact@basal-app.fr</strong> from <strong>your account’s email address</strong>, with the subject <em>“Account deletion”</em>.</p>
  <p>Writing from the account’s address is what lets us check that the request really comes from you: it is the only protection against someone asking for another person’s account to be deleted. If you no longer have access to that address, say so in your message and we will find another way to verify you.</p>
  <p>The request is handled within <strong>30 days at most</strong>, and in practice much faster.</p>

  <h2>3. What is deleted, and what is not</h2>
  <table>
    <tr>
      <th>Data</th>
      <th>Becomes</th>
    </tr>
    <tr>
      <td>Your account and your email address</td>
      <td><strong>Deleted</strong> permanently</td>
    </tr>
    <tr>
      <td>Your data backed up on the server (profile, weight, meals, recipes, sessions, targets)</td>
      <td><strong>Deleted</strong> permanently</td>
    </tr>
    <tr>
      <td>The data still on your phone</td>
      <td><strong>Kept</strong> — the app goes back to being local, as before the account was created. To erase it too, uninstall the app or clear its data from your phone’s settings.</td>
    </tr>
    <tr>
      <td>Your Premium subscription, if you have one</td>
      <td><strong>Not cancelled.</strong> A subscription belongs to your Google Play account or your Apple ID, not to your Basal account — we have no way of cancelling it for you. See below.</td>
    </tr>
  </table>
  <p>No copy is kept after deletion: there is no grace period, no bin, no archive. A deleted account cannot be restored, and the data it held is lost. <strong>If you want to keep it, export it first</strong> from Settings → <strong>My data</strong> (export as JSON or CSV).</p>

  <h2>4. Cancelling a Premium subscription</h2>
  <p>Cancellation is done entirely with the platform where you subscribed, never in the app:</p>
  <ul>
    <li><strong>Android</strong> — Play Store → your profile → Payments &amp; subscriptions → Subscriptions → Basal → Cancel.</li>
    <li><strong>iPhone</strong> — phone Settings → your name → Subscriptions → Basal → Cancel Subscription.</li>
  </ul>
  <p>Deleting your Basal account without cancelling would let the subscription renew. Do both if that is what you want.</p>

  <h2>5. Questions</h2>
  <div class="contact">
    <p style="margin:0 0 12px">For any question about deleting your account or about how your data is handled: <strong>contact@basal-app.fr</strong></p>
    <p style="margin:0">What is collected, why and where, is detailed in the <a href="{u("confidentialite")}">privacy policy</a>.</p>
  </div>'''
    if l == 'es':
        return f'''  <h1 id="contenu">Eliminar tu cuenta — Basal</h1>
  <p class="updated">Última actualización: 7 de agosto de 2026</p>

  {av}

  <p>Esta página explica cómo eliminar tu cuenta de la aplicación <strong>Basal</strong> (seguimiento nutricional, peso, metabolismo y actividad) y los datos asociados. Hay dos caminos: desde la aplicación, o por correo electrónico si ya no la tienes.</p>

  <div class="note">
    Recordatorio útil: <strong>no hace falta una cuenta para usar Basal.</strong> Si nunca creaste una, no hay nada que eliminar: ninguno de tus datos ha salido de tu teléfono, y desinstalar la aplicación los borra.
  </div>

  <h2>1. Desde la aplicación (inmediato)</h2>
  <ol>
    <li>Abre Basal.</li>
    <li>Ve a <strong>Ajustes</strong> (el engranaje arriba a la derecha de cualquier pestaña).</li>
    <li>Abre <strong>Cuenta</strong> («Cuenta, copia de seguridad y estado Premium»).</li>
    <li>Desplázate hasta <strong>«Eliminar mi cuenta»</strong>.</li>
    <li>Confirma.</li>
  </ol>
  <p>La eliminación es <strong>inmediata y definitiva</strong>. Ninguna solicitud que enviar, ningún plazo de espera, ninguna validación por nuestra parte.</p>

  <h2>2. Por correo electrónico (si ya no tienes la aplicación)</h2>
  <p>Si has desinstalado Basal o cambiado de teléfono, escribe a <strong>contact@basal-app.fr</strong> desde <strong>la dirección de correo de tu cuenta</strong>, con el asunto <em>«Eliminación de cuenta»</em>.</p>
  <p>Escribir desde la dirección de la cuenta es lo que nos permite comprobar que la solicitud viene realmente de ti: es la única protección contra alguien que pidiera eliminar la cuenta de otra persona. Si ya no tienes acceso a esa dirección, dilo en tu mensaje y buscaremos otra forma de verificarte.</p>
  <p>La solicitud se tramita en un plazo de <strong>30 días como máximo</strong>, y en la práctica mucho antes.</p>

  <h2>3. Lo que se elimina y lo que no</h2>
  <table>
    <tr>
      <th>Dato</th>
      <th>Queda</th>
    </tr>
    <tr>
      <td>Tu cuenta y tu dirección de correo</td>
      <td><strong>Eliminadas</strong> definitivamente</td>
    </tr>
    <tr>
      <td>Tus datos guardados en el servidor (perfil, peso, comidas, recetas, sesiones, objetivos)</td>
      <td><strong>Eliminados</strong> definitivamente</td>
    </tr>
    <tr>
      <td>Los datos que siguen en tu teléfono</td>
      <td><strong>Conservados</strong>: la aplicación vuelve a ser local, como antes de crear la cuenta. Para borrarlos también, desinstala la aplicación o borra sus datos desde los ajustes de tu teléfono.</td>
    </tr>
    <tr>
      <td>Tu suscripción Premium, si tienes una</td>
      <td><strong>No se cancela.</strong> Una suscripción pertenece a tu cuenta de Google Play o a tu ID de Apple, no a tu cuenta de Basal: no tenemos ninguna forma de cancelarla por ti. Ver más abajo.</td>
    </tr>
  </table>
  <p>No se conserva ninguna copia tras la eliminación: no hay periodo de gracia, ni papelera, ni archivo. Una cuenta eliminada no se puede restaurar, y los datos que contenía se pierden. <strong>Si quieres conservarlos, expórtalos antes</strong> desde Ajustes → <strong>Mis datos</strong> (exportación en JSON o CSV).</p>

  <h2>4. Cancelar una suscripción Premium</h2>
  <p>La cancelación se hace por completo en la plataforma donde te suscribiste, nunca en la aplicación:</p>
  <ul>
    <li><strong>Android</strong>: Play Store → tu perfil → Pagos y suscripciones → Suscripciones → Basal → Cancelar.</li>
    <li><strong>iPhone</strong>: Ajustes del teléfono → tu nombre → Suscripciones → Basal → Cancelar suscripción.</li>
  </ul>
  <p>Eliminar tu cuenta de Basal sin cancelar dejaría que la suscripción se renovara. Haz las dos cosas si es lo que quieres.</p>

  <h2>5. Preguntas</h2>
  <div class="contact">
    <p style="margin:0 0 12px">Para cualquier pregunta sobre la eliminación de tu cuenta o sobre el tratamiento de tus datos: <strong>contact@basal-app.fr</strong></p>
    <p style="margin:0">Lo que se recoge, por qué y dónde, se detalla en la <a href="{u("confidentialite")}">política de privacidad</a>.</p>
  </div>'''
    return f'''  <h1 id="contenu">Konto löschen — Basal</h1>
  <p class="updated">Zuletzt aktualisiert: 7. August 2026</p>

  {av}

  <p>Diese Seite erklärt, wie du dein Konto in der App <strong>Basal</strong> (Ernährungs-, Gewichts-, Stoffwechsel- und Aktivitätstracking) und die damit verbundenen Daten löschst. Es gibt zwei Wege: in der App, oder per E-Mail, wenn du sie nicht mehr hast.</p>

  <div class="note">
    Zur Erinnerung: <strong>Für Basal brauchst du kein Konto.</strong> Wenn du nie eines angelegt hast, gibt es nichts zu löschen – keine deiner Daten hat dein Handy verlassen, und das Deinstallieren der App löscht sie.
  </div>

  <h2>1. In der App (sofort)</h2>
  <ol>
    <li>Öffne Basal.</li>
    <li>Gehe zu <strong>Einstellungen</strong> (das Zahnrad oben rechts in jedem Tab).</li>
    <li>Öffne <strong>Konto</strong> („Konto, Sicherung und Premium-Status“).</li>
    <li>Scrolle bis <strong>„Mein Konto löschen“</strong>.</li>
    <li>Bestätige.</li>
  </ol>
  <p>Die Löschung erfolgt <strong>sofort und endgültig</strong>. Kein Antrag, keine Wartezeit, keine Freigabe durch uns.</p>

  <h2>2. Per E-Mail (wenn du die App nicht mehr hast)</h2>
  <p>Wenn du Basal deinstalliert oder dein Handy gewechselt hast, schreibe an <strong>contact@basal-app.fr</strong> von <strong>der E-Mail-Adresse deines Kontos</strong>, mit dem Betreff <em>„Kontolöschung“</em>.</p>
  <p>Dass du von der Adresse des Kontos schreibst, erlaubt uns zu prüfen, dass die Anfrage wirklich von dir kommt: Das ist der einzige Schutz davor, dass jemand die Löschung des Kontos einer anderen Person verlangt. Wenn du keinen Zugang mehr zu dieser Adresse hast, sag es in deiner Nachricht, und wir suchen einen anderen Weg, dich zu verifizieren.</p>
  <p>Die Anfrage wird innerhalb von <strong>höchstens 30 Tagen</strong> bearbeitet, in der Praxis viel schneller.</p>

  <h2>3. Was gelöscht wird und was nicht</h2>
  <table>
    <tr>
      <th>Daten</th>
      <th>Werden</th>
    </tr>
    <tr>
      <td>Dein Konto und deine E-Mail-Adresse</td>
      <td>endgültig <strong>gelöscht</strong></td>
    </tr>
    <tr>
      <td>Deine auf dem Server gesicherten Daten (Profil, Gewicht, Mahlzeiten, Rezepte, Einheiten, Ziele)</td>
      <td>endgültig <strong>gelöscht</strong></td>
    </tr>
    <tr>
      <td>Die Daten, die auf deinem Handy geblieben sind</td>
      <td><strong>behalten</strong> – die App wird wieder lokal, wie vor dem Anlegen des Kontos. Um auch sie zu löschen, deinstalliere die App oder lösche ihre Daten in den Einstellungen deines Handys.</td>
    </tr>
    <tr>
      <td>Dein Premium-Abo, falls du eines hast</td>
      <td><strong>nicht gekündigt.</strong> Ein Abo gehört zu deinem Google-Play-Konto oder deiner Apple-ID, nicht zu deinem Basal-Konto – wir können es nicht für dich kündigen. Siehe unten.</td>
    </tr>
  </table>
  <p>Nach der Löschung wird keine Kopie aufbewahrt: Es gibt keine Kulanzfrist, keinen Papierkorb, kein Archiv. Ein gelöschtes Konto kann nicht wiederhergestellt werden, und die darin enthaltenen Daten sind verloren. <strong>Wenn du sie behalten willst, exportiere sie vorher</strong> über Einstellungen → <strong>Meine Daten</strong> (Export als JSON oder CSV).</p>

  <h2>4. Ein Premium-Abo kündigen</h2>
  <p>Die Kündigung erfolgt vollständig bei der Plattform, bei der du abgeschlossen hast, nie in der App:</p>
  <ul>
    <li><strong>Android</strong> – Play Store → dein Profil → Zahlungen und Abos → Abos → Basal → Kündigen.</li>
    <li><strong>iPhone</strong> – Einstellungen des Handys → dein Name → Abonnements → Basal → Abo kündigen.</li>
  </ul>
  <p>Dein Basal-Konto zu löschen, ohne zu kündigen, würde das Abo weiterlaufen lassen. Mach beides, wenn du das willst.</p>

  <h2>5. Fragen</h2>
  <div class="contact">
    <p style="margin:0 0 12px">Für alle Fragen zur Löschung deines Kontos oder zur Verarbeitung deiner Daten: <strong>contact@basal-app.fr</strong></p>
    <p style="margin:0">Was erhoben wird, warum und wo, steht in der <a href="{u("confidentialite")}">Datenschutzerklärung</a>.</p>
  </div>'''


META = {'en': ('Delete your account — Basal', 'How to delete your Basal account and the data linked to it, from the app or by email.'),
        'es': ('Eliminar tu cuenta — Basal', 'Cómo eliminar tu cuenta de Basal y los datos asociados, desde la aplicación o por correo electrónico.'),
        'de': ('Konto löschen — Basal', 'Wie du dein Basal-Konto und die damit verbundenen Daten löschst, in der App oder per E-Mail.')}

PAGES = {l: legale(l, C, *META[l], corps(l)) for l in META}
