from commun import U, page, stores

FR = '/metabolisme-de-base.html'
DATE = '2026-11-11'
C = 'metabolisme-de-base'
EXISTANTS = {'es': '/es/metabolismo-basal.html', 'de': '/de/grundumsatz.html'}

EN = dict(court='Basal metabolic rate', surtitre='Calories and expenditure', publie='2026-11-02',
    h1='Basal metabolic rate: what it is and what changes it',
    chapeau='Your basal metabolic rate is the energy your body spends at complete rest, to breathe, keep your heart beating and hold its temperature. In a low-activity adult, it is the largest part of the day’s expenditure. Here is how it is estimated, what really changes it, and what a formula cannot know about you.',
    sommaire=[('definition', 'Definition'), ('share', 'Its share of expenditure'), ('estimate', 'How it is estimated'), ('examples', 'Worked examples'), ('what-changes-it', 'What changes it'),
              ('age', 'Age, really?'), ('eating-below', 'Eating below your basal metabolic rate'), ('unknown', 'What we do not know'), ('sources', 'Sources')],
    corps=f'''      <div class="en-bref">
        <p class="surtitre">In short</p>
        <p>Basal metabolic rate is usually between 1,200 and 2,000 kcal a day in adults. It depends above all on your lean mass (muscles and organs), so on your weight and height, far more than on your age. A formula like Mifflin-St Jeor estimates it to within about 10% for most people, but it can be further off for you.</p>
      </div>

      <h2 id="definition">Definition</h2>
      <p>The <strong>basal metabolic rate</strong> (BMR) is the energy expenditure of a person who is awake, lying down, at complete rest, twelve hours after their last meal, in a room at neutral temperature. It is the running cost of the body: heart, breathing, brain, liver, kidneys, cell renewal, temperature control.</p>
      <p>When measured in a lab, it is more often called <strong>resting metabolic rate</strong> (RMR), with slightly less strict conditions and often a slightly higher value. The usual formulas, including the one Basal uses, actually estimate this resting expenditure. The difference is small and everyday language mixes the two.</p>

      <h2 id="share">Its share of expenditure</h2>
      <p>Your daily expenditure has three blocks:</p>
      <ul>
        <li><strong>basal metabolic rate</strong>, about 60 to 70% of expenditure in a low-activity person;</li>
        <li><strong>digestion</strong> (the thermic effect of food), about 10%;</li>
        <li><strong>activity</strong>: sport, but above all all the movement of daily life (walking, standing, moving around). It is the block that varies most from one person to another.</li>
      </ul>
      <p>That is why your basal metabolic rate is not what you should eat: it is the starting point. To get your total expenditure, it is multiplied by an activity factor, from 1.2 for a sedentary person to 1.9 for intense daily sport. The <a href="{U["tdee"]["en"]}">calorie calculator</a> does both steps.</p>

      <h2 id="estimate">How it is estimated</h2>
      <p>Direct measurement uses indirect calorimetry: a device analyses the oxygen consumed and the carbon dioxide breathed out over twenty to thirty minutes. It is found in hospitals and some labs, rarely elsewhere.</p>
      <p>Day to day, an equation is used. Basal uses <strong>Mifflin-St Jeor</strong> (1990), which the American Dietetic Association’s systematic review (Frankenfield, 2005) judged the most reliable of the common equations in adults, including overweight adults:</p>
      <ul>
        <li>man: <code>10 × weight (kg) + 6.25 × height (cm) − 5 × age + 5</code></li>
        <li>woman: <code>10 × weight (kg) + 6.25 × height (cm) − 5 × age − 161</code></li>
      </ul>
      <p>The older Harris-Benedict equation (1919) overestimates the expenditure of today’s populations on average. If you know your lean mass, for example from a DEXA scan, the Katch-McArdle equation (<code>370 + 21.6 × lean mass in kg</code>) takes it into account directly. Bioimpedance scales give a lean mass too imprecise to benefit from it.</p>

      <h2 id="examples">Worked examples</h2>
      <p>These results are calculated by the app’s own code: a test checks that they stay correct if the formula changes.</p>
      <div class="calcul" role="group" aria-label="Basal metabolic rate examples">
        <div class="titre">With Mifflin-St Jeor</div>
        <div class="ligne"><span>Woman, 45, 165 cm, 60 kg</span><b>1,245 kcal</b></div>
        <div class="ligne"><span>Woman, 30, 175 cm, 70 kg</span><b>1,483 kcal</b></div>
        <div class="ligne"><span>Man, 30, 175 cm, 70 kg</span><b>1,649 kcal</b></div>
        <div class="ligne"><span>The same man at 50</span><b>1,549 kcal</b></div>
        <div class="ligne"><span>Man, 55, 180 cm, 90 kg</span><b>1,755 kcal</b></div>
      </div>
      <p>At the same height, weight and age, the formula gives a woman 166 kcal less: that is the average difference in lean mass between the sexes, not a difference in metabolic “speed”. For your own number, the <a href="{U["tdee"]["en"]}">calculator</a> shows your basal metabolic rate and daily expenditure, without sending anything.</p>

      <h2 id="what-changes-it">What changes it</h2>
      <p>A study of 150 adults whose basal metabolic rate was measured (Johnstone, 2005) looked at what explains the differences between people:</p>
      <ul>
        <li><strong>lean mass</strong> alone explains about 63% of the differences;</li>
        <li><strong>fat mass</strong>, about 6%: it spends little, but it does spend;</li>
        <li><strong>age</strong>, about 2%;</li>
        <li>about a quarter of the differences remain unexplained.</li>
      </ul>
      <p>Once lean mass is accounted for, sex adds almost nothing. Muscle counts, but less than often claimed: a kilo of muscle at rest spends around 13 kcal a day, while the liver, brain, heart and kidneys, which weigh little, spend much more. Gaining 2 kg of muscle raises basal metabolic rate by a few dozen kcal, not several hundred.</p>
      <p>Weight loss, on the other hand, lowers it: a lighter body spends less. Part of that drop goes beyond what the weight loss explains — that is <a href="{U["metabolisme-adaptatif"]["en"]}">metabolic adaptation</a>, and it is why a formula calculated once is not enough during a diet.</p>

      <h2 id="age">Age, really?</h2>
      <p>The formula takes off 5 kcal per year of age: an average observed across groups, which mixes age with the muscle loss that often comes with it. A large study of over 6,400 people (Pontzer, 2021) found that expenditure, adjusted for body size and composition, stays <strong>stable between 20 and 60</strong>, then falls by about 0.7% a year.</p>
      <p>In other words, “metabolism slows down at 40” is mainly true when you lose muscle and move less. Staying active and strength training limit most of the decline.</p>

      <h2 id="eating-below">Eating below your basal metabolic rate</h2>
      <p>Since total expenditure is higher than basal metabolic rate, eating a little below it does not mean the body “shuts down”. But such a low intake leaves little room for protein, fibre and micronutrients, and adds to fatigue and muscle loss.</p>
      <p>Basal therefore applies a simple rule: the suggested calorie target <strong>never goes below your estimated basal metabolic rate</strong>. It is a cautious choice by the app, not a physiological law. The <a href="{U["deficit"]["en"]}">calorie deficit</a> guide details a reasonable pace of loss.</p>

      <h2 id="unknown">What we do not know</h2>
      <div class="inconnu">
        <p><strong>Your exact number.</strong> A formula gives the average of people who resemble you on paper. For some people, the gap with a measurement exceeds 10%, that is 150 kcal or more.</p>
        <p><strong>Your lean mass.</strong> It explains most of the differences, but no formula based on weight and height knows it.</p>
        <p style="margin:0"><strong>The effect of sleep, stress or cold on your day.</strong> It exists, but it is small and hard to put a number on for a given person.</p>
      </div>
      <p>The only way to correct the estimate without a lab is to compare what you eat with how your weight actually changes over a few weeks. That is what the <a href="{U["depense-reelle"]["en"]}">real expenditure calculator</a> does, and what the app does continuously.</p>

      <div class="appel">
        <p class="appel-t">Your metabolism, recalculated from your data</p>
        <p>Basal starts from Mifflin-St Jeor, then corrects your expenditure with what you eat and your actual weight. Tracking is free and needs no account.</p>
        {stores("en", "en-basal-metabolic-rate")}
      </div>

      <h2 id="sources">Sources</h2>
      <ol class="sources">
        <li>Mifflin MD, St Jeor ST et al. “A new predictive equation for resting energy expenditure in healthy individuals”. <i>American Journal of Clinical Nutrition</i>, 1990, 51(2), p. 241-247.</li>
        <li>Frankenfield D, Roth-Yousey L, Compher C. “Comparison of predictive equations for resting metabolic rate in healthy nonobese and obese adults: a systematic review”. <i>Journal of the American Dietetic Association</i>, 2005, 105(5), p. 775-789.</li>
        <li>Johnstone AM et al. “Factors influencing variation in basal metabolic rate include fat-free mass, fat mass, age, and circulating thyroxine but not sex, circulating leptin, or triiodothyronine”. <i>American Journal of Clinical Nutrition</i>, 2005, 82(5), p. 941-948.</li>
        <li>Pontzer H et al. “Daily energy expenditure through the human life course”. <i>Science</i>, 2021, 373(6556), p. 808-812.</li>
        <li>Wang Z et al. “Specific metabolic rates of major organs and tissues across adulthood: evaluation by mechanistic model of resting energy expenditure”. <i>American Journal of Clinical Nutrition</i>, 2010, 92(6), p. 1369-1377.</li>
      </ol>

      <h2 style="font-size:1.5rem;margin-top:48px">Going further</h2>
      <div class="guides" style="grid-template-columns:repeat(auto-fit,minmax(240px,1fr))">
        <a class="guide" href="{U["combien"]["en"]}"><span class="surtitre" style="margin:0">Guide</span><h3>How many calories a day?</h3><p>From basal metabolic rate to your real need, with worked examples.</p></a>
        <a class="guide" href="{U["metabolisme-adaptatif"]["en"]}"><span class="surtitre" style="margin:0">Guide</span><h3>Adaptive metabolism</h3><p>Why a formula is not enough, and how to correct it.</p></a>
      </div>''')

PAGES = {
    'en': page('en', C, EN, dict(title='Basal metabolic rate: definition, formula and what changes it — Basal',
        description='Basal metabolic rate is the energy spent at complete rest: 60 to 70% of a low-activity person’s expenditure. Mifflin-St Jeor formula, worked examples, the role of lean mass and age, with sources.',
        og_title='Basal metabolic rate: what it is and what changes it', og_description='How it is estimated, what really changes it (lean mass, weight, age), and what a formula does not know. With sources.')),
}
