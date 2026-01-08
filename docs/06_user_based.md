# 06 - Filtrage collaboratif user-based

Fonctions principales

1) `predict_user_based(u, item_id, sim_matrix, R, k=20, min_common=3)`
- But : prédire la note que l'utilisateur `u` donnerait à `item_id` en pondérant par la similarité des autres utilisateurs.
- Étapes :
  - Récupérer les utilisateurs ayant noté `item_id` (`raters`).
  - Extraire les similarités entre `u` et ces utilisateurs depuis `sim_matrix`.
  - Conserver les `k` plus proches voisins.
  - Moyenne pondérée des notes des voisins (pondération par la similarité absolue).
- Retour : prédiction (float) ou `NaN` si impossible.

2) `recommend_user_based(u, sim_matrix, R, k_neighbors=20, n_rec=10)`
- But : générer les `n_rec` meilleures recommandations pour `u` en appliquant `predict_user_based` sur tous les items non vus.

3) `display_user_based_reco(user_id, sim_matrix, R, items, k_neighbors=30, n_rec=10)`
- But : formatage et affichage des recommandations (jointure avec `items` pour récupérer le titre).

Points d'attention
- Complexité : prédire pour tous les items non vus peut être coûteux si la grille est grande.
- Normalisations (centrer par utilisateur) non implémentées : ici la méthode est une moyenne pondérée simple.
- `min_common` est défini mais non utilisé en profondeur ; on peut l'ajouter pour exiger un nombre minimal de co-notations.
