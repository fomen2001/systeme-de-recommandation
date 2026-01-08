# Documentation du projet — Résumé des fichiers explicatifs

Ce document répertorie les fichiers Markdown générés pour expliquer chaque partie du notebook `projet-sys-recommand-M2.ipynb`.

- [01 - Imports et bibliothèques](docs/01_imports.md) : bibliothèques utilisées.
- [02 - Chargement des données](docs/02_load_data.md) : lecture de `u.data`, `u.user`, `u.item`, `u.genre`.
- [03 - Exploration des données](docs/03_exploration.md) : calculs de sparsité et visualisations.
- [04 - Construction de la matrice R](docs/04_matrix.md) : pivot table users×items.
- [05 - Calcul des similarités](docs/05_similarity.md) : cosinus et Pearson, user/item.
- [06 - Filtrage collaboratif user-based](docs/06_user_based.md) : fonctions de prédiction et recommandation.
- [07 - Filtrage collaboratif item-based](docs/07_item_based.md) : fonctions item-based.
- [08 - Utilitaires et évaluation simple](docs/08_utils_and_evaluation.md) : affichage, tests et overlap@k.

Usage
- Ouvrir les fichiers dans `docs/` pour lire les explications.
- Si vous voulez que je génère des versions plus détaillées (exemples d'exécution, complexité, améliorations possibles), dites-moi lesquelles.
