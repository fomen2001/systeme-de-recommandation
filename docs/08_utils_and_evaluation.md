# 08 - Utilitaires et mesure simple de comparaison

Fonctions et usage

- `show_recos(user_id, recos, items_df, title="Recommandations")` : affichage lisible des recommandations (titre et score).
- Sélection d'exemples : génération de `test_users` par tirage aléatoire pour visualiser des recommandations d'exemple.
- Choix de la similarité : le notebook permet d'alterner entre `user_cosine`, `item_cosine`, `user_pearson`, `item_pearson`.

Comparaison user vs item
- Le notebook compare qualitativement les recommandations user-based et item-based pour les mêmes utilisateurs.

Mesure simple
- `overlap_topk(reco_a, reco_b, k=10)` : mesure la proportion d'items communs dans les top-k des deux listes (valeur entre 0 et 1).
- Utilisé pour estimer la similarité des recommandations produites par deux méthodes.

Notes sur l'évaluation
- `overlap_topk` est une métrique intuitive mais limitée. Pour une évaluation plus robuste, considérer : précision@k, rappel@k, MAP, NDCG, et tests sur un split train/test.
