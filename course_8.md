


# Apprentissage vs recherche

recherche:
énumérations organisées pour chercher une solution
On injecte de la connaissance par la modélisation des états et en utilisant des heuristiques
-> exploration de l'univers d'état.


apprentissage:
On collecte des données
-> échantillonnage de l'univers
-> On essaye d'inférer (généraliser) de la connaissance à partir d'exemples
On injecte de la connaissance en utilisant des modèles qui ont potentiellement généré les données


On commence par modéliser le contexte par des caractéristiques supposées être pertinentes (pour le problème)

Puis on regarde la pertinence de chaque caractéristiques: la corrélation avec l'objectif en question et le contenu d'information

# Apprentissage

On part de données et on cherche:
- une association que l'on connait
    -> apprentissage supervisé: on connait la décision associée à certains exemples de nos données
    -> méthodes: classification (label discret) (exemple: chien ou chat), régression (label continu) (exemple: donner un prix en fonction du nombre de pièces, d'étages, etc...), ...
- une structure que l'on veut découvrir
    -> apprentissage non-supervisée: on cherche des structures dans les données qui nous permettront de mieux les comprendre
    -> méthodes: clustering (chercher des groupes homogènes de données) (différence avec classification: on ne donne pas d'exemple...), embedding (on recherche des représentations pertinentes pour les données....), ...


Nous on va se concentrer sur l'apprentissage supervisé

### Classification

On connaît les classes (décisions, labels) pour certaines données... On s'en sert pour apprendre une fonction qui attribuera des classes aux données non classifiées (prédiction)

### Régression

C'est la même chose que la classification, mais les classes sont continues...

On peut montrer que si on a une classificationn binaire, on peut estimer les labels par une régression...


On va faire de l'apprentissage transductif plutôt que de l'apprentissage inductif: il faut se concentrer sur le problème là où il est et ne pas essayer de résoudre un problème plus général.
On ne comprend pas trop ce qui se passe, mais on a l'output désiré...

deep learning: c'est une technique
donc deep learning => machine learning, mais pas machine learning => deep learning

On choisit un modèle de fonction d'apprentissage avec des paramètres $\theta$ et on cherche les paramètres optimaux grâce aux données X données pour entraîner le modèle... On veut minimiser l'erreur...

Il faut:

définir un objectif (quels sont les classes ? Qu'est ce qu'on veut prédire ?)

on fixe un modèle d'apprentissages (réseaux de neuronnes, etc... quel est sa complexité ? sa capacité ? ai-je assez de données pour entraîner le modèle ?) (Il ne faut pas utiliser la masse pour écraser le moustique !!)

On rassemble les données (quel est leur représentation ? quel est le volume, la diversité de données ?)

On fixe une mesure d'évaluation (quelle est la qualité de mon apprentissage ? ...)

La plupart du temps, on a des labels qui sont déterministes (un expert (cela peut être une machine) a décidé que tel objet appartient à tel cathégorie...)

On doit être capable de quantifier la qualité de l'apprentissage
-> on définit des mesures d'évaluation

Système non informatif: fait autant d'erreurs que de bons résultats

Système informatif: fait plus de bons résultats que d'erreurs, mais si le modèle fait plus d'erreurs que de bons résultats, il suffit de 'renverser' le problème

!!!!!!! Il faut vraiment différencier l'entrainement du test. On va vouloir estimer la meilleure prédiction sur l'ensemble d'entrainement

L'erreur d'entrainement donne des informations sur la flexibilité du modèle, mais pas sur la qualité des résultats obtenus dans la réalité

Holdout: on prend des données de test, on les met de côté et on y touche plus... Comme cela, lorsqu'on a fini d'entrainer notre modèle, on va pouvoir le tester sur les données mises de côté

Erreur entrainement: optimisation correcte ou pas
erreur test: information sur la qualité de l'apprentissage...
