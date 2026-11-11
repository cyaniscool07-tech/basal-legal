from commun import U, page

FR = '/peser-cru-ou-cuit.html'
DATE = '2026-11-11'
C = 'peser'
SOM = ['pourquoi', 'tableau', 'erreur', 'methode', 'plat', 'inconnu', 'sources']


def corps(l, t):
    p = lambda xs: '\n'.join(f'      <p>{x}</p>' for x in xs)
    rows = '\n'.join('            <tr>' + ''.join(f'<td>{x}</td>' for x in r) + '</tr>' for r in t['tab'])
    calc = lambda titre, label, lignes: f'''      <div class="calcul" role="group" aria-label="{label}">
        <div class="titre">{titre}</div>
''' + '\n'.join(f'        <div class="ligne"><span>{a}</span><b>{b}</b></div>' for a, b in lignes) + '\n      </div>'
    meth = '\n'.join(f'        <li><strong>{a}</strong> {b}</li>' for a, b in t['methode'])
    etapes = '\n'.join(f'        <li>{x}</li>' for x in t['etapes'])
    inc = t['inc']
    plus = '\n'.join(f'        <a class="guide" href="{u}"><span class="surtitre" style="margin:0">{s}</span><h3>{h}</h3><p>{d}</p></a>' for u, s, h, d in t['plus'])
    return f'''      <div class="en-bref">
        <p class="surtitre">{t["bref_t"]}</p>
        <p>{t["bref"]}</p>
      </div>

      <h2 id="pourquoi">{t["s"][0]}</h2>
{p(t["a"])}

      <h2 id="tableau">{t["s"][1]}</h2>
      <div class="tableau">
        <table>
          <caption>{t["tab_cap"]}</caption>
          <thead><tr>{''.join(f'<th scope="col">{c}</th>' for c in t["tab_cols"])}</tr></thead>
          <tbody>
{rows}
          </tbody>
        </table>
        <p class="source">{t["tab_src"]}</p>
      </div>

      <h2 id="erreur">{t["s"][2]}</h2>
      <p>{t["err_intro"]}</p>
{calc(*t["calc1"])}
{calc(*t["calc2"])}
      <p>{t["err_fin"]}</p>

      <h2 id="methode">{t["s"][3]}</h2>
      <ul>
{meth}
      </ul>

      <h2 id="plat">{t["s"][4]}</h2>
      <p>{t["plat"]}</p>
      <ol>
{etapes}
      </ol>
      <p>{t["plat_fin"]}</p>

      <h2 id="inconnu">{t["s"][5]}</h2>
      <div class="inconnu">
        <p><strong>{inc[0][0]}</strong> {inc[0][1]}</p>
        <p><strong>{inc[1][0]}</strong> {inc[1][1]}</p>
        <p style="margin:0"><strong>{inc[2][0]}</strong> {inc[2][1]}</p>
      </div>

      <div class="appel-contexte">
        <div><strong>{t["appel_t"]}</strong><p>{t["appel"]}</p></div>
        <a class="bouton vif" href="{U["accueil"][l]}#download">{t["dl"]}</a>
      </div>

      <h2 id="sources">{t["s"][6]}</h2>
      <ol class="sources">
        <li>ANSES. Ciqual 2025 food composition table. Licence Ouverte / Etalab 2.0.</li>
        <li>Bognár A. <i>Tables on weight yield of food and retention factors of food constituents for the calculation of nutrient composition of cooked foods (dishes)</i>. Bundesforschungsanstalt für Ernährung, Karlsruhe, 2002.</li>
        <li>USDA, Agricultural Research Service. <i>USDA Table of Cooking Yields for Meat and Poultry</i>, Release 2, 2014.</li>
      </ol>
      <p>{t["methode_lien"]}</p>

      <h2 style="font-size:1.5rem;margin-top:48px">{t["plus_t"]}</h2>
      <div class="guides" style="grid-template-columns:repeat(auto-fit,minmax(240px,1fr))">
{plus}
      </div>'''


EN = dict(bref_t='In short',
    bref='Weigh raw when you can, and choose the “raw” or “dry” food in the table: that figure does not depend on how you cook. If you can only weigh cooked, choose the “cooked” food. The mistake to avoid is mixing the two: 80 g of dry pasta is 291 kcal, but if you weigh the 174 g of cooked pasta it makes and choose “pasta, raw”, you count 633, more than double.',
    s=['Why weight changes when cooking', 'Raw and cooked, food by food', 'What the mistake costs', 'The simplest method', 'One dish for several servings', 'What we do not know', 'Sources'],
    a=['Cooking neither creates nor destroys calories in any meaningful amount. What changes is water. Dry starches (pasta, rice, couscous, quinoa, pulses) absorb it: their weight is multiplied by two to three, and their calories per 100 g are divided accordingly. Meat and fish lose it, with a little fat: they weigh less after cooking, and each 100 g is more calorie-dense.',
       'The same food therefore has two values per 100 g, both correct. The ANSES Ciqual table used by Basal often gives both.'],
    tab_cap='Energy per 100 g, and weight after cooking 100 g of raw food', tab_cols=['Food', 'Raw or dry', 'Cooked', '100 g raw gives'],
    tab=[['Standard pasta', '364 kcal', '167 kcal', '≈ 218 g'], ['White rice', '350 kcal', '155 kcal', '≈ 226 g'], ['Quinoa', '358 kcal', '149 kcal', '≈ 240 g'], ['Green lentils', '327 kcal', '125 kcal', '≈ 262 g'],
         ['Potato, boiled', '80 kcal', '81 kcal', '≈ 99 g'], ['Chicken breast, pan-fried', '110 kcal', '141 kcal', '≈ 78 g'], ['Turkey escalope, pan-fried', '108 kcal', '124 kcal', '≈ 87 g'], ['Minced beef 10% fat', '170 kcal', '210 kcal', '≈ 81 g']],
    tab_src='Energy: Ciqual 2025 table (ANSES), as built into the app. Weight after cooking: derived from the ratio of the two energies, assuming cooking only changes water. It is a good approximation for starches; for meat, which also loses a little fat, it is an order of magnitude.',
    err_intro='These results are calculated from the values of the table built into the app: a test checks that they stay correct if the table is updated.',
    calc1=('80 g of dry pasta, about 174 g once cooked', 'Weighing mistake examples', [('Weighed dry, “raw” entry', '291 kcal'), ('Weighed cooked, “cooked” entry', '291 kcal'), ('Weighed cooked, “raw” entry', '633 kcal'), ('Weighed dry, “cooked” entry', '134 kcal')]),
    calc2=('150 g of raw chicken breast, about 117 g once pan-fried', 'Weighing mistake examples for chicken', [('Weighed raw, “raw” entry', '165 kcal'), ('Weighed cooked, “raw” entry', '129 kcal'), ('Weighed raw, “pan-fried” entry', '212 kcal')]),
    err_fin=f'On starches, the mistake is counted in hundreds of calories per plate, either way. On meat it is smaller, around forty calories, but it also affects protein. Repeated every day, it is enough to explain why a deficit “on paper” does not move the scale (see <a href="{U["deficit"]["en"]}">the calorie deficit</a>).',
    methode=[('Weigh raw or dry, before cooking, when possible.', 'The figure depends neither on cooking time, nor on drained water, nor on your saucepan. It is also, most often, the state shown on packets.'),
             ('If you can only weigh cooked', '(canteen, ready meal, yesterday’s leftovers), choose the “cooked” entry. The result will be a little less precise, but correct.'),
             ('Read the food’s name before confirming.', 'In a search, “white rice, raw” and “white rice, cooked” come one after the other. That is where the mistake slips in.'),
             ('Keep the same habit.', 'A small constant error corrects itself if your expenditure is recalculated from your actual weight. An error that changes from day to day does not.')],
    plat='For a dish cooked in one go (bolognese, curry, chilli), you cannot weigh each serving raw. The reliable method:',
    etapes=['Weigh all the ingredients raw and add up their calories.', 'Weigh the whole dish once cooked, without the pan.', 'Calories in your serving = total × (weight of your serving ÷ weight of the cooked dish).'],
    plat_fin=f'In Basal, a recipe is entered with raw quantities, and a batch can record the weight of the cooked dish: the app then shows the cooked weight of one serving, to weigh on your plate. The <a href="{U["meal-prep"]["en"]}">meal prep guide</a> covers how to store these dishes.',
    inc=[('Your cooking yield.', 'Very soft pasta absorbs more water than al dente pasta, well-done meat loses more than rare. A table’s “cooked” values correspond to average cooking.'),
         ('Cooking fat.', 'A spoonful of oil is about 90 kcal, and it appears in neither the raw nor the cooked value of a table. It is counted separately.'),
         ('The share of fat lost by meat.', 'It varies with the cut and the cooking. That is why the table’s weights after cooking are an order of magnitude for meat.')],
    appel_t='Raw and cooked, side by side in the search', appel='Basal includes the Ciqual table with both states when they exist, and calculates your recipes from raw quantities. Tracking is free and needs no account.', dl='Download',
    methode_lien=f'How the app calculates recipes and servings is explained on the <a href="{U["methode"]["en"]}">Method</a> page.',
    plus_t='Going further', plus=[(U['meal-prep']['en'], 'Guide', 'Meal prep: prepare your week', 'Which recipes to choose, how many days they keep.'),
                                  (U['recettes']['en'], 'Recipes', 'Calculated recipes', 'Everyday recipes, calories and macros per serving.'),
                                  (U['deficit']['en'], 'Guide', 'The calorie deficit', 'How much less to eat to lose weight, without overdoing it.')])

ES = dict(bref_t='En resumen',
    bref='Pesa en crudo cuando puedas y elige el alimento «crudo» o «seco» en la tabla: esa cifra no depende de tu cocción. Si solo puedes pesar cocinado, elige el alimento «cocido». El error que hay que evitar es mezclar ambos: 80 g de pasta seca son 291 kcal, pero si pesas los 174 g de pasta cocida que dan y eliges «pasta cruda», cuentas 633, más del doble.',
    s=['Por qué cambia el peso al cocinar', 'Crudo y cocido, alimento por alimento', 'Lo que cuesta el error', 'El método más sencillo', 'Un plato para varias raciones', 'Lo que no se sabe', 'Fuentes'],
    a=['La cocción no crea ni destruye calorías en cantidad apreciable. Lo que cambia es el agua. Los feculentos secos (pasta, arroz, sémola, quinoa, legumbres) la absorben: su peso se multiplica por dos o tres y sus calorías por 100 g se dividen en la misma proporción. La carne y el pescado la pierden, con algo de grasa: pesan menos tras la cocción y cada 100 g es más calórico.',
       'El mismo alimento tiene por tanto dos valores por 100 g, los dos exactos. La tabla Ciqual de la ANSES, que usa Basal, suele dar ambos.'],
    tab_cap='Energía por 100 g y peso tras cocinar 100 g de alimento crudo', tab_cols=['Alimento', 'Crudo o seco', 'Cocido', '100 g crudos dan'],
    tab=[['Pasta estándar', '364 kcal', '167 kcal', '≈ 218 g'], ['Arroz blanco', '350 kcal', '155 kcal', '≈ 226 g'], ['Quinoa', '358 kcal', '149 kcal', '≈ 240 g'], ['Lentejas verdes', '327 kcal', '125 kcal', '≈ 262 g'],
         ['Patata, hervida', '80 kcal', '81 kcal', '≈ 99 g'], ['Pechuga de pollo, a la sartén', '110 kcal', '141 kcal', '≈ 78 g'], ['Filete de pavo, a la sartén', '108 kcal', '124 kcal', '≈ 87 g'], ['Carne picada 10 % de grasa', '170 kcal', '210 kcal', '≈ 81 g']],
    tab_src='Energía: tabla Ciqual 2025 (ANSES), tal como está integrada en la aplicación. Peso tras la cocción: deducido de la relación entre ambas energías, suponiendo que la cocción solo cambia el agua. Es una buena aproximación para los feculentos; para la carne, que también pierde algo de grasa, es un orden de magnitud.',
    err_intro='Estos resultados se calculan con los valores de la tabla integrada en la aplicación: una prueba automática comprueba que siguen siendo exactos si la tabla se actualiza.',
    calc1=('80 g de pasta seca, unos 174 g una vez cocida', 'Ejemplos de error al pesar', [('Pesada seca, entrada «cruda»', '291 kcal'), ('Pesada cocida, entrada «cocida»', '291 kcal'), ('Pesada cocida, entrada «cruda»', '633 kcal'), ('Pesada seca, entrada «cocida»', '134 kcal')]),
    calc2=('150 g de pechuga de pollo cruda, unos 117 g una vez hecha a la sartén', 'Ejemplos de error al pesar el pollo', [('Pesada cruda, entrada «cruda»', '165 kcal'), ('Pesada cocinada, entrada «cruda»', '129 kcal'), ('Pesada cruda, entrada «a la sartén»', '212 kcal')]),
    err_fin=f'Con los feculentos, el error se cuenta en cientos de calorías por plato, en un sentido o en otro. Con la carne es menor, unas cuarenta calorías, pero también afecta a las proteínas. Repetido cada día, basta para explicar que un déficit «sobre el papel» no mueva la báscula (ver <a href="{U["deficit"]["es"]}">el déficit calórico</a>).',
    methode=[('Pesa en crudo o en seco, antes de cocinar, cuando sea posible.', 'La cifra no depende ni del tiempo de cocción, ni del agua escurrida, ni de tu cazuela. Además, suele ser el estado indicado en los paquetes.'),
             ('Si solo puedes pesar cocinado', '(comedor, plato preparado, sobras de ayer), elige la entrada «cocido». El resultado será algo menos preciso, pero correcto.'),
             ('Lee el nombre del alimento antes de confirmar.', 'En una búsqueda, «arroz blanco, crudo» y «arroz blanco, cocido» aparecen seguidos. Ahí es donde se cuela el error.'),
             ('Mantén la misma costumbre.', 'Un pequeño error constante se corrige solo si tu gasto se recalcula con tu peso real. Un error que cambia de un día a otro, no.')],
    plat='Para un plato cocinado de una vez (boloñesa, curry, chili), no se puede pesar en crudo cada ración. El método fiable:',
    etapes=['Pesa todos los ingredientes en crudo y suma sus calorías.', 'Pesa el plato entero una vez cocinado, sin la cazuela.', 'Calorías de tu ración = total × (peso de tu ración ÷ peso del plato cocinado).'],
    plat_fin=f'En Basal, una receta se introduce con las cantidades en crudo, y una preparación en lote puede anotar el peso del plato cocinado: la aplicación muestra entonces el peso cocinado de una ración, para pesarlo en tu plato. La <a href="{U["meal-prep"]["es"]}">guía del meal prep</a> explica cómo conservar estos platos.',
    inc=[('El rendimiento de tu cocción.', 'La pasta muy cocida absorbe más agua que la pasta al dente, y una carne muy hecha pierde más que una poco hecha. Los valores «cocidos» de una tabla corresponden a una cocción media.'),
         ('La grasa de cocinar.', 'Una cucharada de aceite son unas 90 kcal, y no aparece ni en el valor crudo ni en el cocido de una tabla. Se cuenta aparte.'),
         ('La parte de grasa que pierde la carne.', 'Varía según la pieza y la cocción. Por eso los pesos tras la cocción de la tabla son un orden de magnitud para la carne.')],
    appel_t='Crudo y cocido, juntos en la búsqueda', appel='Basal incluye la tabla Ciqual con sus dos estados cuando existen y calcula tus recetas a partir de las cantidades en crudo. El seguimiento es gratis y sin cuenta.', dl='Descargar',
    methode_lien=f'La forma en que la aplicación calcula las recetas y las raciones se detalla en la página <a href="{U["methode"]["es"]}">Método</a>.',
    plus_t='Para saber más', plus=[(U['meal-prep']['es'], 'Guía', 'Meal prep: prepara tu semana', 'Qué recetas elegir y cuántos días se conservan.'),
                                   (U['recettes']['es'], 'Recetas', 'Recetas calculadas', 'Recetas del día a día, calorías y macros por ración.'),
                                   (U['deficit']['es'], 'Guía', 'El déficit calórico', 'Cuánto comer de menos para perder peso, sin pasarse.')])

DE = dict(bref_t='Kurz gesagt',
    bref='Wiege roh, wenn du kannst, und wähle in der Tabelle das Lebensmittel „roh“ oder „trocken“: Diese Zahl hängt nicht von deiner Zubereitung ab. Kannst du nur gegart wiegen, wähle „gegart“. Der Fehler, den du vermeiden solltest, ist beides zu mischen: 80 g trockene Nudeln haben 291 kcal, aber wenn du die 174 g gekochten Nudeln wiegst und „Nudeln, roh“ wählst, zählst du 633, mehr als das Doppelte.',
    s=['Warum sich das Gewicht beim Kochen ändert', 'Roh und gegart, Lebensmittel für Lebensmittel', 'Was der Fehler kostet', 'Die einfachste Methode', 'Ein Gericht für mehrere Portionen', 'Was man nicht weiß', 'Quellen'],
    a=['Kochen erzeugt oder vernichtet keine nennenswerte Menge Kalorien. Was sich ändert, ist das Wasser. Trockene Stärkebeilagen (Nudeln, Reis, Couscous, Quinoa, Hülsenfrüchte) nehmen es auf: Ihr Gewicht verdoppelt bis verdreifacht sich, und ihre Kalorien pro 100 g sinken entsprechend. Fleisch und Fisch verlieren Wasser, dazu etwas Fett: Sie wiegen nach dem Garen weniger, und jede 100 g sind kalorienreicher.',
       'Dasselbe Lebensmittel hat also zwei Werte pro 100 g, beide richtig. Die Ciqual-Tabelle der ANSES, die Basal nutzt, nennt oft beide.'],
    tab_cap='Energie pro 100 g und Gewicht nach dem Garen von 100 g Rohware', tab_cols=['Lebensmittel', 'Roh oder trocken', 'Gegart', '100 g roh ergeben'],
    tab=[['Nudeln, Standard', '364 kcal', '167 kcal', '≈ 218 g'], ['Weißer Reis', '350 kcal', '155 kcal', '≈ 226 g'], ['Quinoa', '358 kcal', '149 kcal', '≈ 240 g'], ['Grüne Linsen', '327 kcal', '125 kcal', '≈ 262 g'],
         ['Kartoffel, gekocht', '80 kcal', '81 kcal', '≈ 99 g'], ['Hähnchenbrust, gebraten', '110 kcal', '141 kcal', '≈ 78 g'], ['Putenschnitzel, gebraten', '108 kcal', '124 kcal', '≈ 87 g'], ['Rinderhack 10 % Fett', '170 kcal', '210 kcal', '≈ 81 g']],
    tab_src='Energie: Ciqual-Tabelle 2025 (ANSES), wie in der App enthalten. Gewicht nach dem Garen: aus dem Verhältnis der beiden Energiewerte abgeleitet, unter der Annahme, dass sich beim Garen nur das Wasser ändert. Für Stärkebeilagen ist das eine gute Näherung; für Fleisch, das auch etwas Fett verliert, eine Größenordnung.',
    err_intro='Diese Ergebnisse sind aus den Werten der in der App enthaltenen Tabelle berechnet: Ein Test prüft, dass sie stimmen, wenn die Tabelle aktualisiert wird.',
    calc1=('80 g trockene Nudeln, gekocht etwa 174 g', 'Beispiele für Wiegefehler', [('Trocken gewogen, Eintrag „roh“', '291 kcal'), ('Gekocht gewogen, Eintrag „gekocht“', '291 kcal'), ('Gekocht gewogen, Eintrag „roh“', '633 kcal'), ('Trocken gewogen, Eintrag „gekocht“', '134 kcal')]),
    calc2=('150 g rohe Hähnchenbrust, gebraten etwa 117 g', 'Beispiele für Wiegefehler bei Hähnchen', [('Roh gewogen, Eintrag „roh“', '165 kcal'), ('Gebraten gewogen, Eintrag „roh“', '129 kcal'), ('Roh gewogen, Eintrag „gebraten“', '212 kcal')]),
    err_fin=f'Bei Stärkebeilagen geht der Fehler in die Hunderte Kalorien pro Teller, in die eine oder andere Richtung. Bei Fleisch ist er kleiner, etwa vierzig Kalorien, betrifft aber auch das Eiweiß. Täglich wiederholt reicht er, um zu erklären, warum ein Defizit „auf dem Papier“ die Waage nicht bewegt (siehe <a href="{U["deficit"]["de"]}">Kaloriendefizit</a>).',
    methode=[('Wiege roh oder trocken, vor dem Kochen, wenn möglich.', 'Die Zahl hängt weder von der Kochzeit noch vom abgegossenen Wasser noch von deinem Topf ab. Meist ist es auch der Zustand, der auf der Packung steht.'),
             ('Wenn du nur gegart wiegen kannst', '(Kantine, Fertiggericht, Reste von gestern), wähle den Eintrag „gegart“. Das Ergebnis ist etwas ungenauer, aber richtig.'),
             ('Lies den Namen des Lebensmittels vor dem Bestätigen.', 'In einer Suche stehen „Reis, weiß, roh“ und „Reis, weiß, gekocht“ direkt nacheinander. Genau da schleicht sich der Fehler ein.'),
             ('Bleib bei derselben Gewohnheit.', 'Ein kleiner, gleichbleibender Fehler korrigiert sich von selbst, wenn dein Verbrauch aus deinem tatsächlichen Gewicht neu berechnet wird. Ein Fehler, der sich von Tag zu Tag ändert, nicht.')],
    plat='Bei einem Gericht, das auf einmal gekocht wird (Bolognese, Curry, Chili), kann man nicht jede Portion roh wiegen. Die zuverlässige Methode:',
    etapes=['Wiege alle Zutaten roh und addiere ihre Kalorien.', 'Wiege das ganze Gericht nach dem Kochen, ohne den Topf.', 'Kalorien deiner Portion = Summe × (Gewicht deiner Portion ÷ Gewicht des gekochten Gerichts).'],
    plat_fin=f'In Basal wird ein Rezept mit Rohmengen eingegeben, und bei einer Vorratsportion lässt sich das Gewicht des fertigen Gerichts notieren: Die App zeigt dann das gegarte Gewicht einer Portion, das du auf deinem Teller abwiegst. Der <a href="{U["meal-prep"]["de"]}">Meal-Prep-Ratgeber</a> erklärt, wie man diese Gerichte aufbewahrt.',
    inc=[('Der Ertrag deiner Zubereitung.', 'Sehr weiche Nudeln nehmen mehr Wasser auf als al dente gekochte, gut durchgebratenes Fleisch verliert mehr als englisches. Die „gegart“-Werte einer Tabelle entsprechen einer durchschnittlichen Zubereitung.'),
         ('Das Bratfett.', 'Ein Löffel Öl hat etwa 90 kcal und taucht weder im Roh- noch im Garwert einer Tabelle auf. Es wird extra gezählt.'),
         ('Der Fettanteil, den Fleisch verliert.', 'Er hängt vom Stück und der Zubereitung ab. Deshalb sind die Gewichte nach dem Garen in der Tabelle für Fleisch eine Größenordnung.')],
    appel_t='Roh und gegart, nebeneinander in der Suche', appel='Basal enthält die Ciqual-Tabelle mit beiden Zuständen, wo es sie gibt, und berechnet deine Rezepte aus Rohmengen. Das Tracking ist kostenlos und ohne Konto.', dl='Herunterladen',
    methode_lien=f'Wie die App Rezepte und Portionen berechnet, steht auf der Seite <a href="{U["methode"]["de"]}">Methode</a>.',
    plus_t='Weiterlesen', plus=[(U['meal-prep']['de'], 'Ratgeber', 'Meal Prep: deine Woche vorbereiten', 'Welche Rezepte, und wie viele Tage sie halten.'),
                                (U['recettes']['de'], 'Rezepte', 'Berechnete Rezepte', 'Alltagsrezepte, Kalorien und Makros pro Portion.'),
                                (U['deficit']['de'], 'Ratgeber', 'Das Kaloriendefizit', 'Wie viel weniger essen, um abzunehmen, ohne zu übertreiben.')])


def art(l, t, court, surtitre, h1, chapeau):
    return dict(court=court, surtitre=surtitre, publie='2026-11-02', h1=h1, chapeau=chapeau, sommaire=list(zip(SOM, t['s'])), corps=corps(l, t))


PAGES = {
    'en': page('en', C, art('en', EN, 'Raw or cooked', 'Meals', 'Weighing food raw or cooked: which to choose, and the mistake to avoid',
        'Pasta, rice or lentils double in weight when cooked, and chicken loses a fifth. Both ways of weighing are correct, on one condition: choose the food in the table in the same state as what you put on the scale. Here are the numbers, and what the mistake costs.'),
        dict(title='Weigh food raw or cooked? The mistake to avoid — Basal', description='Pasta, rice and lentils double in weight when cooked: which value to choose, raw or cooked, worked examples from the Ciqual table and the mistake that doubles calories.',
             og_title='Weighing food raw or cooked: which to choose', og_description='Both are correct, on one condition. The numbers, and what the mistake costs.')),
    'es': page('es', C, art('es', ES, 'Crudo o cocido', 'Comidas', 'Pesar los alimentos crudos o cocinados: cuál elegir y el error que hay que evitar',
        'La pasta, el arroz o las lentejas duplican su peso al cocinarse, y el pollo pierde una quinta parte. Las dos formas de pesar son correctas con una condición: elegir en la tabla el alimento en el mismo estado que el que has puesto en la báscula. Estas son las cifras y lo que cuesta el error.'),
        dict(title='¿Pesar crudo o cocinado? El error que hay que evitar — Basal', description='La pasta, el arroz y las lentejas duplican su peso al cocinarse: qué valor elegir, crudo o cocido, ejemplos con la tabla Ciqual y el error que duplica las calorías.',
             og_title='Pesar los alimentos crudos o cocinados: cuál elegir', og_description='Las dos formas son correctas con una condición. Las cifras y lo que cuesta el error.')),
    'de': page('de', C, art('de', DE, 'Roh oder gekocht', 'Mahlzeiten', 'Lebensmittel roh oder gekocht wiegen: was du wählen solltest, und der Fehler, den du vermeiden musst',
        'Nudeln, Reis oder Linsen verdoppeln beim Kochen ihr Gewicht, Hähnchen verliert ein Fünftel. Beide Arten zu wiegen sind richtig, unter einer Bedingung: in der Tabelle das Lebensmittel im selben Zustand zu wählen wie das, was auf der Waage liegt. Hier die Zahlen, und was der Fehler kostet.'),
        dict(title='Roh oder gekocht wiegen? Der Fehler, den du vermeiden solltest — Basal', description='Nudeln, Reis und Linsen verdoppeln beim Kochen ihr Gewicht: welchen Wert wählen, roh oder gekocht, Beispiele aus der Ciqual-Tabelle und der Fehler, der die Kalorien verdoppelt.',
             og_title='Roh oder gekocht wiegen: was wählen?', og_description='Beides ist richtig, unter einer Bedingung. Die Zahlen, und was der Fehler kostet.')),
}
