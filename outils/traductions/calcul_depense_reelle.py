from calcul_macros import ld

FR = '/calcul-depense-reelle.html'
DATE = '2026-11-11'


def main(t):
    niveaux = ''.join(f'\n                <option value="{v}"{" selected" if v == "1.55" else ""}>{x}</option>' for v, x in zip(['1.2', '1.375', '1.55', '1.725', '1.9'], t['niveaux']))
    return f'''<main id="contenu" class="wrap">
  <nav class="fil" aria-label="{t["fil"]}"><a href="{t["accueil_url"]}">{t["accueil"]}</a><span aria-hidden="true">›</span><a href="{t["hub_url"]}">{t["hub"]}</a><span aria-hidden="true">›</span>{t["court"]}</nav>
  <header class="article-tete" style="border:0;padding-bottom:0">
    <p class="surtitre">{t["surtitre"]}</p>
    <h1>{t["h1"]}</h1>
    <p class="chapeau">{t["chapeau"]}</p>
  </header>

  <div class="outil">
    <form class="carte" id="calc" novalidate>
      <div class="champs">
        <div class="champ large">
          <label for="apport">{t["apport"]}</label>
          <input id="apport" type="number" inputmode="numeric" min="500" max="8000" placeholder="2100">
          <span class="aide">{t["apport_aide"]}</span>
        </div>
        <div class="champ"><label for="debut">{t["debut"]}</label><input id="debut" type="number" inputmode="decimal" step="0.1" min="30" max="300" placeholder="{t["ph_debut"]}"></div>
        <div class="champ"><label for="fin">{t["fin"]}</label><input id="fin" type="number" inputmode="decimal" step="0.1" min="30" max="300" placeholder="{t["ph_fin"]}"></div>
        <div class="champ"><label for="jours">{t["jours"]}</label><input id="jours" type="number" inputmode="numeric" min="1" max="365" placeholder="21"></div>
        <p class="aide large" style="margin:0">{t["pesee"]}</p>
        <details class="champ large">
          <summary>{t["comparer"]}</summary>
          <div class="champs" style="margin-top:14px">
            <div class="champ large">
              <span id="sexe-t" style="font-weight:600;font-size:.9rem">{t["sexe"]}</span>
              <div class="segment" role="radiogroup" aria-labelledby="sexe-t">
                <input type="radio" name="sexe" id="h" value="h" checked><label for="h">{t["homme"]}</label>
                <input type="radio" name="sexe" id="f" value="f"><label for="f">{t["femme"]}</label>
              </div>
            </div>
            <div class="champ"><label for="age">{t["age"]}</label><input id="age" type="number" inputmode="numeric" min="18" max="100" placeholder="30"></div>
            <div class="champ"><label for="taille">{t["taille"]}</label><input id="taille" type="number" inputmode="numeric" min="120" max="230" placeholder="175"></div>
            <div class="champ">
              <label for="activite">{t["activite"]}</label>
              <select id="activite">{niveaux}
              </select>
            </div>
          </div>
        </details>
      </div>
    </form>

    <section class="carte resultat" aria-live="polite" aria-labelledby="res-t">
      <p class="surtitre" id="res-t">{t["res"]}</p>
      <div class="grand"><span id="depense" data-flottant="{t["flottant"]}">—</span><small>{t["kcaljour"]}</small></div>
      <p id="message" style="margin:14px 0 0">{t["vide"]}</p>
      <div id="sortie" hidden>
        <div class="sous">
          <div><b id="s-maintien">—</b><span>{t["maintien"]}</span></div>
          <div><b id="s-perte">—</b><span id="s-perte-t">{t["perte"]}</span></div>
        </div>
        <p id="comparaison" hidden style="margin:0 0 8px"></p>
        <p id="alerte" hidden style="margin:0;color:#fb923c"></p>
      </div>
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


def script(locale, s):
    """s : dict des textes traduits du script."""
    return [
        ("'Renseigne les quatre premiers champs pour voir le résultat.'", repr(s['vide'])),
        ("'Une des valeurs sort des bornes plausibles : vérifie l’apport (500 à 8 000 kcal) et les poids (30 à 300 kg).'", repr(s['bornes'])),
        ("'Il faut au moins ' + JOURS_MIN + ' jours entre les deux moyennes : en dessous, l’eau et le sel pèsent plus que la graisse.'",
         f"{s['min_a']!r} + JOURS_MIN + {s['min_b']!r}"),
        ("'Basal est réservée aux personnes majeures et ne calcule pas de besoins caloriques avant 18 ans : à cet âge, ils se déterminent avec un professionnel de santé.'", repr(s['majeur'])),
        ("'pas d’objectif de perte : la dépense mesurée est sous le plancher de sécurité, signe probable d’un journal incomplet'", repr(s['sous_plancher'])),
        ("'pour perdre : relevé au plancher de sécurité'", repr(s['releve'])),
        ("'pour perdre à un rythme modéré (− 15 %)'", repr(s['perte'])),
        ("'La formule annonçait ' + nb(formule) + ' kcal : ta dépense réelle est ' + (ecart >= 0 ? 'supérieure' : 'inférieure') + ' de ' + Math.abs(Math.round(ecart)) + ' %.'",
         f"{s['cmp_a']!r} + nb(formule) + {s['cmp_b']!r} + (ecart >= 0 ? {s['sup']!r} : {s['inf']!r}) + {s['cmp_c']!r} + Math.abs(Math.round(ecart)) + {s['cmp_d']!r}"),
        ("'Cet écart sort des bornes que l’application accepte (0,8 à 1,6 fois la formule). La cause la plus fréquente est un journal incomplet.'", repr(s['ecart'])),
        ("'Variation : ' + dec(fin)", f"{s['variation']!r} + dec(fin)"),
        ("' kg en ' + jours + ' jours'", f"{s['en_a']!r} + jours + {s['en_b']!r}"),
        ("' kcal / jour'", repr(s['kcaljour'])),
        ("' × 7 700 ÷ '", repr(s['x7700'])),
        ("'fr-FR'", repr(locale)),
    ]


T_EN = dict(fil='Breadcrumb', accueil='Home', accueil_url='/en/', hub='Calculators', hub_url='/en/calculators/', court='Real expenditure', surtitre='Free calculator',
    h1='Work out your real expenditure from your weight',
    chapeau='A formula guesses your expenditure from your age, height and weight. Here it is worked out from what you actually ate and how your weight changed: the method the Basal app uses. The calculation runs in your browser, nothing is sent.',
    apport='Average intake (kcal per day)', apport_aide='The average of your calories over the whole period, counting only the days you logged everything.',
    debut='Starting weight (kg)', fin='End weight (kg)', ph_debut='80.0', ph_fin='79.4', jours='Days between the two',
    pesee='Weigh yourself every morning. The starting weight is the average of your first week, the end weight the average of your last: 4 weeks of tracking give 21 days between them.',
    comparer='Compare with the formula (optional)', sexe='Sex', homme='Male', femme='Female', age='Age', taille='Height (cm)', activite='Activity',
    niveaux=['Sedentary', 'Lightly active', 'Moderately active', 'Active', 'Very active'], res='Your estimated real expenditure', flottant='Real expenditure', kcaljour='kcal / day',
    vide='Fill in the first four fields to see the result.', maintien='to maintain your weight', perte='to lose at a moderate pace (− 15%)',
    corps='''      <h2>The calculation in detail</h2>
      <p class="formule"><code>expenditure = average intake − (end weight − starting weight) × 7,700 ÷ days</code></p>
      <p>One kilogram of body mass represents about 7,700 kcal. If you lost weight, you spent more than you ate: the difference, spread per day, is added to your intake.</p>
      <div class="calcul" role="group" aria-label="The calculation with your values">
        <div class="ligne"><span>Average intake</span><b id="d-apport">2,100 kcal</b></div>
        <div class="ligne"><span id="d-var-t">Change: 79.4 − 80.0 = − 0.6 kg in 21 days</span><b id="d-var">− 0.6 kg</b></div>
        <div class="ligne"><span id="d-jour-t">− 0.6 × 7,700 ÷ 21</span><b id="d-jour">− 220 kcal / day</b></div>
        <div class="ligne total"><span>Real expenditure: average intake minus this change</span><b id="d-total">2,320 kcal / day</b></div>
      </div>
      <p>The example above is the one the tool shows until you enter your own values.</p>

      <h2>Why it is more accurate than a formula</h2>
      <p>A formula like Mifflin-St Jeor gives the average expenditure of people who resemble you on four criteria, with a typical error of about 10%. Your weight, on the other hand, reacts to what you actually spend. Over a few weeks, it tells you whether your intake was above or below your expenditure, and by how much.</p>

      <h2>Measuring well</h2>
      <ul class="liste">
        <li>Weigh yourself every morning, under the same conditions, and average by week: a single day’s weight moves by several hundred grams with water and salt.</li>
        <li>Log everything you eat, including the off days. Forgotten meals make your expenditure look lower than it is.</li>
        <li>Count at least three to four weeks. Below 10 days, the tool refuses to calculate: noise outweighs the signal.</li>
      </ul>

      <h2>What this calculation does not know</h2>
      <div class="inconnu">
        <p><strong>The start of a diet skews the calculation.</strong> In the first days the body mostly loses water and glycogen, far lighter in calories than fat. Measuring from the second week avoids overestimating your expenditure.</p>
        <p><strong>It is only as good as your log.</strong> A steady 200 kcal error in your meals ends up as is in the result.</p>
        <p style="margin:0"><strong>It is not medical advice.</strong> An expenditure far from what you would expect can have a cause worth showing a doctor.</p>
      </div>
''', appel_t='The same calculation, every week', appel='Basal redoes it at every weigh-in, with your logged meals: rolling weight average, plausibility bounds and gradual adjustment.',
    dl='Download', note='This tool is for information only. Basal is not a medical device and does not replace advice from a health professional.')

S_EN = dict(vide='Fill in the first four fields to see the result.', bornes='One of the values is outside plausible bounds: check the intake (500 to 8,000 kcal) and the weights (30 to 300 kg).',
    min_a='You need at least ', min_b=' days between the two averages: below that, water and salt weigh more than fat.',
    majeur='Basal is for adults only and does not calculate calorie needs under 18: at that age, they should be set with a health professional.',
    sous_plancher='no weight-loss target: the measured expenditure is below the safety floor, probably a sign of an incomplete log',
    releve='to lose: raised to the safety floor', perte='to lose at a moderate pace (− 15%)',
    cmp_a='The formula predicted ', cmp_b=' kcal: your real expenditure is ', sup='higher', inf='lower', cmp_c=' by ', cmp_d='%.',
    ecart='This gap is outside the bounds the app accepts (0.8 to 1.6 times the formula). The most common cause is an incomplete log.',
    variation='Change: ', en_a=' kg in ', en_b=' days', kcaljour=' kcal / day', x7700=' × 7,700 ÷ ')

T_ES = dict(fil='Ruta de navegación', accueil='Inicio', accueil_url='/es/', hub='Calculadoras', hub_url='/es/calculadoras/', court='Gasto real', surtitre='Calculadora gratis',
    h1='Calcula tu gasto real a partir de tu peso',
    chapeau='Una fórmula adivina tu gasto a partir de tu edad, tu altura y tu peso. Aquí se deduce de lo que has comido de verdad y de la evolución de tu peso: es el método que usa la aplicación Basal. El cálculo se hace en tu navegador, no se envía nada.',
    apport='Ingesta media (kcal al día)', apport_aide='La media de tus calorías en todo el periodo, contando solo los días en que lo registraste todo.',
    debut='Peso inicial (kg)', fin='Peso final (kg)', ph_debut='80,0', ph_fin='79,4', jours='Días entre ambos',
    pesee='Pésate cada mañana. El peso inicial es la media de tu primera semana y el final la media de la última: 4 semanas de seguimiento dan 21 días entre ambos.',
    comparer='Comparar con la fórmula (opcional)', sexe='Sexo', homme='Hombre', femme='Mujer', age='Edad', taille='Altura (cm)', activite='Actividad',
    niveaux=['Sedentario', 'Ligeramente activo', 'Moderadamente activo', 'Activo', 'Muy activo'], res='Tu gasto real estimado', flottant='Gasto real', kcaljour='kcal / día',
    vide='Rellena los cuatro primeros campos para ver el resultado.', maintien='para mantener tu peso', perte='para perder a un ritmo moderado (− 15 %)',
    corps='''      <h2>El detalle del cálculo</h2>
      <p class="formule"><code>gasto = ingesta media − (peso final − peso inicial) × 7.700 ÷ días</code></p>
      <p>Un kilo de masa corporal representa unas 7.700 kcal. Si has perdido peso, has gastado más de lo que has comido: la diferencia, repartida por día, se suma a tu ingesta.</p>
      <div class="calcul" role="group" aria-label="El cálculo con tus valores">
        <div class="ligne"><span>Ingesta media</span><b id="d-apport">2.100 kcal</b></div>
        <div class="ligne"><span id="d-var-t">Variación: 79,4 − 80,0 = − 0,6 kg en 21 días</span><b id="d-var">− 0,6 kg</b></div>
        <div class="ligne"><span id="d-jour-t">− 0,6 × 7.700 ÷ 21</span><b id="d-jour">− 220 kcal / día</b></div>
        <div class="ligne total"><span>Gasto real: ingesta media menos esta variación</span><b id="d-total">2.320 kcal / día</b></div>
      </div>
      <p>El ejemplo de arriba es el que muestra la herramienta mientras no introduces tus valores.</p>

      <h2>Por qué es más exacto que una fórmula</h2>
      <p>Una fórmula como Mifflin-St Jeor da el gasto medio de las personas que se parecen a ti en cuatro criterios, con un error habitual de un 10 %. Tu peso, en cambio, reacciona a lo que gastas de verdad. En unas semanas, dice si tu ingesta estaba por encima o por debajo de tu gasto, y cuánto.</p>

      <h2>Medir bien</h2>
      <ul class="liste">
        <li>Pésate cada mañana, en las mismas condiciones, y haz la media por semana: el peso de un día varía varios cientos de gramos con el agua y la sal.</li>
        <li>Registra todo lo que comes, incluidos los días malos. Las comidas olvidadas hacen creer que el gasto es más bajo de lo que es.</li>
        <li>Cuenta al menos tres o cuatro semanas. Por debajo de 10 días, la herramienta no calcula: el ruido supera a la señal.</li>
      </ul>

      <h2>Lo que este cálculo no sabe</h2>
      <div class="inconnu">
        <p><strong>El inicio de una dieta falsea el cálculo.</strong> Los primeros días, el cuerpo pierde sobre todo agua y glucógeno, mucho más ligeros en calorías que la grasa. Medir a partir de la segunda semana evita sobrestimar tu gasto.</p>
        <p><strong>Solo vale lo que vale tu registro.</strong> Un error constante de 200 kcal en tus comidas se traslada tal cual al resultado.</p>
        <p style="margin:0"><strong>No es un consejo médico.</strong> Un gasto muy alejado de lo esperado puede tener una causa que conviene consultar con un médico.</p>
      </div>
''', appel_t='El mismo cálculo, cada semana', appel='Basal lo rehace en cada pesada, con tus comidas registradas: media móvil del peso, límites de plausibilidad y ajuste progresivo.',
    dl='Descargar', note='Esta herramienta es informativa. Basal no es un dispositivo médico y no sustituye el consejo de un profesional sanitario.')

S_ES = dict(vide='Rellena los cuatro primeros campos para ver el resultado.', bornes='Uno de los valores está fuera de los límites plausibles: revisa la ingesta (500 a 8.000 kcal) y los pesos (30 a 300 kg).',
    min_a='Hacen falta al menos ', min_b=' días entre las dos medias: por debajo, el agua y la sal pesan más que la grasa.',
    majeur='Basal está reservada a personas mayores de edad y no calcula necesidades calóricas antes de los 18 años: a esa edad se determinan con un profesional de la salud.',
    sous_plancher='sin objetivo de pérdida: el gasto medido está por debajo del mínimo de seguridad, probablemente por un registro incompleto',
    releve='para perder: subido al mínimo de seguridad', perte='para perder a un ritmo moderado (− 15 %)',
    cmp_a='La fórmula anunciaba ', cmp_b=' kcal: tu gasto real es ', sup='superior', inf='inferior', cmp_c=' en un ', cmp_d=' %.',
    ecart='Esta diferencia está fuera de los límites que acepta la aplicación (0,8 a 1,6 veces la fórmula). La causa más frecuente es un registro incompleto.',
    variation='Variación: ', en_a=' kg en ', en_b=' días', kcaljour=' kcal / día', x7700=' × 7.700 ÷ ')

T_DE = dict(fil='Brotkrümelnavigation', accueil='Startseite', accueil_url='/de/', hub='Rechner', hub_url='/de/rechner/', court='Tatsächlicher Verbrauch', surtitre='Kostenloser Rechner',
    h1='Tatsächlichen Verbrauch aus dem Gewicht berechnen',
    chapeau='Eine Formel schätzt deinen Verbrauch aus Alter, Größe und Gewicht. Hier wird er aus dem abgeleitet, was du wirklich gegessen hast, und aus dem Verlauf deines Gewichts: die Methode der Basal-App. Die Berechnung läuft in deinem Browser, es wird nichts gesendet.',
    apport='Durchschnittliche Zufuhr (kcal pro Tag)', apport_aide='Der Durchschnitt deiner Kalorien über den ganzen Zeitraum, nur mit den Tagen, an denen du alles eingetragen hast.',
    debut='Anfangsgewicht (kg)', fin='Endgewicht (kg)', ph_debut='80,0', ph_fin='79,4', jours='Tage dazwischen',
    pesee='Wiege dich jeden Morgen. Das Anfangsgewicht ist der Durchschnitt deiner ersten Woche, das Endgewicht der deiner letzten: 4 Wochen Tracking ergeben 21 Tage dazwischen.',
    comparer='Mit der Formel vergleichen (optional)', sexe='Geschlecht', homme='Mann', femme='Frau', age='Alter', taille='Größe (cm)', activite='Aktivität',
    niveaux=['Sitzend', 'Leicht aktiv', 'Mäßig aktiv', 'Aktiv', 'Sehr aktiv'], res='Dein geschätzter tatsächlicher Verbrauch', flottant='Tatsächlicher Verbrauch', kcaljour='kcal / Tag',
    vide='Fülle die ersten vier Felder aus, um das Ergebnis zu sehen.', maintien='um dein Gewicht zu halten', perte='um in moderatem Tempo abzunehmen (− 15 %)',
    corps='''      <h2>Die Berechnung im Detail</h2>
      <p class="formule"><code>Verbrauch = durchschnittliche Zufuhr − (Endgewicht − Anfangsgewicht) × 7.700 ÷ Tage</code></p>
      <p>Ein Kilogramm Körpermasse entspricht etwa 7.700 kcal. Hast du abgenommen, hast du mehr verbraucht als gegessen: Die Differenz, auf den Tag umgerechnet, kommt zu deiner Zufuhr hinzu.</p>
      <div class="calcul" role="group" aria-label="Die Berechnung mit deinen Werten">
        <div class="ligne"><span>Durchschnittliche Zufuhr</span><b id="d-apport">2.100 kcal</b></div>
        <div class="ligne"><span id="d-var-t">Veränderung: 79,4 − 80,0 = − 0,6 kg in 21 Tagen</span><b id="d-var">− 0,6 kg</b></div>
        <div class="ligne"><span id="d-jour-t">− 0,6 × 7.700 ÷ 21</span><b id="d-jour">− 220 kcal / Tag</b></div>
        <div class="ligne total"><span>Tatsächlicher Verbrauch: Zufuhr minus diese Veränderung</span><b id="d-total">2.320 kcal / Tag</b></div>
      </div>
      <p>Das Beispiel oben zeigt das Werkzeug, solange du keine eigenen Werte eingibst.</p>

      <h2>Warum das genauer ist als eine Formel</h2>
      <p>Eine Formel wie Mifflin-St Jeor liefert den durchschnittlichen Verbrauch von Menschen, die dir in vier Merkmalen ähneln, mit einem üblichen Fehler von etwa 10 %. Dein Gewicht dagegen reagiert auf das, was du wirklich verbrauchst. Über einige Wochen zeigt es, ob deine Zufuhr über oder unter deinem Verbrauch lag, und um wie viel.</p>

      <h2>Richtig messen</h2>
      <ul class="liste">
        <li>Wiege dich jeden Morgen unter gleichen Bedingungen und bilde Wochendurchschnitte: Das Gewicht eines Tages schwankt mit Wasser und Salz um mehrere hundert Gramm.</li>
        <li>Trage alles ein, was du isst, auch an misslungenen Tagen. Vergessene Mahlzeiten lassen den Verbrauch niedriger erscheinen, als er ist.</li>
        <li>Rechne mit mindestens drei bis vier Wochen. Unter 10 Tagen rechnet das Werkzeug nicht: Das Rauschen überwiegt das Signal.</li>
      </ul>

      <h2>Was diese Berechnung nicht weiß</h2>
      <div class="inconnu">
        <p><strong>Der Beginn einer Diät verfälscht die Rechnung.</strong> In den ersten Tagen verliert der Körper vor allem Wasser und Glykogen, kalorisch viel leichter als Fett. Ab der zweiten Woche zu messen verhindert, deinen Verbrauch zu überschätzen.</p>
        <p><strong>Sie ist nur so gut wie dein Tagebuch.</strong> Ein gleichbleibender Fehler von 200 kcal bei deinen Mahlzeiten landet unverändert im Ergebnis.</p>
        <p style="margin:0"><strong>Es ist kein ärztlicher Rat.</strong> Ein Verbrauch weit weg vom Erwarteten kann eine Ursache haben, die ein Arzt ansehen sollte.</p>
      </div>
''', appel_t='Dieselbe Rechnung, jede Woche', appel='Basal rechnet sie bei jedem Wiegen neu, mit deinen eingetragenen Mahlzeiten: gleitender Gewichtsdurchschnitt, Plausibilitätsgrenzen und schrittweise Anpassung.',
    dl='Herunterladen', note='Dieses Werkzeug dient nur der Information. Basal ist kein Medizinprodukt und ersetzt nicht den Rat medizinischen Fachpersonals.')

S_DE = dict(vide='Fülle die ersten vier Felder aus, um das Ergebnis zu sehen.', bornes='Einer der Werte liegt außerhalb plausibler Grenzen: Prüfe die Zufuhr (500 bis 8.000 kcal) und die Gewichte (30 bis 300 kg).',
    min_a='Es braucht mindestens ', min_b=' Tage zwischen den beiden Durchschnitten: Darunter wiegen Wasser und Salz mehr als Fett.',
    majeur='Basal ist Volljährigen vorbehalten und berechnet vor 18 Jahren keinen Kalorienbedarf: In diesem Alter bestimmt man ihn mit medizinischem Fachpersonal.',
    sous_plancher='kein Abnehmziel: Der gemessene Verbrauch liegt unter der Sicherheitsgrenze, wahrscheinlich wegen eines unvollständigen Tagebuchs',
    releve='zum Abnehmen: auf die Sicherheitsgrenze angehoben', perte='um in moderatem Tempo abzunehmen (− 15 %)',
    cmp_a='Die Formel sagte ', cmp_b=' kcal voraus: Dein tatsächlicher Verbrauch ist ', sup='höher', inf='niedriger', cmp_c=', um ', cmp_d=' %.',
    ecart='Diese Abweichung liegt außerhalb der Grenzen, die die App akzeptiert (0,8- bis 1,6-fache der Formel). Die häufigste Ursache ist ein unvollständiges Tagebuch.',
    variation='Veränderung: ', en_a=' kg in ', en_b=' Tagen', kcaljour=' kcal / Tag', x7700=' × 7.700 ÷ ')

PAGES = {
    'en': {'slug': '/en/real-expenditure-calculator.html',
           'tete': dict(title='Real expenditure calculator (maintenance calories) | Basal', locale='en_GB',
                        description='Work out your real energy expenditure from what you eat and how your weight changes: the energy-balance method Basal uses. Free, no sign-up, nothing is sent.',
                        og_title='Real expenditure calculator (maintenance calories)', og_description='Your real expenditure from your intake and your weight trend, not from a formula.'),
           'main': main(T_EN), 'script': script('en-GB', S_EN),
           'ld': ld('Real expenditure calculator', '/en/real-expenditure-calculator.html', 'Real energy expenditure from average intake and weight change (energy balance, 7,700 kcal per kg).', 'en',
                    '/en/', 'Home', '/en/calculators/', 'Calculators', 'Real expenditure')},
    'es': {'slug': '/es/gasto-real.html',
           'tete': dict(title='Calcula tu gasto real (calorías de mantenimiento) | Basal', locale='es_ES',
                        description='Calcula tu gasto energético real a partir de lo que comes y de la evolución de tu peso: el método del balance energético que usa Basal. Gratis, sin registro, no se envía nada.',
                        og_title='Calcula tu gasto real (calorías de mantenimiento)', og_description='Tu gasto real a partir de tu ingesta y de la tendencia de tu peso, no de una fórmula.'),
           'main': main(T_ES), 'script': script('es-ES', S_ES),
           'ld': ld('Calculadora de gasto real', '/es/gasto-real.html', 'Gasto energético real a partir de la ingesta media y la variación de peso (balance energético, 7.700 kcal por kg).', 'es',
                    '/es/', 'Inicio', '/es/calculadoras/', 'Calculadoras', 'Gasto real')},
    'de': {'slug': '/de/tatsaechlicher-verbrauch.html',
           'tete': dict(title='Tatsächlichen Verbrauch berechnen (Erhaltungskalorien) | Basal', locale='de_DE',
                        description='Berechne deinen tatsächlichen Energieverbrauch aus dem, was du isst, und dem Verlauf deines Gewichts: die Energiebilanz-Methode von Basal. Kostenlos, ohne Anmeldung, es wird nichts gesendet.',
                        og_title='Tatsächlichen Verbrauch berechnen (Erhaltungskalorien)', og_description='Dein tatsächlicher Verbrauch aus Zufuhr und Gewichtsverlauf, nicht aus einer Formel.'),
           'main': main(T_DE), 'script': script('de-DE', S_DE),
           'ld': ld('Rechner für den tatsächlichen Verbrauch', '/de/tatsaechlicher-verbrauch.html', 'Tatsächlicher Energieverbrauch aus durchschnittlicher Zufuhr und Gewichtsveränderung (Energiebilanz, 7.700 kcal pro kg).', 'de',
                    '/de/', 'Startseite', '/de/rechner/', 'Rechner', 'Tatsächlicher Verbrauch')},
}
