import { defineConfig } from 'astro/config';

// URL inchangées : `preserve` sort cgu.astro en /cgu.html et en/index.astro en /en/index.html,
// comme le site écrit à la main (lot 2 de la refonte, 2026-10-30). HTML non compressé pour que
// la comparaison avec l'ancien site reste lisible.
export default defineConfig({
  site: 'https://basal-app.fr',
  build: { format: 'preserve' },
  compressHTML: false,
});
