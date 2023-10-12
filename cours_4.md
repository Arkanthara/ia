# Recherche heuristique

Essayer d'aller vers la solution optimale

On applique une connaissance à priori pour réussir à se diriger vers le bon chemin

## Definition Heuristique

Une heuristique est une fonction h d'estimation de coût telle que

$h \rightarrow R^+$ avec $h(v) =0$ si $state(v) = s_G$

$h(v)$ représente une estimation du coût du chemin de l'état actuel à l'état final $s_G$ passant par le noeud v (ayant v comme première étape...). On cherche à minimiser $h(v)$ ...

Elle ne doit pas changer la complétude de l'algorithme: si il y a une solution, elle ne doit pas l'empêcher de l'atteindre.

Une recherche aveugle est une heuristique

La qualité d'une heuristique est bonne en moyenne, mais n'est pas garantie....

## Definition fonction d'évaluation

La fonction d'évaluation $f$ fournit le coût estimé d'une solution (chemin) passant par le noeud $v$.

### Recherche en coût uniforme

$g(v):$ coût du chemin de la racine au noeud v

$g(v)$ représente la somme des coûts de transition entre les états $c(s, s')$ le long du chemin.

solution 1: utiliser $f(v) = h(v)$ : Heuristique pure $\rightarrow$ Greedy Best First Search

solution 2: utiliser $f(v) = g(v) + h(v)$: prise en compte de la situation actuelle.

### Greedy BFS

Complet

Non optimal

#### Complexité

Temps: $O(b^m)$ avec m profondeur maximale

Espace: $O(b^m)$ conserve les noeuds pour $f(v)$

## Definition heuristique admissible

Une heuristique est admissible si elle sous-estime le coût du chemin vers la solution.

(Il n'y a que la solution finale qui ressemble à la solution finale)

Si $h^*(v)$ est le coût réel, alors si $h$ est admissible, on aura:

$0 \leq h(v) \leq h^*(v)$

Une heuristique qui maintient cet ordre est dite consistante:

s'il existe une transition de $s$ à $s'$ de coût $c(s, s')$ alors

$h(s) \leq h(s') + c(s, s')$

Plus l'heuristique est proche de $h^*$, plus elle est précise....



#### Beam search

C'est Best First search avec une limite de longueur pour la liste:

- consommation mémoire limitée

- Temps de recherche réduit

On limite le nombre d'états suivants à explorer...

On ne développe que les B états les plus prometteurs.

#### $A^*$

C'est l'algorithme BFS avec la fonction d'évaluation:

$f(v) = g(v) + h(v)$

où h est une heuristique admissible et consistante, et

$c(s, s') \geq \epsilon \gt 0 \ \forall s, s'$

Sous ces conditions:

L'algorithme $A^*$ est complet et optimal

- sur graphe fini

- sur graphe infini avec: 
  
  - un facteur de branchement fini
  
  - un coût par arrête strictement positif $c(s, s') \geq 0$

#### $IDA^*$ (iterative deepening $A^*$)

IDS limite la profondeur $\rightarrow$ évite que la recherche en profondeur explore des chemins indéfiniment.



Même principe: $IDA^*$ limite $f(v)$

Ne pas approfondir des chemins de coût excessif !!!

Complet

Optimal

Utilise moins de mémoire que $A^*$

Ne nécessite pas de tri explicite

Revisite des chemins hors du chemin courant

N'offre pas une utilisation optimale de la mémoire

#### SMA* (Simplified Memory-bounded A*)

Idée simple:

On fixe la limite mémoire

si la limite est atteinte, on enlève le noeud le moins intéressant



Comme $A^*$ tant que la limite n'est pas atteinte

complet si la mémoire est suffisante

optimal si la mémoire est suffisante pour contenir les données importantes...



### Génération d'heuristiques

Une stratégie de création d'heuristiques est la relaxation du problème:

On rend le problème plus simple

on enlève des contraintes



Un problème idéalmenet relaxé est:

simple à résoudre

bien moins couteux à résoudre que



Stratégies de recherche

locale: pas d'arbre conservé, juste une connaissance locale (seule la solution importante, pas le chemin)

steepest: on développe seulement le noeud de coût minimal (Dijkstra)



### Quand utiliser la recherche ?

Espace d'état est de taille raisonnable

Il existe de bonnes heuristiques

On ne peut pas calculer de gradient vers la solution (peut être vu comme une heuristique pour améilorer la solution courante)



### Résumé

Heuristique permet d'exploiter l'aléa dans les recherches

doit pas changer complétude

peut être admissible et/ou consistante

$A^*$: complet et optimal

$\rightarrow$  varinates en fonction des contraintes


