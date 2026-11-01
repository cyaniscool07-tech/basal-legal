// Améliorations communes aux pages de contenu ; chacune ne fait rien si l'élément visé est absent.
(function () {
  // Sous 980 px, le sommaire latéral est masqué : on en place une copie repliable en tête de l'article.
  var liste = document.querySelector('.sommaire ol'), corps = document.querySelector('.article .corps');
  if (liste && corps) {
    var plie = document.createElement('details');
    plie.className = 'sommaire-mobile';
    plie.innerHTML = '<summary>Sommaire</summary>';
    plie.appendChild(liste.cloneNode(true));
    plie.addEventListener('click', function (e) { if (e.target.closest('a')) plie.open = false; });
    corps.insertBefore(plie, corps.firstChild);
  }

  // Calculateurs, sur mobile : tant que la carte résultat est plus bas que l'écran, une barre en bas de l'écran
  // affiche le chiffre principal (marqué data-flottant) ; un toucher y fait défiler.
  var valeur = document.querySelector('[data-flottant]'), carte = valeur && valeur.closest('.carte.resultat');
  if (!carte || !('IntersectionObserver' in window)) return;
  var barre = document.createElement('button');
  barre.type = 'button';
  barre.className = 'resultat-flottant';
  barre.hidden = true;
  document.body.appendChild(barre);
  var enDessous = false;
  function maj() {
    var unite = valeur.nextElementSibling && valeur.nextElementSibling.tagName === 'SMALL' ? ' ' + valeur.nextElementSibling.textContent : '';
    var texte = valeur.textContent.trim() + unite;
    barre.hidden = !(enDessous && /\d/.test(valeur.textContent));
    barre.textContent = valeur.dataset.flottant + ' : ' + texte;
  }
  new IntersectionObserver(function (e) {
    enDessous = !e[0].isIntersecting && e[0].boundingClientRect.top > 0;
    maj();
  }).observe(carte);
  new MutationObserver(maj).observe(carte, { subtree: true, childList: true, characterData: true });
  barre.addEventListener('click', function () { carte.scrollIntoView({ behavior: 'smooth', block: 'center' }); });
})();
