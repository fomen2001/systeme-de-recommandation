# 05 - Calcul des similarités

Vue d'ensemble
- Le notebook calcule des similarités entre utilisateurs et entre items, en utilisant deux métriques principales : cosinus et Pearson.

Cosinus
- Prépare `R_filled = R.fillna(0)`.
- `cosine_similarity(R_filled)` donne une matrice user×user.
- `cosine_similarity(R_filled.T)` donne une matrice item×item.
- Le cosinus fonctionne bien quand on remplace les valeurs manquantes par 0 (représente absence de signal).

Pearson
- `R.T.corr(method="pearson")` : corrélations entre utilisateurs (en transposant), mesure centrée sur la moyenne.
- `R.corr(method="pearson")` : corrélations entre items.
- Pearson peut produire davantage de NaN si peu d'éléments en commun existent.

Choix
- Le code propose d'utiliser cosinus pour la majorité des expériences, avec l'option Pearson commentée.
