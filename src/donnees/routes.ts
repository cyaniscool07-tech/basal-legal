// Rubriques du site et leur adresse dans chaque langue : une seule source pour le menu (Entete.astro).
// Une adresse dont la page n'existe pas encore est ignorée à la construction (voir `existe`).
export type Lang = 'fr' | 'en' | 'es' | 'de';

export const RUBRIQUES: { cle: string; chemin: Record<Lang, string>; nom: Record<Lang, string> }[] = [
  { cle: 'guides', chemin: { fr: '/guides/', en: '/en/guides/', es: '/es/guias/', de: '/de/ratgeber/' }, nom: { fr: 'Guides', en: 'Guides', es: 'Guías', de: 'Ratgeber' } },
  { cle: 'recettes', chemin: { fr: '/recettes/', en: '/en/recipes/', es: '/es/recetas/', de: '/de/rezepte/' }, nom: { fr: 'Recettes', en: 'Recipes', es: 'Recetas', de: 'Rezepte' } },
  { cle: 'calculateurs', chemin: { fr: '/calculateurs/', en: '/en/calculators/', es: '/es/calculadoras/', de: '/de/rechner/' }, nom: { fr: 'Calculateurs', en: 'Calculators', es: 'Calculadoras', de: 'Rechner' } },
  { cle: 'methode', chemin: { fr: '/methode.html', en: '/en/method.html', es: '/es/metodo.html', de: '/de/methode.html' }, nom: { fr: 'Méthode', en: 'Method', es: 'Método', de: 'Methode' } },
  { cle: 'apropos', chemin: { fr: '/a-propos.html', en: '/en/about.html', es: '/es/sobre-basal.html', de: '/de/ueber-basal.html' }, nom: { fr: 'À propos', en: 'About', es: 'Sobre Basal', de: 'Über Basal' } },
];

// Adresses des pages construites, tirées des fichiers de src/pages (routes dynamiques : leur dossier).
const fichiers = Object.keys(import.meta.glob('/src/pages/**/*.astro'));
const adresses = new Set(
  fichiers.map((f) => f.replace('/src/pages', '').replace(/\.astro$/, '.html').replace(/\/index\.html$/, '/').replace(/\/\[slug\]\.html$/, '/'))
);
export const existe = (chemin: string) => adresses.has(chemin);
