# Cours 3

## Algorithme générale de recherche

### Arbre de recherche

le graphe peut être représenté par sa matrice de transition ou par $\Gamma$

- Recherche aveugle: aucune informations connues

- Recherche heuristique: on a des informations qui peuvent nous guider...

### Résumé

Certains problèmes peuvent se formaliser sous forme de recherche de chemin dans un graphe d'état

- Notion d'état + action / transition = graphe d'état

- Chemin = solution



# Recherche aveugle

## Introduction

- On applique le principe de recherche de solution sans utiliser de connaissance a priori (C'est la recherche aveugle...)

- Essentiellement, cela revient à prendre la fonction de voisinage

- L'alternative est la recherche heuristique

Le graphe d’états donne une formalisation pour la résolution de problèmes

### BFS (Recherche en Largeur)

On explore toutes les stratégies à la fois...

#### Complexité

Nombre maximum (moyen) de successeurs d'un état: b

Profondeur de la solution dans l'arbre: d

Nombre de noeuds de l'arbre produit:

 $N = b^0 + b^1 + \dots + b^d = \frac{b^{d + 1}-1}{b - 1} = O(b^d)$

##### $\Rightarrow$ Complexité

- Temps: $O(b^d)$

- Espace: $O(b^d)$

#### Propriétés

- Complet: permet de trouver la solution

- Optimal: trouve la solution la plus simple

### DFS (Recherche en profondeur)

On explore chaque stratégie jusqu'au bout

#### Complexité

Nombre maximum (moyen)  de successeurs d'un état: b = facteur de branchement

Profondeur de la solution dans l'arbre: d

Profondeur maximum d'une feuille: m

##### $\Rightarrow$ Complexité

- Temps: $b^0 + b^1 + \dots + b^m = O(b^m)$ (m peut être >> d...)

- Espace: $O(b*m)$

#### Propriétés

- Complet si l'arbre est fini

- Non optimal (en général)

#### IDS (Iterative Depth Search) Recherche en profondeur limitée

Comme m est un facteur de complexité, on borne m par M

#### Propriétés

- Complet si $d \leq M$

- Pas de garantie d'optimalité (Peut-être qu'on aurait pu trouver la solution à l'étape $M + 1$ )

#### Complexité

- Temps: $O(b^M)$

- Espace: $O(b*M)$

### Approfondissement itératif IDS

On fait une recherche IDS et on incrémente à chaque fois m tant que $m \leq M$.

#### Propriété

Complet: car on explore éventuellement toutes les solutions

Optimal: car on trouve la solution la plus simple (profondeur d) avant les autres

#### Complexité

Temps: $(d + 1) b^0 + db^1 + \dots + b^d = O(b^d)$

Espace: $O(b*d)$

### Recherche bidirectionnelle

On développe des chemins à partir de start et de goal.... Puis on joint le chemin (on exploite le fait que $b^\frac{d}{2} << b^d$)

#### Propriété

Complet: car les recherches se rejoignent si une solution existe

Optimal: car on trouve la solution la plus simple à la jointure des chemins

#### Complexité

Temps: $O(b^\frac{d}{2})$

Espace: $O(b^\frac{d}{2})$

### Recherche en coût uniforme

Similaire à la recherche en largeur... Analogue au plus court chemin de Dijkstra

#### Propriétés

Complet: garantit de trouver la solution

Optimal: trouve la solution la moins coûteuse

#### Complexité

Temps: $O(b^d)$

Espace: $O(b^d)$

## Résumé

DFS -> IDS

BFS -> Dijkstra avec coût différent de 1