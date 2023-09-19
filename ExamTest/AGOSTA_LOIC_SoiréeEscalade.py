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
