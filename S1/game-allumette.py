import turtle as np
import random

ALLU_DEPART_16 = 16
ALLU_DEPART_4 = 4


def game_allumette():
    allu_depart = random.choice([ALLU_DEPART_16, ALLU_DEPART_4])
    nom_joueurs = ["Joueur 1", "Ordinateur 1"]  # Liste des joueurs
    depart_joueurs = random.choice(nom_joueurs)  # Choisir un joueur au hasard

    allu_joueur1 = 0
    allu_ordi = 0

    print(f"Le nombre d'allumettes au départ est de {allu_depart}")

    while (allu_depart != 0):
        if depart_joueurs == nom_joueurs[0]:
            allu_joueur1 = int(
                input("Joueur 1 : Combien d'allumettes voulez-vous prendre ? "))
            allu_depart = allu_depart - allu_joueur1
            print(allu_depart)
            if allu_joueur1 > 3:
                print("Vous ne pouvez pas prendre plus de 3 allumettes !")
            print(f"Joueur 1 : A pris {allu_joueur1} allumettes")
        elif depart_joueurs == nom_joueurs[1]:
            allu_ordi = random.randint(1, 3000)
            print(f"Ordinateur 1 : A pris {allu_ordi} allumettes")
            allu_depart = allu_depart - allu_ordi
            allu_joueur1 = int(
                input("Joueur 1 : Combien d'allumettes voulez-vous prendre ? "))
            allu_depart = allu_depart - allu_joueur1
            if allu_joueur1 > 3:
                print("Vous ne pouvez pas prendre plus de 3 allumettes !")
            print(f"Joueur 1 : A pris {allu_joueur1} allumettes")
        allu_total = allu_depart
        if allu_total < 4:
            print("Ordi 1 : A gagné !")
        else:
            print("Ordi 1 : A perdu !")


def main():
    game_allumette()


if __name__ == '__main__':
    main()
