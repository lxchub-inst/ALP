"""
Nom : LOIC AGOSTA
Version : 1.0
"""

# Imports

# Constantes
CHOIX_BIG_MAC = 1
CHOIX_MC_NUGGETS = 2

CHOIX_FRITES = 1
CHOIX_SALADE = 2

CHOIX_COCA = 1
CHOIX_COCA_ZERO = 2

BIG_MAC = 509
MC_NUGGETS = 170

FRITES = 350
SALADE = 50

COCA_COLA = 175
COCA_COLA_ZERO = 1

SURPLUS_CALORIQUES = 0.25

# ProcÃ©dures et fonctions
def calcul_calorique(plat_principal, accompagnement, boisson):
    if plat_principal == 1 and accompagnement == 1:
        if boisson == 1:
            return (BIG_MAC + FRITES + COCA_COLA) * SURPLUS_CALORIQUES + (BIG_MAC + FRITES + COCA_COLA)
        elif boisson == 2:
            return BIG_MAC + FRITES + COCA_COLA_ZERO
    elif plat_principal == 1 and accompagnement == 2:
        if boisson == 1:
            return BIG_MAC + SALADE + COCA_COLA
        elif boisson == 2:
            return BIG_MAC + SALADE + COCA_COLA_ZERO
    elif plat_principal == 2 and accompagnement == 1:
        if boisson == 1:
            return MC_NUGGETS + FRITES + COCA_COLA
        elif boisson == 2:
            return MC_NUGGETS + FRITES + COCA_COLA_ZERO
    elif plat_principal == 2 and accompagnement == 2:
        if boisson == 1:
            return MC_NUGGETS + SALADE + COCA_COLA
        else:
            return MC_NUGGETS + SALADE + COCA_COLA_ZERO

def affichage(plat_principal, accompagnement, boisson):
    resultat = calcul_calorique(plat_principal, accompagnement, boisson)
    print(f"\nCalories totales de votre menu : {resultat} kcal")

# ProcÃ©dure main()
def main():
    print("Choisissez un plat principal : \n 1. Big Mac \n 2. Mc Nuggets")
    plat_principal = int(input("Entrez le numéro correspondant (1 ou 2): "))

    print("\nChoisissez un accompagnement : \n 1. Frites \n 2. Salade verte")
    accompagnement = int(input("Entrez le numéro correspondant (1 ou 2): "))

    print("\nChoisissez une boisson : \n 1. Coco Cola \n 2. Coco Cola Zero")
    boisson = int(input("Entrez le numéro correspondant (1 ou 2): "))

    calcul_calorique(plat_principal, accompagnement, boisson)
    affichage(plat_principal, accompagnement, boisson)
    
# Appel de la procÃ©dure main()
if __name__ == "__main__":
    main()