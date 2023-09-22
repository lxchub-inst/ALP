"""
Nom : AGOSTA LOIC
Version : 1.0
"""

CATEGORIE_VOITURE = 1
CATEGORIE_CAMION_SANS_REMORQUE = 2
CATEGORIE_CAMION_AVEC_REMORQUE = 3
LONG_SUPP = 8
TAXE_SUPP = 5
SUPPLEMENT_AVEC_REMORQUE = 30


def prix_poids(poids):
    if poids < 4:
        return 15
    elif poids < 10:
        return 20
    elif poids >= 10 and poids <= 25:
        return 30
    elif poids >= 26 and poids <= 38:
        return 42
    else:
        return 50

def prix_billet(categorie, poids, longeur):
    if categorie == CATEGORIE_VOITURE:
        return 15
    elif categorie == CATEGORIE_CAMION_AVEC_REMORQUE or CATEGORIE_CAMION_SANS_REMORQUE:
        prix_final_poids = prix_poids(poids)
        longeur_supp = longeur_supplementaire(longeur)
        prix_total = prix_final_poids + longeur_supp
        if categorie == CATEGORIE_CAMION_AVEC_REMORQUE:
            return prix_total * SUPPLEMENT_AVEC_REMORQUE / 100 + prix_total
        return prix_total


def longeur_supplementaire(longeur):
    if longeur > 8:
        return (longeur - LONG_SUPP) * TAXE_SUPP
    else:
        return 0

def afficher_prix_total(categorie, prix_total):
    if categorie == CATEGORIE_VOITURE:
        print(f"Le véhicule est une voiture")
        print(f"Le prix total est de {prix_total} CHF")
    elif categorie == CATEGORIE_CAMION_SANS_REMORQUE:
        print(f"Le véhicule est un camion")
        print(f"Le prix total est de {prix_total} CHF")
    else:
        print(f"Le véhicule est un camion avec remorque")
        print(f"Le prix total est de {prix_total} CHF")

def main():
    categorie = int(input("Entrez la catégorie du véihicule :"))
    longeur = int(input("Entrez la longeur du véhicule : "))
    poids = int(input("Entrez le poids du véhicule : "))

    prix_total = prix_billet(categorie, poids, longeur)
    afficher_prix_total(categorie, prix_total)

if __name__ == '__main__':
    main()