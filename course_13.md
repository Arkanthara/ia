En ajoutant une dimension, on transforme une fonction affine en fonction linéaire -> permet de représenter les classifications sous forme de produit scalaire....


# Perceptron

Perceptron: indique qu'on peut encore diviser les données ????

Il faut que les classes soient équilibrées... La convergence demande à ce que les classes soient équilibrées

(idée: descente en gradient: trouver le minimum de la fonction pour minimiser l'erreur ...)

- choisir un pas d'apprentissage n
- initialiser les poids w aléatoirement
- répéter pour chaque donnée (augmentée avec $x^{0} = 1$)
    - $\phi_{\theta}(x_{i}) = w^ŧx_{i}$
    - mise à jour $ w \leftarrow w + n(y - \phi_{\theta}(x_{i}))x_{i}         (\Delta - rule)$ (Fait basculer l'hyper plan...
- jusqu'à convergence


# Fonction d'apprentissage:

$$\phi_{\theta}(x_{i}) = ((\sum_{k = 0}^{K} w_{k}x^{k}) \gt 0)$$

C'est la structure d'un neurone qui s'active si un certain seuil de l'activationn est dépassé (a > 0)

Hessien -> courbure de la fonction...

ADAM (algorithme)


La fonction de perte est la somme pour toutes les données d'apprentissage de la distance entre la donnée réel et la prédiction (erreur cumulée)


Maintenant, on ne va plus se concentrer sur chaque points, mais sur la fonction de perte... On est intéressé par le résultat global et on regarde l'impact de chaque paramètre sur le résultat global (en utilisant des dérivées partielles...)
