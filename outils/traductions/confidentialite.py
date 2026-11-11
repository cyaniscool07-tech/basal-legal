import os
from commun import legale

FR = '/confidentialite.html'
DATE = '2026-11-11'
C = 'confidentialite'
EXISTANTS = {'en': '/en/privacy.html'}  # traduction anglaise écrite à la main : reliée, pas réécrite
ICI = os.path.dirname(os.path.abspath(__file__))
# Corps traduits dans confidentialite.<lang>.html (texte long, plus lisible hors du code).
META = {'es': ('Política de privacidad — Basal', 'Política de privacidad de la aplicación Basal (seguimiento nutricional, peso, metabolismo y actividad).'),
        'de': ('Datenschutzerklärung — Basal', 'Datenschutzerklärung der App Basal (Ernährungs-, Gewichts-, Stoffwechsel- und Aktivitätstracking).')}
PAGES = {l: legale(l, C, *META[l], open(os.path.join(ICI, f'confidentialite.{l}.html'), encoding='utf-8').read().rstrip()) for l in META}
