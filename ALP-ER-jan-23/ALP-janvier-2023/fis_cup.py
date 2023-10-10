from fis_cup_data import *

"""La fonction du if permet de vérifier si le placement est dans le dictionnaire, 
   en passant en crochet le paramètre [placement] """


def points(placement):
    if placement not in DIC_POINTS:
        return 0
    return DIC_POINTS[placement]


"""La fonction permet de retourner une valeur qui affiche la somme d'une certaine rangé par rapport à un
dictionnaire de valeurs."""


def points_podium():
    nb_points = 0
    for placement in range(1, 4):
        nb_points += points(placement)
    return nb_points


"""La fonction permet d'afficher la valeur totale d'un dictionnaire de valeurs."""


def points_course():
    nb_points = 0
    for placement in DIC_POINTS:
        nb_points += DIC_POINTS[placement]
    return nb_points


def question1():
    print("=== Question 1 ===")
    print("Points pour le placement 99:", points(99))
    print("Points pour le placement 0:", points(0))
    print("Points pour le placement -1:", points(-1))
    print("Points pour le placement 4:", points(4))
    print("Total des points pour le podium:", points_podium())
    print("Total des points pour une course:", points_course())


def disqualifications_pour_une_course(num_course):
    nb_skieuses = TAB_PLACEMENTS.shape[0]
    nb_disca = 0
    for num_skieuse in range(nb_skieuses):
        if TAB_PLACEMENTS[num_skieuse, num_course] == "DISQUALIFICATION":
            nb_disca += 1
    return nb_disca


def question2():
    print("=== Question 2 ===")
    print("Nombre de disqualifications pour chaque course:")
    for k in LST_COURSES:
        print("Course", k, ":", disqualifications_pour_une_course(k))


def question3():
    print("=== Question 3 ===")
    # skieuses = ['Jessica Richer', 'Claire Martin', 'Julie Durand', 'Jessica Durand', 'Céline Martin']
    # for skieuse in skieuses:
    #    afficher_moyenne_placements(skieuse)


def question4():
    print("=== Question 4 ===")


def main():
    question1()
    question2()
    question3()
    question4()


if __name__ == '__main__':
    main()
