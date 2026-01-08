# 02 - Chargement des données

But
- Charger le jeu de données MovieLens (dossier `ml-100k`) : notes (`u.data`), utilisateurs (`u.user`), films (`u.item`) et genres (`u.genre`).

Points clés du code
- `DATA_DIR = "ml-100k"` : dossier contenant les fichiers.
- `ratings = pd.read_csv(ratings_path, sep="\t", names=["user_id","item_id","rating","timestamp"])` : format tabulé.
- `users = pd.read_csv(users_path, sep="|", names=["user_id","age","gender","occupation","zip_code"])`.
- `genres` : lecture pour extraire la liste des genres.
- `items` : lecture de `u.item` avec colonnes `item_id, title, release_date, ...` et colonnes binaires pour chaque genre. Encodage `latin-1` pour les titres.

Conseils
- Vérifier les chemins si le dossier est ailleurs.
- Afficher `head()` pour valider que les colonnes sont correctement parsées.
