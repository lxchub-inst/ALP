# Épreuve du 21.09.2022
# Exercice 1 – Sapin de Noël
# Nom et prénom: Vogt Clément


# Imports
from turtle import *

# Procédures et fonctions
def donnees_entrees():
    nb_fleches = int(input("Entrez un nombre de flèches"))
    longueur = int(input("Entrez une longueur pour les segments"))
    angle = int(input("Entrez un angle"))
    couleur = input("Entrez une couleur")
    return nb_fleches, longueur, angle, couleur

def fleche(longueur, angle):
    forward(longueur)
    left(180-angle)
    forward(longueur)
    back(longueur)
    left(angle*2)
    forward(longueur)
    back(longueur)
    left(180-angle)
    back(longueur)
    
def sapin(nb_fleches, longueur, angle, couleur):
    for i in range(1,nb_fleches+1):
        if i%3==0:
            color(couleur)
        else:
            color("green")
        fleche(longueur, angle)
        forward(longueur)

# Procédure main()
def main():
    hideturtle() # pour ne pas voir la tortue
    nb_fleches, longueur, angle, couleur = donnees_entrees()
    left(90)
    sapin(nb_fleches, longueur, angle, couleur)

# Appel de la procédure main()
if __name__ == "__main__":
    main()