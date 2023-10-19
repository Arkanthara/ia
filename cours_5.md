# Satisfaction et propagation de contraintes



Ici, ce qui compte, c'est la solution finale et pas forcément le chemin qui mène à la solution finale.

On n'étudie pas toutes les combinaisons... On ne s'occupe que des configurations  valides.





### Contraintes

Un problème de satisfaction de contrainte (PSC) est représenté par:

- Un ensemble de variables $X = (x_1, \dots, x_N)$
  
  Chaque variable $x_i$ ayant un domaine de valeurs admissibles $D_i$ (en général discret et fini)

- Un ensemble de contraintes sur les variables: $C=(c_1, \dots, c_M)$
  
  Chaque contrainte $c_j$ est une proposition logique (égalité, inégalité, ...) qui s'applique sur les variables $X$



Dans le cours, on ne va que traîter des PSC finis....



Rappel résolution linéaire: algo du simplex...



#### Commutativité des affectations

Remarque: Une affectation valide ne dépend pas de l'ordre dans lequel elle a été construite

Transition:

- Choix de une variable $x_p$ à affecter

- Affectation de $x_p$ à ses valeurs admissibles $D_p$



#### Forward checking

Affecter une valeur à une variable rend invalide d'autres affectations (par les contraintes) (_forward checking_)

- Lors de l'affectation, on regarde l'impact sur les domaines valides des autres variables non-affectées

- blabla (pas eu le temps de copier...)
  
  
  
  Forward checking: création de domaine pour chaque variable donnant les valeurs possibles ????

Heurisitique: fixer la variable qui va me contraindre le plus (la variable qui a le plus petit domaine...)



Algorithme myope: ne voit pas plus loin que le bout de son nez... Manque d'anticipation.... (C'est le cas pour le forward checking...)
