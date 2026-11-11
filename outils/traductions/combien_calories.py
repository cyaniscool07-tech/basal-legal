from commun import U, page, stores

FR = '/combien-de-calories-par-jour.html'
DATE = '2026-11-11'
C = 'combien'
EXISTANTS = {'es': '/es/cuantas-calorias-al-dia.html'}

EN = dict(court='Calories per day', surtitre='Calories and expenditure', publie='2026-10-20', maj='2026-10-30',
    h1='How many calories a day?',
    chapeau='The 2,000 kcal figure printed on food labels is not your need. It is a reference value for comparing products with each other. Your real need depends on your height, weight, age, sex and above all on what you do with your days.',
    sommaire=[('by-profile', 'Ballpark figures by profile'), ('work-out-your-own', 'How to work out your own need'), ('to-lose-weight', 'To lose weight: how many calories less?'),
              ('to-build-muscle', 'To build muscle: how many calories more?'), ('what-the-formula-cannot-know', 'What the formula cannot know'), ('in-practice', 'In practice')],
    corps=f'''    <h2 id="by-profile">Ballpark figures by profile</h2>
    <p>Here is the estimated daily expenditure of four profiles, from the least to the most active. It is the number of calories that keeps weight stable: no loss, no gain.</p>

    <div class="encadre">
      <div class="ligne"><span>Woman, 30, 1.65 m, 62 kg</span><b>1,610 to 2,310 kcal</b></div>
      <div class="ligne"><span>Woman, 60, 1.62 m, 68 kg</span><b>1,480 to 2,120 kcal</b></div>
      <div class="ligne"><span>Man, 30, 1.78 m, 78 kg</span><b>2,100 to 3,010 kcal</b></div>
      <div class="ligne"><span>Man, 60, 1.75 m, 82 kg</span><b>1,940 to 2,790 kcal</b></div>
    </div>

    <p>The range goes from “sedentary” (under 5,000 steps a day, no sport) to “active” (6 to 7 sessions a week or over 10,000 steps a day). For the same profile, the gap is often more than 700 kcal: activity weighs more than age.</p>

    <h2 id="work-out-your-own">How to work out your own need</h2>
    <p>The calculation has two steps. First the <strong><a href="{U["metabolisme-de-base"]["en"]}">basal metabolic rate</a></strong>, the energy your body spends at complete rest to breathe, keep its temperature and run its organs. The most widely used formula today is Mifflin-St Jeor.</p>
    <p>Then this basal metabolic rate is multiplied by an <strong>activity factor</strong>, from 1.2 for a sedentary life to 1.9 for a physical job with training. The result is your daily energy expenditure, often called TDEE.</p>
    <p><a href="{U["tdee"]["en"]}">Basal’s calculator</a> does both steps for you, with no sign-up and nothing sent.</p>

    <h2 id="to-lose-weight">To lose weight: how many calories less?</h2>
    <p>To lose weight, you need to eat a little less than you spend. A gap of <strong>10 to 20%</strong> below your daily expenditure is a reasonable starting point for most people: enough to see a result within a few weeks, not so much that energy or muscle suffer.</p>
    <p>For the moderately active 30-year-old woman above (about 2,080 kcal), that gives an intake of 1,660 to 1,870 kcal a day. All the details, including the pace of loss to expect, are in <a href="{U["deficit"]["en"]}">the calorie deficit guide</a>.</p>

    <div class="encadre">
      <p><strong>Going very low does not speed things up much.</strong> It is generally considered that an intake below 1,200 kcal for a woman or 1,500 kcal for a man should not be kept up without medical supervision. Hunger, fatigue and muscle loss quickly take back what you thought you had gained.</p>
    </div>

    <h2 id="to-build-muscle">To build muscle: how many calories more?</h2>
    <p>Conversely, building muscle calls for a slight surplus: around <strong>5 to 10%</strong> above expenditure, with enough protein and training that progresses. Beyond that, the surplus mostly goes to fat. <a href="{U["prise-de-masse"]["en"]}">The bulking guide</a> gives the numbers.</p>

    <h2 id="what-the-formula-cannot-know">What the formula cannot know</h2>
    <p>A formula describes a population, not a person. For a given individual, the typical error is around 10%, or 200 kcal a day either way. That is often exactly the gap between “I am losing” and “I am stalling”.</p>
    <p>The only way to know your real need is to measure it: log what you eat and weigh yourself regularly for two to three weeks, then compare. If your weight (as a trend, not day to day) does not move, your average intake is your true maintenance. That is the principle of <a href="{U["metabolisme-adaptatif"]["en"]}">adaptive metabolism</a>.</p>

    <h2 id="in-practice">In practice</h2>
    <ul>
      <li>Work out your expenditure with a formula to get a starting point, not a truth.</li>
      <li>To lose weight, take off 10 to 20%. To build muscle, add 5 to 10%.</li>
      <li>Keep that number for two to three weeks before judging it: one day’s weight says nothing.</li>
      <li>Then adjust in small steps, 100 to 150 kcal, based on your weight trend.</li>
    </ul>

    <div class="appel">
      <p class="appel-t">Your real need, measured rather than guessed</p>
      <p>Basal starts from the formula, then compares your meals and weigh-ins to recalculate your real expenditure over the weeks. Tracking is free, ad-free and needs no account.</p>
      {stores("en", "en-calories-per-day")}
    </div>''')

DE = dict(court='Kalorien am Tag', surtitre='Kalorien und Verbrauch', publie='2026-10-20', maj='2026-10-30',
    h1='Wie viele Kalorien am Tag?',
    chapeau='Die 2.000 kcal auf Verpackungen sind nicht dein Bedarf. Es ist ein Referenzwert, um Produkte miteinander zu vergleichen. Dein tatsächlicher Bedarf hängt von Größe, Gewicht, Alter, Geschlecht und vor allem davon ab, was du mit deinen Tagen machst.',
    sommaire=[('nach-profil', 'Größenordnungen nach Profil'), ('eigenen-bedarf-berechnen', 'So berechnest du deinen eigenen Bedarf'), ('zum-abnehmen', 'Zum Abnehmen: wie viele Kalorien weniger?'),
              ('fuer-muskelaufbau', 'Für Muskelaufbau: wie viele Kalorien mehr?'), ('was-die-formel-nicht-weiss', 'Was die Formel nicht wissen kann'), ('in-der-praxis', 'In der Praxis')],
    corps=f'''    <h2 id="nach-profil">Größenordnungen nach Profil</h2>
    <p>Hier der geschätzte Tagesverbrauch von vier Profilen, vom am wenigsten bis zum am meisten aktiven. Es ist die Kalorienmenge, bei der das Gewicht stabil bleibt: weder Abnahme noch Zunahme.</p>

    <div class="encadre">
      <div class="ligne"><span>Frau, 30 Jahre, 1,65 m, 62 kg</span><b>1.610 bis 2.310 kcal</b></div>
      <div class="ligne"><span>Frau, 60 Jahre, 1,62 m, 68 kg</span><b>1.480 bis 2.120 kcal</b></div>
      <div class="ligne"><span>Mann, 30 Jahre, 1,78 m, 78 kg</span><b>2.100 bis 3.010 kcal</b></div>
      <div class="ligne"><span>Mann, 60 Jahre, 1,75 m, 82 kg</span><b>1.940 bis 2.790 kcal</b></div>
    </div>

    <p>Die Spanne reicht von „sitzend“ (unter 5.000 Schritte am Tag, kein Sport) bis „aktiv“ (6 bis 7 Einheiten pro Woche oder über 10.000 Schritte am Tag). Beim selben Profil liegen oft über 700 kcal dazwischen: Die Aktivität wiegt mehr als das Alter.</p>

    <h2 id="eigenen-bedarf-berechnen">So berechnest du deinen eigenen Bedarf</h2>
    <p>Die Berechnung hat zwei Schritte. Zuerst der <strong><a href="{U["metabolisme-de-base"]["de"]}">Grundumsatz</a></strong>, die Energie, die dein Körper in völliger Ruhe verbraucht, um zu atmen, die Temperatur zu halten und die Organe arbeiten zu lassen. Die heute meistgenutzte Formel ist die von Mifflin-St Jeor.</p>
    <p>Dann wird dieser Grundumsatz mit einem <strong>Aktivitätsfaktor</strong> multipliziert, von 1,2 bei sitzender Lebensweise bis 1,9 bei körperlicher Arbeit mit Training. Das Ergebnis ist dein täglicher Energieverbrauch, oft TDEE genannt.</p>
    <p><a href="{U["tdee"]["de"]}">Der Rechner von Basal</a> macht beide Schritte für dich, ohne Anmeldung und ohne etwas zu senden.</p>

    <h2 id="zum-abnehmen">Zum Abnehmen: wie viele Kalorien weniger?</h2>
    <p>Um abzunehmen, musst du etwas weniger essen, als du verbrauchst. Ein Abstand von <strong>10 bis 20 %</strong> unter dem Tagesverbrauch ist für die meisten ein vernünftiger Startpunkt: genug, um in einigen Wochen ein Ergebnis zu sehen, ohne Energie oder Muskeln zu opfern.</p>
    <p>Für die mäßig aktive 30-jährige Frau oben (etwa 2.080 kcal) ergibt das eine Zufuhr von 1.660 bis 1.870 kcal am Tag. Alle Details, auch das zu erwartende Tempo, stehen im <a href="{U["deficit"]["de"]}">Ratgeber zum Kaloriendefizit</a>.</p>

    <div class="encadre">
      <p><strong>Sehr tief zu gehen beschleunigt kaum etwas.</strong> Allgemein gilt, dass eine Zufuhr unter 1.200 kcal bei Frauen oder 1.500 kcal bei Männern nicht ohne ärztliche Begleitung durchgehalten werden sollte. Hunger, Müdigkeit und Muskelverlust holen schnell zurück, was man zu gewinnen glaubte.</p>
    </div>

    <h2 id="fuer-muskelaufbau">Für Muskelaufbau: wie viele Kalorien mehr?</h2>
    <p>Umgekehrt braucht Muskelaufbau einen leichten Überschuss: etwa <strong>5 bis 10 %</strong> über dem Verbrauch, mit genug Eiweiß und einem Training, das sich steigert. Darüber hinaus geht der Überschuss vor allem in Fett. <a href="{U["prise-de-masse"]["de"]}">Der Ratgeber zum Masseaufbau</a> nennt die Zahlen.</p>

    <h2 id="was-die-formel-nicht-weiss">Was die Formel nicht wissen kann</h2>
    <p>Eine Formel beschreibt eine Bevölkerungsgruppe, keinen Menschen. Für eine einzelne Person liegt der übliche Fehler bei etwa 10 %, also 200 kcal am Tag in die eine oder andere Richtung. Das ist oft genau der Unterschied zwischen „ich nehme ab“ und „ich stagniere“.</p>
    <p>Der einzige Weg, deinen tatsächlichen Bedarf zu kennen, ist ihn zu messen: zwei bis drei Wochen eintragen, was du isst, dich regelmäßig wiegen und dann vergleichen. Bewegt sich dein Gewicht (im Trend, nicht von Tag zu Tag) nicht, ist deine durchschnittliche Zufuhr dein echter Erhaltungsbedarf. Das ist das Prinzip der <a href="{U["metabolisme-adaptatif"]["de"]}">metabolischen Anpassung</a>.</p>

    <h2 id="in-der-praxis">In der Praxis</h2>
    <ul>
      <li>Berechne deinen Verbrauch mit einer Formel, um einen Startpunkt zu haben, keine Wahrheit.</li>
      <li>Zum Abnehmen 10 bis 20 % abziehen, für Muskelaufbau 5 bis 10 % hinzufügen.</li>
      <li>Halte die Zahl zwei bis drei Wochen, bevor du sie beurteilst: Das Gewicht eines Tages sagt nichts.</li>
      <li>Passe dann in kleinen Schritten von 100 bis 150 kcal an, je nach Trend deines Gewichts.</li>
    </ul>

    <div class="appel">
      <p class="appel-t">Dein echter Bedarf, gemessen statt geraten</p>
      <p>Basal startet mit der Formel und vergleicht dann deine Mahlzeiten und dein Gewicht, um deinen tatsächlichen Verbrauch über die Wochen neu zu berechnen. Das Tracking ist kostenlos, werbefrei und braucht kein Konto.</p>
      {stores("de", "de-kalorien-am-tag")}
    </div>''')

PAGES = {
    'en': page('en', C, EN, dict(title='How many calories a day? (women, men, by age) — Basal',
        description='How many calories a day for a woman or a man, by age and activity: worked examples, and how to calculate your own need.',
        og_title='How many calories a day?', og_description='Worked examples by profile, and how to measure your real need rather than guess it.')),
    'de': page('de', C, DE, dict(title='Wie viele Kalorien am Tag? (Frau, Mann, nach Alter) — Basal',
        description='Wie viele Kalorien am Tag für Frauen und Männer, nach Alter und Aktivität: Rechenbeispiele und wie du deinen eigenen Bedarf berechnest.',
        og_title='Wie viele Kalorien am Tag?', og_description='Rechenbeispiele nach Profil, und wie du deinen echten Bedarf misst statt rätst.')),
}
