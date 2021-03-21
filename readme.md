---
title: "NSI - Première"
subtitle: "Projet snake - pygame zero"
author: "qkzk"
date: "2021/03/21"
theme: metropolis
geometry: margin=1.5cm

---

# Snake en pygame zero

L'objectif de ce petit projet est de vous familiariser avec la création
de jeux vidéos à l'aide de la librairie **pygame zero**

Cette libriairie s'appuie sur pygame et devrait être installée sur vos postes.

# Objectifs


Vous produisez un jeu snake jouable.

Le serpent se meut automatiquement.

S'il mange la nourriture il grandit et celle-ci réapparait dans une case
vide.

S'il quitte l'écran ou se mord, il meurt. La mort consiste à réinitialiser
le serpent.

# Deux approches

Selon vos aptitudes et vos connaissances en la matière, vous pouvez décider :

1. **de partir de zéro**

  En vous aidant seulement de la documentation de pygame zero.

2. **de partir de la version [snake_eleve](snake_eleve.py) et de poursuivre
  seul.**


3. **de partir de la version [snake_eleve](snake_eleve.py) et de faire le tutoriel**

# Principes généraux des jeux vidéos

Un jeu vidéo peut être résumé ainsi :

Une boucle infinie fait progresser le jeu :

```
A chaque tour :
  On écoute les intéractions du joueur,
  On met l'état du jeu à jour,
  On dessine les éléments à l'écran,
  On attend quelques milisecondes.
```

# Pygame zero

Le principe de pygame zéro est de proposer quelques fonctions simples
qui sont appelées automatiquement.

Ainsi :

* les intéractions du joueur sont accessibles avec la fonction `on_key_down(key)`
* la mise à jour de l'état du jeu se fait dans la fonction `update()`
* le graphisme se fait dans `draw()`

# Script pygame zéro minimal

Le script suivant lance pygame zero

```python
import pgzrun

pgzrun.go()
```

On définit généralement quelques constantes :

```python
import pgzrun
TITLE = "snake"
WIDTH = 400
HEIGHT = 400


pgzrun.go()
```

On a ainsi réglé le titre de la fenêtre et ses dimensions.

Attention, en pygame zero, on utilise généralement des variables _globales_
qui sont définies à la racine du script et sont mises à jour dans `update`
et dans les fonctions d'événements comme `on_key_down`.

Ce n'est pas une bonne pratique, mais c'est facile.

# État de départ [snake_eleve.py](snake_eleve.py)

Dans la version de départ :

* une grille est dessinée à l'écran.
* toutes les fonctions sont déclarées avec leurs paramètres et la documentation
* votre serpent est dessiné, sa nourriture aussi.
* il ne se passe rien

# Étape 1. Comprendre ce qui se passe.

Lisez le code et la documentation des fonctions.

# Étape 2. Repérez les fonctions dont la documention précise "A faire"

Il y en a 7 :

* `new_food`
* `check_if_snake_has_eaten`
* `new_head`
* `move_snake`
* `check_death`
* `update`
* `on_key_down`

# Étape 3. Déplacer le serpent tout droit.

Nous allons commencer par déplacer le serpent.

Pour cela, remplir la fonction `new_head`

Comme elle n'est jamais appelée, il ne se passera rien.

Ensuite passer à `move_snake`. Pour l'instant, on ignore le paramètre `has_eaten`
et on efface le dernier élément du serpent à chaque déplacement.

Intégrer `move_snake` à `update`.

_à cette étape, le serpent quitte l'écran par la droite à chaque partie_

# Étape 4. Déplacer le serpent.

Cela se fait dans la fonction `on_key_down`.

Vérifiez ce qui se passe quand on appuie sur une touche.

Vous pouvez compléter la fonction `on_key_down` de manière similaire à ce
qui est présent :

Si on presse la flêche droite, la direction change vers `[1, 0]`
etc.

_A cette étape, le serpent doit pouvoir tourner_

# Étape 5. Mourrir

Dans notre version du jeu :

* le serpent meurt lorsqu'il se mord la queue,
* ou lorsqu'il quitte l'écran.

Quand il meurt, il est réinitialisé et le jeu se poursuit normalement.

Il revient donc à son état de départ et une nouvelle nourriture apparaît.

Modifier la fonction `check_death` afin de détecter ces événements.

Modifier la fonction `update` pour en tenir compte.

_A cette étape le serpent meurt et réapparait_

# Étape 6. Détecter qu'on mange... et réagir

La détection se déroule dans `check_if_snake_has_eaten` qui renvoie Vrai si et seulement
si la tête est sur la nourriture.

La réaction se fait en deux temps :

1. lorsque le serpent mange, le dernier morceau de sa queue n'est pas effacé.
2. lorsque le serpent mange, la nourriture réapparait dans une case vide.

1. il faut modifier `move_snake` en fonction du paramètre `has_eaten`.
2. il faut modifier `new_food`. L'algorithme est décrit dans le commentaire.

_A cette étape le serpent grandit quand il mange, la nourriture réapparait_

Le jeu devrait être terminé...

# Extensions

De nombreux points sont améliorables :

* afficher un score (la longueur du serpent)
* conserver un high score. Tant qu'on ne quitte pas le jeu puis de manière
  persistante en l'écrivant dans un fichier
* améliorer les graphismes avec des sprites (chercher Actor dans la documentation
  de pygame zero)
* snake joue tout seul. Il est possible de créer un snake qui joue sans s'arrêter
  et gagne à chaque partie. C'est nettement plus difficile :)


