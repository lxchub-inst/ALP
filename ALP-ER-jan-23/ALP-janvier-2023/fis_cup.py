from fis_cup_data import *


def points(placement):
    # Vérifier que la clé
    if placement in DIC_POINTS:
        return DIC_POINTS[placement]
    else:
        return 0


def points_podium():
    total_points = 0
    for placement in range(1, 4):
        total_points += points(placement)
    return total_points


def points_course():
    total_points = 0
    for placement in DIC_POINTS:
        total_points += points(placement)
    return total_points


def question1():
    print("=== Question 1 ===")
    print("Points pour le placement :", points(99))
    print("Points pour le placement :", points(0))
    print("Points pour le placement :", points(-1))
    print("Points pour le placement :", points(4))
    print("Total des points pour le podium :", points_podium())
    print("Total des points pour une course :", points_course())


def disqualification_par_course():
    # On affecte la colonne du tableau pour la première lecture
    nb_skieuse = TAB_PLACEMENTS.shape[0]

    # On crée une variable pour stocker les disqualifications
    nb_disqualification = 0

    # On créer une boucle sur l'index des skieuses
    for i in range(nb_skieuse):

        # On crée une vérification si la constante est présente dans le tableau
        if TAB_PLACEMENTS[nb_skieuse, i] == -1:
            nb_disqualification += 1
    return nb_disqualification


def disqualifications():
    resultat_disqualification = disqualification_par_course()
    for i in range()


def question2():
    print("=== Question 2 ===")
    disqualification_par_course()


def question3():
    print("=== Question 3 ===")
    # skieuses = ['Jessica Richer', 'Claire Martin', 'Julie Durand', 'Jessica Durand', 'Céline Martin']
    # for skieuse in skieuses:
    #     afficher_moyenne_placements(skieuse)


def question4():
    print("=== Question 4 ===")


def main():
    question1()
    question2()
    question3()
    question4()


if __name__ == '__main__':
    main()
