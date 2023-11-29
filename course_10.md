élagage: simplifier l'arbre et limiter sa profondeur -> évite surapprentissage... Compromis entre performance et complexité

Si on arrive à avoir un arbre avec profondeur maximale, alors l'erreur d'entrainement est de 0.

Si les données de tests sont cohérentes avec l'entrainement, on aura une erreur de test nulle également.

Par contre, on a une complexité élevée et un risque de surapprentissage -> simplifier l'arbre...



Régression plus dure que classification...

Indice Gini: approximation de l'entropie...

Partitionner en seuil le nombre de données fini pour trouver la partition .... On peut dire que l'on veut une tolérance de tant pour la variance de la partition créée par le seuil...


Index gini:
probabilité d'une classe fois la probabilité de ne pas être dans cette classe....

Du fait d'avoir la moyenne, on lisse 


Random forest: la construction d'un arbre est biaisé vers les données d'entrainement -> construction de plusieurs arbres et on fait la moyenne des résultats....

-> on peut filtrer des caractéristiques...

-> chaque arbre fait sa prédiction et ensuite on prend le résultat de ces prédictions...



