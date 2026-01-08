# 04 - Construction de la matrice R (users × items)

But
- Construire une matrice `R` où chaque ligne est un utilisateur et chaque colonne un film, la valeur étant la note (ou `NaN` si non noté).

Code clé
- `R = ratings.pivot_table(index="user_id", columns="item_id", values="rating")`
- `R.fillna(0)` est utilisé plus tard pour calculer des similarités (cosinus) qui ne gèrent pas bien les NaN.

Remarques
- Garder la version avec `NaN` est utile pour les prédictions (savoir ce qui est effectivement noté).
- Le remplissage par 0 est une stratégie simple pour la similarité cosinus mais peut biaiser les mesures si beaucoup de zéros artificiels existent.
