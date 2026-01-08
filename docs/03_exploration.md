# 03 - Exploration des données

Objectifs
- Comprendre la distribution des notes, la densité/sparsité et le comportement des utilisateurs/films.

Calculs et visualisations
- `n_users`, `n_items`, `n_ratings` : dénombrement des entités.
- `sparsity = 1 - (n_ratings / (n_users * n_items))` : fraction de la matrice user×item non renseignée.
- Histogrammes / barplots : distribution des notes, nombre de notes par utilisateur, nombre de notes par film (`matplotlib`).

Interprétation
- Une forte sparsité (proche de 1) est typique des systèmes de recommandation et impacte les méthodes (ex: filtrage collaboratif basé sur voisinage).
- Visualiser la distribution aide à décider d'éventuelles normalisations (centrer par utilisateur, etc.).
