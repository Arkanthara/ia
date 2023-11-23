Paramètres optimisés par rapport aux données d'entrainement

Garder des données en réserve pour les tests

-> erreur d'entrainement
-> erreur de test -> Ce sont les plus importantes ! Elles déterminent la qualité de l'apprentissage du modèle ! On fait une estimation de l'erreur de prédiction sur des données inconnues
(On peut faire la moyenne de l'erreur entre la prédiction et la valeur réelle obtenue...

Il faut choisir un nombre de données de test tel que la moyenne des erreurs de test ait une valeur statistiquement significative...

Hyper-paramètres: c'est la structure de notre modèle

Holdout -> divise données en données d'entrainement et données de tests...
Ensuite, on refait un holdout sur les données d'entrainement pour séparer ces données en données d'entrainement et données de validation d'hyper paramètres pour avoir la meilleure architecture possible...

On va mettre ensuite une variance sur notre erreur d'entrainement...

Un des principes: parcimonie des modèles (simplicité): privilégier la simplicité... Si 2 modèles donnent les mêmes erreurs d'entrainement, il faut privilégier le plus simple... min = erreur d'entrainement + nombre de paramètres

Chaque paramètre va consommer un nombre de données pour se calibrer. Plus on a de paramètres, plus on a besoin de données... Donc moins on a de paramètre, plus ils sont bien ajustés...

Attention ! Il faut considérer que les données sont bruitées -> un modèle trop flexible risque d'apprendre le bruit de ces données...

Attention ! Cela entraine un problème de sur-apprentissage ! (C'est un peu comme si la machine apprenait tout par coeur, mais ne fait pas de généralisation... Ex: étudiant apprend par coeur mais n'a pas compris des équations -> si l'étudiant tombe sur une nouvelle équation, il ne saura pas quoi répondre...)

-> Plus on est collé aux données d'entrainement, moins on arrive à généraliser...

On me révelle la valeur de ma vraie fonction pour une valeur ponctuelle -> généraliser -> si on a un x_j près de x_i, alors phi de x_j ne sera pas trop loin de phi de x_i

La fonction phi est une fonction lipschitzienne... $||x_i - x_j|| \leq C || \Phi(x_i) - \Phi(x_j) ||$

La propagation de l'information d'un point est gaussienne... $P(|\Phi(x_i) - \Phi(x_j)|) = N(\Phi(x_i), \sigma)$ = \frac{1}{z} e^{\frac{||\Phi(x_j) - \Phi(x_i)||^{2}}{2 \sigma ^{2}}$


L'apprentissage se base sur les données pour estimer la réalité comme une fonction (dont on estime les paramètres

Le choix de représentation des données est important pour les performances

Le protocole d'apprentissage inclut:
- un objectif, un modèle, des données labélisées et une mesure d'évaluation

Les données sont la vue partielle du monde auquel le modèle a accès (en plus de ses propres hypothèses)


# Arbre de décision

L'idée de l'arbre de décision est de partitionner les données d'une certaine façon et d'enregistrer le partitionnement.... Le but est d'optimiser les partitions...

On partitionne les données en deux et ainsi de suite pour trouver un bon partitionnement des données

On peut ensuite labéliser les partitions.... (Mettre oui ou non dans les partitions)

Quel est l'arbre optimal que je peux construire ?
Comment construit-on l'arbre ???

Construire un arbre = construire des expressions logiques (décisions)"

Défi: réduire la longueur de l'arbre...

Construction de l'arbre: on va créer des partitions qui minimisent l'entropie

On va s'imposer des coupures (tester toutes les coupures possibles est difficile...): on met des seuils sur les caractéristiques et on essaye ainsi à trouver des partitions -> arbre de plus grande profondeur
