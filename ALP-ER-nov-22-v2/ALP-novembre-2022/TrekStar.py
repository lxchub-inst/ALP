# ER ALP 31-10-2022
################### NOM ET PRENOM ici !
###################

from math import ceil

# constantes ici si vous en ajoutez
CODE_ABANDON = 0

# Constantes fournies -- NE PAS MODIFIER !!
DIST_TOT_TREK = 200

KIRK = [29, 26, 30, 29, 28, 30, 28]
PICARD = [29, 33, 27, 29, 37, 30]
SULU = [21, 22, 16, 18, 28, 0]


# Functions fournies -- NE PAS MODIFIER !!
def arrondi_dixieme(x):  # arrondi un nombre au dixième
    return round(x, 1)


def arrondi_superieur(x):
    return ceil(x)


##############################################
# Votre code ici
def distance_parcourus(parcours):
    somme_parcours = 0
    for ele_parcours in range(len(parcours)):
        somme_parcours += parcours[ele_parcours]
    return somme_parcours


def toujours_en_course(parcours):
    somme_parcours = distance_parcourus(parcours)
    for ele_parcours in range(len(parcours)):
        if somme_parcours < DIST_TOT_TREK and parcours[ele_parcours - 1] != 0:
            return True
        else:
            return False


def parcours_jours(parcours):
    nb_jours = 0
    for i in range(len(parcours)):
        if parcours[i] != 0:
            nb_jours += 1
    return nb_jours


def vitesse_moyenne(parcours):
    nb_jours = 0
    moyenne = 0
    for ele_parcours in range(parcours_jours(parcours)):
        somme_parcours = distance_parcourus(parcours)
        nb_jours += 1
        moyenne = somme_parcours / nb_jours
    return arrondi_dixieme(moyenne)


def distance_restante(parcours):
    return DIST_TOT_TREK - distance_parcourus(parcours)


def mi_parcours(parcours):
    moitie_parcours = DIST_TOT_TREK / 2
    nb_jours = 0
    for ele_parcours in range(len(parcours)):
        if distance_parcourus(parcours) > moitie_parcours or distance_parcourus(parcours) == DIST_TOT_TREK:
            nb_jours += 1
    return nb_jours


def meilleur_performance(parcours):
    max_jours = 0
    for ele_parcours in range(len(parcours)):
        if parcours[ele_parcours] > parcours[max_jours]:
            max_jours = ele_parcours
    return max_jours


def evolution_moyenne(parcours):
    print("Voici l'évolution de sa moyenne au jour le jour (km/jours) :")
    nb_ele_parcours = 0
    for ele_parcours in range(parcours_jours(parcours)):
        nb_ele_parcours += parcours[ele_parcours]
        print("au jour", ele_parcours, ":", arrondi_dixieme(nb_ele_parcours / (ele_parcours + 1)))


def jours_restants_parcours(parcours):
    return arrondi_superieur(distance_restante(parcours) / vitesse_moyenne(parcours))


# procédure recap à compléter
def recap(parcours, nom):
    print("Parcours de", nom)
    """A CODER"""
    if distance_parcourus(parcours) == DIST_TOT_TREK:
        print(nom, "a atteint l'objectif en", parcours_jours(parcours), "jours")
        print(nom, "a réalisé la moitié de la distance en", mi_parcours(parcours), "jours")
    else:
        if toujours_en_course(parcours):
            print(nom, "est toujours en course après", distance_parcourus(parcours), "km")
            print("Il reste", distance_restante(parcours), "km qui devraient être parcours en",
                  jours_restants_parcours(parcours), "jour(s) s'il maintient sa moyenne qui est de",
                  vitesse_moyenne(parcours), "km par jour")
        else:
            print(nom, "a abandonné au bout de", distance_parcourus(parcours), "km et", parcours_jours(parcours))
    if not toujours_en_course(parcours):
        print("Ce qui représente une moyenne globale de", vitesse_moyenne(parcours), "km par jour")
    evolution_moyenne(parcours)
    if toujours_en_course(parcours):
        print("Jusqu'à maintenantnt", end=" ")
    else:
        print("Au final", end=" ")
    print("sa meilleur performance est de", parcours[meilleur_performance(parcours)],
          "km réalisé le jour n°", meilleur_performance(parcours))


def jour_depassement(parcours1, parcours2):
    nb_parcours1 = parcours_jours(parcours1)
    nb_parcours2 = parcours_jours(parcours2)
    nb_jours = 0
    if nb_parcours1 < nb_parcours2:
        nb_jours += nb_parcours1
    else:
        nb_jours += nb_parcours2
    return nb_jours


# procédure depassement à compléter
def depassement(parcours1, parcours2, nom1, nom2):
    """A CODER"""
    print("Comparaison entre", nom1, "et", nom2)
    num_jours = 0
    nb_jours = jour_depassement(parcours1, parcours2)
    somme_parcours1 = 0
    somme_parcours2 = 0

    while num_jours < nb_jours and somme_parcours1 <= somme_parcours2:
        somme_parcours1 += parcours1[num_jours]
        somme_parcours2 += parcours2[num_jours]
        num_jours += 1
    if num_jours < nb_jours:
        print(nom1, "a dépassé pour la 1ère fois", nom2, "au jour n°", num_jours - 1)
    else:
        print(nom1, "n'a jamais dépassé", nom2)


# Procedure main fournie -- NE PAS MODIFIER !!
def main():
    recap(KIRK, "Kirk")
    print("--------------------------------------------")
    recap(PICARD, "Picard")
    print("--------------------------------------------")
    recap(SULU, "Sulu")
    print("--------------------------------------------")
    print("--------------------------------------------")
    depassement(PICARD, KIRK, "Picard", "Kirk")
    print("--------------------------------------------")
    depassement(SULU, KIRK, "Sulu", "Kirk")


# Appel de main -- NE PAS MODIFIER !!
if __name__ == '__main__':
    main()
