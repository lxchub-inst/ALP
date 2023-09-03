""" 
Prénom : Loic
Nom : AGOSTA
Date : 29.08.2023
"""

import random
import numpy as np

ALLU_DEPART_16 = 16
ALLU_DEPART_4 = 4


def game_allumette():
    # On choisit un nombre d'allumettes au hasard entre 4 et 16
    allu_depart = random.choice([ALLU_DEPART_16, ALLU_DEPART_4])
    # On crée une liste avec les noms des joueurs
    nom_joueurs = ["Joueur 1", "Ordinateur 1"]
    depart_joueurs = random.choice(nom_joueurs)

    allu_total = allu_depart

    print(f"Le nombre d'allumettes au départ est de {allu_depart}")

    while allu_total > 0:

        def affichage_allumettes(allumettes):
            # Création d'un tableau avec autant de "I" que d'allumettes restantes
            tab_joueur = ["I" for i in range(allumettes)]

            if tab_joueur == []:
                print("Il n'y a plus d'allumettes !")
            else:
                # np.array() pour afficher le tableau en une ligne
                print(f"Allumettes restantes : {np.array(tab_joueur)}")

        if depart_joueurs == nom_joueurs[0]:
            allu_joueur1 = 0

            while allu_joueur1 < 1 or allu_joueur1 > min(3, allu_total):
                allu_joueur1 = int(
                    input("Joueur 1 : Combien d'allumettes voulez-vous prendre (entre 1 et 3) ? "))

                if allu_joueur1 < 1 or allu_joueur1 > min(3, allu_total):
                    print(
                        f"Vous ne pouvez prendre que 1, 2 ou 3 allumettes (maximum {min(3, allu_total)}) !")
                    """ 
                    Si le joueur entre un nombre d'allumettes incorrect, on lui affiche un message d'erreur et on lui redemande de saisir un nombre d'allumettes
                    """

            # On retire le nombre d'allumettes que le joueur a pris au nombre d'allumettes restantes
            allu_total -= allu_joueur1
            affichage_allumettes(allu_total)
            print(f"Joueur 1 : A pris {allu_joueur1} allumettes")

        elif depart_joueurs == nom_joueurs[1]:
            # L'ordinateur prend un nombre d'allumettes aléatoire entre 1 et 3 (ou le nombre d'allumettes restantes si il en reste moins de 3)
            allu_ordi = random.randint(1, min(3, allu_total))
            allu_total -= allu_ordi
            print(f"Ordinateur 1 : A pris {allu_ordi} allumettes")

        print(f"Il reste {allu_total} allumettes.")
        affichage_allumettes(allu_total)

        # On change de joueur, si c'était le joueur 1, c'est maintenant l'ordi et vice-versa
        depart_joueurs = nom_joueurs[1] if depart_joueurs == nom_joueurs[0] else nom_joueurs[0]

    if depart_joueurs == nom_joueurs[0]:
        print("Ordi 1 : A gagné !")
    else:
        print("Joueur 1 : A gagné !")


def main():
    game_allumette()


if __name__ == '__main__':
    main()
