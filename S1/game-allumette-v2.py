import random
import numpy as np

ALLU_DEPART_16 = 16
ALLU_DEPART_4 = 4


def game_allumette():
    allu_depart = random.choice([ALLU_DEPART_16, ALLU_DEPART_4])
    nom_joueurs = ["Joueur 1", "Ordinateur 1"]
    depart_joueurs = random.choice(nom_joueurs)

    allu_total = allu_depart

    print(f"Le nombre d'allumettes au départ est de {allu_depart}")

    while allu_total > 0:

        def affichage_allumettes(allumettes):
            tab_joueur = []  # On initialise une liste pour stocker les allumettes

            for i in range(allumettes):
                # On ajoute un "I" à chaque tour de boucle
                tab_joueur.append("I")
            # On affiche le tableau d'allumettes séparées par un espace
            if tab_joueur == []:
                print("Il n'y a plus d'allumettes !")
            else:
                print(f"Allumettes restantes : {np.array(tab_joueur)}")

        if depart_joueurs == nom_joueurs[0]:

            # On initialise la variable à 0 pour entrer dans la boucle
            allu_joueur1 = 0

            # On vérifie que le nombre d'allumettes prises est bien entre 1 et 3
            while allu_joueur1 < 1 or allu_joueur1 > 3:
                allu_joueur1 = int(
                    input("Joueur 1 : Combien d'allumettes voulez-vous prendre (entre 1 et 3) ? "))
                if allu_joueur1 < 1 or allu_joueur1 > 3:
                    print("Vous ne pouvez prendre que 1, 2 ou 3 allumettes !")

                if allu_joueur1 > allu_total:
                    print(
                        f"Vous ne pouvez pas prendre plus que ce qu'il reste ({allu_total} allumettes) !")
            allu_total -= allu_joueur1

            # On actualise la liste d'allumettes pour le joueur suivant
            affichage_allumettes(allu_total)

            print(f"Joueur 1 : A pris {allu_joueur1} allumettes")

        elif depart_joueurs == nom_joueurs[1]:
            """
            Éviter de prendre plus que ce qu'il reste
            On initialise la variable pour entrer dans la boucle
            """
            allu_ordi = random.randint(1, min(3, allu_total))
            allu_total -= allu_ordi
            print(f"Ordinateur 1 : A pris {allu_ordi} allumettes")

        # On affiche le nombre d'allumettes restantes pour les deux joueurs
        print(f"Il reste {allu_total} allumettes.")

        # On actualise la liste d'allumettes pour le joueur suivant
        affichage_allumettes(allu_total)

        # Changer de joueur
        depart_joueurs = nom_joueurs[1] if depart_joueurs == nom_joueurs[0] else nom_joueurs[0]

    if depart_joueurs == nom_joueurs[0]:
        print("Ordi 1 : A gagné !")
    else:
        print("Joueur 1 : A gagné !")


def main():
    game_allumette()


if __name__ == '__main__':
    main()
