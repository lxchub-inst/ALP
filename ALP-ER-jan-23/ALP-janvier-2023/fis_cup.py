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


def disqualification_par_course(nb_course):
    # On affecte la colonne du tableau pour la première lecture
    tab_skieuse = TAB_PLACEMENTS.shape[0]

    # On crée une variable pour stocker les disqualifications
    nb_disqualification = 0

    # On créer une boucle sur l'index des skieuses
    for ele_skieuse in range(tab_skieuse):

        # On crée une vérification si la constante est présente dans le tableau
        if TAB_PLACEMENTS[ele_skieuse, nb_course] == -1:
            nb_disqualification += 1
    return nb_disqualification


def disqualifications():
    # On crée une liste pour stocker les nouvelles valeurs
    liste_disqualification = {}

    """ 
    On crée une boucle sur la constante des liste des courses pour afficher les prénoms en fonction du tableau 
    qui a été défini avant
    """
    for ele_course in range(len(LST_COURSES)):
        liste_disqualification[LST_COURSES[ele_course]] = disqualification_par_course(ele_course)
    return liste_disqualification


def question2():
    print("=== Question 2 ===")

    # Pour chaque élément dans la fonction disqualifications
    for ele_course in disqualifications():

        # Afficahge du nom d'élément (ele_course), et la
        print("Course au nom de", ele_course, ":", disqualifications()[ele_course])


def moyenne_placements(nb_skieuse):

    # On crée une variable et on affecte le tableau dessus
    tab_skieuse = TAB_PLACEMENTS.shape[1]
    tab_skieuses = TAB_PLACEMENTS

    # On crée une variable pour stocker la somme des colonnes
    somme_skieuse = 0
    nb_courses = 0

    # On crée une boucle sur le tableau
    for ele_skieuse in range(tab_skieuse):

        # Une condition pour vérifier si chaque élément de la clonne n'est pas égale à 1
        if tab_skieuses[nb_skieuse, ele_skieuse] != -1:

            # Une condition pour vérifier si chaque élément de la clonne n'est pas égale à 0
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
    # On crée une variable pour stocker les points
    points_skieuse = 0

    # On crée une boucle sur le tableau
    for ele_course in range(TAB_PLACEMENTS.shape[1]):
        points_skieuse += points(TAB_PLACEMENTS[ele_skieuse, ele_course])
    return points_skieuse


def points_par_skieuse():
    liste_points = {}

    # On crée une boucle sur le tableau
    for ele_skieuse in range(TAB_PLACEMENTS.shape[0]):
        liste_points[ele_skieuse] = points_pour_une_skieuse(ele_skieuse)
    return liste_points


def leader(liste_points):
    # Cette variable sert à stocker le numéro de la skieuse
    num_leader = None

    # On crée une boucle sur le tableau
    for ele_skieuse in liste_points:

        # On crée une condition pour vérifier si la variable est vide ou si la valeur est supérieur à la variable
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
