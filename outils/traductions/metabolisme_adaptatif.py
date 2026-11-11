from commun import U, page, stores

FR = '/metabolisme-adaptatif.html'
DATE = '2026-11-11'
C = 'metabolisme-adaptatif'

EN = dict(court='Adaptive metabolism', surtitre='Calories and expenditure', publie='2026-08-07', maj='2026-10-30',
    h1='Adaptive metabolism: why a formula is not enough',
    chapeau='Almost every nutrition app estimates your energy expenditure with the same equation. It has a structural flaw — and it can be fixed.',
    sommaire=[('what-a-formula-calculates', 'What a formula calculates'), ('the-activity-factor', 'The activity factor, the weak link'),
              ('correct-with-what-you-can-measure', 'Correcting with what can be measured'), ('what-this-method-cannot-do', 'What this method cannot do'), ('in-practice', 'In practice')],
    corps=f'''    <h2 id="what-a-formula-calculates">What a formula calculates</h2>
    <p>The Mifflin-St Jeor equation, the most widely used today, estimates your <a href="{U["metabolisme-de-base"]["en"]}">basal metabolic rate</a> from four variables: your weight, height, age and sex. The result is then multiplied by an activity factor — sedentary, moderate, active — to get your total expenditure for a day.</p>
    <p>It is a good starting point. It is not a measurement. The equation was built by observing a population, and it gives the <em>average</em> expenditure of people who resemble you on those four variables. It knows nothing about your muscle mass, your thyroid, your dieting history, or what your body actually does when you eat less.</p>

    <div class="encadre">
      <p><strong>The size of the gap.</strong> Validation studies of these equations commonly report errors of about 10% across a population, and more for atypical individuals. On an expenditure of 2,500 kcal, 10% is 250 kcal a day — the difference between losing weight and stalling.</p>
    </div>

    <h2 id="the-activity-factor">The activity factor, the weak link</h2>
    <p>Choosing between “sedentary” and “moderately active” multiplies your basal metabolic rate by 1.2 or by 1.55. Between the two, the gap is over 500 kcal a day for a basal metabolic rate of 1,700 kcal. And you make that choice yourself, once, in a menu, with no reference point.</p>
    <p>Two people who are identical on paper can pick two different categories and be given targets a whole meal apart.</p>

    <h2 id="correct-with-what-you-can-measure">Correcting with what can be measured</h2>
    <p>There is, however, a way to know. Over a long enough period, the change in your weight and what you ate answer each other: if you log your meals and weigh yourself regularly, your real energy balance can be worked out from the gap between the two.</p>
    <p>About 7,700 kcal separate one kilogram of body mass. Someone who eats 2,100 kcal a day on average and loses 400 grams a week is therefore spending roughly 2,540 kcal a day — whatever the formula says. That is the expenditure that counts, because it is observed, not assumed.</p>
    <p>That is the principle of adaptive metabolism: start from the theoretical estimate, then correct it gradually as the data comes in. After a few weeks, the estimate rests on your own data rather than on a population average.</p>

    <h2 id="what-this-method-cannot-do">What this method cannot do</h2>
    <p>It depends entirely on the quality of what you log. Half-logged meals give a wrong expenditure, and wrong in the direction that hurts you: underestimating your intake makes your metabolism look slower than it is.</p>
    <p>It needs time. A given day’s weight depends on water, salt, gut content, the hormonal cycle — variations far larger than the signal you are looking for over a few days. It takes about ten days between two meaningful weigh-ins, and several weeks before a trend deserves the name.</p>
    <p>And it does not replace a medical check-up. An expenditure far from what you would expect can have a cause worth showing a doctor, not an app.</p>

    <div class="encadre">
      <p>That is why Basal shows “not enough data” rather than a number until its thresholds are met. <strong>A number presented with confidence when it rests on three weigh-ins is worth less than no number at all</strong> — it gives false certainty on which real decisions get made.</p>
    </div>

    <h2 id="in-practice">In practice</h2>
    <ul>
      <li>Log your meals completely, including the off days — especially those.</li>
      <li>Weigh yourself under the same conditions, in the morning, daily rather than weekly: the average is what counts, not the single reading.</li>
      <li>Wait three weeks before judging an expenditure figure.</li>
      <li>If the estimate is far from the formula, look at the quality of your log first before concluding anything about your metabolism.</li>
    </ul>

    <div class="appel">
      <p class="appel-t">What the app keeps track of for you</p>
      <p>Basal applies this method: it starts from Mifflin-St Jeor, checks your meals against how your weight changes, and only shows a corrected expenditure once it has enough to back it up. Tracking is free and needs no account. To run the calculation once, on your own numbers: <a href="{U["depense-reelle"]["en"]}">work out your real expenditure</a>.</p>
      {stores("en", "en-adaptive-metabolism")}
    </div>

    <p>Also read: <a href="{U["deficit"]["en"]}">the calorie deficit</a>, to know how much to cut and what pace of loss to expect.</p>''')

ES = dict(court='Metabolismo adaptativo', surtitre='Calorías y gasto', publie='2026-08-07', maj='2026-10-30',
    h1='El metabolismo adaptativo: por qué una fórmula no basta',
    chapeau='Casi todas las aplicaciones de nutrición estiman tu gasto energético con la misma ecuación. Tiene un defecto estructural — y tiene arreglo.',
    sommaire=[('lo-que-calcula-una-formula', 'Lo que calcula una fórmula'), ('el-coeficiente-de-actividad', 'El coeficiente de actividad, el eslabón débil'),
              ('corregir-con-lo-medible', 'Corregir con lo que se puede medir'), ('lo-que-este-metodo-no-puede-hacer', 'Lo que este método no puede hacer'), ('en-la-practica', 'En la práctica')],
    corps=f'''    <h2 id="lo-que-calcula-una-formula">Lo que calcula una fórmula</h2>
    <p>La ecuación de Mifflin-St Jeor, la más usada hoy, estima tu <a href="{U["metabolisme-de-base"]["es"]}">metabolismo basal</a> a partir de cuatro variables: tu peso, tu altura, tu edad y tu sexo. Después se multiplica el resultado por un coeficiente de actividad — sedentario, moderado, activo — para obtener el gasto total de un día.</p>
    <p>Es un buen punto de partida. No es una medida. La ecuación se construyó observando a una población y da el gasto <em>medio</em> de las personas que se parecen a ti en esas cuatro variables. No conoce tu masa muscular, ni tu tiroides, ni tu historial de dietas, ni lo que hace realmente tu cuerpo cuando comes menos.</p>

    <div class="encadre">
      <p><strong>El orden de magnitud de la desviación.</strong> Los estudios de validación de estas ecuaciones suelen indicar errores de un 10 % en una población, y más en personas atípicas. Sobre un gasto de 2.500 kcal, un 10 % son 250 kcal al día — la diferencia entre perder peso y estancarse.</p>
    </div>

    <h2 id="el-coeficiente-de-actividad">El coeficiente de actividad, el eslabón débil</h2>
    <p>Elegir entre «sedentario» y «moderadamente activo» multiplica tu metabolismo basal por 1,2 o por 1,55. Entre ambos, la diferencia supera las 500 kcal al día para un metabolismo basal de 1.700 kcal. Y esa elección la haces tú, una vez, en un menú, sin referencia.</p>
    <p>Dos personas idénticas sobre el papel pueden elegir dos categorías distintas y recibir objetivos separados por una comida entera.</p>

    <h2 id="corregir-con-lo-medible">Corregir con lo que se puede medir</h2>
    <p>Sin embargo, hay una forma de saberlo. En un periodo lo bastante largo, la variación de tu peso y lo que has comido se responden: si registras tus comidas y te pesas con regularidad, el balance energético real se deduce de la diferencia entre ambos.</p>
    <p>Un kilo de masa corporal equivale a unas 7.700 kcal. Alguien que come de media 2.100 kcal al día y pierde 400 gramos por semana gasta por tanto unas 2.540 kcal diarias — diga lo que diga la fórmula. Ese gasto es el que cuenta, porque se observa, no se supone.</p>
    <p>Es el principio del metabolismo adaptativo: partir de la estimación teórica y corregirla poco a poco a medida que se acumulan los datos. Al cabo de unas semanas, la estimación se apoya en tus propios datos y no en una media de población.</p>

    <h2 id="lo-que-este-metodo-no-puede-hacer">Lo que este método no puede hacer</h2>
    <p>Depende por completo de la calidad de lo que registras. Comidas anotadas a medias dan un gasto falso, y falso en el sentido que te perjudica: subestimar lo que comes hace creer en un metabolismo más lento de lo que es.</p>
    <p>Necesita tiempo. El peso de un día concreto depende del agua, la sal, el contenido digestivo y el ciclo hormonal — variaciones mucho mayores que la señal que se busca en pocos días. Hacen falta unos diez días entre dos pesadas significativas, y varias semanas para que una tendencia merezca ese nombre.</p>
    <p>Y no sustituye una revisión médica. Un gasto muy alejado de lo esperado puede tener una causa que debe ver un médico, no una aplicación.</p>

    <div class="encadre">
      <p>Por eso Basal muestra «datos insuficientes» en lugar de una cifra mientras no se alcanzan los umbrales. <strong>Un número presentado con seguridad cuando se apoya en tres pesadas vale menos que ningún número</strong> — da una falsa certeza sobre la que se toman decisiones reales.</p>
    </div>

    <h2 id="en-la-practica">En la práctica</h2>
    <ul>
      <li>Registra tus comidas completas, incluidos los días malos — sobre todo esos.</li>
      <li>Pésate en las mismas condiciones, por la mañana, mejor a diario que una vez por semana: cuenta la media, no la medida.</li>
      <li>Deja pasar tres semanas antes de juzgar una cifra de gasto.</li>
      <li>Si la estimación se aleja mucho de la fórmula, revisa primero la calidad de tu registro antes de concluir nada sobre tu metabolismo.</li>
    </ul>

    <div class="appel">
      <p class="appel-t">Lo que la aplicación hace por ti</p>
      <p>Basal aplica este método: parte de Mifflin-St Jeor, compara tus comidas con la evolución de tu peso y solo muestra un gasto corregido cuando tiene con qué respaldarlo. El seguimiento es gratis y no pide ninguna cuenta. Para hacer el cálculo una vez, con tus propias cifras: <a href="{U["depense-reelle"]["es"]}">calcula tu gasto real</a>.</p>
      {stores("es", "es-metabolismo-adaptativo")}
    </div>

    <p>Lee también: <a href="{U["deficit"]["es"]}">el déficit calórico</a>, para saber cuánto restar y qué ritmo de pérdida esperar.</p>''')

DE = dict(court='Metabolische Anpassung', surtitre='Kalorien und Verbrauch', publie='2026-08-07', maj='2026-10-30',
    h1='Metabolische Anpassung: Warum eine Formel nicht reicht',
    chapeau='Fast alle Ernährungs-Apps schätzen deinen Energieverbrauch mit derselben Gleichung. Sie hat einen strukturellen Fehler — und der lässt sich beheben.',
    sommaire=[('was-eine-formel-berechnet', 'Was eine Formel berechnet'), ('der-aktivitaetsfaktor', 'Der Aktivitätsfaktor, das schwache Glied'),
              ('mit-messbarem-korrigieren', 'Mit Messbarem korrigieren'), ('was-diese-methode-nicht-kann', 'Was diese Methode nicht kann'), ('in-der-praxis', 'In der Praxis')],
    corps=f'''    <h2 id="was-eine-formel-berechnet">Was eine Formel berechnet</h2>
    <p>Die Mifflin-St-Jeor-Gleichung, heute die meistgenutzte, schätzt deinen <a href="{U["metabolisme-de-base"]["de"]}">Grundumsatz</a> aus vier Variablen: Gewicht, Größe, Alter und Geschlecht. Das Ergebnis wird dann mit einem Aktivitätsfaktor multipliziert — sitzend, mäßig, aktiv —, um den Gesamtverbrauch eines Tages zu erhalten.</p>
    <p>Das ist ein guter Ausgangspunkt. Es ist keine Messung. Die Gleichung wurde an einer Bevölkerungsgruppe entwickelt und liefert den <em>durchschnittlichen</em> Verbrauch von Menschen, die dir in diesen vier Variablen ähneln. Sie kennt weder deine Muskelmasse noch deine Schilddrüse, deine Diätgeschichte oder das, was dein Körper tatsächlich tut, wenn du weniger isst.</p>

    <div class="encadre">
      <p><strong>Die Größenordnung der Abweichung.</strong> Validierungsstudien dieser Gleichungen berichten üblicherweise Fehler von etwa 10 % in einer Bevölkerungsgruppe, bei untypischen Personen mehr. Bei einem Verbrauch von 2.500 kcal sind 10 % 250 kcal pro Tag — der Unterschied zwischen Abnehmen und Stillstand.</p>
    </div>

    <h2 id="der-aktivitaetsfaktor">Der Aktivitätsfaktor, das schwache Glied</h2>
    <p>Die Wahl zwischen „sitzend“ und „mäßig aktiv“ multipliziert deinen Grundumsatz mit 1,2 oder mit 1,55. Dazwischen liegen bei einem Grundumsatz von 1.700 kcal über 500 kcal pro Tag. Und diese Wahl triffst du selbst, einmal, in einem Menü, ohne Bezugspunkt.</p>
    <p>Zwei auf dem Papier identische Menschen können zwei verschiedene Kategorien wählen und Ziele bekommen, die eine ganze Mahlzeit auseinanderliegen.</p>

    <h2 id="mit-messbarem-korrigieren">Mit Messbarem korrigieren</h2>
    <p>Es gibt aber einen Weg, es zu wissen. Über einen ausreichend langen Zeitraum antworten sich die Veränderung deines Gewichts und das, was du gegessen hast: Wenn du deine Mahlzeiten einträgst und dich regelmäßig wiegst, ergibt sich die tatsächliche Energiebilanz aus der Differenz zwischen beidem.</p>
    <p>Etwa 7.700 kcal entsprechen einem Kilogramm Körpermasse. Wer im Schnitt 2.100 kcal pro Tag isst und 400 Gramm pro Woche verliert, verbraucht also rund 2.540 kcal täglich — egal, was die Formel sagt. Dieser Verbrauch zählt, weil er beobachtet und nicht angenommen ist.</p>
    <p>Das ist das Prinzip der metabolischen Anpassung: von der theoretischen Schätzung ausgehen und sie schrittweise korrigieren, während sich die Daten sammeln. Nach einigen Wochen stützt sich die Schätzung auf deine eigenen Daten statt auf einen Bevölkerungsdurchschnitt.</p>

    <h2 id="was-diese-methode-nicht-kann">Was diese Methode nicht kann</h2>
    <p>Sie hängt vollständig von der Qualität deiner Einträge ab. Halb eingetragene Mahlzeiten ergeben einen falschen Verbrauch, und zwar in die Richtung, die dir schadet: Wer seine Zufuhr unterschätzt, hält seinen Stoffwechsel für langsamer, als er ist.</p>
    <p>Sie braucht Zeit. Das Gewicht eines Tages hängt von Wasser, Salz, Darminhalt und Hormonzyklus ab — Schwankungen, die das gesuchte Signal über wenige Tage weit übertreffen. Zwischen zwei aussagekräftigen Wiegungen braucht es etwa zehn Tage, und mehrere Wochen, bis ein Trend den Namen verdient.</p>
    <p>Und sie ersetzt keine ärztliche Untersuchung. Ein Verbrauch, der stark vom Erwarteten abweicht, kann eine Ursache haben, die ein Arzt ansehen sollte, keine App.</p>

    <div class="encadre">
      <p>Deshalb zeigt Basal „zu wenige Daten“ statt einer Zahl, solange die Schwellen nicht erreicht sind. <strong>Eine Zahl, die selbstsicher präsentiert wird, obwohl sie auf drei Wiegungen beruht, ist weniger wert als gar keine Zahl</strong> — sie gibt eine falsche Sicherheit, auf deren Grundlage echte Entscheidungen fallen.</p>
    </div>

    <h2 id="in-der-praxis">In der Praxis</h2>
    <ul>
      <li>Trage deine Mahlzeiten vollständig ein, auch an misslungenen Tagen — gerade an denen.</li>
      <li>Wiege dich unter gleichen Bedingungen, morgens, lieber täglich als einmal pro Woche: Es zählt der Durchschnitt, nicht der einzelne Wert.</li>
      <li>Lass drei Wochen vergehen, bevor du eine Verbrauchszahl beurteilst.</li>
      <li>Weicht die Schätzung stark von der Formel ab, prüfe zuerst die Qualität deines Tagebuchs, bevor du etwas über deinen Stoffwechsel schließt.</li>
    </ul>

    <div class="appel">
      <p class="appel-t">Was die App für dich im Blick behält</p>
      <p>Basal wendet diese Methode an: Es startet mit Mifflin-St Jeor, gleicht deine Mahlzeiten mit dem Verlauf deines Gewichts ab und zeigt einen korrigierten Verbrauch erst, wenn es ihn belegen kann. Das Tracking ist kostenlos und braucht kein Konto. Um die Rechnung einmal mit deinen eigenen Zahlen zu machen: <a href="{U["depense-reelle"]["de"]}">tatsächlichen Verbrauch berechnen</a>.</p>
      {stores("de", "de-metabolische-anpassung")}
    </div>

    <p>Lies auch: <a href="{U["deficit"]["de"]}">das Kaloriendefizit</a>, um zu wissen, wie viel du einsparen solltest und welches Tempo du erwarten kannst.</p>''')

PAGES = {
    'en': page('en', C, EN, dict(title='Adaptive metabolism: why a formula gets it wrong — Basal',
        description='Mifflin-St Jeor estimates your expenditure from your height, age and weight. Why that estimate is wrong, and how to correct it with your own data.',
        og_title='Adaptive metabolism: why a formula is not enough', og_description='How to correct an energy expenditure estimate with your own data, and what this method cannot do.')),
    'es': page('es', C, ES, dict(title='Metabolismo adaptativo: por qué una fórmula se equivoca — Basal',
        description='Mifflin-St Jeor estima tu gasto a partir de tu altura, tu edad y tu peso. Por qué esa estimación se equivoca y cómo corregirla con tus datos.',
        og_title='El metabolismo adaptativo: por qué una fórmula no basta', og_description='Cómo corregir una estimación del gasto energético con tus propios datos, y lo que este método no puede hacer.')),
    'de': page('de', C, DE, dict(title='Metabolische Anpassung: Warum eine Formel danebenliegt — Basal',
        description='Mifflin-St Jeor schätzt deinen Verbrauch aus Größe, Alter und Gewicht. Warum diese Schätzung danebenliegt und wie du sie mit deinen Daten korrigierst.',
        og_title='Metabolische Anpassung: Warum eine Formel nicht reicht', og_description='Wie man eine Schätzung des Energieverbrauchs mit eigenen Daten korrigiert, und was diese Methode nicht kann.')),
}
