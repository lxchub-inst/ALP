#ER ALP 31-10-2022
################### NOM ET PRENOM ici !
###################

from math import ceil

#constantes ici si vous en ajoutez



#Constantes fournies -- NE PAS MODIFIER !!
DIST_TOT_TREK = 200

KIRK = [29, 26, 30, 29, 28, 30, 28]
PICARD = [29, 33, 27, 29, 37, 30]
SULU = [21, 22, 16, 18, 28, 0]

#Fonctions fournies -- NE PAS MODIFIER !!
def arrondi_dixieme(x):#arrondi un nombre au dixième
    return round(x, 1)

def arrondi_superieur(x):
    return ceil(x)

##############################################
#Votre code ici

def nb_jours(parcours):
    total = 0
    for i in range(len(parcours)):
        if parcours[i] != 0:
            total += 1
    return total
def distance_parcouru(parcours):
    somme = 0
    """ On créer une boucle sur la liste parcours et on ajoute chaque élément à la variable somme. """
    for i in range(len(parcours)):
        somme += parcours[i]
    return somme

def tjrs_en_course(parcours):
    for i in range(len(parcours)):
        if parcours[i] == 0:
            en_course = False
        else:
            en_course = True
    return en_course

def vitesse_moyenne(parcours):
    resultat = distance_parcouru(parcours) / nb_jours(parcours)
    return resultat
def vitesse_moyenne_v2(parcours):
    somme = 0
    nb_jours = 0
    for i in range(len(parcours)):
        somme += parcours[i]
        if parcours[i] != 0:
            nb_jours += 1
    moyenne = somme / nb_jours
    return moyenne

def distance_restantes(parcours):
    return DIST_TOT_TREK - distance_parcouru(parcours)

def mi_parcours(parcours):
    moitie_parcours = distance_parcouru(parcours) / 2
    somme = 0
    for i in range(len(parcours)):
        somme += parcours[i]
        if somme >= moitie_parcours:
            return i

def meilleur_performance(parcours):
    meilleur = 0
    for i in range(len(parcours)):
        if parcours[i] > meilleur:
            meilleur = parcours[i]
    return meilleur

def evolution_moyenne(parcours):
    somme = 0
    jours = 0
    moyenne = 0

    for i in range(len(parcours)):
        if parcours[i] != 0:
            somme += parcours[i]
            jours += 1
        moyenne = somme / jours
        print("au jour", jours, "la moyenne est de", arrondi_dixieme(moyenne))

def jours_restants(parcours):
    jours_restants = distance_restantes(parcours) / vitesse_moyenne(parcours)
    return arrondi_superieur(jours_restants)

#procédure recap à compléter
def recap(parcours, nom): 
    print("Parcours de", nom)
    if distance_parcouru(parcours) == DIST_TOT_TREK:
        print(nom, "atteint l'objectif en", nb_jours(parcours), "jours")
        print(nom, "a réalisé la moitié de la distance en ", mi_parcours(parcours), "jours")
    elif distance_parcouru(parcours) < DIST_TOT_TREK:
        print(nom, "est toujours en course après ", distance_parcouru(parcours), "km")
        if distance_parcouru(parcours) > nb_jours(parcours):
            print("Il reste", distance_restantes(parcours), "km qui devrait être parcouru en", jours_restants(parcours), "jours s'il maintient sa moyenne qui est de ", arrondi_dixieme(vitesse_moyenne(parcours)), "km/jour")
        else:
            print(nom, " abandonné au bout de ", distance_parcouru(parcours), "km et ", nb_jours(parcours), "jours")

#precédure depassement à compléter
def depassement(parcours1, parcours2, nom1, nom2):
    '''A CODER'''
    pass 



#Procedure main fournie -- NE PAS MODIFIER !!
def main():
    # print(distance_parcouru(KIRK))
    # print(vitesse_moyenne(KIRK))
    # print(vitesse_moyenne_v2(KIRK))
    # print(distance_restantes(KIRK))
    # print(mi_parcours(KIRK))
    # print(meilleur_performance(KIRK))
    # evolution_moyenne(KIRK)
    # print(jours_restants(SULU))

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
    
#Appel de main -- NE PAS MODIFIER !!
if __name__ == '__main__':
    main()

