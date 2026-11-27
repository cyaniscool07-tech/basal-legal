from commun import U, article_seo, recette

FR = '/calories-steak-hache.html'
DATE = '2026-11-27'
C = 'steak-hache'
for _l in ('en', 'es', 'de'):
    U.setdefault('r-steak', {})[_l] = recette(_l, 'steak-pommes-de-terre')[0]


def tableau(cap, cols, lignes):
    tete = ''.join(f'<th scope="col">{c}</th>' for c in cols)
    corps = ''.join(f'<tr><th scope="row">{l[0]}</th>' + ''.join(f'<td>{x}</td>' for x in l[1:]) + '</tr>' for l in lignes)
    return f'<div class="tableau"><table><caption>{cap}</caption><thead><tr>{tete}</tr></thead><tbody>{corps}</tbody></table></div>'


def lignes(dec, g):
    v = [('5 %', '130', '21.9', '155', '25.5'), ('10 %', '170', '20', '210', '26.1'), ('15 %', '215', '20.2', '239', '23.6'), ('20 %', '249', '17.2', '265', '23')]
    f = (lambda x: x.replace('.', ',')) if dec == ',' else (lambda x: x)
    pc = (lambda x: x.replace(' %', '%')) if dec == '.' else (lambda x: x)
    return [(pc(a), b, f(c) + g, d, f(e) + g) for a, b, c, d, e in v]


SOURCE = {
 'en': 'ANSES. <i>Ciqual French food composition table, 2025</i>: beef, minced steak, 5%, 10%, 15% and 20% fat, raw and cooked.',
 'es': 'ANSES. <i>Tabla de composición de alimentos Ciqual 2025</i>: ternera, hamburguesa de carne picada al 5 %, 10 %, 15 % y 20 % de grasa, cruda y cocinada.',
 'de': 'ANSES. <i>Französische Lebensmittel-Nährwerttabelle Ciqual 2025</i>: Rind, Hacksteak mit 5 %, 10 %, 15 % und 20 % Fett, roh und gegart.',
}

EN = dict(publie=DATE,
 title='Beef mince calories: 5%, 15%, raw or cooked',
 desc='Beef mince (ground beef) per 100 g: 130 kcal at 5% fat, 215 kcal at 15%, raw. Raw and cooked values from the Ciqual table, per patty.',
 court='Beef mince calories', surtitre='Meals',
 h1='Beef mince calories: 5, 10, 15 or 20% fat, raw or cooked',
 chapeau='Beef mince at 5% fat provides 130 kcal per 100 g raw; at 20% fat it provides 249: almost double, for slightly less protein. The percentage on the pack matters more than anything else, and the value changes again depending on whether you weigh before or after cooking.',
 situation='You are eating a beef patty or mince and do not know which line to pick in your app: 5% or 15%, raw or cooked. <strong>With Basal:</strong> you search for the food, pick the fat percentage on the pack and the state you weighed it in; the values come from the Ciqual table of ANSES, the French food safety agency.',
 bref='Per 100 g of raw beef mince: 130 kcal at 5% fat, 170 kcal at 10%, 215 kcal at 15% and 249 kcal at 20%. Cooked, the same meat provides 155, 210, 239 and 265 kcal per 100 g, because it has lost water. A 100 g raw patty at 5% fat provides about 22 g of protein.',
 sections=[
  ('table', 'Beef mince calories and protein per 100 g', tableau('Beef mince, per 100 g (Ciqual table, ANSES)', ['Fat', 'Raw: kcal', 'Raw: protein', 'Cooked: kcal', 'Cooked: protein'], lignes('.', ' g')) + '<p>Carbohydrates are zero or close to it. The whole difference in calories comes from fat: 4.6 g per 100 g raw at 5%, 20 g at 20%.</p>'),
  ('patty', 'For a 100 g or 125 g patty', '<p>Shop-bought beef patties usually weigh 100 g or 125 g raw (the weight is on the pack):</p><ul><li><strong>100 g, 5%</strong>: 130 kcal and 22 g of protein;</li><li><strong>100 g, 15%</strong>: 215 kcal and 20 g of protein;</li><li><strong>125 g, 5%</strong>: 163 kcal and 27 g of protein;</li><li><strong>125 g, 15%</strong>: 269 kcal and 25 g of protein.</li></ul><p>Between a 125 g patty at 5% and the same at 15%, the gap is about 106 kcal. One patty a day for a week adds up to a little over 700 kcal.</p>'),
  ('cooked', 'Why cooked mince has more calories per 100 g', '<p>Cooking does not create calories: the meat loses water, so what is left is more concentrated. Based on the Ciqual values, and assuming the protein stays in the meat, a 100 g raw patty at 5% fat weighs only about 86 g once cooked. Those 86 g at 155 kcal per 100 g come to 133 kcal: almost exactly the 130 kcal of the raw patty.</p><p>What matters is choosing the line that matches what you weighed. Weighed on its pack: raw value. Weighed on the plate: cooked value. The details, for every food, are in the guide <a href="@peser">weighing food raw or cooked</a>.</p>'),
  ('choose', '5% or 15% mince: which to choose', '<ul><li><strong>For a cut</strong>: 5% gives more protein for fewer calories. It is the simplest choice for sticking to a <a href="@deficit">calorie deficit</a>.</li><li><strong>For taste and texture</strong>: 15% stays juicier. It is not a bad choice, as long as you log it as such: the most common mistake is eating 15% and logging 5%.</li><li><strong>For protein</strong>: from 5 to 15%, it stays close to 20 g per 100 g raw. At 20%, it drops to 17 g.</li></ul><p>To place these amounts in your day, the guide <a href="@proteines">how much protein per day</a> gives the benchmarks, and the <a href="@calc-proteines">protein calculator</a> works it out for your weight.</p>'),
  ('basal', 'Logging it in Basal', '<p>In Basal, you search for the food and pick the line that matches your pack: fat percentage and state (raw or cooked) are in the name. Then you enter the weight. If you always buy the same product, the barcode scanner uses the values on its label. This is free, ad-free and needs no account.</p>'),
  ('unknown', 'What we don’t know', '<p>Ciqual values are averages. A given brand can differ by a few calories; its label is the reference. Water loss varies with cooking: well-done meat loses more than rare, and the cooked weight worked out above (86 g) is an estimate, not a measurement. Some fat melts into the pan; Ciqual does not say how much, and it is not deducted here.</p>'),
 ],
 appel=('The right mince, the right line', 'Basal offers raw and cooked values, with the fat percentage in the name. Tracking is free, ad-free and needs no account.'),
 sources=[SOURCE['en']],
 plus=[('peser', None, 'Weighing food raw or cooked', 'The mistake that doubles the calories of rice and pasta.'),
       ('filet-mignon', None, 'Pork tenderloin protein', 'Raw, cooked, per serving, and against other meats.'),
       ('r-steak', 'Recipe', 'Beef patty and potatoes', 'The recipe, with its calories per serving.')])

ES = dict(publie=DATE,
 title='Calorías de la carne picada: 5 %, 15 %, cruda o cocinada',
 desc='Carne picada de ternera por 100 g: 130 kcal al 5 % de grasa, 215 kcal al 15 %, cruda. Valores crudos y cocinados de la tabla Ciqual, por hamburguesa.',
 court='Calorías de la carne picada', surtitre='Comidas',
 h1='Calorías de la carne picada: 5, 10, 15 o 20 % de grasa, cruda o cocinada',
 chapeau='Una hamburguesa de ternera al 5 % de grasa aporta 130 kcal por 100 g en crudo; al 20 %, aporta 249: casi el doble, con algo menos de proteína. El porcentaje de la bandeja cuenta más que todo lo demás, y el valor cambia otra vez según peses antes o después de cocinar.',
 situation='Comes una hamburguesa o carne picada y no sabes qué línea elegir en tu app: 5 % o 15 %, cruda o cocinada. <strong>Con Basal:</strong> buscas el alimento, eliges el porcentaje de grasa de la bandeja y el estado en que lo pesaste; los valores vienen de la tabla Ciqual de la ANSES, la agencia francesa de seguridad alimentaria.',
 bref='Por 100 g de carne picada de ternera cruda: 130 kcal al 5 % de grasa, 170 kcal al 10 %, 215 kcal al 15 % y 249 kcal al 20 %. Cocinada, la misma carne aporta 155, 210, 239 y 265 kcal por 100 g, porque ha perdido agua. Una hamburguesa de 100 g cruda al 5 % aporta unos 22 g de proteína.',
 sections=[
  ('tabla', 'Calorías y proteínas de la carne picada por 100 g', tableau('Carne picada de ternera, por 100 g (tabla Ciqual, ANSES)', ['Grasa', 'Cruda: kcal', 'Cruda: proteína', 'Cocinada: kcal', 'Cocinada: proteína'], lignes(',', ' g')) + '<p>Los hidratos de carbono son nulos o casi. Toda la diferencia de calorías viene de la grasa: 4,6 g por 100 g en crudo al 5 %, 20 g al 20 %.</p>'),
  ('hamburguesa', 'Para una hamburguesa de 100 g o de 125 g', '<p>Las hamburguesas de ternera del comercio suelen pesar 100 g o 125 g en crudo (el peso viene en la bandeja):</p><ul><li><strong>100 g, 5 %</strong>: 130 kcal y 22 g de proteína;</li><li><strong>100 g, 15 %</strong>: 215 kcal y 20 g de proteína;</li><li><strong>125 g, 5 %</strong>: 163 kcal y 27 g de proteína;</li><li><strong>125 g, 15 %</strong>: 269 kcal y 25 g de proteína.</li></ul><p>Entre una hamburguesa de 125 g al 5 % y la misma al 15 %, la diferencia es de unas 106 kcal. Una al día durante una semana suma algo más de 700 kcal.</p>'),
  ('cocinada', 'Por qué la carne cocinada tiene más calorías por 100 g', '<p>La cocción no crea calorías: la carne pierde agua, así que lo que queda está más concentrado. Según los valores de Ciqual, y suponiendo que la proteína se queda en la carne, una hamburguesa de 100 g cruda al 5 % pesa solo unos 86 g una vez cocinada. Esos 86 g a 155 kcal por 100 g suman 133 kcal: casi exactamente las 130 kcal de la hamburguesa cruda.</p><p>Lo importante es elegir la línea que corresponde a lo que pesaste. Pesada en su bandeja: valor crudo. Pesada en el plato: valor cocinado. El detalle, para todos los alimentos, está en la guía <a href="@peser">pesar crudo o cocinado</a>.</p>'),
  ('elegir', 'Carne picada al 5 % o al 15 %: cuál elegir', '<ul><li><strong>Para una definición</strong>: la del 5 % da más proteína por menos calorías. Es la opción más sencilla para mantener un <a href="@deficit">déficit calórico</a>.</li><li><strong>Por sabor y textura</strong>: la del 15 % queda más jugosa. No es una mala elección, siempre que la apuntes como tal: el error más frecuente es comer 15 % y apuntar 5 %.</li><li><strong>Por la proteína</strong>: del 5 al 15 %, se mantiene cerca de 20 g por 100 g en crudo. Al 20 %, baja a 17 g.</li></ul><p>Para situar estas cantidades en tu día, la guía <a href="@proteines">cuántas proteínas al día</a> da las referencias, y la <a href="@calc-proteines">calculadora de proteínas</a> hace el cálculo para tu peso.</p>'),
  ('basal', 'Apuntarla en Basal', '<p>En Basal, buscas el alimento y eliges la línea que corresponde a tu bandeja: el porcentaje de grasa y el estado (crudo o cocinado) figuran en el nombre. Luego introduces el peso. Si siempre compras el mismo producto, el escáner de código de barras usa los valores de su etiqueta. Es gratuito, sin publicidad y sin cuenta.</p>'),
  ('desconocido', 'Lo que no sabemos', '<p>Los valores de Ciqual son medias. Una marca concreta puede apartarse en unas calorías; su etiqueta es la referencia. La pérdida de agua varía con la cocción: una carne muy hecha pierde más que una poco hecha, y el peso cocinado calculado arriba (86 g) es una estimación, no una medida. Parte de la grasa se queda en la sartén; Ciqual no dice cuánta, y no se descuenta aquí.</p>'),
 ],
 appel=('La carne correcta, la línea correcta', 'Basal te ofrece los valores crudos y cocinados, con el porcentaje de grasa en el nombre. El seguimiento es gratuito, sin publicidad y sin cuenta.'),
 sources=[SOURCE['es']],
 plus=[('peser', None, 'Pesar crudo o cocinado', 'El error que duplica las calorías del arroz y la pasta.'),
       ('filet-mignon', None, 'Proteínas del solomillo de cerdo', 'Crudo, cocinado, por ración y frente a otras carnes.'),
       ('r-steak', 'Receta', 'Hamburguesa con patatas', 'La receta, con sus calorías por ración.')])

DE = dict(publie=DATE,
 title='Hackfleisch Kalorien: 5 %, 15 %, roh oder gebraten',
 desc='Rinderhack pro 100 g: 130 kcal bei 5 % Fett, 215 kcal bei 15 %, roh. Rohe und gebratene Werte aus der Ciqual-Tabelle, pro Hacksteak.',
 court='Hackfleisch Kalorien', surtitre='Mahlzeiten',
 h1='Kalorien von Rinderhack: 5, 10, 15 oder 20 % Fett, roh oder gebraten',
 chapeau='Ein Rinderhacksteak mit 5 % Fett liefert 130 kcal pro 100 g roh, eines mit 20 % liefert 249: fast doppelt so viel, bei etwas weniger Protein. Der Prozentwert auf der Packung zählt mehr als alles andere, und der Wert ändert sich noch einmal, je nachdem, ob du vor oder nach dem Braten wiegst.',
 situation='Du isst ein Hacksteak oder Hackfleisch und weißt nicht, welche Zeile du in deiner App wählen sollst: 5 % oder 15 %, roh oder gebraten. <strong>Mit Basal:</strong> Du suchst das Lebensmittel, wählst den Fettanteil der Packung und den Zustand, in dem du gewogen hast; die Werte stammen aus der Ciqual-Tabelle der ANSES, der französischen Behörde für Lebensmittelsicherheit.',
 bref='Pro 100 g rohem Rinderhack: 130 kcal bei 5 % Fett, 170 kcal bei 10 %, 215 kcal bei 15 % und 249 kcal bei 20 %. Gebraten liefert dasselbe Fleisch 155, 210, 239 und 265 kcal pro 100 g, weil es Wasser verloren hat. Ein rohes Hacksteak von 100 g mit 5 % Fett liefert etwa 22 g Protein.',
 sections=[
  ('tabelle', 'Kalorien und Protein von Rinderhack pro 100 g', tableau('Rinderhack, pro 100 g (Ciqual-Tabelle, ANSES)', ['Fett', 'Roh: kcal', 'Roh: Protein', 'Gebraten: kcal', 'Gebraten: Protein'], lignes(',', ' g')) + '<p>Kohlenhydrate sind null oder fast null. Der gesamte Kalorienunterschied kommt vom Fett: 4,6 g pro 100 g roh bei 5 %, 20 g bei 20 %.</p>'),
  ('hacksteak', 'Für ein Hacksteak von 100 g oder 125 g', '<p>Hacksteaks aus dem Handel wiegen meist 100 g oder 125 g roh (das Gewicht steht auf der Packung):</p><ul><li><strong>100 g, 5 %</strong>: 130 kcal und 22 g Protein;</li><li><strong>100 g, 15 %</strong>: 215 kcal und 20 g Protein;</li><li><strong>125 g, 5 %</strong>: 163 kcal und 27 g Protein;</li><li><strong>125 g, 15 %</strong>: 269 kcal und 25 g Protein.</li></ul><p>Zwischen einem 125-g-Hacksteak mit 5 % und demselben mit 15 % liegen etwa 106 kcal. Eines pro Tag eine Woche lang ergibt etwas über 700 kcal.</p>'),
  ('gebraten', 'Warum gebratenes Hack mehr Kalorien pro 100 g hat', '<p>Braten erzeugt keine Kalorien: Das Fleisch verliert Wasser, also ist der Rest konzentrierter. Nach den Ciqual-Werten, und unter der Annahme, dass das Protein im Fleisch bleibt, wiegt ein rohes 100-g-Hacksteak mit 5 % Fett gebraten nur noch etwa 86 g. Diese 86 g mit 155 kcal pro 100 g ergeben 133 kcal: fast genau die 130 kcal des rohen Hacksteaks.</p><p>Entscheidend ist, die Zeile zu wählen, die zu dem passt, was du gewogen hast. Auf der Packung gewogen: roher Wert. Auf dem Teller gewogen: gebratener Wert. Die Details für alle Lebensmittel stehen im Ratgeber <a href="@peser">roh oder gekocht wiegen</a>.</p>'),
  ('auswahl', 'Hack mit 5 % oder 15 % Fett: was wählen', '<ul><li><strong>In einer Diät</strong>: 5 % liefert mehr Protein für weniger Kalorien. Das ist die einfachste Wahl, um ein <a href="@deficit">Kaloriendefizit</a> zu halten.</li><li><strong>Für Geschmack und Saftigkeit</strong>: 15 % bleibt saftiger. Das ist keine schlechte Wahl, solange du es auch so einträgst: Der häufigste Fehler ist, 15 % zu essen und 5 % einzutragen.</li><li><strong>Für Protein</strong>: Von 5 bis 15 % bleibt es bei etwa 20 g pro 100 g roh. Bei 20 % sinkt es auf 17 g.</li></ul><p>Um diese Mengen in deinen Tag einzuordnen, gibt der Ratgeber <a href="@proteines">wie viel Protein pro Tag</a> die Richtwerte, und der <a href="@calc-proteines">Proteinrechner</a> rechnet es für dein Gewicht aus.</p>'),
  ('basal', 'In Basal eintragen', '<p>In Basal suchst du das Lebensmittel und wählst die Zeile, die zu deiner Packung passt: Fettanteil und Zustand (roh oder gebraten) stehen im Namen. Dann gibst du das Gewicht ein. Kaufst du immer dasselbe Produkt, übernimmt der Barcode-Scanner die Werte von seinem Etikett. Das ist kostenlos, werbefrei und braucht kein Konto.</p>'),
  ('unbekannt', 'Was wir nicht wissen', '<p>Ciqual-Werte sind Durchschnittswerte. Eine bestimmte Marke kann um einige Kalorien abweichen; ihr Etikett ist maßgeblich. Der Wasserverlust hängt vom Garen ab: Durchgebratenes Fleisch verliert mehr als blutiges, und das oben berechnete Gargewicht (86 g) ist eine Schätzung, keine Messung. Ein Teil des Fetts bleibt in der Pfanne; Ciqual sagt nicht, wie viel, und es wird hier nicht abgezogen.</p>'),
 ],
 appel=('Das richtige Hack, die richtige Zeile', 'Basal bietet rohe und gebratene Werte, mit dem Fettanteil im Namen. Das Tracking ist kostenlos, werbefrei und braucht kein Konto.'),
 sources=[SOURCE['de']],
 plus=[('peser', None, 'Roh oder gekocht wiegen', 'Der Fehler, der die Kalorien von Reis und Nudeln verdoppelt.'),
       ('filet-mignon', None, 'Protein im Schweinefilet', 'Roh, gebraten, pro Portion und im Vergleich zu anderem Fleisch.'),
       ('r-steak', 'Rezept', 'Hacksteak mit Bratkartoffeln', 'Das Rezept, mit seinen Kalorien pro Portion.')])

PAGES = {l: article_seo(l, C, a, f'{l}-{C}') for l, a in (('en', EN), ('es', ES), ('de', DE))}
