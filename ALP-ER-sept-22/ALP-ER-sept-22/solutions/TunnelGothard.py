# Épreuve du 21.09.2022
# Exercice 2 – Tunnel du Gothard
# Nom et prénom: Vogt Clément


# Constantes
VOITURE = 1
CAMION_AVEC_REMORQUE = 3
PRIX_VOITURE = 15
PRIX_P1 = 20
PRIX_P2 = 30
PRIX_P3 = 42
PRIX_P4 = 50;
LIM_POIDS = 4
LIM_P1 = 10
LIM_P2 = 25
LIM_P3 = 38
LONGUEUR_SANS_TAXE = 8
PRIX_TAXE = 5
TAUX_SUPPL_REMORQUE = 0.3
    
# Procédures et fonctions
def donnees_entrees():
    categorie = int(input("Entrez une catégorie:"))
    longueur = int(input("Entrez une longueur:"))
    poids = int(input("Entrez un poids en tonne:"))
    return categorie, longueur, poids

def prix_du_billet(categorie, longueur, poids):
    if categorie == VOITURE:
        prix = PRIX_VOITURE
    else:
        if poids < LIM_POIDS:
            prix = PRIX_VOITURE
        else:
            if poids < LIM_P1:
                prix = PRIX_P1
            elif poids <= LIM_P2:
                prix = PRIX_P2
            elif poids <= LIM_P3:
                prix = PRIX_P3
            else:
                prix = PRIX_P4    
            if longueur > LONGUEUR_SANS_TAXE:
                prix += PRIX_TAXE * (longueur-LONGUEUR_SANS_TAXE)
        if categorie == CAMION_AVEC_REMORQUE:
            prix += prix * TAUX_SUPPL_REMORQUE          
    return prix
    
def afficher_resultats(categorie, prix):
    print("Le véhicule est ",end="")
    if categorie == VOITURE:
        print("une voiture")
    elif categorie == CAMION_AVEC_REMORQUE:
        print("un camion avec remorque")
    else:
        print("un camion")    
    print("Le prix total du billet est de", prix, "CHF")
    
# Procédure main()
def main():
    categorie, longueur, poids = donnees_entrees()
    prix = prix_du_billet(categorie, longueur, poids)
    afficher_resultats(categorie, prix)
    
# Appel de la procédure main()
if __name__ == "__main__":
    main()