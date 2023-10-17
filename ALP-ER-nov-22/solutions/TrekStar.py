# ER ALP 31-10-2022
# Clément Vogt
###################

from math import ceil

# constantes ici si vous en ajoutez
CODE_ABANDON = 0

# Constantes fournies -- NE PAS MODIFIER !!
DIST_TOT_TREK = 200

KIRK = [29, 26, 30, 29, 28, 30, 28]
PICARD = [29, 33, 27, 29, 37, 30]
SULU = [21, 22, 16, 18, 28, 0]


# Fonctions fournies -- NE PAS MODIFIER !!
def arrondi_dixieme(x):  # arrondi un nombre au dixième
    return round(x, 1)


def arrondi_superieur(x):
    return ceil(x)


##############################################
# Votre code ici

def nombre_de_jours(parcours):
    nb_jours = len(parcours)
    if parcours[-1] == CODE_ABANDON:
        nb_jours -= 1
    return nb_jours


def distance_parcourue(parcours):
    somme = 0
    for num_jour in range(nombre_de_jours(parcours)):
        somme += parcours[num_jour]
    return somme


def est_toujours_en_course(parcours):
    return parcours[-1] != CODE_ABANDON and distance_parcourue(parcours) < DIST_TOT_TREK


def vitesse_moyenne_globale(parcours):
    return arrondi_dixieme(distance_parcourue(parcours) / nombre_de_jours(parcours))


def distance_restante(distance_parcourue):
    return DIST_TOT_TREK - distance_parcourue


def mi_parcours(parcours):
    somme = 0
    num_jour = 0
    while somme < DIST_TOT_TREK / 2:
        somme += parcours[num_jour]
        num_jour += 1
    return num_jour


def jour_de_la_meilleur_performance(parcours):
    num_meilleur_jour = 0
    for num_jour in range(1, nombre_de_jours(parcours)):
        if parcours[num_jour] > parcours[num_meilleur_jour]:
            num_meilleur_jour = num_jour
    return num_meilleur_jour


def afficher_evolution_moyenne(parcours):
    print("Voici l'évolution de sa moyenne au jour le jour (km/jour) :")
    somme = 0
    for num_jour in range(nombre_de_jours(parcours)):
        somme += parcours[num_jour]
        print("au jour", num_jour, ":", arrondi_dixieme(somme / (num_jour + 1)))


def nombre_de_jours_restants(parcours):
    return arrondi_superieur(distance_restante(distance_parcourue(parcours)) / vitesse_moyenne_globale(parcours))


def plus_petit_nombre_de_jours(parcours1, parcours2):
    nb_jours_1 = nombre_de_jours(parcours1)
    nb_jours_2 = nombre_de_jours(parcours2)
    if nb_jours_1 < nb_jours_2:
        nb_jours = nb_jours_1
    else:
        nb_jours = nb_jours_2
    return nb_jours


# procédure recap à compléter
def recap(parcours, nom):
    print("Parcours de", nom)
    d_parcourue = distance_parcourue(parcours)
    nb_jours = nombre_de_jours(parcours)
    v_moyenne = vitesse_moyenne_globale(parcours)
    est_en_course = est_toujours_en_course(parcours)
    if d_parcourue == DIST_TOT_TREK:
        print(nom, "a atteint l'objectif en", nb_jours, "jours")
        print(nom, "a réalisé la moitié de la distance en", mi_parcours(parcours), "jours")
    else:
        if est_en_course:
            print(nom, "est toujours en course après", d_parcourue, "km")
            print("Il reste", distance_restante(d_parcourue), "km qui devraient être parcourus en",
                  nombre_de_jours_restants(parcours), "jour(s) s'il maintient sa moyenne qui est de", v_moyenne,
                  "km par jour")
        else:
            print(nom, "a abandonné au bout de", distance_parcourue(parcours), "km et", nb_jours, "jours")
    if not est_en_course:
        print("Ce qui représente une moyenne globale de", v_moyenne, "km par jour")
    afficher_evolution_moyenne(parcours)
    if est_en_course:
        print("Jusqu'à maintenant", end=" ")
    else:
        print("Au final", end=" ")
    num_meilleur_jour = jour_de_la_meilleur_performance(parcours)
    print("sa meilleure performance est de", parcours[num_meilleur_jour], "km réalisée le jour n°", num_meilleur_jour)


# precédure depassement à compléter
def depassement(parcours1, parcours2, nom1, nom2):
    print("Comparaison entre", nom1, "et", nom2)
    nb_jours = plus_petit_nombre_de_jours(parcours1, parcours2)
    num_jour = 0
    somme_1 = 0
    somme_2 = 0
    while num_jour < nb_jours and somme_1 <= somme_2:
        somme_1 += parcours1[num_jour]
        somme_2 += parcours2[num_jour]
        num_jour += 1
    if num_jour < nb_jours:
        print(nom1, "a dépassé pour la 1ère fois", nom2, "au jour n°", num_jour - 1)
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
