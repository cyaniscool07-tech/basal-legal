from calcul_macros import ld

FR = '/calcul-1rm.html'
DATE = '2026-11-11'


def main(t):
    return f'''<main id="contenu" class="wrap">
  <nav class="fil" aria-label="{t["fil"]}"><a href="{t["accueil_url"]}">{t["accueil"]}</a><span aria-hidden="true">›</span><a href="{t["hub_url"]}">{t["hub"]}</a><span aria-hidden="true">›</span>1RM</nav>
  <header class="article-tete" style="border:0;padding-bottom:0">
    <p class="surtitre">{t["surtitre"]}</p>
    <h1>{t["h1"]}</h1>
    <p class="chapeau">{t["chapeau"]}</p>
  </header>

  <div class="outil">
    <form class="carte" id="calc" novalidate>
      <div class="champs">
        <div class="champ"><label for="charge">{t["charge"]}</label><input id="charge" type="number" inputmode="decimal" step="0.5" min="1" max="500" placeholder="80"></div>
        <div class="champ"><label for="reps">{t["reps"]}</label><input id="reps" type="number" inputmode="numeric" min="1" max="30" placeholder="8"></div>
        <p class="aide large" style="margin:0">{t["aide"]}</p>
      </div>
    </form>

    <section class="carte resultat" aria-live="polite" aria-labelledby="res-t">
      <p class="surtitre" id="res-t">{t["res"]}</p>
      <div class="grand"><span id="rm" data-flottant="{t["res"]}">—</span><small>kg</small></div>
      <p id="message" style="margin:14px 0 0">{t["vide"]}</p>
      <p id="alerte" hidden style="margin:14px 0 0;color:#fb923c">{t["alerte"]}</p>
    </section>
  </div>

  <div class="article" style="grid-template-columns:minmax(0,1fr);padding-top:56px">
    <div class="corps">
{t["corps"]}
      <div class="appel-contexte">
        <div><strong>{t["appel_t"]}</strong><p>{t["appel"]}</p></div>
        <a class="bouton vif" href="{t["accueil_url"]}#download">{t["dl"]}</a>
      </div>
    </div>
  </div>

  <aside class="note-page">
    <p>{t["note"]}</p>
  </aside>
</main>'''


def script(locale, vide, bornes, table_vide):
    return [
        ("'Renseigne la charge et le nombre de répétitions.'", repr(vide)),
        ("'Vérifie les valeurs : charge de 1 à 500 kg, de 1 à 30 répétitions entières.'", repr(bornes)),
        ("'<tr><td colspan=\"3\" class=\"vide\">Le tableau se remplit avec ton résultat.</td></tr>'", "'<tr><td colspan=\"3\" class=\"vide\">" + table_vide + "</td></tr>'"),
        ("'fr-FR'", repr(locale)),
    ]


def tableau(t):
    return f'''      <h2>{t[0]}</h2>
      <div class="tableau">
        <table>
          <caption>{t[1]}</caption>
          <thead><tr><th scope="col">{t[2]}</th><th scope="col" class="n">{t[3]}</th><th scope="col" class="n">{t[4]}</th></tr></thead>
          <tbody id="table-charges"><tr><td colspan="3" class="vide">{t[5]}</td></tr></tbody>
        </table>
        <p class="source">{t[6]}</p>
      </div>
'''


PAGES = {
    'en': {
        'slug': '/en/one-rep-max-calculator.html',
        'tete': dict(title='One-rep max (1RM) calculator, Epley formula | Basal', locale='en_GB',
                     description='Estimate your one-rep max (1RM) from a set, with the Epley formula used by the Basal app, plus your loads from 1 to 12 reps.',
                     og_title='One-rep max (1RM) calculator', og_description='Your estimated maximum from a set you actually did, with the Epley formula.'),
        'main': main(dict(fil='Breadcrumb', accueil='Home', accueil_url='/en/', hub='Calculators', hub_url='/en/calculators/', surtitre='Free calculator',
            h1='Work out your 1RM, the most you can lift for one rep',
            chapeau='Your estimated maximum load from a set you actually did, without testing a max. It is the Epley formula, the one the Basal app uses to track your progress. Nothing is sent.',
            charge='Weight lifted (kg)', reps='Reps', aide='Use a set taken close to failure, with clean technique. A set of a single rep is already your maximum: the calculation keeps it as is.',
            res='Your estimated 1RM', vide='Enter the weight and the number of reps.', alerte='Above about ten reps, the estimate becomes less reliable: fatigue and endurance weigh more than strength.',
            corps=tableau(['Your loads from 1 to 12 reps', 'Loads estimated from your 1RM', 'Reps', 'Estimated load', 'Share of 1RM', 'The table fills in with your result.',
                           'Reverse Epley formula: load = 1RM ÷ (1 + reps ÷ 30). Rounded to 0.5 kg.']) + '''
      <h2>The calculation in detail</h2>
      <p class="formule"><code>1RM ≈ load × (1 + reps ÷ 30)</code></p>
      <div class="calcul" role="group" aria-label="Example">
        <div class="titre">Example: 80 kg lifted 8 times</div>
        <div class="ligne"><span>80 × (1 + 8 ÷ 30)</span><b>101.3 kg</b></div>
        <div class="ligne"><span>100 kg lifted once: already a real maximum, kept as is</span><b>100 kg</b></div>
      </div>
      <p>The Epley formula (1985) is the most widely used. At one rep it would return 1.033 times the load, although the load lifted is already the maximum: the app and this calculator therefore keep it as is, rather than inflating a real record by 3%.</p>

      <h2>What it is for</h2>
      <p>An estimated 1RM lets you compare sessions with different rep counts: 80 kg for 8 and 90 kg for 4 give almost the same 1RM (101.3 and 102 kg). That is how the app tracks an exercise’s progress from one week to the next.</p>

      <h2>What this calculation does not know</h2>
      <div class="inconnu">
        <p><strong>It is an estimate.</strong> The link between reps and maximum load varies with the exercise, your training and the day’s fatigue.</p>
        <p style="margin:0"><strong>It is not an invitation to test your max.</strong> A one-rep attempt is done warmed up, with controlled technique, and with a spotter or safeties on exercises that need them.</p>
      </div>
''', appel_t='Your progress, session after session', appel='Basal logs your sets and loads, calculates your estimated 1RM for each exercise and shows your records next to your weight trend.',
            dl='Download', note='This tool is for information only. Basal is not a medical device and does not replace advice from a health professional or a coach.')),
        'script': script('en-GB', 'Enter the weight and the number of reps.', 'Check the values: load from 1 to 500 kg, 1 to 30 whole reps.', 'The table fills in with your result.'),
        'ld': ld('One-rep max (1RM) calculator', '/en/one-rep-max-calculator.html', 'Estimated one-rep max from a set, Epley formula, with loads from 1 to 12 reps.', 'en',
                 '/en/', 'Home', '/en/calculators/', 'Calculators', '1RM'),
    },
    'es': {
        'slug': '/es/calculadora-1rm.html',
        'tete': dict(title='Calculadora de 1RM, carga máxima (fórmula de Epley) | Basal', locale='es_ES',
                     description='Estima tu carga máxima en una repetición (1RM) a partir de una serie, con la fórmula de Epley de la aplicación Basal, y tus cargas de 1 a 12 repeticiones.',
                     og_title='Calculadora de 1RM, carga máxima', og_description='Tu carga máxima estimada a partir de una serie que has hecho de verdad, con la fórmula de Epley.'),
        'main': main(dict(fil='Ruta de navegación', accueil='Inicio', accueil_url='/es/', hub='Calculadoras', hub_url='/es/calculadoras/', surtitre='Calculadora gratis',
            h1='Calcula tu 1RM, la carga máxima en una repetición',
            chapeau='Tu carga máxima estimada a partir de una serie que has hecho de verdad, sin intentar un máximo. Es la fórmula de Epley, la que usa la aplicación Basal para seguir tu progresión. No se envía nada.',
            charge='Carga levantada (kg)', reps='Repeticiones', aide='Usa una serie llevada cerca del fallo, con técnica limpia. Una serie de una sola repetición ya es tu máximo: el cálculo la mantiene tal cual.',
            res='Tu 1RM estimado', vide='Indica la carga y el número de repeticiones.', alerte='Por encima de unas diez repeticiones, la estimación es menos fiable: la fatiga y la resistencia pesan más que la fuerza.',
            corps=tableau(['Tus cargas de 1 a 12 repeticiones', 'Cargas estimadas a partir de tu 1RM', 'Repeticiones', 'Carga estimada', 'Parte del 1RM', 'La tabla se rellena con tu resultado.',
                           'Fórmula de Epley invertida: carga = 1RM ÷ (1 + repeticiones ÷ 30). Redondeado a 0,5 kg.']) + '''
      <h2>El detalle del cálculo</h2>
      <p class="formule"><code>1RM ≈ carga × (1 + repeticiones ÷ 30)</code></p>
      <div class="calcul" role="group" aria-label="Ejemplo">
        <div class="titre">Ejemplo: 80 kg levantados 8 veces</div>
        <div class="ligne"><span>80 × (1 + 8 ÷ 30)</span><b>101,3 kg</b></div>
        <div class="ligne"><span>100 kg levantados 1 vez: ya es un máximo real, se mantiene tal cual</span><b>100 kg</b></div>
      </div>
      <p>La fórmula de Epley (1985) es la más extendida. Con una repetición devolvería 1,033 veces la carga, aunque la carga levantada ya es el máximo: la aplicación y esta calculadora la mantienen tal cual, en lugar de inflar un récord real un 3 %.</p>

      <h2>Para qué sirve</h2>
      <p>Un 1RM estimado permite comparar sesiones con distinto número de repeticiones: 80 kg por 8 y 90 kg por 4 dan casi el mismo 1RM (101,3 y 102 kg). Así es como la aplicación sigue la progresión de un ejercicio de una semana a otra.</p>

      <h2>Lo que este cálculo no sabe</h2>
      <div class="inconnu">
        <p><strong>Es una estimación.</strong> La relación entre repeticiones y carga máxima varía según el ejercicio, el entrenamiento y el cansancio del día.</p>
        <p style="margin:0"><strong>No es una invitación a probar tu máximo.</strong> Un intento a una repetición se hace bien calentado, con técnica dominada y con un compañero o seguros en los ejercicios que lo requieren.</p>
      </div>
''', appel_t='Tu progresión, sesión tras sesión', appel='Basal registra tus series y tus cargas, calcula tu 1RM estimado para cada ejercicio y muestra tus récords junto a la tendencia de tu peso.',
            dl='Descargar', note='Esta herramienta es informativa. Basal no es un dispositivo médico y no sustituye el consejo de un profesional sanitario o de un entrenador.')),
        'script': script('es-ES', 'Indica la carga y el número de repeticiones.', 'Revisa los valores: carga de 1 a 500 kg, de 1 a 30 repeticiones enteras.', 'La tabla se rellena con tu resultado.'),
        'ld': ld('Calculadora de 1RM, carga máxima', '/es/calculadora-1rm.html', 'Carga máxima estimada en una repetición a partir de una serie, fórmula de Epley, con cargas de 1 a 12 repeticiones.', 'es',
                 '/es/', 'Inicio', '/es/calculadoras/', 'Calculadoras', '1RM'),
    },
    'de': {
        'slug': '/de/1rm-rechner.html',
        'tete': dict(title='1RM-Rechner: Maximalkraft berechnen (Epley-Formel) | Basal', locale='de_DE',
                     description='Schätze dein One-Rep-Max (1RM) aus einem Satz, mit der Epley-Formel der Basal-App, und deine Gewichte für 1 bis 12 Wiederholungen.',
                     og_title='1RM-Rechner: Maximalkraft berechnen', og_description='Dein geschätztes Maximalgewicht aus einem Satz, den du wirklich gemacht hast, mit der Epley-Formel.'),
        'main': main(dict(fil='Brotkrümelnavigation', accueil='Startseite', accueil_url='/de/', hub='Rechner', hub_url='/de/rechner/', surtitre='Kostenloser Rechner',
            h1='1RM berechnen, das Maximalgewicht für eine Wiederholung',
            chapeau='Dein geschätztes Maximalgewicht aus einem Satz, den du wirklich gemacht hast, ohne ein Maximum zu testen. Es ist die Epley-Formel, die auch die Basal-App für deinen Fortschritt nutzt. Es wird nichts gesendet.',
            charge='Bewegtes Gewicht (kg)', reps='Wiederholungen', aide='Nimm einen Satz nahe am Muskelversagen, mit sauberer Technik. Ein Satz mit einer einzigen Wiederholung ist bereits dein Maximum: Die Berechnung übernimmt ihn unverändert.',
            res='Dein geschätztes 1RM', vide='Gib Gewicht und Anzahl der Wiederholungen ein.', alerte='Ab etwa zehn Wiederholungen wird die Schätzung ungenauer: Ermüdung und Ausdauer zählen dann mehr als Kraft.',
            corps=tableau(['Deine Gewichte für 1 bis 12 Wiederholungen', 'Aus deinem 1RM geschätzte Gewichte', 'Wiederholungen', 'Geschätztes Gewicht', 'Anteil am 1RM', 'Die Tabelle füllt sich mit deinem Ergebnis.',
                           'Umgekehrte Epley-Formel: Gewicht = 1RM ÷ (1 + Wiederholungen ÷ 30). Auf 0,5 kg gerundet.']) + '''
      <h2>Die Berechnung im Detail</h2>
      <p class="formule"><code>1RM ≈ Gewicht × (1 + Wiederholungen ÷ 30)</code></p>
      <div class="calcul" role="group" aria-label="Beispiel">
        <div class="titre">Beispiel: 80 kg, 8-mal bewegt</div>
        <div class="ligne"><span>80 × (1 + 8 ÷ 30)</span><b>101,3 kg</b></div>
        <div class="ligne"><span>100 kg, 1-mal bewegt: bereits ein echtes Maximum, unverändert übernommen</span><b>100 kg</b></div>
      </div>
      <p>Die Epley-Formel (1985) ist die verbreitetste. Bei einer Wiederholung ergäbe sie das 1,033-Fache des Gewichts, obwohl das bewegte Gewicht bereits das Maximum ist: Die App und dieser Rechner übernehmen es deshalb unverändert, statt einen echten Rekord um 3 % aufzublähen.</p>

      <h2>Wofür es gut ist</h2>
      <p>Ein geschätztes 1RM macht Einheiten mit unterschiedlicher Wiederholungszahl vergleichbar: 80 kg für 8 und 90 kg für 4 ergeben fast dasselbe 1RM (101,3 und 102 kg). So verfolgt die App den Fortschritt einer Übung von Woche zu Woche.</p>

      <h2>Was diese Berechnung nicht weiß</h2>
      <div class="inconnu">
        <p><strong>Es ist eine Schätzung.</strong> Das Verhältnis von Wiederholungen zu Maximalgewicht hängt von der Übung, dem Training und der Tagesform ab.</p>
        <p style="margin:0"><strong>Es ist keine Aufforderung, dein Maximum zu testen.</strong> Ein Versuch mit einer Wiederholung gehört aufgewärmt, mit sicherer Technik und mit Sicherung oder Ablagen bei den Übungen, die das verlangen.</p>
      </div>
''', appel_t='Dein Fortschritt, Einheit für Einheit', appel='Basal speichert deine Sätze und Gewichte, berechnet dein geschätztes 1RM für jede Übung und zeigt deine Rekorde neben dem Verlauf deines Gewichts.',
            dl='Herunterladen', note='Dieses Werkzeug dient nur der Information. Basal ist kein Medizinprodukt und ersetzt nicht den Rat medizinischen Fachpersonals oder eines Trainers.')),
        'script': script('de-DE', 'Gib Gewicht und Anzahl der Wiederholungen ein.', 'Prüfe die Werte: Gewicht von 1 bis 500 kg, 1 bis 30 ganze Wiederholungen.', 'Die Tabelle füllt sich mit deinem Ergebnis.'),
        'ld': ld('1RM-Rechner: Maximalkraft berechnen', '/de/1rm-rechner.html', 'Geschätztes One-Rep-Max aus einem Satz, Epley-Formel, mit Gewichten für 1 bis 12 Wiederholungen.', 'de',
                 '/de/', 'Startseite', '/de/rechner/', 'Rechner', '1RM'),
    },
}
