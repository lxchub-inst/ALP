""" 
Prénom : Loic
Nom : AGOSTA
Date : 08.09..2023

Version : 3.0
"""

# Importation des modules
import random
import numpy as np

# Définition des constantes
ALLU_DEPART_MAX = 16
ALLU_DEPART_MIN = 4

# Définition des fonctions


def démarrage_jeu():
    allu_depart = random.choice([ALLU_DEPART_MIN, ALLU_DEPART_MAX])
    print("Bienvenue sur le Jeu de Nim !")
    print("Le but du jeu est de prendre la dernière allumette.")
    print("Pour cela, vous devez prendre entre 1 et 3 allumettes à chaque tour.")
    print("Le joueur qui prend la dernière allumette a perdu.")
    print("Bonne chance !")
    print("\n")
    print(f"Le nombre d'allumettes de départ est {allu_depart}.")
    return allu_depart


def afficher_allumettes(allumettes):
    if allumettes == 0:
        print("Il n'y a plus d'allumettes !")
    else:
        print(f"Allumettes restantes : {'I ' * allumettes}")


def joueurs(allu_total, depart_joueurs, nom_joueurs):
    while allu_total != 0:
        if depart_joueurs == nom_joueurs[0]:
            all_joueur = 0
            while all_joueur < 1 or all_joueur > min(3, allu_total):
                all_joueur = int(input(f"Combien d'allumettes voulez-vous prendre (entre 1 et 3, au maximum {min(3, allu_total)}) ? : "))
                if all_joueur < 1 or all_joueur > min(3, allu_total):
                    print(f"Vous ne pouvez que prendre entre 1 et {min(3, allu_total)} allumettes.")
            allu_total -= all_joueur
            print(f"Vous avez retiré {all_joueur} allumettes")
        elif depart_joueurs == nom_joueurs[1]:
            allu_ordi = random.randint(1, min(3, allu_total))
            allu_total -= allu_ordi
            print(f"Ordinateur a pris {allu_ordi} allumettes")
        depart_joueurs = changer_joueurs(depart_joueurs, nom_joueurs)
        afficher_allumettes(allu_total)
    afficher_gagnant(depart_joueurs, nom_joueurs)


def afficher_gagnant(depart_joueurs, nom_joueurs):
    if depart_joueurs == nom_joueurs[0]:
        print("L'ordinateur a gagné !")
    else:
        print("Vous avez gagné !")

def jeu_nim():
    nom_joueurs = ["Joueur", "Ordinateur"]
    depart_joueurs = random.choice(nom_joueurs)
    allu_depart = démarrage_jeu()
    allu_total = allu_depart

    joueurs(allu_total, depart_joueurs, nom_joueurs)

def changer_joueurs(depart_joueurs, nom_joueurs):
    return nom_joueurs[1] if depart_joueurs == nom_joueurs[0] else nom_joueurs[0]

def main():
    jeu_nim()

if __name__ == '__main__':
    main()