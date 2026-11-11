from commun import U, L, page

FR = '/methode.html'
DATE = '2026-11-11'
C = 'methode'
IDS = ['bmr', 'expenditure', 'target', 'macros', 'adaptive', 'trend', 'sessions', '1rm', 'recipes', 'limits', 'sources']
MET = [('3,5', '5,0', '6,0'), ('8,0', '9,8', '12,8'), ('2,8', '3,5', '5,0'), ('4,0', '8,0', '10,0'), ('5,8', '8,3', '10,0'), ('5,0', '7,0', '10,0'),
       ('4,5', '6,5', '8,0'), ('5,0', '7,3', '8,0'), ('5,0', '8,0', '10,0'), ('6,0', '8,5', '10,5'), ('2,5', '3,0', '4,0'), ('5,8', '7,5', '9,0'),
       ('3,0', '4,8', '7,8'), ('3,0', '4,5', '6,0')]
COEF = [('1,2', '1 979'), ('1,375', '2 267'), ('1,55', '2 556'), ('1,725', '2 844'), ('1,9', '3 133')]
PROT = [('1,8', '2,2'), ('1,4', '1,8'), ('1,6', '2,0')]


def n(l, s):
    """Nombre écrit à la française (« 1 648,75 ») → format de la langue."""
    return s.replace(',', '.').replace(' ', ',') if l == 'en' else s.replace(' ', '.')


def corps(l, t):
    N = lambda s: n(l, s)
    ul = lambda xs: '\n'.join(f'        <li>{x}</li>' for x in xs)
    calc = lambda label, titre, lignes, total=None: f'''      <div class="calcul" role="group" aria-label="{label}">
        <div class="titre">{titre}</div>
''' + '\n'.join(f'        <div class="ligne{" total" if total is not None and k == len(lignes) - 1 else ""}"><span>{a}</span><b>{b}</b></div>' for k, (a, b) in enumerate(lignes)) + '\n      </div>'
    coef = '\n'.join(f'            <tr><td>{a}</td><td>{b}</td><td class="n">× {N(c)}</td><td class="n">{N(d)} kcal</td></tr>' for (a, b), (c, d) in zip(t['niveaux'], COEF))
    prot = '\n'.join(f'            <tr><td>{a}</td><td class="n">{N(b)}</td><td class="n">{N(c)}</td></tr>' for a, (b, c) in zip(t['buts'], PROT))
    met = '\n'.join(f'            <tr><td>{a}</td>' + ''.join(f'<td class="n">{N(x)}</td>' for x in v) + '</tr>' for a, v in zip(t['activites'], MET))
    s = t['s']
    return f'''      <div class="en-bref">
        <p class="surtitre">{t["bref_t"]}</p>
        <p>{t["bref"]}</p>
      </div>

      <h2 id="bmr">{s[0]}</h2>
      <p>{t["bmr"]}</p>
      <ul>
{ul(t["bmr_f"])}
      </ul>
{calc(*t["bmr_calc"])}
      <p>{t["bmr_apres"]}</p>

      <h2 id="expenditure">{s[1]}</h2>
      <p>{t["dep"]}</p>
      <div class="tableau">
        <table>
          <caption>{t["coef_cap"]}</caption>
          <thead><tr>{"".join(f'<th scope="col"{" class=" + chr(34) + "n" + chr(34) if k > 1 else ""}>{h}</th>' for k, h in enumerate(t["coef_th"]))}</tr></thead>
          <tbody>
{coef}
          </tbody>
        </table>
        <p class="source">{t["coef_src"]}</p>
      </div>

      <h2 id="target">{s[2]}</h2>
      <p>{t["obj"]}</p>
      <div class="tableau">
        <table>
          <caption>{t["pal_cap"]}</caption>
          <thead><tr>{"".join(f'<th scope="col"{" class=" + chr(34) + "n" + chr(34) if k else ""}>{h}</th>' for k, h in enumerate(t["pal_th"]))}</tr></thead>
          <tbody>
            <tr><td>{t["perte"]}</td><td class="n">− 10 %</td><td class="n">− 15 %</td><td class="n">− 20 %</td></tr>
            <tr><td>{t["prise"]}</td><td class="n">+ 5 %</td><td class="n">+ 10 %</td><td class="n">+ 15 %</td></tr>
          </tbody>
        </table>
        <p class="source">{t["pal_src"]}</p>
      </div>
      <p>{t["plancher"]}</p>
{calc(*t["obj_calc"], total=True)}

      <h2 id="macros">{s[3]}</h2>
      <p>{t["mac"]}</p>
      <div class="tableau">
        <table>
          <caption>{t["prot_cap"]}</caption>
          <thead><tr>{"".join(f'<th scope="col"{" class=" + chr(34) + "n" + chr(34) if k else ""}>{h}</th>' for k, h in enumerate(t["prot_th"]))}</tr></thead>
          <tbody>
{prot}
          </tbody>
        </table>
        <p class="source">{t["prot_src"]}</p>
      </div>
      <ul>
{ul(t["mac_l"])}
      </ul>
{calc(*t["mac_calc"])}

      <h2 id="adaptive">{s[4]}</h2>
      <p>{t["ad"]}</p>
      <p><code>{t["ad_f"]}</code></p>
      <p>{t["ad_7700"]}</p>
      <ul>
{ul(t["ad_cond"])}
      </ul>
      <p>{t["ad_insuf"]}</p>
      <p>{t["ad_gf"]}</p>
      <ul>
{ul(t["ad_gf_l"])}
      </ul>
{calc(*t["ad_calc"], total=True)}
      <p>{t["ad_pause"]}</p>

      <h2 id="trend">{s[5]}</h2>
      <p>{t["tend"]}</p>

      <h2 id="sessions">{s[6]}</h2>
      <p>{t["seances"]}</p>
      <div class="tableau">
        <table>
          <caption>{t["met_cap"]}</caption>
          <thead><tr>{"".join(f'<th scope="col"{" class=" + chr(34) + "n" + chr(34) if k else ""}>{h}</th>' for k, h in enumerate(t["met_th"]))}</tr></thead>
          <tbody>
{met}
          </tbody>
        </table>
        <p class="source">{t["met_src"]}</p>
      </div>

      <h2 id="1rm">{s[7]}</h2>
      <p>{t["rm"]}</p>

      <h2 id="recipes">{s[8]}</h2>
      <p>{t["rec"]}</p>

      <h2 id="limits">{s[9]}</h2>
      <div class="inconnu">
        <p>{t["lim"][0]}</p>
        <p>{t["lim"][1]}</p>
        <p style="margin:0">{t["lim"][2]}</p>
      </div>

      <div class="appel-contexte">
        <div><strong>{t["appel_t"]}</strong><p>{t["appel"]}</p></div>
        <a class="bouton vif" href="{U["accueil"][l]}#download">{t["telecharger"]}</a>
      </div>

      <h2 id="sources">{s[10]}</h2>
      <ol class="sources">
        <li>Mifflin MD, St Jeor ST et al. “A new predictive equation for resting energy expenditure in healthy individuals”. <i>American Journal of Clinical Nutrition</i>, 1990, 51(2), p. 241-247.</li>
        <li>Frankenfield D, Roth-Yousey L, Compher C. “Comparison of predictive equations for resting metabolic rate in healthy nonobese and obese adults: a systematic review”. <i>Journal of the American Dietetic Association</i>, 2005, 105(5), p. 775-789.</li>
        <li>Wishnofsky M. “Caloric equivalents of gained or lost weight”. <i>American Journal of Clinical Nutrition</i>, 1958, 6(5), p. 542-546.</li>
        <li>Ainsworth BE et al. “2011 Compendium of Physical Activities: a second update of codes and MET values”. <i>Medicine &amp; Science in Sports &amp; Exercise</i>, 2011, 43(8), p. 1575-1581; {t["maj2024"]}: <a href="https://pacompendium.com/">pacompendium.com</a>.</li>
        <li>Epley B. <i>Poundage Chart</i>. Boyd Epley Workout, 1985.</li>
        <li>Institute of Medicine. <i>Dietary Reference Intakes for Energy, Carbohydrate, Fiber, Fat, Fatty Acids, Cholesterol, Protein, and Amino Acids</i>. National Academies Press, 2005 ({t["fibres_src"]}).</li>
        <li>ANSES. <a href="https://ciqual.anses.fr/">{t["ciqual"]}</a>, {t["licence"]}.</li>
      </ol>

      <h2 style="font-size:1.5rem;margin-top:48px">{t["plus_t"]}</h2>
      <div class="guides" style="grid-template-columns:repeat(auto-fit,minmax(240px,1fr))">
        <a class="guide" href="{U["metabolisme-adaptatif"][l]}"><span class="surtitre" style="margin:0">Guide</span><h3>{t["plus"][0][0]}</h3><p>{t["plus"][0][1]}</p></a>
        <a class="guide" href="{U["calculateurs"][l]}"><span class="surtitre" style="margin:0">{t["outils"]}</span><h3>{t["plus"][1][0]}</h3><p>{t["plus"][1][1]}</p></a>
      </div>'''


def textes(l):
    N = lambda s: n(l, s)
    u = lambda k: U[k][l]
    if l == 'en':
        return dict(
            s=['Basal metabolic rate', 'Daily expenditure', 'Calorie target', 'Protein, fat, carbohydrates', 'Adaptive expenditure', 'Weight trend', 'Session expenditure', 'Strength maximum', 'Recipe values', 'What these calculations do not do', 'Sources'],
            bref_t='In short',
            bref='Basal starts from a published formula (Mifflin-St Jeor) to estimate your expenditure, derives a target and macros anchored to your weight, then corrects the expenditure with what you eat and how your weight actually changes. Every correction is bounded and gradual, and the app shows nothing until there is enough data.',
            bmr='This is the energy spent at complete rest. Basal uses the Mifflin-St Jeor equation, published in 1990 and the most widely used today:',
            bmr_f=['man: <code>10 × weight (kg) + 6.25 × height (cm) − 5 × age + 5</code>', 'woman: <code>10 × weight (kg) + 6.25 × height (cm) − 5 × age − 161</code>'],
            bmr_calc=('Basal metabolic rate example', 'Example: man, 30, 175 cm, 70 kg', [('10 × 70 + 6.25 × 175 − 5 × 30 + 5', '1,648.75 kcal'), ('The same person as a woman (− 161 instead of + 5)', '1,482.75 kcal')]),
            bmr_apres=f'What makes it vary, and its limits, are explained in the <a href="{u("metabolisme-de-base")}">basal metabolic rate</a> guide. This value is never changed afterwards: it stays the theoretical reference, and acts as the floor for the calorie target.',
            dep='A day’s total expenditure is the basal metabolic rate multiplied by an activity factor, chosen at sign-up. The step counts shown in the app are there to help you place yourself; they do not enter any calculation.',
            coef_cap='The app’s activity factors', coef_th=['Level', 'Guide', 'Factor', 'Example (1,648.75 kcal)'],
            niveaux=[('Sedentary', 'little or no sport · under 5,000 steps a day'), ('Lightly active', '1 to 3 sessions a week · 5,000 to 7,500 steps'), ('Moderately active', '3 to 5 sessions a week · 7,500 to 10,000 steps'), ('Active', '6 to 7 sessions a week · 10,000 to 12,500 steps'), ('Very active', 'intense daily sport · over 12,500 steps')],
            coef_src='Rounded to the kcal. This is the weak point of any formula: between “sedentary” and “moderately active”, the gap is over 500 kcal a day.',
            obj='The target is a percentage of expenditure, not a fixed number of calories: taking 500 kcal off everyone is a reasonable deficit for some and a severe one for others.',
            pal_cap='Target levels', pal_th=['Goal', 'Gentle', 'Moderate (default)', 'Intense'], perte='Weight loss', prise='Weight gain',
            pal_src='The surplus for gaining is deliberately smaller than the deficit for losing: a large surplus mostly adds fat mass.',
            plancher='<strong>Safety floor.</strong> The target never goes below the basal metabolic rate, nor below 800 kcal a day. When this floor applies, the app says so instead of correcting silently.',
            obj_calc=('Target example', 'Example: same profile, moderately active, moderate loss', [('Expenditure: 1,648.75 × 1.55', '2,555.6 kcal'), ('Target: 2,555.6 × (1 − 0.15)', '2,172 kcal / day')]),
            mac='Protein and fat are anchored to weight, and carbohydrates take the rest. The reverse (a fixed percentage of calories) gave too little protein on low targets.',
            prot_cap='Protein, in grams per kilo of reference weight', prot_th=['Goal', 'Little or no sport', '3 sessions a week or more'], buts=['Loss', 'Maintenance', 'Gain'],
            prot_src='“Active” from the “moderately active” level up. The need rises in a deficit, where protein protects muscle mass.',
            mac_l=[f'<strong>Reference weight.</strong> Needs follow lean mass, not total weight. Up to a BMI of 25, it is the actual weight. Above that, only a quarter of the excess counts (adjusted body weight formula). Example: 120 kg at 175 cm gives a reference weight of 87.4 kg. See the <a href="{u("calc-proteines")}">protein calculator</a>.',
                   '<strong>Fat.</strong> The larger of two numbers: 0.8 g per kilo of reference weight (floor), or 30% of calories.',
                   '<strong>Carbohydrates.</strong> What remains after protein (4 kcal/g) and fat (9 kcal/g), divided by 4. Never negative.',
                   '<strong>Fibre.</strong> 14 g per 1,000 kcal.'],
            mac_calc=('Macros example', 'Example: 70 kg, 175 cm, active, 2,172 kcal target for loss', [('Protein: 70 × 2.2', '154 g'), ('Fat: the larger of 70 × 0.8 = 56 g and 2,172 × 0.3 ÷ 9 = 72.4 g', '72 g'), ('Carbohydrates: (2,172 − 154 × 4 − 72 × 9) ÷ 4', '227 g'), ('Fibre: 2,172 ÷ 1,000 × 14', '30 g')]),
            ad='This is the formula corrected by your data. Over a rolling 28-day window, Basal compares your intake with how your smoothed weight changes:',
            ad_f='observed expenditure = average intake − (change in smoothed weight × 7,700) ÷ number of days',
            ad_7700='7,700 kcal is the usual energy equivalent of one kilogram of body mass. The estimate is only calculated if the window contains:',
            ad_cond=['at least 4 weigh-ins, spread over at least 10 days;', 'at least 8 days of logged meals, covering at least 60% of the period.'],
            ad_insuf='Otherwise, the app shows “not enough data”. A day with no food logged at all is ignored: it does not count as a fast.',
            ad_gf='<strong>Three safeguards</strong> stop an unusual week from derailing the number:',
            ad_gf_l=['<strong>plausibility bounds</strong>: the observation is brought back between 0.8 and 1.6 times the current theoretical expenditure, which protects against a heavily under-reported log;',
                     '<strong>smoothing</strong>: at each usable weigh-in, the estimate only covers 30% of the gap with the observation;',
                     '<strong>maximum step</strong>: never more than 150 kcal of change per recalculation.'],
            ad_calc=('Adaptive expenditure example', 'Example: the formula says 2,556 kcal', [('Average logged intake', '2,100 kcal / day'), ('Smoothed weight: − 0.6 kg in 21 days, so 0.6 × 7,700 ÷ 21', '220 kcal / day'), ('Observed expenditure: 2,100 + 220', '2,320 kcal'), ('1st recalculation: 2,556 + 0.3 × (2,320 − 2,556)', '2,485 kcal'), ('2nd recalculation, if the observation stays at 2,320 kcal', '2,436 kcal'), ('3rd recalculation: the estimate joins the observation smoothly', '2,401 kcal')]),
            ad_pause=f'For a strategy’s “at maintenance” breaks, the app uses this measured expenditure rather than the formula, provided it rests on at least 5 recalculations and the latest is less than 21 days old. To do this calculation once, from your averages: <a href="{u("depense-reelle")}">calculate your real expenditure</a>.',
            tend=f'The weight shown as the trend is the average of the weigh-ins over the last 7 days. Water, salt, glycogen and digestion move your weight from one day to the next far more than fat does; it is this average, not the day’s weigh-in, that feeds adaptive expenditure. See <a href="{u("variations")}">why your weight changes from one day to the next</a>.',
            seances='Session calories are calculated, never typed in: <code>kcal = MET × weight (kg) × duration (hours)</code>. The MET (metabolic equivalent) depends on the activity and the perceived intensity. Example: 1 hour of moderate strength training at 70 kg gives 5.0 × 70 × 1 = 350 kcal.',
            met_cap='MET values used by the app', met_th=['Activity', 'Light', 'Moderate', 'Intense'],
            activites=['Strength training', 'Running', 'Walking', 'Cycling', 'Swimming', 'Football', 'Basketball', 'Tennis', 'CrossFit', 'HIIT', 'Yoga', 'Climbing', 'Dance', 'Other'],
            met_src='Compendium of Physical Activities (Ainsworth et al., 2011, updated in 2024). CrossFit and HIIT, absent from the Compendium, are based on measurements of complete sessions, rest included (Feito et al., 2018; Nalcakan, 2014; Kliszczewicz et al., 2014). The climbing levels and “moderate” yoga are interpolations, for lack of separate codes.',
            rm=f'The estimated one-rep maximum (1RM) follows the Epley formula: <code>1RM ≈ load × (1 + reps ÷ 30)</code>. Example: 80 kg lifted 8 times gives an estimated 1RM of 101.3 kg. A set of a single rep is already a real maximum: the app then keeps the load as it is, instead of inflating it by 3%. Work out yours with the <a href="{u("1rm")}">1RM calculator</a>.',
            rec=f'The calories and macros of the <a href="{u("recettes")}">recipes</a> are calculated ingredient by ingredient, to the gram, from ANSES’s Ciqual 2025 food composition table (France). The split shown on each recipe relates the energy from protein (4 kcal/g), carbohydrates (4 kcal/g) and fat (9 kcal/g) to their total.',
            lim=['<strong>These are estimates.</strong> An expenditure formula is commonly off by about 10% across a population, more for atypical profiles. Adaptive expenditure narrows that gap, but it depends on the quality of your log.',
                 '<strong>The app does not measure your body composition.</strong> The reference weight for macros is a standard approximation, not a measurement of your lean mass.',
                 '<strong>This is not medical advice.</strong> Basal is not a medical device. An expenditure very far from what is expected, pregnancy, illness or an eating disorder are matters for a health professional.'],
            appel_t='These calculations, on your data.', appel='Basal redoes them for you every week, from your meals and weigh-ins. Free, no account.', telecharger='Download',
            maj2024='2024 update', fibres_src='fibre: 14 g per 1,000 kcal', ciqual='Ciqual 2025 food composition table', licence='Etalab 2.0 open licence',
            plus_t='Going further', outils='Tools', plus=[('Adaptive metabolism', 'Why a formula is not enough, and how to correct it.'), ('The calculators', 'Expenditure and macros, with the same formulas as the app.')],
        )
    if l == 'es':
        return dict(
            s=['Metabolismo basal', 'Gasto diario', 'Objetivo calórico', 'Proteínas, grasas, hidratos', 'Gasto adaptativo', 'Tendencia del peso', 'Gasto de las sesiones', 'Máximo en musculación', 'Valores de las recetas', 'Lo que estos cálculos no hacen', 'Fuentes'],
            bref_t='En resumen',
            bref='Basal parte de una fórmula publicada (Mifflin-St Jeor) para estimar tu gasto, deduce un objetivo y unos macros anclados a tu peso, y luego corrige el gasto con lo que comes y la evolución real de tu peso. Cada corrección está acotada y es progresiva, y la app no muestra nada mientras los datos no basten.',
            bmr='Es la energía gastada en reposo completo. Basal usa la ecuación de Mifflin-St Jeor, publicada en 1990 y la más utilizada hoy:',
            bmr_f=['hombre: <code>10 × peso (kg) + 6,25 × altura (cm) − 5 × edad + 5</code>', 'mujer: <code>10 × peso (kg) + 6,25 × altura (cm) − 5 × edad − 161</code>'],
            bmr_calc=('Ejemplo de metabolismo basal', 'Ejemplo: hombre, 30 años, 175 cm, 70 kg', [('10 × 70 + 6,25 × 175 − 5 × 30 + 5', '1.648,75 kcal'), ('La misma persona, como mujer (− 161 en lugar de + 5)', '1.482,75 kcal')]),
            bmr_apres=f'Lo que lo hace variar, y sus límites, se explican en la guía del <a href="{u("metabolisme-de-base")}">metabolismo basal</a>. Este valor no se modifica nunca después: sigue siendo la referencia teórica y sirve de suelo al objetivo calórico.',
            dep='El gasto total de un día es el metabolismo basal multiplicado por un coeficiente de actividad, elegido al registrarte. Las referencias en pasos que muestra la app sirven para situarte; no entran en ningún cálculo.',
            coef_cap='Coeficientes de actividad de la aplicación', coef_th=['Nivel', 'Referencia', 'Coeficiente', 'Ejemplo (1.648,75 kcal)'],
            niveaux=[('Sedentario', 'poco o ningún deporte · menos de 5.000 pasos al día'), ('Ligeramente activo', '1 a 3 sesiones por semana · 5.000 a 7.500 pasos'), ('Moderadamente activo', '3 a 5 sesiones por semana · 7.500 a 10.000 pasos'), ('Activo', '6 a 7 sesiones por semana · 10.000 a 12.500 pasos'), ('Muy activo', 'deporte intenso a diario · más de 12.500 pasos')],
            coef_src='Redondeado al kcal. Es el punto débil de cualquier fórmula: entre «sedentario» y «moderadamente activo», la diferencia supera las 500 kcal al día.',
            obj='El objetivo es un porcentaje del gasto, no un número fijo de calorías: quitar 500 kcal a todo el mundo es un déficit razonable para unos y severo para otros.',
            pal_cap='Niveles de objetivo', pal_th=['Objetivo', 'Suave', 'Moderado (por defecto)', 'Intenso'], perte='Pérdida de peso', prise='Aumento de peso',
            pal_src='El superávit para ganar es a propósito menor que el déficit para perder: un superávit grande añade sobre todo masa grasa.',
            plancher='<strong>Suelo de seguridad.</strong> El objetivo nunca baja del metabolismo basal ni de 800 kcal al día. Cuando se aplica este suelo, la app lo indica en lugar de corregir en silencio.',
            obj_calc=('Ejemplo de objetivo', 'Ejemplo: mismo perfil, moderadamente activo, pérdida moderada', [('Gasto: 1.648,75 × 1,55', '2.555,6 kcal'), ('Objetivo: 2.555,6 × (1 − 0,15)', '2.172 kcal / día')]),
            mac='Las proteínas y las grasas se anclan al peso, y los hidratos se llevan el resto. Lo contrario (un porcentaje fijo de las calorías) daba proteínas insuficientes con objetivos bajos.',
            prot_cap='Proteínas, en gramos por kilo de peso de referencia', prot_th=['Objetivo', 'Poco o nada deportista', '3 sesiones por semana o más'], buts=['Pérdida', 'Mantenimiento', 'Ganancia'],
            prot_src='«Deportista» a partir del nivel «moderadamente activo». La necesidad sube en déficit, donde las proteínas protegen la masa muscular.',
            mac_l=[f'<strong>Peso de referencia.</strong> Las necesidades siguen a la masa magra, no al peso total. Hasta un IMC de 25, es el peso real. Por encima, solo cuenta una cuarta parte del exceso (fórmula del peso ajustado). Ejemplo: 120 kg para 175 cm dan un peso de referencia de 87,4 kg. Ver la <a href="{u("calc-proteines")}">calculadora de proteínas</a>.',
                   '<strong>Grasas.</strong> El mayor de dos números: 0,8 g por kilo de peso de referencia (suelo), o el 30 % de las calorías.',
                   '<strong>Hidratos.</strong> Lo que queda tras las proteínas (4 kcal/g) y las grasas (9 kcal/g), dividido entre 4. Nunca negativo.',
                   '<strong>Fibra.</strong> 14 g por cada 1.000 kcal.'],
            mac_calc=('Ejemplo de macros', 'Ejemplo: 70 kg, 175 cm, deportista, objetivo de 2.172 kcal en pérdida', [('Proteínas: 70 × 2,2', '154 g'), ('Grasas: el mayor entre 70 × 0,8 = 56 g y 2.172 × 0,3 ÷ 9 = 72,4 g', '72 g'), ('Hidratos: (2.172 − 154 × 4 − 72 × 9) ÷ 4', '227 g'), ('Fibra: 2.172 ÷ 1.000 × 14', '30 g')]),
            ad='Es la corrección de la fórmula con tus datos. En una ventana móvil de 28 días, Basal compara tu ingesta con la evolución de tu peso suavizado:',
            ad_f='gasto observado = ingesta media − (variación del peso suavizado × 7.700) ÷ número de días',
            ad_7700='7.700 kcal es el equivalente energético habitual de un kilo de masa corporal. La estimación solo se calcula si la ventana contiene:',
            ad_cond=['al menos 4 pesajes, repartidos en al menos 10 días;', 'al menos 8 días de comidas registradas, que cubran al menos el 60 % del periodo.'],
            ad_insuf='Si no, la app muestra «datos insuficientes». Un día sin ningún alimento anotado se ignora: no cuenta como un ayuno.',
            ad_gf='<strong>Tres salvaguardas</strong> impiden que una semana atípica descarrile la cifra:',
            ad_gf_l=['<strong>límites de plausibilidad</strong>: la observación se lleva a entre 0,8 y 1,6 veces el gasto teórico del momento, lo que protege de un diario muy infradeclarado;',
                     '<strong>suavizado</strong>: en cada pesaje aprovechable, la estimación solo recorre el 30 % de la diferencia con la observación;',
                     '<strong>paso máximo</strong>: nunca más de 150 kcal de variación por recálculo.'],
            ad_calc=('Ejemplo de gasto adaptativo', 'Ejemplo: la fórmula indica 2.556 kcal', [('Ingesta media registrada', '2.100 kcal / día'), ('Peso suavizado: − 0,6 kg en 21 días, es decir 0,6 × 7.700 ÷ 21', '220 kcal / día'), ('Gasto observado: 2.100 + 220', '2.320 kcal'), ('1.er recálculo: 2.556 + 0,3 × (2.320 − 2.556)', '2.485 kcal'), ('2.º recálculo, si la observación sigue en 2.320 kcal', '2.436 kcal'), ('3.er recálculo: la estimación alcanza la observación sin saltos', '2.401 kcal')]),
            ad_pause=f'Para las pausas «en mantenimiento» de una estrategia, la app usa este gasto medido en lugar de la fórmula, siempre que se base en al menos 5 recálculos y que el último tenga menos de 21 días. Para hacer este cálculo una vez, a partir de tus medias: <a href="{u("depense-reelle")}">calcular tu gasto real</a>.',
            tend=f'El peso que se muestra como tendencia es la media de los pesajes de los últimos 7 días. El agua, la sal, el glucógeno y la digestión hacen variar el peso de un día a otro mucho más que la grasa; es esta media, no el pesaje del día, la que alimenta el gasto adaptativo. Ver <a href="{u("variations")}">por qué tu peso cambia de un día para otro</a>.',
            seances='Las calorías de una sesión se calculan, nunca se introducen a mano: <code>kcal = MET × peso (kg) × duración (horas)</code>. El MET (equivalente metabólico) depende de la actividad y de la intensidad percibida. Ejemplo: 1 h de musculación moderada con 70 kg da 5,0 × 70 × 1 = 350 kcal.',
            met_cap='Valores MET usados por la aplicación', met_th=['Actividad', 'Ligera', 'Moderada', 'Intensa'],
            activites=['Musculación', 'Correr', 'Caminar', 'Ciclismo', 'Natación', 'Fútbol', 'Baloncesto', 'Tenis', 'CrossFit', 'HIIT', 'Yoga', 'Escalada', 'Baile', 'Otra'],
            met_src='Compendium of Physical Activities (Ainsworth et al., 2011, actualizado en 2024). CrossFit y HIIT, ausentes del Compendium, se basan en mediciones de sesiones completas, descansos incluidos (Feito et al., 2018; Nalcakan, 2014; Kliszczewicz et al., 2014). Los niveles de la escalada y del yoga «moderado» son interpolaciones, a falta de códigos distintos.',
            rm=f'El máximo estimado a una repetición (1RM) sigue la fórmula de Epley: <code>1RM ≈ carga × (1 + repeticiones ÷ 30)</code>. Ejemplo: 80 kg levantados 8 veces dan un 1RM estimado de 101,3 kg. Una serie de una sola repetición ya es un máximo real: la app conserva entonces la carga tal cual, en lugar de inflarla un 3 %. Calcula el tuyo con la <a href="{u("1rm")}">calculadora de 1RM</a>.',
            rec=f'Las calorías y los macros de las <a href="{u("recettes")}">recetas</a> se calculan ingrediente por ingrediente, al gramo, a partir de la tabla de composición Ciqual 2025 de la ANSES (Francia). El reparto que aparece en cada receta relaciona la energía de las proteínas (4 kcal/g), los hidratos (4 kcal/g) y las grasas (9 kcal/g) con su total.',
            lim=['<strong>Son estimaciones.</strong> Una fórmula de gasto suele equivocarse en torno a un 10 % en una población, y más en perfiles atípicos. El gasto adaptativo reduce esa diferencia, pero depende de la calidad de tu diario.',
                 '<strong>La app no mide tu composición corporal.</strong> El peso de referencia de los macros es una aproximación estándar, no una medición de tu masa magra.',
                 '<strong>No es un consejo médico.</strong> Basal no es un dispositivo médico. Un gasto muy alejado de lo esperado, un embarazo, una enfermedad o un trastorno de la conducta alimentaria son cosa de un profesional sanitario.'],
            appel_t='Estos cálculos, con tus datos.', appel='Basal los rehace por ti cada semana, a partir de tus comidas y tus pesajes. Gratis, sin cuenta.', telecharger='Descargar',
            maj2024='actualización de 2024', fibres_src='fibra: 14 g por cada 1.000 kcal', ciqual='Tabla de composición nutricional de los alimentos Ciqual 2025', licence='licencia abierta Etalab 2.0',
            plus_t='Para saber más', outils='Herramientas', plus=[('El metabolismo adaptativo', 'Por qué una fórmula no basta, y cómo corregirla.'), ('Las calculadoras', 'Gasto y macros, con las mismas fórmulas que la aplicación.')],
        )
    return dict(
        s=['Grundumsatz', 'Täglicher Verbrauch', 'Kalorienziel', 'Eiweiß, Fett, Kohlenhydrate', 'Adaptiver Verbrauch', 'Gewichtstrend', 'Verbrauch der Einheiten', 'Maximum im Krafttraining', 'Werte der Rezepte', 'Was diese Berechnungen nicht leisten', 'Quellen'],
        bref_t='Kurz gesagt',
        bref='Basal geht von einer veröffentlichten Formel (Mifflin-St Jeor) aus, um deinen Verbrauch zu schätzen, leitet daraus ein Ziel und an dein Gewicht gekoppelte Makros ab und korrigiert den Verbrauch dann mit dem, was du isst, und der tatsächlichen Entwicklung deines Gewichts. Jede Korrektur ist begrenzt und schrittweise, und die App zeigt nichts an, solange die Daten nicht ausreichen.',
        bmr='Das ist die Energie, die in völliger Ruhe verbraucht wird. Basal nutzt die Mifflin-St-Jeor-Gleichung, 1990 veröffentlicht und heute die am häufigsten verwendete:',
        bmr_f=['Mann: <code>10 × Gewicht (kg) + 6,25 × Größe (cm) − 5 × Alter + 5</code>', 'Frau: <code>10 × Gewicht (kg) + 6,25 × Größe (cm) − 5 × Alter − 161</code>'],
        bmr_calc=('Beispiel Grundumsatz', 'Beispiel: Mann, 30 Jahre, 175 cm, 70 kg', [('10 × 70 + 6,25 × 175 − 5 × 30 + 5', '1.648,75 kcal'), ('Dieselbe Person als Frau (− 161 statt + 5)', '1.482,75 kcal')]),
        bmr_apres=f'Was ihn verändert und wo seine Grenzen liegen, erklärt der Ratgeber zum <a href="{u("metabolisme-de-base")}">Grundumsatz</a>. Dieser Wert wird danach nie mehr verändert: Er bleibt der theoretische Bezugswert und dient als Untergrenze für das Kalorienziel.',
        dep='Der Gesamtverbrauch eines Tages ist der Grundumsatz mal einem Aktivitätsfaktor, der bei der Anmeldung gewählt wird. Die in der App angezeigten Schrittzahlen dienen nur zur Einordnung; sie fließen in keine Berechnung ein.',
        coef_cap='Aktivitätsfaktoren der App', coef_th=['Stufe', 'Richtwert', 'Faktor', 'Beispiel (1.648,75 kcal)'],
        niveaux=[('Sitzend', 'wenig oder kein Sport · unter 5.000 Schritte am Tag'), ('Leicht aktiv', '1 bis 3 Einheiten pro Woche · 5.000 bis 7.500 Schritte'), ('Mäßig aktiv', '3 bis 5 Einheiten pro Woche · 7.500 bis 10.000 Schritte'), ('Aktiv', '6 bis 7 Einheiten pro Woche · 10.000 bis 12.500 Schritte'), ('Sehr aktiv', 'täglich intensiver Sport · über 12.500 Schritte')],
        coef_src='Auf die kcal gerundet. Das ist die Schwachstelle jeder Formel: Zwischen „sitzend“ und „mäßig aktiv“ liegen mehr als 500 kcal pro Tag.',
        obj='Das Ziel ist ein Prozentsatz des Verbrauchs, keine feste Kalorienzahl: Allen 500 kcal abzuziehen ist für die einen ein vernünftiges Defizit und für die anderen ein hartes.',
        pal_cap='Zielstufen', pal_th=['Ziel', 'Sanft', 'Moderat (Standard)', 'Intensiv'], perte='Abnehmen', prise='Zunehmen',
        pal_src='Der Überschuss beim Zunehmen ist bewusst kleiner als das Defizit beim Abnehmen: Ein großer Überschuss bringt vor allem Fettmasse.',
        plancher='<strong>Sicherheitsuntergrenze.</strong> Das Ziel fällt nie unter den Grundumsatz und nie unter 800 kcal pro Tag. Greift diese Untergrenze, sagt die App das, statt stillschweigend zu korrigieren.',
        obj_calc=('Beispiel Ziel', 'Beispiel: gleiches Profil, mäßig aktiv, moderates Abnehmen', [('Verbrauch: 1.648,75 × 1,55', '2.555,6 kcal'), ('Ziel: 2.555,6 × (1 − 0,15)', '2.172 kcal / Tag')]),
        mac='Eiweiß und Fett sind an das Gewicht gekoppelt, die Kohlenhydrate bekommen den Rest. Umgekehrt (ein fester Prozentsatz der Kalorien) ergab sich bei niedrigen Zielen zu wenig Eiweiß.',
        prot_cap='Eiweiß, in Gramm pro Kilo Bezugsgewicht', prot_th=['Ziel', 'Wenig oder kein Sport', '3 Einheiten pro Woche oder mehr'], buts=['Abnehmen', 'Halten', 'Zunehmen'],
        prot_src='„Sportlich“ ab der Stufe „mäßig aktiv“. Der Bedarf steigt im Defizit, wo Eiweiß die Muskelmasse schützt.',
        mac_l=[f'<strong>Bezugsgewicht.</strong> Der Bedarf richtet sich nach der fettfreien Masse, nicht nach dem Gesamtgewicht. Bis zu einem BMI von 25 ist es das tatsächliche Gewicht. Darüber zählt nur ein Viertel des Überschusses (Formel des angepassten Gewichts). Beispiel: 120 kg bei 175 cm ergeben ein Bezugsgewicht von 87,4 kg. Siehe den <a href="{u("calc-proteines")}">Proteinrechner</a>.',
               '<strong>Fett.</strong> Die größere von zwei Zahlen: 0,8 g pro Kilo Bezugsgewicht (Untergrenze) oder 30 % der Kalorien.',
               '<strong>Kohlenhydrate.</strong> Was nach Eiweiß (4 kcal/g) und Fett (9 kcal/g) übrig bleibt, geteilt durch 4. Nie negativ.',
               '<strong>Ballaststoffe.</strong> 14 g pro 1.000 kcal.'],
        mac_calc=('Beispiel Makros', 'Beispiel: 70 kg, 175 cm, sportlich, Ziel 2.172 kcal beim Abnehmen', [('Eiweiß: 70 × 2,2', '154 g'), ('Fett: die größere Zahl aus 70 × 0,8 = 56 g und 2.172 × 0,3 ÷ 9 = 72,4 g', '72 g'), ('Kohlenhydrate: (2.172 − 154 × 4 − 72 × 9) ÷ 4', '227 g'), ('Ballaststoffe: 2.172 ÷ 1.000 × 14', '30 g')]),
        ad='Das ist die Korrektur der Formel durch deine Daten. Über ein gleitendes Fenster von 28 Tagen vergleicht Basal deine Zufuhr mit der Entwicklung deines geglätteten Gewichts:',
        ad_f='beobachteter Verbrauch = durchschnittliche Zufuhr − (Änderung des geglätteten Gewichts × 7.700) ÷ Anzahl der Tage',
        ad_7700='7.700 kcal sind das übliche Energieäquivalent eines Kilogramms Körpermasse. Die Schätzung wird nur berechnet, wenn das Fenster Folgendes enthält:',
        ad_cond=['mindestens 4 Wägungen, verteilt auf mindestens 10 Tage;', 'mindestens 8 Tage mit erfassten Mahlzeiten, die mindestens 60 % des Zeitraums abdecken.'],
        ad_insuf='Sonst zeigt die App „nicht genug Daten“ an. Ein Tag ganz ohne eingetragenes Lebensmittel wird ignoriert: Er zählt nicht als Fastentag.',
        ad_gf='<strong>Drei Schutzmechanismen</strong> verhindern, dass eine untypische Woche die Zahl entgleisen lässt:',
        ad_gf_l=['<strong>Plausibilitätsgrenzen</strong>: Die Beobachtung wird auf das 0,8- bis 1,6-Fache des aktuellen theoretischen Verbrauchs begrenzt, was vor einem stark untertriebenen Tagebuch schützt;',
                 '<strong>Glättung</strong>: Bei jeder verwertbaren Wägung legt die Schätzung nur 30 % des Abstands zur Beobachtung zurück;',
                 '<strong>maximaler Schritt</strong>: nie mehr als 150 kcal Änderung pro Neuberechnung.'],
        ad_calc=('Beispiel adaptiver Verbrauch', 'Beispiel: Die Formel sagt 2.556 kcal', [('Durchschnittlich erfasste Zufuhr', '2.100 kcal / Tag'), ('Geglättetes Gewicht: − 0,6 kg in 21 Tagen, also 0,6 × 7.700 ÷ 21', '220 kcal / Tag'), ('Beobachteter Verbrauch: 2.100 + 220', '2.320 kcal'), ('1. Neuberechnung: 2.556 + 0,3 × (2.320 − 2.556)', '2.485 kcal'), ('2. Neuberechnung, wenn die Beobachtung bei 2.320 kcal bleibt', '2.436 kcal'), ('3. Neuberechnung: Die Schätzung erreicht die Beobachtung ohne Sprung', '2.401 kcal')]),
        ad_pause=f'Für die Pausen „auf Erhaltung“ einer Strategie nutzt die App diesen gemessenen Verbrauch statt der Formel, sofern er auf mindestens 5 Neuberechnungen beruht und die letzte weniger als 21 Tage zurückliegt. Um diese Rechnung einmal mit deinen Durchschnittswerten zu machen: <a href="{u("depense-reelle")}">tatsächlichen Verbrauch berechnen</a>.',
        tend=f'Das als Trend angezeigte Gewicht ist der Durchschnitt der Wägungen der letzten 7 Tage. Wasser, Salz, Glykogen und Verdauung lassen das Gewicht von einem Tag zum nächsten viel stärker schwanken als Fett; dieser Durchschnitt, nicht die Wägung des Tages, speist den adaptiven Verbrauch. Siehe <a href="{u("variations")}">warum sich dein Gewicht von einem Tag auf den anderen ändert</a>.',
        seances='Die Kalorien einer Einheit werden berechnet, nie eingetippt: <code>kcal = MET × Gewicht (kg) × Dauer (Stunden)</code>. Der MET (metabolisches Äquivalent) hängt von der Aktivität und der empfundenen Intensität ab. Beispiel: 1 Stunde moderates Krafttraining bei 70 kg ergibt 5,0 × 70 × 1 = 350 kcal.',
        met_cap='Von der App verwendete MET-Werte', met_th=['Aktivität', 'Leicht', 'Moderat', 'Intensiv'],
        activites=['Krafttraining', 'Laufen', 'Gehen', 'Radfahren', 'Schwimmen', 'Fußball', 'Basketball', 'Tennis', 'CrossFit', 'HIIT', 'Yoga', 'Klettern', 'Tanzen', 'Sonstiges'],
        met_src='Compendium of Physical Activities (Ainsworth et al., 2011, aktualisiert 2024). CrossFit und HIIT, die im Compendium fehlen, beruhen auf Messungen vollständiger Einheiten, Pausen inklusive (Feito et al., 2018; Nalcakan, 2014; Kliszczewicz et al., 2014). Die Stufen beim Klettern und „moderates“ Yoga sind Interpolationen, da es keine eigenen Codes gibt.',
        rm=f'Das geschätzte Maximum für eine Wiederholung (1RM) folgt der Epley-Formel: <code>1RM ≈ Gewicht × (1 + Wiederholungen ÷ 30)</code>. Beispiel: 80 kg, 8-mal gehoben, ergeben ein geschätztes 1RM von 101,3 kg. Ein Satz mit nur einer Wiederholung ist bereits ein echtes Maximum: Die App übernimmt dann das Gewicht unverändert, statt es um 3 % aufzublähen. Berechne deins mit dem <a href="{u("1rm")}">1RM-Rechner</a>.',
        rec=f'Die Kalorien und Makros der <a href="{u("recettes")}">Rezepte</a> werden Zutat für Zutat, auf das Gramm genau, aus der Nährwerttabelle Ciqual 2025 der ANSES (Frankreich) berechnet. Die auf jedem Rezept angezeigte Aufteilung setzt die Energie aus Eiweiß (4 kcal/g), Kohlenhydraten (4 kcal/g) und Fett (9 kcal/g) ins Verhältnis zu ihrer Summe.',
        lim=['<strong>Das sind Schätzungen.</strong> Eine Verbrauchsformel liegt in einer Bevölkerung häufig um etwa 10 % daneben, bei untypischen Profilen mehr. Der adaptive Verbrauch verringert diese Abweichung, hängt aber von der Qualität deines Tagebuchs ab.',
                 '<strong>Die App misst deine Körperzusammensetzung nicht.</strong> Das Bezugsgewicht für die Makros ist eine Standardnäherung, keine Messung deiner fettfreien Masse.',
                 '<strong>Das ist keine medizinische Beratung.</strong> Basal ist kein Medizinprodukt. Ein Verbrauch, der weit vom Erwarteten abweicht, eine Schwangerschaft, eine Krankheit oder eine Essstörung gehören in die Hände medizinischen Fachpersonals.'],
        appel_t='Diese Berechnungen, mit deinen Daten.', appel='Basal macht sie jede Woche für dich neu, aus deinen Mahlzeiten und Wägungen. Kostenlos, ohne Konto.', telecharger='Herunterladen',
        maj2024='Aktualisierung 2024', fibres_src='Ballaststoffe: 14 g pro 1.000 kcal', ciqual='Nährwerttabelle Ciqual 2025', licence='offene Lizenz Etalab 2.0',
        plus_t='Weiterlesen', outils='Werkzeuge', plus=[('Metabolische Anpassung', 'Warum eine Formel nicht reicht, und wie man sie korrigiert.'), ('Die Rechner', 'Verbrauch und Makros, mit denselben Formeln wie die App.')],
    )


META = {
    'en': ('Method', 'How Basal calculates', 'All the app’s formulas, with their constants, sources and limits. The worked examples on this page are recalculated by the app’s own code: if a formula changes, a test flags it and the page is updated.', 'App version 1.4',
           dict(title='Calculation method: formulas and sources — Basal', description='All the formulas in the Basal app: basal metabolic rate, expenditure, target, macros, adaptive expenditure, sessions and 1RM, with their constants, sources and limits.',
                og_title='Calculation method: formulas and sources — Basal', og_description='All the formulas in the Basal app, with their constants, sources and limits.')),
    'es': ('Método', 'Cómo calcula Basal', 'Todas las fórmulas de la aplicación, con sus constantes, sus fuentes y sus límites. Los ejemplos numéricos de esta página los recalcula el propio código de la app: si una fórmula cambia, un test lo señala y la página se actualiza.', 'Aplicación versión 1.4',
           dict(title='Método de cálculo: fórmulas y fuentes — Basal', description='Todas las fórmulas de la app Basal: metabolismo basal, gasto, objetivo, macros, gasto adaptativo, sesiones y 1RM, con sus constantes, sus fuentes y sus límites.',
                og_title='Método de cálculo: fórmulas y fuentes — Basal', og_description='Todas las fórmulas de la app Basal, con sus constantes, sus fuentes y sus límites.')),
    'de': ('Methode', 'Wie Basal rechnet', 'Alle Formeln der App, mit ihren Konstanten, Quellen und Grenzen. Die Rechenbeispiele auf dieser Seite werden vom Code der App selbst neu berechnet: Ändert sich eine Formel, meldet das ein Test, und die Seite wird aktualisiert.', 'App-Version 1.4',
           dict(title='Berechnungsmethode: Formeln und Quellen — Basal', description='Alle Formeln der Basal-App: Grundumsatz, Verbrauch, Ziel, Makros, adaptiver Verbrauch, Einheiten und 1RM, mit ihren Konstanten, Quellen und Grenzen.',
                og_title='Berechnungsmethode: Formeln und Quellen — Basal', og_description='Alle Formeln der Basal-App, mit ihren Konstanten, Quellen und Grenzen.')),
}

PAGES = {}
for l in ('en', 'es', 'de'):
    court, h1, chap, version, tete = META[l]
    t = textes(l)
    p = page(l, C, dict(court=court, surtitre=court, h1=h1, chapeau=chap, publie='2026-10-30', sommaire=list(zip(IDS, t['s'])), corps=corps(l, t)), tete)
    g = L[l]['guides']
    # La Méthode n'est pas un guide : fil Accueil › Méthode, et la version de l'app à la place de la date de mise à jour.
    p['main'] = p['main'].replace(f'<a href="{U["guides"][l]}">{g}</a><span aria-hidden="true">›</span>', '', 1).replace(
        '</time></span>\n    </div>', f'</time></span>\n      <span aria-hidden="true">·</span>\n      <span>{version}</span>\n    </div>', 1)
    p['ld'][1]['itemListElement'] = [p['ld'][1]['itemListElement'][0], dict(p['ld'][1]['itemListElement'][2], position=2)]
    PAGES[l] = p
