# Clément Vogt

from fis_cup_data import *

DISQUALIFICATION = -1
NON_PARTICIPATION = 0
PLACE_SI_DISQUALIFIEE = 40

def points(placement):
    if placement not in DIC_POINTS:
        return 0
    return DIC_POINTS[placement]

def points_podium():
    nb_points = 0
    for placement in range(1,4):
        nb_points += points(placement)
    return nb_points

def points_course():
    nb_points = 0
    for k in DIC_POINTS:
        nb_points += DIC_POINTS[k]
    return nb_points
    
def question1():
    print("=== Question 1 ===")
    print("Points pour le placement 99:",points(99))
    print("Points pour le placement 0:",points(0))
    print("Points pour le placement -1:",points(-1))
    print("Points pour le placement 4:",points(4))
    print("Total des points pour le podium:",points_podium())
    print("Total des points pour une course:",points_course())
 
 
def disqualifications_pour_une_course(num_course):
    nb_skieuses = TAB_PLACEMENTS.shape[0]
    nb_disca = 0
    for num_skieuse in range(nb_skieuses):
        if TAB_PLACEMENTS[num_skieuse,num_course] == DISQUALIFICATION:
            nb_disca += 1
    return nb_disca

def disqualifications():
    dic_disca_par_course = {}
    for num_course in range(len(LST_COURSES)):
        dic_disca_par_course[LST_COURSES[num_course]] = disqualifications_pour_une_course(num_course)
    return dic_disca_par_course
        
def question2():
    print("=== Question 2 ===")
    dic_disca_par_course = disqualifications()
    print("Nombre de disqualifications pour chaque course:")
    for k in dic_disca_par_course:
        print("Course",k,":",dic_disca_par_course[k])


def moyenne_placements(num_skieuse):
    nb_courses = TAB_PLACEMENTS.shape[1]
    somme_des_placements = 0
    nb_courses_avec_participation = 0
    for num_course in range(nb_courses):
        if TAB_PLACEMENTS[num_skieuse,num_course] != NON_PARTICIPATION:
            if TAB_PLACEMENTS[num_skieuse,num_course] != DISQUALIFICATION:
                somme_des_placements += TAB_PLACEMENTS[num_skieuse,num_course]
            else:
                somme_des_placements += PLACE_SI_DISQUALIFIEE
            nb_courses_avec_participation += 1
    if nb_courses_avec_participation > 0:
        return round(somme_des_placements / nb_courses_avec_participation,1)
    else:
        return 0
    
def afficher_moyenne_placements(nom_skieuse):
    print("Moyenne des placements de",nom_skieuse,"à la position",DIC_NOMS[nom_skieuse],":",moyenne_placements(DIC_NOMS[nom_skieuse]))
    
def question3():
    print("=== Question 3 ===")
    skieuses = ['Jessica Richer', 'Claire Martin', 'Julie Durand', 'Jessica Durand', 'Céline Martin']
    for skieuse in skieuses:
        afficher_moyenne_placements(skieuse)


def points_pour_une_skieuse(num_skieuse):
    nb_courses = TAB_PLACEMENTS.shape[1]
    nb_points = 0
    for num_course in range(nb_courses):
        nb_points += points(TAB_PLACEMENTS[num_skieuse,num_course])
    return nb_points  

def points_par_skieuse():
    nb_skieuses = TAB_PLACEMENTS.shape[0]
    dic_points_skieuses = {}
    for num_skieuse in range(nb_skieuses):
        dic_points_skieuses[num_skieuse] = points_pour_une_skieuse(num_skieuse)
    return dic_points_skieuses

def leader(dic_points_skieuses):
    num_leader = None
    for k in dic_points_skieuses:
        if num_leader is None or dic_points_skieuses[k] > dic_points_skieuses[num_leader]:
            num_leader = k
    return num_leader

def second(dic_points_skieuses,num_leader):
    num_second = None
    for k in dic_points_skieuses:
        if num_second is None or dic_points_skieuses[k] > dic_points_skieuses[num_second] and k != num_leader:
            num_second = k
    return num_second
        
def question4():
    print("=== Question 4 ===")
    dic_points_skieuses = points_par_skieuse()
    print("Total des points par skieuse:")
    print(dic_points_skieuses)
    num_leader = leader(dic_points_skieuses)
    print("Skieuse avec le plus de points: no.",num_leader)
    num_second = second(dic_points_skieuses,num_leader)
    print("Nombre de points qui la séparent de la deuxième place:",dic_points_skieuses[num_leader] - dic_points_skieuses[num_second])


def main():
    question1()
    question2()
    question3()
    question4()


if __name__ == '__main__':
    main()
