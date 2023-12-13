import numpy as np

# Création d'un tableau de Pythagore
# 1. Créer un tableau de 10 lignes et 10 colonnes


def affiche_pythagore(tableau):
    for lignes in range(13):
        for colonnes in range(13):
            # on affiche les lignes et colonnes
            print(tableau[lignes][colonnes], end=" ")
    return tableau


def creer_tableau(nb_lignes, nb_colonnes):
    tableau = np.empty((nb_lignes, nb_colonnes), int)
    for lignes in range(nb_lignes):
        for colonnes in range(nb_colonnes):
            tableau[lignes, colonnes] = lignes * colonnes
    return tableau


def main():
    nb_lignes = int(input("Entrez le nombre de lignes : "))
    nb_colonnes = int(input("Entrez le nombre de colonnes : "))
    print(creer_tableau(nb_lignes, nb_colonnes))



main()
