from commun import U, article_seo, recette
from steak_hache import tableau

FR = '/quantite-pesto-pates.html'
DATE = '2026-11-27'
C = 'pesto'
for _l in ('en', 'es', 'de'):
    U.setdefault('r-pesto', {})[_l] = recette(_l, 'pates-pesto-poulet')[0]

MGP = 'https://www.mgp.fr/files/live/sites/mgp/files/PDF/Fiches%20recettes%20APMS/2.%20Pates%20au%20pesto.pdf'
MORRISONS = 'https://groceries.morrisons.com/products/Barilla-Pesto-Genovese-Pasta-Sauce-190g/113499733'

EN = dict(publie=DATE,
 title='How much pesto per 100 g of pasta? Amounts and calories',
 desc='Pesto for pasta: from 12 to 50 g per 100 g of dry pasta depending on the source. The calories of each amount, homemade or jarred, and how to use less.',
 court='How much pesto for pasta', surtitre='Meals',
 h1='How much pesto per 100 g of pasta? The amounts, and their calories',
 chapeau='Depending on the source, the advice ranges from 12 g to 50 g of pesto per 100 g of dry pasta: a fourfold difference. For an 80 g serving of pasta, that is anywhere from 37 to almost 200 kcal of sauce. The amount is not a detail: it decides whether the plate comes to 330 or 490 kcal.',
 situation='You are making pesto pasta and wondering how much to use, and how many calories it adds. <strong>With Basal:</strong> you weigh the pesto like the pasta; for a shop-bought jar, the barcode scanner uses the values on its label.',
 bref='A French healthy-eating recipe card uses 12.5 g of pesto per 100 g of pasta; a pesto maker recommends 50 g. With a pesto at 370 kcal per 100 g (the Ciqual average), a tablespoon of about 15 g provides roughly 55 kcal. For 80 g of dry pasta (291 kcal), 20 g of pesto brings the plate to about 365 kcal.',
 sections=[
  ('amounts', 'How much pesto per 100 g of pasta', '<p>There is no official amount. Here is what three verifiable sources give, scaled to 100 g of dry pasta:</p>' + tableau('Pesto per 100 g of dry pasta, by source', ['Source', 'Amount given', 'Per 100 g of pasta'], [
     ('Recipe card from the MGP, a French mutual insurer', '50 g for 400 g of pasta, 4 people (50 g for 320 g of wholewheat pasta in its balanced version)', '12.5 g (15.6 g)'),
     ('Basal recipe for <a href="@r-pesto">pesto pasta with chicken</a>', '115 g of homemade pesto for 200 g of pasta', 'about 57 g'),
     ('Usage advice on a Barilla pesto', '40 g for 80 g of pasta', '50 g')]) + '<p>The manufacturer recommends four times more than the healthy-eating recipe card. A practical middle ground: <strong>one tablespoon (about 15 g) per 100 g of pasta</strong> already gives a clear colour and flavour, especially with a little cooking water to spread the sauce.</p>'),
  ('calories', 'Pesto calories, amount by amount', '<p>For an 80 g serving of standard dry pasta (291 kcal according to Ciqual), with a pesto at 370 kcal per 100 g:</p><ul><li><strong>10 g of pesto</strong> (MGP amount): 37 kcal, a plate of about 328 kcal;</li><li><strong>20 g</strong> (a slightly heaped tablespoon): 74 kcal, about 365 kcal;</li><li><strong>40 g</strong> (the manufacturer’s advice): 148 kcal, about 439 kcal.</li></ul><p>With a richer pesto, such as Barilla’s (482 kcal per 100 g according to its label), the recommended 40 g come to 193 kcal and the plate to about 484 kcal. Almost all of these calories come from the oil: the Ciqual pesto sauce contains 35 g of fat per 100 g.</p>'),
  ('homemade', 'Homemade or jarred pesto', '<p>Homemade pesto is not necessarily lighter. The one in the Basal recipe (30 g of basil, 30 g of parmesan, 30 g of olive oil, 20 g of almonds and 5 g of garlic) comes to about 460 kcal per 100 g, based on the Ciqual values of each ingredient: the oil alone provides half. Its advantage lies elsewhere: you choose how much oil goes in. With 15 g of oil instead of 30, the same pesto loses about 135 kcal.</p><p>For a jar, the label is the reference: values vary widely from one brand to another.</p>'),
  ('lighter', 'Keeping the flavour with less pesto', '<ul><li><strong>Keep a ladle of cooking water</strong>: the starch binds the sauce, and a small amount of pesto coats all the pasta.</li><li><strong>Mix off the heat</strong>, in the serving dish: the basil keeps its aroma.</li><li><strong>Add volume that counts for little</strong>: cherry tomatoes, courgettes, rocket.</li><li><strong>Add protein</strong> (chicken, tuna, chickpeas) rather than more pasta: the plate is more filling for the same calories.</li></ul>'),
  ('basal', 'Logging it in Basal', '<p>In Basal, you log the pasta and the pesto as two lines, each with its weight. For a jar, the barcode scanner uses the values on the label; otherwise, searching for “pesto” offers the pesto sauce from the Ciqual table. If you often make the same recipe, you save it once with its ingredients and log your share in servings. This is free, ad-free and needs no account.</p>'),
  ('unknown', 'What we don’t know', '<p>The “right” amount of pesto is a matter of taste: no source is authoritative, and the three cited here do not agree. The pesto calories given are those of the Ciqual average (370 kcal per 100 g) or of a specific label; your jar may differ. The weight of a tablespoon depends on whether it is level or heaped: weighing is safer.</p>'),
 ],
 appel=('The sauce counts too', 'Pasta, pesto, oil: Basal adds up each line and shows you the meal total. Tracking is free, ad-free and needs no account.'),
 sources=['ANSES. <i>Ciqual French food composition table, 2025</i>: pesto sauce, prepacked; standard dry pasta, raw; fresh basil; parmesan; extra virgin olive oil; almond with skin; raw garlic.',
          f'MGP. <a href="{MGP}" hreflang="fr" lang="fr">“Pâtes au pesto” recipe card</a> (in French): 400 g of pasta and 50 g of pesto for 4 people.',
          f'Barilla, Pesto alla Genovese 190 g: usage advice (40 g of pesto for 80 g of dry pasta) and nutrition values, from the <a href="{MORRISONS}">Morrisons product page</a>, accessed on 27 November 2026.'],
 plus=[('r-pesto', 'Recipe', 'Pesto pasta with chicken', 'The homemade pesto, with its calories per serving.'),
       ('peser', None, 'Weighing food raw or cooked', 'The mistake that doubles the calories of rice and pasta.'),
       ('compter', None, 'How to count calories', 'The simple method, and the omissions that skew it.')])

ES = dict(publie=DATE,
 title='¿Cuánto pesto por 100 g de pasta? Cantidades y calorías',
 desc='Pesto para pasta: de 12 a 50 g por 100 g de pasta seca según la fuente. Las calorías de cada cantidad, casero o de bote, y cómo usar menos.',
 court='Cuánto pesto para la pasta', surtitre='Comidas',
 h1='¿Cuánto pesto por 100 g de pasta? Las cantidades y sus calorías',
 chapeau='Según la fuente, se recomienda entre 12 g y 50 g de pesto por 100 g de pasta seca: una diferencia de uno a cuatro. Para una ración de 80 g de pasta, son de 37 a casi 200 kcal de salsa. La cantidad no es un detalle: decide si el plato tiene 330 o 490 kcal.',
 situation='Preparas pasta al pesto y te preguntas cuánto poner y cuántas calorías añade. <strong>Con Basal:</strong> pesas el pesto como la pasta; con un bote del supermercado, el escáner de código de barras usa los valores de su etiqueta.',
 bref='Una ficha de receta francesa de alimentación equilibrada usa 12,5 g de pesto por 100 g de pasta; un fabricante de pesto recomienda 50 g. Con un pesto de 370 kcal por 100 g (media Ciqual), una cucharada de unos 15 g aporta unas 55 kcal. Para 80 g de pasta seca (291 kcal), 20 g de pesto llevan el plato a unas 365 kcal.',
 sections=[
  ('cantidades', 'Cuánto pesto por 100 g de pasta', '<p>No existe una cantidad oficial. Esto es lo que dan tres fuentes verificables, llevadas a 100 g de pasta seca:</p>' + tableau('Pesto por 100 g de pasta seca, según la fuente', ['Fuente', 'Cantidad indicada', 'Por 100 g de pasta'], [
     ('Ficha de receta de la MGP, mutua francesa', '50 g para 400 g de pasta, 4 personas (50 g para 320 g de pasta integral en su versión equilibrada)', '12,5 g (15,6 g)'),
     ('Receta Basal de <a href="@r-pesto">pasta con pesto y pollo</a>', '115 g de pesto casero para 200 g de pasta', 'unos 57 g'),
     ('Consejo de uso de un pesto Barilla', '40 g para 80 g de pasta', '50 g')]) + '<p>El fabricante recomienda cuatro veces más que la ficha de alimentación equilibrada. Una referencia práctica entre ambas: <strong>una cucharada (unos 15 g) por 100 g de pasta</strong> ya da un color y un sabor claros, sobre todo con un poco de agua de cocción para repartir la salsa.</p>'),
  ('calorias', 'Las calorías del pesto, cantidad por cantidad', '<p>Para una ración de 80 g de pasta seca normal (291 kcal según Ciqual), con un pesto de 370 kcal por 100 g:</p><ul><li><strong>10 g de pesto</strong> (cantidad MGP): 37 kcal, un plato de unas 328 kcal;</li><li><strong>20 g</strong> (una cucharada algo colmada): 74 kcal, unas 365 kcal;</li><li><strong>40 g</strong> (consejo del fabricante): 148 kcal, unas 439 kcal.</li></ul><p>Con un pesto más rico, como el de Barilla (482 kcal por 100 g según su etiqueta), los 40 g recomendados suman 193 kcal y el plato unas 484 kcal. Casi todas estas calorías vienen del aceite: la salsa pesto de la tabla Ciqual contiene 35 g de grasa por 100 g.</p>'),
  ('casero', 'Pesto casero o de bote', '<p>Un pesto casero no es necesariamente más ligero. El de la receta Basal (30 g de albahaca, 30 g de parmesano, 30 g de aceite de oliva, 20 g de almendras y 5 g de ajo) tiene unas 460 kcal por 100 g, según los valores Ciqual de cada ingrediente: el aceite aporta por sí solo la mitad. Su ventaja está en otra parte: tú eliges la cantidad de aceite. Con 15 g de aceite en vez de 30, el mismo pesto pierde unas 135 kcal.</p><p>Para un bote, la etiqueta es la referencia: los valores cambian mucho de una marca a otra.</p>'),
  ('aligerar', 'Mantener el sabor con menos pesto', '<ul><li><strong>Guarda un cucharón de agua de cocción</strong>: el almidón liga la salsa y una pequeña cantidad de pesto cubre toda la pasta.</li><li><strong>Mezcla fuera del fuego</strong>, en la fuente: la albahaca conserva su aroma.</li><li><strong>Añade volumen que cuenta poco</strong>: tomates cherry, calabacín, rúcula.</li><li><strong>Añade proteína</strong> (pollo, atún, garbanzos) en lugar de más pasta: el plato sacia más por las mismas calorías.</li></ul>'),
  ('basal', 'Apuntarlo en Basal', '<p>En Basal, apuntas la pasta y el pesto como dos líneas, cada una con su peso. Para un bote, el escáner de código de barras usa los valores de la etiqueta; si no, la búsqueda «pesto» propone la salsa pesto de la tabla Ciqual. Si haces a menudo la misma receta, la guardas una vez con sus ingredientes y apuntas tu parte en raciones. Es gratuito, sin publicidad y sin cuenta.</p>'),
  ('desconocido', 'Lo que no sabemos', '<p>La cantidad «correcta» de pesto es cuestión de gusto: ninguna fuente hace autoridad, y las tres citadas aquí no coinciden. Las calorías del pesto son las de la media Ciqual (370 kcal por 100 g) o las de una etiqueta concreta; tu bote puede apartarse. El peso de una cucharada depende de si está rasa o colmada: pesar es más seguro.</p>'),
 ],
 appel=('La salsa también cuenta', 'Pasta, pesto, aceite: Basal suma cada línea y te muestra el total de la comida. El seguimiento es gratuito, sin publicidad y sin cuenta.'),
 sources=['ANSES. <i>Tabla de composición de alimentos Ciqual 2025</i>: salsa pesto envasada; pasta seca normal cruda; albahaca fresca; parmesano; aceite de oliva virgen extra; almendra con piel; ajo crudo.',
          f'MGP. <a href="{MGP}" hreflang="fr" lang="fr">Ficha de receta «Pâtes au pesto»</a> (en francés): 400 g de pasta y 50 g de pesto para 4 personas.',
          f'Barilla, Pesto alla Genovese 190 g: consejo de uso (40 g de pesto para 80 g de pasta seca) y valores nutricionales, según la <a href="{MORRISONS}" hreflang="en" lang="en">ficha de producto de Morrisons</a> (en inglés), consultada el 27 de noviembre de 2026.'],
 plus=[('r-pesto', 'Receta', 'Pasta con pesto y pollo', 'El pesto casero, con sus calorías por ración.'),
       ('peser', None, 'Pesar crudo o cocinado', 'El error que duplica las calorías del arroz y la pasta.'),
       ('compter', None, 'Cómo contar calorías', 'El método sencillo y los olvidos que lo falsean.')])

DE = dict(publie=DATE,
 title='Wie viel Pesto pro 100 g Nudeln? Mengen und Kalorien',
 desc='Pesto für Nudeln: je nach Quelle 12 bis 50 g pro 100 g trockene Nudeln. Die Kalorien jeder Menge, selbst gemacht oder aus dem Glas.',
 court='Wie viel Pesto für Nudeln', surtitre='Mahlzeiten',
 h1='Wie viel Pesto pro 100 g Nudeln? Die Mengen und ihre Kalorien',
 chapeau='Je nach Quelle werden 12 g bis 50 g Pesto pro 100 g trockene Nudeln empfohlen: ein Unterschied um das Vierfache. Für eine Portion von 80 g Nudeln sind das 37 bis fast 200 kcal Soße. Die Menge ist kein Detail: Sie entscheidet, ob der Teller 330 oder 490 kcal hat.',
 situation='Du machst Nudeln mit Pesto und fragst dich, wie viel du nehmen sollst und wie viele Kalorien das bringt. <strong>Mit Basal:</strong> Du wiegst das Pesto wie die Nudeln; bei einem Glas aus dem Supermarkt übernimmt der Barcode-Scanner die Werte vom Etikett.',
 bref='Eine französische Rezeptkarte für ausgewogene Ernährung nimmt 12,5 g Pesto pro 100 g Nudeln; ein Pesto-Hersteller empfiehlt 50 g. Bei einem Pesto mit 370 kcal pro 100 g (Ciqual-Durchschnitt) liefert ein Esslöffel von etwa 15 g rund 55 kcal. Für 80 g trockene Nudeln (291 kcal) bringen 20 g Pesto den Teller auf etwa 365 kcal.',
 sections=[
  ('mengen', 'Wie viel Pesto pro 100 g Nudeln', '<p>Eine offizielle Menge gibt es nicht. Das geben drei überprüfbare Quellen an, umgerechnet auf 100 g trockene Nudeln:</p>' + tableau('Pesto pro 100 g trockene Nudeln, je nach Quelle', ['Quelle', 'Angegebene Menge', 'Pro 100 g Nudeln'], [
     ('Rezeptkarte der MGP, eines französischen Versicherers auf Gegenseitigkeit', '50 g für 400 g Nudeln, 4 Personen (50 g für 320 g Vollkornnudeln in der ausgewogenen Variante)', '12,5 g (15,6 g)'),
     ('Basal-Rezept <a href="@r-pesto">Pasta mit Pesto und Hähnchen</a>', '115 g selbst gemachtes Pesto für 200 g Nudeln', 'etwa 57 g'),
     ('Verwendungshinweis eines Barilla-Pestos', '40 g für 80 g Nudeln', '50 g')]) + '<p>Der Hersteller empfiehlt viermal so viel wie die Rezeptkarte. Ein praktischer Mittelweg: <strong>ein Esslöffel (etwa 15 g) pro 100 g Nudeln</strong> gibt schon deutlich Farbe und Geschmack, vor allem mit etwas Nudelwasser, um die Soße zu verteilen.</p>'),
  ('kalorien', 'Pesto-Kalorien, Menge für Menge', '<p>Für eine Portion von 80 g normalen trockenen Nudeln (291 kcal laut Ciqual), mit einem Pesto von 370 kcal pro 100 g:</p><ul><li><strong>10 g Pesto</strong> (MGP-Menge): 37 kcal, ein Teller mit etwa 328 kcal;</li><li><strong>20 g</strong> (ein leicht gehäufter Esslöffel): 74 kcal, etwa 365 kcal;</li><li><strong>40 g</strong> (Empfehlung des Herstellers): 148 kcal, etwa 439 kcal.</li></ul><p>Mit einem reichhaltigeren Pesto wie dem von Barilla (482 kcal pro 100 g laut Etikett) ergeben die empfohlenen 40 g 193 kcal und der Teller etwa 484 kcal. Fast alle diese Kalorien kommen vom Öl: Die Pesto-Soße der Ciqual-Tabelle enthält 35 g Fett pro 100 g.</p>'),
  ('selbstgemacht', 'Selbst gemachtes Pesto oder aus dem Glas', '<p>Selbst gemachtes Pesto ist nicht unbedingt leichter. Das aus dem Basal-Rezept (30 g Basilikum, 30 g Parmesan, 30 g Olivenöl, 20 g Mandeln und 5 g Knoblauch) hat nach den Ciqual-Werten jeder Zutat etwa 460 kcal pro 100 g: Das Öl allein liefert die Hälfte. Sein Vorteil liegt woanders: Du bestimmst die Ölmenge. Mit 15 g Öl statt 30 verliert dasselbe Pesto etwa 135 kcal.</p><p>Bei einem Glas ist das Etikett maßgeblich: Die Werte unterscheiden sich stark von Marke zu Marke.</p>'),
  ('leichter', 'Den Geschmack mit weniger Pesto behalten', '<ul><li><strong>Behalte eine Kelle Nudelwasser</strong>: Die Stärke bindet die Soße, und eine kleine Menge Pesto überzieht alle Nudeln.</li><li><strong>Misch abseits vom Herd</strong>, in der Servierschüssel: Das Basilikum behält sein Aroma.</li><li><strong>Füge Volumen hinzu, das wenig zählt</strong>: Kirschtomaten, Zucchini, Rucola.</li><li><strong>Füge Protein hinzu</strong> (Hähnchen, Thunfisch, Kichererbsen) statt mehr Nudeln: Der Teller sättigt mehr bei gleichen Kalorien.</li></ul>'),
  ('basal', 'In Basal eintragen', '<p>In Basal trägst du Nudeln und Pesto als zwei Zeilen ein, jede mit ihrem Gewicht. Bei einem Glas übernimmt der Barcode-Scanner die Werte vom Etikett; sonst schlägt die Suche „Pesto“ die Pesto-Soße aus der Ciqual-Tabelle vor. Kochst du oft dasselbe Rezept, speicherst du es einmal mit seinen Zutaten und trägst deinen Anteil in Portionen ein. Das ist kostenlos, werbefrei und braucht kein Konto.</p>'),
  ('unbekannt', 'Was wir nicht wissen', '<p>Die „richtige“ Pesto-Menge ist Geschmackssache: Keine Quelle ist maßgeblich, und die drei hier genannten stimmen nicht überein. Die Pesto-Kalorien sind die des Ciqual-Durchschnitts (370 kcal pro 100 g) oder eines bestimmten Etiketts; dein Glas kann abweichen. Das Gewicht eines Esslöffels hängt davon ab, ob er gestrichen oder gehäuft ist: Wiegen ist sicherer.</p>'),
 ],
 appel=('Die Soße zählt mit', 'Nudeln, Pesto, Öl: Basal addiert jede Zeile und zeigt dir die Summe der Mahlzeit. Das Tracking ist kostenlos, werbefrei und braucht kein Konto.'),
 sources=['ANSES. <i>Französische Lebensmittel-Nährwerttabelle Ciqual 2025</i>: Pesto-Soße, Fertigprodukt; normale trockene Nudeln, roh; frisches Basilikum; Parmesan; natives Olivenöl extra; Mandel mit Haut; Knoblauch roh.',
          f'MGP. <a href="{MGP}" hreflang="fr" lang="fr">Rezeptkarte „Pâtes au pesto“</a> (auf Französisch): 400 g Nudeln und 50 g Pesto für 4 Personen.',
          f'Barilla, Pesto alla Genovese 190 g: Verwendungshinweis (40 g Pesto für 80 g trockene Nudeln) und Nährwerte, laut <a href="{MORRISONS}" hreflang="en" lang="en">Produktseite von Morrisons</a> (auf Englisch), abgerufen am 27. November 2026.'],
 plus=[('r-pesto', 'Rezept', 'Pasta mit Pesto und Hähnchen', 'Das selbst gemachte Pesto, mit seinen Kalorien pro Portion.'),
       ('peser', None, 'Roh oder gekocht wiegen', 'Der Fehler, der die Kalorien von Reis und Nudeln verdoppelt.'),
       ('compter', None, 'Kalorien zählen', 'Die einfache Methode und die Lücken, die alles verfälschen.')])

PAGES = {l: article_seo(l, C, a, f'{l}-{C}') for l, a in (('en', EN), ('es', ES), ('de', DE))}
