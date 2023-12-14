

Problème: les points les plus éloignés influent sur la décision....


Fonction logistique: prend un input et le met dans un intervale 0 1.

Ce qui est intéressant est de savoir de combien la fonction de perte change en fonction des poids ou des labels

Il n'y a pas de paramètres dans la fonction logistique elle même...


perceptron: batch de 1 (-> oscille)
neurone: plus grand batch (-> n'oscille pas...)
1 neuronne -> fonction linéaire ne marchant que si les données sont séparables...

On a besoin de couches cachées pour rendre le problème non linéaire (sinon, 1 neurone va simplement résoudre linéairement le problème...)

-> dernière couche fait une classification linéaire
mais tous les neuronnes avant vont transformer l'espace des caractéristiques pour que celles ci deviennent séparables...

tenseur: fonction multi-linéaire....

graphe computationnel: but: calculer la dérivée d'une fonction...

1 écrire fonction sous forme d'un graphe computationnel

différentiation automatique

créer une nouvelle algèbre avec des fonctions et leurs dérivées...
