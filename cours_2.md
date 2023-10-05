### Problèmes de recherche

But: Résoudre un problème donné

Méthode: par étapes, selon ce qui est possible

Exemple: Jeu du taquin

#### Formalisation

On cherche une solution / une méthodologie plus générale...

- Problème -> modèle, catégorie
- solution -> algorithme
- difficulté -> complexité
- solution -> convergence
- existence des solutions -> propriétés: existence, unicité, optimalité

Pour définir un problème, on doit définir
- un espace d'états S
- un état initial appartenant à S
- un état final appartenant à S

Pour définir un problème, on doit aussi définir les actions possibles...

Les actions passées peuvent ou non influencer le choix de la prochaine action...

### Etats et Transitions

#### Définition

Un état est une configuration d'un système.

Un état peut être observable ou non. (ex: malade ou non... On observe que les symptômes ou les conséquences du fait d'être malade... On n'accède pas directement à l'état)

C'est un ensemble de valeurs des paramètres d'un système. On parle de vecteur d'état

(On transforme la vue de notre système en un vecteur d'état..... Conserver cette note ????)

#### Définition

L'espace d'états (state space) S d'un système rassemble tous les états (revoir cours...)

Dans le cas discret, on peut énumérer tous les états. La taille de S peut être une mesure de la complexité du problème. (Ex: un taquin de 2 est moins complexe qu'un taquin de 20...)
Cela peut être une mesure de complexité, mais ce n'est pas la seule....

On peut distinguer la notion d'espace d'états continu ou dénombrable

Espace continu: par exemple la position d'un robot...

Espace dénombrable: infini, non borné, mais labelisable

Avec un espace d'état infini, on est jamais sûr qu'une solution n'existe pas, même si la recherche reste infructueuse. 

Les états sont liés entre eux par des actions permettant de passer d'un état à un autre (state transition)

#### Définition

Transition: permet de passer d'un état à un autre

(Transition = arête d'un graphe...)

Actions discrètes: transitions dénombrables, états dénombrables

Peut avoir un coût

### Graphe d'Etats

On définit donc le graphe d'états à partir de la fonction de transition ($\Gamma: S \rightarrow S$):
- Les noeuds du graphe sont les états
- Les arêtes du graphe sont les transitions

Pas besoin de connaître tout le graphe pour pouvoir se déplacer... Exemple: robot sur Mars n'a pas besoin de connaître toute la topologie de Mars pour faire 1 m sur Mars...

#### Propriétés

Les propriétés d'un graphe d'états sont autant d'indicateurs sur la complexité du problème
- Degré, degré moyen
- Connexité

Le graphe d'état donne une formalisation pour la résolution de problèmes.

Une solution est un chemin de l'état initial à l'état final

L'existence de la solution est liée à la connexité du graphe

L'optimalité de la solution est liée à son coût

(Il n'y a pas forcément unicité de la solution optimale...)

Signature d'une permutation: (Égal à 1 s'il y a un nombre pair d'inversion, et égal à -1 s'il y a un nombre impair d'inversion...)

On représente le graphe par une matrice d'adjacence T et on a $T_{i,j}^k$ = nombre de chemins de longueur k entre i et j
avec $T_{i, j} = 0$ s'il n'existe pas de chemin de longueur 1 entre i et j et $T_{i, j} = 1$ s'il existe un chemin entre i et j.

On sait que $(Id - T)^{-1}$ nous liste les chemins entre chaque noeud du graphe

Problème: pas praticable car souvent le nombre d'états croît exponentiellement -> DFS et BFS


### Parcours du Graphe


Site: https://visualgo.net/en
