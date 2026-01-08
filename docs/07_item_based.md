# 07 - Filtrage collaboratif item-based

Fonctions principales

1) `predict_item_based(u, item_id, sim_item, R, k=20)`
- But : prédire la note de `u` pour `item_id` en pondérant par similarité entre `item_id` et les autres items notés par `u`.
- Étapes :
  - Récupérer les notes de l'utilisateur `u` (`user_ratings`).
  - Extraire les similarités entre `item_id` et les items notés par `u` depuis `sim_item`.
  - Conserver les `k` items les plus similaires et calculer la moyenne pondérée.
- Retour : prédiction (float) ou `NaN`.

2) `recommend_item_based(u, sim_item, R, k_items=20, n_rec=10)`
- But : pour chaque item non vu par `u`, prédire la note via `predict_item_based` et trier pour renvoyer les top `n_rec`.

3) `display_item_based_reco(user_id, sim_item, R, items, k_items=30, n_rec=10)`
- Formatage et affichage similaire à la version user-based.

Avantages du item-based
- Souvent plus stable dans le temps (les items changent moins que les utilisateurs), et efficace quand le nombre d'utilisateurs est très élevé.
- Complexité différente : on peut pré-calculer les similarités item×item et les réutiliser.
