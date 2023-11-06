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




#procédure recap à compléter
def recap(parcours, nom): 
    '''A CODER'''
    pass 

#precédure depassement à compléter
def depassement(parcours1, parcours2, nom1, nom2):
    '''A CODER'''
    pass 



#Procedure main fournie -- NE PAS MODIFIER !!
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
    
#Appel de main -- NE PAS MODIFIER !!
if __name__ == '__main__':
    main()

