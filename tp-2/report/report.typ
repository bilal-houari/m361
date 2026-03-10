#import "template.typ": *
#import "@preview/codly:1.3.0": *
#show: codly-init.with()

#show: project.with(
  title: "Rapport de TP 2",
  authors: (
    (name: "Bilal Houari", email: "houari.bilal@etu.uae.ac.ma", affiliation: "Lisence I.D.A.I."),
  ),
  date: "Mars 9, 2026",
)

#codly(stroke: 0.5pt + gray)

#show raw.where(block: true): it => {
  align(center)[#block(width: 90%, inset: 0.2em, breakable: false)[#it]]
}

#set table(
  fill: (_, y) => if y == 0 { rgb("#e4e4e4") },
)

#set list(indent: 2em)

= Description du problème traité
L'objectif de ce projet est de concevoir un système logiciel flexible pour un café. Le défi principal réside dans la gestion de la multitude de combinaisons possibles pour une boisson (ex: un café avec du lait, ou un café avec du sucre et du caramel). Plutôt que de créer une classe pour chaque variante (ce qui mènerait à une explosion du nombre de classes), nous devons mettre en place une structure permettant d'ajouter dynamiquement des ingrédients et de gérer des commandes clients incluant un système de fidélité.

= Architecture choisie
L'architecture repose sur plusieurs concepts clés de la Programmation Orientée Objet (POO) en Python :

- #strong[Pattern Décorateur :] C'est le cœur du projet. Nous utilisons une classe abstraite `Boisson` et une classe `DecorateurBoisson`. Cela permet d'envelopper une boisson de base (Café, Thé) avec des ingrédients (Lait, Sucre, Caramel) de manière dynamique.

- #strong[Héritage Simple et Abstrait :] Utilisation de la classe `ABC` pour définir le contrat de base que toutes les boissons doivent suivre (`cout` et `description`).

- #strong[Héritage Multiple :] La classe `CommandeFidele` hérite à la fois de `Commande` (gestion de base) et de `Fidelite` (système de points), permettant de combiner les fonctionnalités sans dupliquer le code.

- #strong[Dataclasses :] Utilisation de `@dataclass` pour la classe `Client`, simplifiant la gestion des données pures.

- #strong[Surcharge d'opérateur :] Redéfinition de la méthode `__add__` pour permettre la combinaison de deux boissons avec le symbole `+`.

= Description des principales fonctionnalités
- #strong[Création de boissons personnalisées :] Possibilité de créer des boissons de base et d'y ajouter autant d'ingrédients que souhaité.

- #strong[Combinaison de boissons :] Utilisation de l'opérateur `+` pour fusionner deux boissons en une seule description et un prix total.

- #strong[Gestion des commandes :] Un système permettant d'ajouter des boissons à un panier, de distinguer les commandes "Sur Place" ou "À Emporter" (polymorphisme), et de calculer le total.

- #strong[Système de fidélité :] Attribution automatique de points de fidélité au client en fonction du montant total lors de la validation de la commande.

= Réponses aux questions de réflexion (Partie 8)
+ #strong[Quelle partie du code permet d'ajouter facilement de nouveaux ingrédients ?]
  - C'est le #strong[Pattern Décorateur] (les classes héritant de `DecorateurBoisson`). Pour ajouter un ingrédient, il suffit de créer une nouvelle petite classe sans toucher au reste du code.

+ #strong[Si nous voulions ajouter une nouvelle boisson (chocolat chaud), quelles classes devraient être modifiées ?] 
  - #strong[Aucune classe existante] ne doit être modifiée. Il suffit de créer une nouvelle classe `ChocolatChaud` qui hérite de `Boisson`. C'est le principe de l'ouverture à l'extension.

+ #strong[Pourquoi séparer les responsabilités entre plusieurs classes rend le programme plus facile à maintenir ?]
  - Cela limite l'impact des changements. Si le prix du lait change, on ne modifie que la classe `Lait`. Si la règle de calcul des points de fidélité change, on ne modifie que la classe `Fidelite`. Cela rend le code plus lisible, plus facile à tester et évite les bugs en cascade.

= Exemple d'exécution
#figure(
  image("screenshot.png", width: 70%)
)