# Imports

# Constantes
PIANO_DROIT = "droit"
PIANO_QUEUE = "à queue"

PRIX_MAX_DROIT = 60
PRIX_MAX_QUEUE = 90

PRIX_ETAGE_MAX_DROIT = 600
PRIX_ETAGE_MAX_QUEUE = 900

PRIX_TRANSPORT = 6

PRIX_MIN = 200
PRIX_MAX = 2500
# Procédures et fonctions

def check_prix_min_max(prix_km, prix_etage):
    prix = prix_km + prix_etage
    if(prix < PRIX_MIN):
        return PRIX_MIN
    elif(prix > PRIX_MAX):
        return PRIX_MAX
    else:
        return prix

def prix_etage_type(type_piano, total_etage):
    if(total_etage > 10):
        if(type_piano == PIANO_DROIT):
            return PRIX_ETAGE_MAX_DROIT
        elif(type_piano == PIANO_QUEUE):
            return PRIX_ETAGE_MAX_QUEUE
    elif(type_piano == PIANO_DROIT):
        return total_etage * PRIX_MAX_DROIT
    elif(type_piano == PIANO_QUEUE):
        return total_etage * PRIX_MAX_QUEUE

def affichage(type_piano, prix_km, prix_final, nmb_km):
    print(f"Prix total à payer pour un {type_piano} : {prix_final}.- (dont {prix_km}.- de transport pour les {nmb_km} km)")

# Procédure main()
def main():
    type_piano = input(f"Veuillez entrer le type du piano ({PIANO_DROIT}, {PIANO_QUEUE}) : ")
    nmb_etage_descendu = int(input("Veuillez entrer le nombre d'étage descendu: "))
    nmb_etage_monter = int(input("Veuillez entrer le nombre d'étage à monter: "))

    nmb_km = int(input("Veuillez entrer le nombre de km: "))

    total_etage = nmb_etage_descendu + nmb_etage_monter

    prix_km = nmb_km * PRIX_TRANSPORT
    prix_etage = prix_etage_type(type_piano, total_etage)
    prix_final = check_prix_min_max(prix_km, prix_etage)

    affichage(type_piano, prix_km, prix_final, nmb_km)

# Appel de la procédure main()
if __name__ == "__main__":
    main()