from fis_cup_data import *


def points(placement):
    if placement not in DIC_POINTS:
        return 0
    else:
        return DIC_POINTS[placement]


def points_podium():
    sum_points = 0
    for placement in range(1, 4):
        sum_points += points(placement)
    return sum_points


def points_course():
    total_points = 0
    for placement in DIC_POINTS:
        total_points += points(placement)
    return total_points


def question1():
    print("=== Question 1 ===")
    print("Points pour le placement 99:", points(99))
    print("Points pour le placement 0:", points(0))
    print("Points pour le placement -1:", points(-1))
    print("Points pour le placement 4:", points(4))
    print("Points pour le placement 50:", points(50))
    print("Total des points pour le podium :", points_podium())
    print("Total des points pour une course :", points_course())


def disqualification_par_course(nb_course):
    tab_skieuse = TAB_PLACEMENTS.shape[0]

    nb_disqualification = 0

    for ele_skieuse in range(tab_skieuse):
        if TAB_PLACEMENTS[ele_skieuse, nb_course] == -1:
            nb_disqualification += 1
    return nb_disqualification


def disqualifications():
    liste_course = {}
    for ele_course in range(len(LST_COURSES)):
        liste_course[LST_COURSES[ele_course]] = disqualification_par_course(ele_course)
    return liste_course


def question2():
    print("=== Question 2 ===")
    for ele_course in disqualifications():
        print("Course au nom de", ele_course, ":", disqualifications()[ele_course])


def moyenne_placements(nb_skieuse):

    tab_skieuse = TAB_PLACEMENTS.shape[1]
    tab_skieuses = TAB_PLACEMENTS

    somme_skieuse = 0
    nb_courses = 0

    for ele_skieuse in range(tab_skieuse):
        if tab_skieuses[nb_skieuse, ele_skieuse] != -1:
            if TAB_PLACEMENTS[nb_skieuse, ele_skieuse] != 0:
                somme_skieuse += tab_skieuses[nb_skieuse, ele_skieuse]
            else:
                somme_skieuse += 40
            nb_courses += 1

        if nb_courses > 0:
            return round(somme_skieuse / nb_courses, 1)
        else:
            return 0


def afficher_moyenne_placements(nb_skieuse):
    print("Moyenne des placements de", nb_skieuse, "à la position", DIC_NOMS[nb_skieuse], ":",
          moyenne_placements(DIC_NOMS[nb_skieuse]))


def question3():
    print("=== Question 3 ===")
    skieuses = ['Jessica Richer', 'Claire Martin', 'Julie Durand', 'Jessica Durand', 'Céline Martin']
    for skieuse in skieuses:
        afficher_moyenne_placements(skieuse)

def points_pour_une_skieuse(ele_skieuse):
    points_skieuse = 0

    for ele_course in range(TAB_PLACEMENTS.shape[1]):
        points_skieuse += points(TAB_PLACEMENTS[ele_skieuse, ele_course])
    return points_skieuse

def points_par_skieuse():
    liste_points = {}

    for ele_skieuse in range(TAB_PLACEMENTS.shape[0]):
        liste_points[ele_skieuse] = points_pour_une_skieuse(ele_skieuse)
    return liste_points

def leader(liste_points):
    num_leader = None

    for ele_skieuse in liste_points:
        if num_leader is None or liste_points[ele_skieuse] > liste_points[num_leader]:
            num_leader = ele_skieuse
    return num_leader

def second(liste_points, num_leader):
    num_second = None
    for ele_skieuse in liste_points:
        if num_second is None or liste_points[ele_skieuse] > liste_points[num_second] and ele_skieuse != num_leader:
            num_second = ele_skieuse
    return num_second
def question4():
    print("=== Question 4 ===")
    print("Total des points par skieuse:")
    print(points_par_skieuse())
    print("Skieuse avec le plus de points : no.", leader(points_par_skieuse()))
    print("Skieuse avec le deuxième plus de points : no.", points_pour_une_skieuse(leader(points_par_skieuse())) -
          points_pour_une_skieuse(second(points_par_skieuse(), leader(points_par_skieuse()))))


def main():
    question1()
    question2()
    question3()
    question4()


if __name__ == '__main__':
    main()
