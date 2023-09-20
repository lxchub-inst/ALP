"""" 
Nom : AGOSTA LOIC
Version : 1.0
"""

# Définition des constantes
PRIX_ENTREE_DEGUISES = 10
PRIX_ENTREE_NON_DEGUISES = 15
PRIX_BOISSON_SUP = 7

DEGUISES = 1
NON_DEGUISES = 2

def calculer_prix_entree(nb_personne, type_personne):
    if type_personne == DEGUISES:
        # Si tout le groupe est déguisé, appliquer le tarif réduit de 10 CHF
        if nb_personne >= 4:
            return (nb_personne * PRIX_ENTREE_DEGUISES) - PRIX_ENTREE_DEGUISES # Entrée gratuite pour le groupe
        else:
            return nb_personne * PRIX_ENTREE_DEGUISES
    elif type_personne == NON_DEGUISES:
        return nb_personne * PRIX_ENTREE_NON_DEGUISES

def calculer_prix_boissons(boissons_sup):
    prix_boissons_supp = boissons_sup * PRIX_BOISSON_SUP
    # Calcul des boissons gratuites en fonction du montant dépensé
    boissons_gratuites = prix_boissons_supp // 50 + prix_boissons_supp // 100
    return prix_boissons_supp - (boissons_gratuites * PRIX_BOISSON_SUP) + PRIX_BOISSON_SUP

def afficher_prix_total(prix_entree, prix_boissons):
    prix_total = prix_entree + prix_boissons
    print(f"Prix à payer : {prix_total} CHF")

def main():
    nb_personne = int(input("Entrez le nombre de personnes : "))
    type_personne = int(input("Entrez le type de personne (1 pour déguisées, 2 pour non déguisées) : "))
    boissons_sup = int(input("Entrez le nombre de boissons supplémentaires : "))

    prix_entree = calculer_prix_entree(nb_personne, type_personne)
    prix_boissons = calculer_prix_boissons(boissons_sup)

    afficher_prix_total(prix_entree, prix_boissons)

if __name__ == '__main__':
    main()

"""
# Épreuve du 29.09.2021
# Nom et prénom: 

# Imports éventuels après ce commentaire

# Constantes éventuelles après ce commentaire
''' A COMPLETER '''
PRIX_ENTREE_SANS_DEGUISEMENT = 15
PRIX_ENTREE_AVEC_DEGUISEMENT = 10
NOMBRE_ENTREE_GRATUITE = 1
ENTRE_GRATUITE_A_PARTIR_DE = 4

BOISSONS_SUPP = 7


# Procédures et fonctions
''' A COMPLETER '''
def calcul_prix_entré(nombre_de_personne, type_de_personne):
    if type_de_personne == 1 and nombre_de_personne >= ENTRE_GRATUITE_A_PARTIR_DE:
        return (nombre_de_personne - NOMBRE_ENTREE_GRATUITE) * PRIX_ENTREE_AVEC_DEGUISEMENT
    elif type_de_personne == 1:
        return nombre_de_personne * PRIX_ENTREE_AVEC_DEGUISEMENT
    elif type_de_personne == 2:
        return nombre_de_personne * PRIX_ENTREE_SANS_DEGUISEMENT

def calcul_prix_final(nombre_boissons, prix_entré):
    return prix_entré + (nombre_boissons * BOISSONS_SUPP)

def calcul_boisson_offerte(prix_final, nombre_de_personne, nombre_boissons):
    if prix_final < 50:
        return nombre_de_personne + nombre_boissons
    else:
        bouteille_offerte = 1
        if prix_final >= 100:
            bouteille_offerte += prix_final // 100
        return bouteille_offerte + nombre_de_personne + nombre_boissons

def affichage(nombre_de_boisson_offerte, nombre_de_personne, prix_final):
    print(f"Entrée pour {nombre_de_personne} personnes, Bon pour {nombre_de_boisson_offerte} boissons, Prix à payer : {prix_final}.-")

# Procédure executer()
def executer():
    ''' A COMPLETER '''
    nombre_de_personne = int(input("Entrez le nombre de personne : "))
    type_de_personne = int(input("Entrez le type de personne\nSi vous êtes déguisés tapez 1\nSi vous n'êtes pas déguisé tapez 2 : "))
    nombre_boissons = int(input("Combien de boissons voulez-vous commandé : "))

    prix_entré = calcul_prix_entré(nombre_de_personne, type_de_personne)
    prix_final = calcul_prix_final(nombre_boissons, prix_entré)
    nombre_de_boisson_offerte = calcul_boisson_offerte(prix_final, nombre_de_personne, nombre_boissons)
    affichage(nombre_de_boisson_offerte, nombre_de_personne, prix_final)


# Appel de la procédure main() - NE PAS MODIFIER
executer()
"""