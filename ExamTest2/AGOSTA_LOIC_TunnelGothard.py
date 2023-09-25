"""
Nom : AGOSTA LOIC
Version : 1.0
"""
CAT_1 = 1
CAT_2 = 2
CAT_3 = 3

PRIX_CAT_1 = 15
PRIX_CAM_4_TONNES = 15
PRIX_CAM_INF_10_TONNES = 20
PRIX_CAM_ENTRE_10_25_TONNES = 30
PRIX_CAM_ENTRE_26_38_TONNES = 42
PRIX_CAM_SUP_38_TONNES = 50
LONGEUR_MAX = 8
TAX_LONGEUR_SUPP = 5
SUPP_PRIX = 30

def categorie_vehicule(categorie):
    if categorie == CAT_1:
        return "voiture"
    elif categorie == CAT_2:
        return "camion sans remorque"
    else:
        return "camion avec remorque"
    
def prix_poids(poids):
    if poids < 4:
        return PRIX_CAM_4_TONNES
    elif poids < 10:
        return PRIX_CAM_INF_10_TONNES
    elif poids >= 10 and poids <= 25:
        return PRIX_CAM_ENTRE_10_25_TONNES
    elif poids >= 26 and poids <= 38:
        return PRIX_CAM_ENTRE_26_38_TONNES
    else:
        return PRIX_CAM_SUP_38_TONNES

def prix_billlet(categorie, poids, longeur):
    if categorie == CAT_1:
        return PRIX_CAT_1
    elif categorie == CAT_2 and poids < 4:
        return PRIX_CAM_4_TONNES
    elif categorie == CAT_3:
        prix_final_poids = prix_poids(poids)
        longeur_supp = longeur_supplementaire(longeur)
        prix_total = prix_final_poids + longeur_supp
        return prix_total * SUPP_PRIX / 100 + prix_total

def longeur_supplementaire(longeur):
    if longeur > LONGEUR_MAX:
        return (longeur - LONGEUR_MAX) * TAX_LONGEUR_SUPP
    else:
        return 0


def afficher_prix_total(categorie, prix_total):
    if categorie == CAT_1:
        print(f"Le véhicule est une voiture")
        print(f"Le prix total est de {prix_total} CHF")
    elif categorie == CAT_2:
        print(f"Le véhicule est un camion")
        print(f"Le prix total est de {prix_total} CHF")
    else:
        print(f"Le véhicule est un camion avec remorque")
        print(f"Le prix total est de {prix_total} CHF")

def main():
    categorie = int(input("Entrez la catégorie du véhicule :"))
    longeur = int(input("Entrez la longeur du véhicule : "))
    poids = int(input("Entrez le poids du véhicule : "))

    prix_total = prix_billlet(categorie, poids, longeur)
    afficher_prix_total(categorie, prix_total)

if __name__ == '__main__':
    main()

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
"""