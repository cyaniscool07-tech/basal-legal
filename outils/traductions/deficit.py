from commun import U, page, stores

FR = '/deficit-calorique.html'
DATE = '2026-11-11'
C = 'deficit'
EXISTANTS = {'es': '/es/deficit-calorico.html'}

EN = dict(court='Calorie deficit', surtitre='Losing or gaining weight', publie='2026-10-20', maj='2026-10-31',
    h1='Calorie deficit: how to calculate it, what pace, mistakes to avoid',
    chapeau='Losing weight always comes down to the same thing: spending a little more energy than you eat, for long enough. The whole difficulty lies in the “a little” and the “long enough”.',
    sommaire=[('what-a-deficit-is', 'What a calorie deficit is'), ('how-to-calculate', 'How to calculate your deficit'), ('what-loss-to-expect', 'What weight loss to expect'),
              ('signs-too-aggressive', 'Signs of a deficit that is too aggressive'), ('keep-muscle', 'Keeping muscle during a deficit'), ('why-it-stalls', 'Why a deficit ends up stalling'), ('in-practice', 'In practice')],
    corps=f'''    <h2 id="what-a-deficit-is">What a calorie deficit is</h2>
    <p>A calorie deficit is the gap between your daily energy expenditure and what you eat. If you spend 2,100 kcal and eat 1,750, your deficit is 350 kcal a day. The body covers the shortfall by drawing on its reserves, mainly fat if the deficit is moderate and protein is sufficient.</p>

    <h2 id="how-to-calculate">How to calculate your deficit</h2>
    <p>First you need your daily expenditure (often called TDEE). You can estimate it with <a href="{U["tdee"]["en"]}">the calculator</a> or from the <a href="{U["combien"]["en"]}">examples by profile</a>. Then take <strong>10 to 20%</strong> off that figure. Up to 25% can be held for a short period if the starting weight is high.</p>

    <div class="encadre">
      <div class="ligne"><span>Woman, 30, 62 kg, moderately active (expenditure ≈ 2,080 kcal)</span><b>1,660 to 1,870 kcal</b></div>
      <div class="ligne"><span>Man, 30, 78 kg, moderately active (expenditure ≈ 2,710 kcal)</span><b>2,170 to 2,440 kcal</b></div>
      <div class="ligne"><span>Woman, 60, 68 kg, lightly active (expenditure ≈ 1,690 kcal)</span><b>1,350 to 1,520 kcal</b></div>
    </div>

    <p>A percentage is better than a fixed number. The often-repeated “minus 500 kcal” is 18% of an active man’s expenditure, but nearly 30% of a small sedentary woman’s: the same advice becomes much harder to stick to.</p>

    <h2 id="what-loss-to-expect">What weight loss to expect</h2>
    <p>It is commonly estimated that about 7,700 kcal correspond to one kilo of fat. A deficit of 500 kcal a day therefore gives, in theory, a little under half a kilo a week.</p>
    <p>A more personal benchmark: aim to lose <strong>0.5 to 1% of your weight a week</strong>. At 62 kg that is 0.3 to 0.6 kg; at 90 kg, 0.45 to 0.9 kg. Beyond that, muscle loss and fatigue increase markedly.</p>

    <div class="encadre">
      <p><strong>The scale does not follow the theory day by day.</strong> Water, salt, carbs stored in muscle and, for women, the menstrual cycle move weight by one or two kilos with nothing to do with fat. Judge a deficit on the two-to-three-week trend, never on a single weigh-in. More in <a href="{U["variations"]["en"]}">why your weight changes from one day to the next</a>.</p>
    </div>

    <h2 id="signs-too-aggressive">Signs of a deficit that is too aggressive</h2>
    <ul>
      <li>Constant hunger that ends in regular binges.</li>
      <li>Fatigue setting in, sleep getting worse.</li>
      <li>Training loads dropping, week after week.</li>
      <li>Fast loss at first, then nothing despite the effort.</li>
    </ul>
    <p>In those cases, raising calories a little is often more effective than tightening further.</p>

    <h2 id="keep-muscle">Keeping muscle during a deficit</h2>
    <p>Two levers protect muscle mass: a high protein intake, commonly between <strong>1.6 and 2.2 g per kilo of body weight</strong>, and keeping up strength training (details in <a href="{U["proteines"]["en"]}">how much protein per day</a>). If your weight drops while your loads hold or go up, the loss is probably coming from fat. The topic is developed in <a href="{U["nutrition-musculation"]["en"]}">nutrition for strength training</a>.</p>

    <h2 id="why-it-stalls">Why a deficit ends up stalling</h2>
    <p>The more weight you lose, the less you spend: a lighter body costs less energy to carry. The body also trims its spontaneous activity a little (you move less without noticing). The deficit calculated at the start therefore shrinks on its own, and the loss slows down.</p>
    <p>The answer is not to keep cutting, but to <strong>recalculate your expenditure</strong> from what is really happening, then adjust in small steps of 100 to 150 kcal. That is exactly what <a href="{U["metabolisme-adaptatif"]["en"]}">adaptive metabolism</a> describes.</p>

    <h2 id="in-practice">In practice</h2>
    <ul>
      <li>Work out your expenditure, then take off 10 to 20%.</li>
      <li>Aim for 0.5 to 1% of your weight a week, measured on the trend.</li>
      <li>Keep your protein high and your strength training going.</li>
      <li>If the trend stops moving for three weeks, recalculate before cutting more.</li>
      <li>Do not go below 1,200 kcal (women) or 1,500 kcal (men) without medical supervision.</li>
    </ul>

    <div class="appel">
      <p class="appel-t">A deficit that adjusts to what your body really does</p>
      <p>Basal compares your meals and your weight trend to measure your real expenditure, and flags when a loss slows down instead of leaving you to cut at random. Tracking is free, ad-free and needs no account.</p>
      {stores("en", "en-calorie-deficit")}
    </div>''')

DE = dict(court='Kaloriendefizit', surtitre='Abnehmen oder zunehmen', publie='2026-10-20', maj='2026-10-31',
    h1='Kaloriendefizit: Berechnung, Tempo und Fehler, die du vermeiden solltest',
    chapeau='Abnehmen läuft immer auf dasselbe hinaus: etwas mehr Energie verbrauchen, als man isst, und das lange genug. Die ganze Schwierigkeit steckt im „etwas“ und im „lange genug“.',
    sommaire=[('was-ein-defizit-ist', 'Was ein Kaloriendefizit ist'), ('defizit-berechnen', 'So berechnest du dein Defizit'), ('welche-abnahme', 'Welche Abnahme du erwarten kannst'),
              ('zu-aggressiv', 'Anzeichen für ein zu aggressives Defizit'), ('muskeln-halten', 'Muskeln im Defizit halten'), ('warum-es-stagniert', 'Warum ein Defizit irgendwann stagniert'), ('in-der-praxis', 'In der Praxis')],
    corps=f'''    <h2 id="was-ein-defizit-ist">Was ein Kaloriendefizit ist</h2>
    <p>Ein Kaloriendefizit ist der Abstand zwischen deinem täglichen Energieverbrauch und dem, was du isst. Verbrauchst du 2.100 kcal und isst 1.750, beträgt dein Defizit 350 kcal am Tag. Der Körper deckt die Lücke aus seinen Reserven, vor allem aus Fett, wenn das Defizit moderat ist und genug Eiweiß da ist.</p>

    <h2 id="defizit-berechnen">So berechnest du dein Defizit</h2>
    <p>Zuerst brauchst du deinen Tagesverbrauch (oft TDEE genannt). Du kannst ihn mit <a href="{U["tdee"]["de"]}">dem Rechner</a> schätzen oder aus den <a href="{U["combien"]["de"]}">Beispielen nach Profil</a>. Dann ziehst du <strong>10 bis 20 %</strong> davon ab. Bis zu 25 % lassen sich kurzzeitig halten, wenn das Ausgangsgewicht hoch ist.</p>

    <div class="encadre">
      <div class="ligne"><span>Frau, 30 Jahre, 62 kg, mäßig aktiv (Verbrauch ≈ 2.080 kcal)</span><b>1.660 bis 1.870 kcal</b></div>
      <div class="ligne"><span>Mann, 30 Jahre, 78 kg, mäßig aktiv (Verbrauch ≈ 2.710 kcal)</span><b>2.170 bis 2.440 kcal</b></div>
      <div class="ligne"><span>Frau, 60 Jahre, 68 kg, leicht aktiv (Verbrauch ≈ 1.690 kcal)</span><b>1.350 bis 1.520 kcal</b></div>
    </div>

    <p>Ein Prozentsatz ist besser als eine feste Zahl. Das oft wiederholte „minus 500 kcal“ sind 18 % des Verbrauchs eines aktiven Mannes, aber fast 30 % bei einer kleinen, sitzenden Frau: derselbe Rat wird viel schwerer durchzuhalten.</p>

    <h2 id="welche-abnahme">Welche Abnahme du erwarten kannst</h2>
    <p>Üblicherweise rechnet man mit etwa 7.700 kcal pro Kilo Fett. Ein Defizit von 500 kcal am Tag ergibt also theoretisch knapp ein halbes Kilo pro Woche.</p>
    <p>Ein persönlicherer Richtwert: <strong>0,5 bis 1 % deines Gewichts pro Woche</strong>. Bei 62 kg sind das 0,3 bis 0,6 kg, bei 90 kg 0,45 bis 0,9 kg. Darüber nehmen Muskelverlust und Müdigkeit deutlich zu.</p>

    <div class="encadre">
      <p><strong>Die Waage folgt der Theorie nicht Tag für Tag.</strong> Wasser, Salz, in den Muskeln gespeicherte Kohlenhydrate und bei Frauen der Zyklus lassen das Gewicht um ein bis zwei Kilo schwanken, ohne Bezug zum Fett. Beurteile ein Defizit am Trend über zwei bis drei Wochen, nie an einer einzelnen Wiegung. Mehr dazu in <a href="{U["variations"]["de"]}">warum dein Gewicht von Tag zu Tag schwankt</a>.</p>
    </div>

    <h2 id="zu-aggressiv">Anzeichen für ein zu aggressives Defizit</h2>
    <ul>
      <li>Ständiger Hunger, der in regelmäßigen Heißhungerattacken endet.</li>
      <li>Müdigkeit, die sich festsetzt, schlechter werdender Schlaf.</li>
      <li>Trainingsgewichte, die Woche für Woche sinken.</li>
      <li>Schnelle Abnahme am Anfang, dann trotz aller Mühe nichts mehr.</li>
    </ul>
    <p>In diesen Fällen hilft es oft mehr, die Kalorien etwas anzuheben, als weiter zu kürzen.</p>

    <h2 id="muskeln-halten">Muskeln im Defizit halten</h2>
    <p>Zwei Hebel schützen die Muskelmasse: eine hohe Eiweißzufuhr, üblicherweise zwischen <strong>1,6 und 2,2 g pro Kilo Körpergewicht</strong>, und weitergeführtes Krafttraining (Details in <a href="{U["proteines"]["de"]}">wie viel Eiweiß am Tag</a>). Sinkt dein Gewicht, während deine Trainingsgewichte halten oder steigen, kommt der Verlust wahrscheinlich aus dem Fett. Mehr dazu in <a href="{U["nutrition-musculation"]["de"]}">Ernährung und Krafttraining</a>.</p>

    <h2 id="warum-es-stagniert">Warum ein Defizit irgendwann stagniert</h2>
    <p>Je mehr du abnimmst, desto weniger verbrauchst du: Ein leichterer Körper kostet weniger Energie. Der Körper reduziert auch etwas seine spontane Bewegung (man bewegt sich weniger, ohne es zu merken). Das am Anfang berechnete Defizit schrumpft also von selbst, und die Abnahme verlangsamt sich.</p>
    <p>Die Antwort ist nicht, immer weiter zu kürzen, sondern den <strong>Verbrauch neu zu berechnen</strong> anhand dessen, was wirklich passiert, und dann in kleinen Schritten von 100 bis 150 kcal anzupassen. Genau das beschreibt die <a href="{U["metabolisme-adaptatif"]["de"]}">metabolische Anpassung</a>.</p>

    <h2 id="in-der-praxis">In der Praxis</h2>
    <ul>
      <li>Berechne deinen Verbrauch und ziehe 10 bis 20 % ab.</li>
      <li>Ziele auf 0,5 bis 1 % deines Gewichts pro Woche, gemessen am Trend.</li>
      <li>Halte dein Eiweiß hoch und dein Krafttraining bei.</li>
      <li>Bewegt sich der Trend drei Wochen lang nicht, rechne neu, bevor du weiter kürzt.</li>
      <li>Geh nicht unter 1.200 kcal (Frauen) oder 1.500 kcal (Männer) ohne ärztliche Begleitung.</li>
    </ul>

    <div class="appel">
      <p class="appel-t">Ein Defizit, das sich an deinen Körper anpasst</p>
      <p>Basal vergleicht deine Mahlzeiten mit dem Trend deines Gewichts, um deinen tatsächlichen Verbrauch zu messen, und meldet, wenn eine Abnahme langsamer wird, statt dich auf gut Glück kürzen zu lassen. Das Tracking ist kostenlos, werbefrei und braucht kein Konto.</p>
      {stores("de", "de-kaloriendefizit")}
    </div>''')

PAGES = {
    'en': page('en', C, EN, dict(title='Calorie deficit: how to calculate it and what pace — Basal',
        description='How to calculate your calorie deficit, what weight loss to expect each week, the signs of a deficit that is too aggressive and how to keep muscle.',
        og_title='Calorie deficit: how to calculate it, what pace, mistakes to avoid', og_description='How much to cut, what loss to expect, and why a deficit ends up stalling.')),
    'de': page('de', C, DE, dict(title='Kaloriendefizit: Berechnung und Tempo — Basal',
        description='So berechnest du dein Kaloriendefizit, welche Abnahme pro Woche du erwarten kannst, Anzeichen für ein zu aggressives Defizit und wie du Muskeln hältst.',
        og_title='Kaloriendefizit: Berechnung, Tempo und Fehler', og_description='Wie viel du einsparen solltest, welche Abnahme du erwarten kannst und warum ein Defizit stagniert.')),
}
