
---

# 📽️ Mini-Projet : Système de Recommandation de Films

**Approche collaborative & basée sur le contenu**

---

## 1️⃣ Contexte et objectif du projet

Les plateformes de streaming utilisent des **systèmes de recommandation** pour proposer aux utilisateurs des contenus adaptés à leurs goûts, afin de :

* améliorer l’expérience utilisateur,
* augmenter le temps passé sur la plateforme,
* favoriser la découverte de nouveaux contenus.

🎯 **Objectif du projet**
Mettre en œuvre plusieurs approches de recommandation de films à partir du dataset **MovieLens 100k**, puis comparer leurs logiques et leurs résultats.

---

## 2️⃣ Données utilisées

Nous utilisons le dataset **MovieLens 100k**, qui contient :

* **100 000 notes**
* **943 utilisateurs**
* **1682 films**

### 📊 Tables principales

* `ratings` : notes (user_id, item_id, rating)
* `items` : films (titre, genres)
* `users` : informations utilisateurs (âge, sexe, profession)

👉 La matrice **utilisateur–film** est très **creuse (sparse)**, ce qui justifie l’usage de méthodes de recommandation avancées.

---

## 3️⃣ Approche 1 : Filtrage collaboratif (rappel)

### 🔹 Principe général

Le filtrage collaboratif repose sur l’idée que :

> *des utilisateurs ayant eu des comportements similaires dans le passé auront des préférences similaires dans le futur.*

Deux variantes ont été implémentées :

* **User-based** : similarité entre utilisateurs
* **Item-based** : similarité entre films

Les similarités sont calculées avec :

* la **similarité cosinus**
* le **coefficient de Pearson**

Les notes sont ensuite **prédites par moyenne pondérée** des voisins les plus similaires.

---

## 4️⃣ Approche 2 : Recommandation basée sur le contenu (Session 3)

Contrairement au filtrage collaboratif, la recommandation basée sur le contenu :

* **n’utilise pas les autres utilisateurs**
* se base uniquement sur les **caractéristiques des films** déjà appréciés par l’utilisateur

---

## 5️⃣ Construction des profils de films

### 🔹 Descripteurs utilisés

Pour chaque film, nous construisons un **profil textuel** à partir de :

* le **titre du film**
* les **genres** (Action, Drama, Comedy, etc.)

📌 Exemple de profil film :

> *“Star Wars Action Adventure Sci-Fi”*

---

## 6️⃣ Représentation vectorielle des films

### 6.1 TF-IDF (Term Frequency – Inverse Document Frequency)

TF-IDF permet de transformer les textes en vecteurs numériques en :

* valorisant les mots **importants pour un film**
* pénalisant les mots trop fréquents

👉 Chaque film est représenté par un **vecteur TF-IDF**.

---

### 6.2 Word2Vec (embeddings)

Word2Vec apprend des **représentations vectorielles continues** des mots à partir du corpus :

* capture des **relations sémantiques**
* permet de représenter un film par la **moyenne des embeddings de ses mots**

👉 Chaque film est représenté par un **vecteur dense**.

---

## 7️⃣ Construction du profil utilisateur

Pour chaque utilisateur, nous construisons un **profil utilisateur agrégé** :

### 🔹 Méthode

1. Sélection des films **bien notés** par l’utilisateur
2. Pondération des films par la note donnée
3. Moyenne pondérée des vecteurs de films

📌 Formellement :
[
Profil_utilisateur = \frac{\sum (note_i - 3) \times vecteur_film_i}{\sum (note_i - 3)}
]

👉 On obtient un **vecteur représentant les goûts de l’utilisateur**.

---

## 8️⃣ Calcul de la similarité et recommandations

### 🔹 Similarité utilisée

* **Similarité cosinus** entre :

  * le profil utilisateur
  * les profils des films non encore vus

### 🔹 Recommandation finale

Les films ayant la **plus forte similarité** avec le profil utilisateur sont recommandés.

---

## 9️⃣ Recommandation de films “similaires à ceux déjà appréciés”

Deux stratégies ont été mises en œuvre :

### ✅ 1. Film → films similaires

* On prend un film bien noté
* On recommande les films les plus proches en similarité contenu

👉 Utile pour la **découverte ciblée**

---

### ✅ 2. Profil utilisateur → films similaires

* On agrège tous les films aimés
* On recommande les films proches du **profil global**

👉 Recommandation plus **personnalisée et stable**

---

## 🔟 Comparaison TF-IDF vs Word2Vec

| Critère           | TF-IDF | Word2Vec   |
| ----------------- | ------ | ---------- |
| Interprétabilité  | Élevée | Moyenne    |
| Sens sémantique   | Faible | Forte      |
| Complexité        | Faible | Moyenne    |
| Qualité des recos | Bonne  | Très bonne |

---

## 1️⃣1️⃣ Limites du projet

* Pas de prise en compte du **temps**
* Pas de **cold start** traité (nouvel utilisateur)
* Dataset limité (pas de descriptions longues)

---

## 1️⃣2️⃣ Conclusion

Ce projet montre que :

* les **systèmes de recommandation** peuvent être implémentés avec différentes approches
* le **filtrage collaboratif** exploite les comportements collectifs
* la **recommandation basée sur le contenu** permet une personnalisation fine
* les **embeddings** (Word2Vec) améliorent la qualité sémantique des recommandations

👉 Une approche **hybride** serait idéale pour un système en production.

---


