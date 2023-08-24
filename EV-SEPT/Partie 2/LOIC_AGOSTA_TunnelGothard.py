# Épreuve du 21.09.2022
# Exercice 2 – Tunnel du Gothard


# Constantes
CAT_1 = "voiture"
CAT_2 = "camion sans remorque"
CAT_3 = "camion avec remorque"
LONGEUR_MAX = 8

# Procédures et fonctions


def categorie_vehicule(categorie):
    if categorie == "1":
        return CAT_1
    elif categorie == "2":
        return CAT_2
    elif categorie == "3":
        return CAT_3
    else:
        return "La catégorie n'est pas valide"


def poids_vehicule(poids):
    if poids < 4:
        return 15
    elif poids < 10:
        return 20
    elif poids >= 10 and poids <= 25:
        return 30
    elif poids >= 26 and poids <= 38:
        return 42
    elif poids > 38:
        return 50
    else:
        return 0


def longeur_vehicule(longeur):
    if longeur > 8:
        return (longeur - LONGEUR_MAX) * 5
    else:
        return 0


def calcul_prix(categorie, longeur, poids):
    if categorie == CAT_1:
        return 15
    elif categorie == CAT_2 or categorie == CAT_3:
        prix_poids = poids_vehicule(poids)
        prix_longeur = longeur_vehicule(longeur)
        prix_final = prix_poids + prix_longeur
        if categorie == CAT_3:
            return prix_final * 30/100 + prix_final
        return prix_final


def affichage_resultat(categorie, prix_total):
    print(
        f"\nLe véhicule est une {categorie} \nLe prix total du billet est de {prix_total} CHF")


# Procédure main()
def main():
    categorie = input("Entrez la catégorie de véhicule : ")
    longeur = int(input("Entrez la longeur du véhicule : "))
    poids = int(input("Entrez le poids du véhicule : "))

    categorie = categorie_vehicule(categorie)
    prix_total = calcul_prix(categorie, longeur, poids)
    affichage_resultat(categorie, prix_total)
    pass  # à remplacer par vos instructions...


# Appel de la procédure main()
if __name__ == "__main__":
    main()
