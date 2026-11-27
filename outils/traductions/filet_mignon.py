from commun import U, article_seo, recette
from steak_hache import tableau

FR = '/proteines-filet-mignon-porc.html'
DATE = '2026-11-27'
C = 'filet-mignon'
for _l in ('en', 'es', 'de'):
    U.setdefault('r-filet', {})[_l] = recette(_l, 'filet-mignon-moutarde')[0]


def comparaison(dec, noms):
    v = [('23.7', '108', '21.9'), ('23.4', '110', '21.3'), ('23.5', '118', '19.9'), ('21.2', '123', '17.2'), ('21.9', '130', '16.8'), ('19.8', '164', '12.1')]
    f = (lambda x: x.replace('.', ',')) if dec == ',' else (lambda x: x)
    return [(n, f(p) + ' g', k + ' kcal', f(r) + ' g') for n, (p, k, r) in zip(noms, v)]


def valeurs(dec, lib):
    f = (lambda x: x.replace('.', ',')) if dec == ',' else (lambda x: x)
    return [(lib[0], '123 kcal', '168 kcal'), (lib[1], f('21.2 g'), f('26.1 g')), (lib[2], f('4.1 g'), f('7.1 g')), (lib[3], f('0.4 g'), '0 g')]


SOURCE = {
 'en': 'ANSES. <i>Ciqual French food composition table, 2025</i>: pork, filet mignon, raw and cooked; chicken breast without skin, raw; turkey escalope, raw; beef rump steak, raw; beef minced steak 5% fat, raw; pork chop, raw.',
 'es': 'ANSES. <i>Tabla de composición de alimentos Ciqual 2025</i>: cerdo, solomillo crudo y cocinado; pechuga de pollo sin piel cruda; escalope de pavo crudo; cadera de ternera cruda; hamburguesa de ternera al 5 % de grasa cruda; chuleta de cerdo cruda.',
 'de': 'ANSES. <i>Französische Lebensmittel-Nährwerttabelle Ciqual 2025</i>: Schweinefilet roh und gegart; Hähnchenbrust ohne Haut roh; Putenschnitzel roh; Rinderhüfte roh; Rinderhacksteak 5 % Fett roh; Schweinekotelett roh.',
}

EN = dict(publie=DATE,
 title='Pork tenderloin protein: 21 g per 100 g (Ciqual)',
 desc='Pork tenderloin: 21.2 g of protein and 123 kcal per 100 g raw, 26.1 g cooked. Per serving, and compared with chicken, turkey and beef.',
 court='Pork tenderloin protein', surtitre='Meals',
 h1='Pork tenderloin: protein and calories per 100 g, raw and cooked',
 chapeau='Pork tenderloin provides 21 g of protein and 123 kcal per 100 g raw, 26 g and 168 kcal once cooked. It is the leanest cut of pork: closer to chicken than to a pork chop.',
 situation='You are cooking a pork tenderloin and want to know how much protein is in your portion. <strong>With Basal:</strong> you log the weight you measured, choosing the raw or cooked line; the values come from the Ciqual table of ANSES, the French food safety agency.',
 bref='100 g of raw pork tenderloin: 21.2 g of protein, 4.1 g of fat, 123 kcal. Cooked: 26.1 g of protein, 7.1 g of fat, 168 kcal. A 150 g raw serving provides about 32 g of protein for 185 kcal.',
 sections=[
  ('values', 'Pork tenderloin protein and calories per 100 g', tableau('Pork tenderloin, per 100 g (Ciqual table, ANSES)', ['', 'Raw', 'Cooked'], valeurs('.', ['Energy', 'Protein', 'Fat', 'Carbohydrates'])) + '<p>The cooked value shows more protein per 100 g because the meat has lost water: the protein is more concentrated, not more plentiful. Based on these values, and assuming the protein stays in the meat, 100 g of raw tenderloin gives about 81 g cooked. The guide <a href="@peser">weighing food raw or cooked</a> explains which value to pick depending on when you weigh.</p>'),
  ('serving', 'How much protein in a serving of pork tenderloin', '<ul><li><strong>120 g raw</strong>: 25 g of protein, 148 kcal;</li><li><strong>150 g raw</strong>: 32 g of protein, 185 kcal;</li><li><strong>200 g raw</strong>: 42 g of protein, 246 kcal.</li></ul><p>The weight of the whole tenderloin is on the pack: divided by the number of servings, it gives your raw portion. The <a href="@r-filet">pork tenderloin with mustard sauce recipe</a> uses 400 g for 4 servings, about 28 g of protein per plate with the sides.</p><p>To see what a serving represents in your day, the guide <a href="@proteines">how much protein per day</a> gives the benchmarks, and the <a href="@calc-proteines">protein calculator</a> works it out for your weight.</p>'),
  ('compared', 'Pork tenderloin, chicken, turkey, beef: which has the most protein', tableau('Per 100 g raw (Ciqual table, ANSES)', ['Meat', 'Protein', 'Energy', 'Protein per 100 kcal'], comparaison('.', ['Turkey escalope', 'Skinless chicken breast', 'Beef rump steak', 'Pork tenderloin', 'Beef mince, 5% fat', 'Pork chop'])) + '<p>Pork tenderloin remains a lean meat, on a par with 5% beef mince. Turkey and chicken do a little better. The pork chop, more than twice as fatty, provides 30% less protein per 100 kcal. The different fat levels of beef mince are covered in <a href="@steak-hache">beef mince calories</a>.</p>'),
  ('basal', 'Logging it in Basal', '<p>In Basal, you search for the food and pick the raw or cooked pork tenderloin line, whichever matches what you weighed, then enter the weight. For a home-cooked dish, you can save the recipe once and log your share in servings. This is free, ad-free and needs no account.</p>'),
  ('unknown', 'What we don’t know', '<p>Ciqual values are averages: a poorly trimmed tenderloin, with its membrane and fat, has a few more calories. Water loss depends on cooking; the cooked weight worked out above (81 g per 100 g raw) is an estimate drawn from the table values, not a measurement. Cooking fat and sauce come on top and are not counted here.</p>'),
 ],
 appel=('Your protein, meal after meal', 'Basal adds up the protein in each food and shows where you stand against your daily target. Tracking is free, ad-free and needs no account.'),
 sources=[SOURCE['en']],
 plus=[('r-filet', 'Recipe', 'Pork tenderloin with mustard sauce', 'The recipe, with its calories per serving.'),
       ('proteines', None, 'Protein per day', 'How much to aim for depending on your goal.'),
       ('steak-hache', None, 'Beef mince calories', '5, 10, 15 or 20% fat, raw or cooked.')])

ES = dict(publie=DATE,
 title='Proteínas del solomillo de cerdo: 21 g por 100 g',
 desc='Solomillo de cerdo: 21,2 g de proteína y 123 kcal por 100 g en crudo, 26,1 g cocinado. Por ración, y comparado con el pollo, el pavo y la ternera.',
 court='Proteínas del solomillo de cerdo', surtitre='Comidas',
 h1='Solomillo de cerdo: proteínas y calorías por 100 g, crudo y cocinado',
 chapeau='El solomillo de cerdo aporta 21 g de proteína y 123 kcal por 100 g en crudo, 26 g y 168 kcal una vez cocinado. Es la pieza más magra del cerdo: más cerca del pollo que de la chuleta.',
 situation='Cocinas un solomillo de cerdo y quieres saber cuánta proteína hay en tu ración. <strong>Con Basal:</strong> apuntas el peso que mediste, eligiendo la línea cruda o cocinada; los valores vienen de la tabla Ciqual de la ANSES, la agencia francesa de seguridad alimentaria.',
 bref='100 g de solomillo de cerdo crudo: 21,2 g de proteína, 4,1 g de grasa, 123 kcal. Cocinado: 26,1 g de proteína, 7,1 g de grasa, 168 kcal. Una ración de 150 g en crudo aporta unos 32 g de proteína por 185 kcal.',
 sections=[
  ('valores', 'Proteínas y calorías del solomillo de cerdo por 100 g', tableau('Solomillo de cerdo, por 100 g (tabla Ciqual, ANSES)', ['', 'Crudo', 'Cocinado'], valeurs(',', ['Energía', 'Proteína', 'Grasa', 'Hidratos de carbono'])) + '<p>El cocinado muestra más proteína por 100 g porque la carne ha perdido agua: la proteína está más concentrada, no hay más. Según estos valores, y suponiendo que la proteína se queda en la carne, 100 g de solomillo crudo dan unos 81 g cocinados. La guía <a href="@peser">pesar crudo o cocinado</a> explica qué valor elegir según el momento en que pesas.</p>'),
  ('racion', 'Cuánta proteína hay en una ración de solomillo', '<ul><li><strong>120 g en crudo</strong>: 25 g de proteína, 148 kcal;</li><li><strong>150 g en crudo</strong>: 32 g de proteína, 185 kcal;</li><li><strong>200 g en crudo</strong>: 42 g de proteína, 246 kcal.</li></ul><p>El peso del solomillo entero viene en el envase: dividido por el número de raciones, da tu ración en crudo. La <a href="@r-filet">receta de solomillo de cerdo a la mostaza</a> usa 400 g para 4 raciones, unos 28 g de proteína por plato con la guarnición.</p><p>Para saber qué supone una ración en tu día, la guía <a href="@proteines">cuántas proteínas al día</a> da las referencias, y la <a href="@calc-proteines">calculadora de proteínas</a> hace el cálculo para tu peso.</p>'),
  ('comparacion', 'Solomillo, pollo, pavo, ternera: cuál aporta más proteína', tableau('Por 100 g en crudo (tabla Ciqual, ANSES)', ['Carne', 'Proteína', 'Energía', 'Proteína por 100 kcal'], comparaison(',', ['Escalope de pavo', 'Pechuga de pollo sin piel', 'Cadera de ternera', 'Solomillo de cerdo', 'Carne picada de ternera al 5 %', 'Chuleta de cerdo'])) + '<p>El solomillo sigue siendo una carne magra, al nivel de la carne picada al 5 %. El pavo y el pollo lo hacen algo mejor. La chuleta de cerdo, más del doble de grasa, aporta un 30 % menos de proteína por 100 kcal. Los distintos porcentajes de grasa de la carne picada se detallan en <a href="@steak-hache">calorías de la carne picada</a>.</p>'),
  ('basal', 'Apuntarlo en Basal', '<p>En Basal, buscas el alimento y eliges la línea de solomillo de cerdo crudo o cocinado, la que corresponda a lo que pesaste, y luego introduces el peso. Para un plato casero, puedes guardar la receta una vez y apuntar tu parte en raciones. Es gratuito, sin publicidad y sin cuenta.</p>'),
  ('desconocido', 'Lo que no sabemos', '<p>Los valores de Ciqual son medias: un solomillo mal limpio, con su membrana y su grasa, tiene algunas calorías más. La pérdida de agua depende de la cocción; el peso cocinado calculado arriba (81 g por 100 g en crudo) es una estimación sacada de los valores de la tabla, no una medida. El aceite de cocinar y la salsa se suman aparte y no se cuentan aquí.</p>'),
 ],
 appel=('Tus proteínas, comida a comida', 'Basal suma la proteína de cada alimento y te muestra dónde estás respecto a tu objetivo del día. El seguimiento es gratuito, sin publicidad y sin cuenta.'),
 sources=[SOURCE['es']],
 plus=[('r-filet', 'Receta', 'Solomillo de cerdo a la mostaza', 'La receta, con sus calorías por ración.'),
       ('proteines', None, 'Proteínas al día', 'Cuántas buscar según tu objetivo.'),
       ('steak-hache', None, 'Calorías de la carne picada', '5, 10, 15 o 20 % de grasa, cruda o cocinada.')])

DE = dict(publie=DATE,
 title='Schweinefilet: Kalorien und Protein pro 100 g',
 desc='Schweinefilet: 21,2 g Protein und 123 kcal pro 100 g roh, 26,1 g gegart. Pro Portion und im Vergleich zu Hähnchen, Pute und Rind.',
 court='Protein im Schweinefilet', surtitre='Mahlzeiten',
 h1='Schweinefilet: Protein und Kalorien pro 100 g, roh und gegart',
 chapeau='Schweinefilet liefert 21 g Protein und 123 kcal pro 100 g roh, gegart 26 g und 168 kcal. Es ist das magerste Stück vom Schwein: näher am Hähnchen als am Kotelett.',
 situation='Du bereitest ein Schweinefilet zu und willst wissen, wie viel Protein in deiner Portion steckt. <strong>Mit Basal:</strong> Du trägst das gewogene Gewicht ein und wählst die rohe oder gegarte Zeile; die Werte stammen aus der Ciqual-Tabelle der ANSES, der französischen Behörde für Lebensmittelsicherheit.',
 bref='100 g rohes Schweinefilet: 21,2 g Protein, 4,1 g Fett, 123 kcal. Gegart: 26,1 g Protein, 7,1 g Fett, 168 kcal. Eine rohe Portion von 150 g liefert etwa 32 g Protein bei 185 kcal.',
 sections=[
  ('werte', 'Protein und Kalorien im Schweinefilet pro 100 g', tableau('Schweinefilet, pro 100 g (Ciqual-Tabelle, ANSES)', ['', 'Roh', 'Gegart'], valeurs(',', ['Energie', 'Protein', 'Fett', 'Kohlenhydrate'])) + '<p>Gegart zeigt mehr Protein pro 100 g, weil das Fleisch Wasser verloren hat: Das Protein ist konzentrierter, nicht mehr. Nach diesen Werten, und unter der Annahme, dass das Protein im Fleisch bleibt, ergeben 100 g rohes Filet etwa 81 g gegart. Der Ratgeber <a href="@peser">roh oder gekocht wiegen</a> erklärt, welchen Wert du je nach Zeitpunkt des Wiegens wählst.</p>'),
  ('portion', 'Wie viel Protein in einer Portion Schweinefilet steckt', '<ul><li><strong>120 g roh</strong>: 25 g Protein, 148 kcal;</li><li><strong>150 g roh</strong>: 32 g Protein, 185 kcal;</li><li><strong>200 g roh</strong>: 42 g Protein, 246 kcal.</li></ul><p>Das Gewicht des ganzen Filets steht auf der Packung: geteilt durch die Zahl der Portionen ergibt es deine rohe Portion. Das <a href="@r-filet">Rezept Schweinefilet mit Senf</a> verwendet 400 g für 4 Portionen, etwa 28 g Protein pro Teller mit Beilage.</p><p>Um eine Portion in deinen Tag einzuordnen, gibt der Ratgeber <a href="@proteines">wie viel Protein pro Tag</a> die Richtwerte, und der <a href="@calc-proteines">Proteinrechner</a> rechnet es für dein Gewicht aus.</p>'),
  ('vergleich', 'Schweinefilet, Hähnchen, Pute, Rind: wer liefert das meiste Protein', tableau('Pro 100 g roh (Ciqual-Tabelle, ANSES)', ['Fleisch', 'Protein', 'Energie', 'Protein pro 100 kcal'], comparaison(',', ['Putenschnitzel', 'Hähnchenbrust ohne Haut', 'Rinderhüfte', 'Schweinefilet', 'Rinderhack, 5 % Fett', 'Schweinekotelett'])) + '<p>Schweinefilet bleibt mageres Fleisch, auf dem Niveau von Rinderhack mit 5 % Fett. Pute und Hähnchen schneiden etwas besser ab. Das Schweinekotelett, mehr als doppelt so fett, liefert 30 % weniger Protein pro 100 kcal. Die verschiedenen Fettstufen von Rinderhack stehen unter <a href="@steak-hache">Hackfleisch Kalorien</a>.</p>'),
  ('basal', 'In Basal eintragen', '<p>In Basal suchst du das Lebensmittel und wählst die Zeile für rohes oder gegartes Schweinefilet, je nachdem, was du gewogen hast, und gibst dann das Gewicht ein. Für ein selbst gekochtes Gericht kannst du das Rezept einmal speichern und deinen Anteil in Portionen eintragen. Das ist kostenlos, werbefrei und braucht kein Konto.</p>'),
  ('unbekannt', 'Was wir nicht wissen', '<p>Ciqual-Werte sind Durchschnittswerte: Ein schlecht pariertes Filet mit Silberhaut und Fett hat einige Kalorien mehr. Der Wasserverlust hängt vom Garen ab; das oben berechnete Gargewicht (81 g pro 100 g roh) ist eine Schätzung aus den Tabellenwerten, keine Messung. Bratfett und Soße kommen hinzu und sind hier nicht mitgezählt.</p>'),
 ],
 appel=('Dein Protein, Mahlzeit für Mahlzeit', 'Basal addiert das Protein jedes Lebensmittels und zeigt dir, wo du im Vergleich zu deinem Tagesziel stehst. Das Tracking ist kostenlos, werbefrei und braucht kein Konto.'),
 sources=[SOURCE['de']],
 plus=[('r-filet', 'Rezept', 'Schweinefilet mit Senf', 'Das Rezept, mit seinen Kalorien pro Portion.'),
       ('proteines', None, 'Protein pro Tag', 'Wie viel du je nach Ziel anpeilen solltest.'),
       ('steak-hache', None, 'Hackfleisch Kalorien', '5, 10, 15 oder 20 % Fett, roh oder gebraten.')])

PAGES = {l: article_seo(l, C, a, f'{l}-{C}') for l, a in (('en', EN), ('es', ES), ('de', DE))}
