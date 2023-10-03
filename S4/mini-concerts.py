# Imports

# Constantes
DEBOUT = 1
ASSIS = 2

PRIX_DEBOUT = 20
PRIX_ASSIS = 30

# Fonctions
def calcul_prix(type_place, nmb_place):
    if type_place == DEBOUT:
        return nmb_place * PRIX_DEBOUT
    elif type_place == ASSIS:
        if nmb_place > 5:
            return (nmb_place * PRIX_ASSIS) - 2 * PRIX_ASSIS
        else:
            return nmb_place * PRIX_ASSIS
        return type_place, nmb_place

def affichage(type_place, nmb_place, prix):
    if type_place == DEBOUT:
        type_place = "debout"
        print(f"\nLe prix a payer pour {nmb_place} places {type_place} est de {prix} CHF")
    elif type_place == ASSIS:
        type_place = "assises"
        print(f"\nLe prix a payer pour {nmb_place} places {type_place} est de {prix} CHF")

# Principal
def main():
    type_place = int(input("Indiquer le type de place : (1. debout / 2. assis) : "))
    nmb_place = int(input("Indiquer le nombre de place : "))

    prix = calcul_prix(type_place, nmb_place)

    if type_place != DEBOUT and type_place != ASSIS:
        print("Le type de place n'est pas correct")
    if nmb_place >= 70:
        print("Le nombre de place ne peut pas dépasser 70")
    else:
        affichage(type_place, nmb_place, prix)

# Appel de la fonction main()
if __name__ == "__main__":
    main()
