# Les employés de la compagnie (type de voyageur n°1) bénéficient d'un rabais de 20% sur le prix de base du billet, 
# les membres du club Cigogne (type n°2) obtiennent un rabais de 10% sur le prix de base du billet, 
# les autres voyageurs (type n°3) n'obtiennent pas de rabais.

# De plus, si le voyageur a déjà volé avec la compagnie lors de l'année courante, il bénéficie d'un rabais supplémentaire (sur le prix de base) 
# proportionnel au nombre de vols effectués; celui ci se monte à 10% pour un vol, à 15% pour 2, 3, ou 4 vols et à 20% pour 5 vols ou plus.

def calcul(prix_initial, type_voyageur, nombre_vol):
    rabaisSup = 0
    rabais = 0
    if type_voyageur == 1:
        rabais = (prix_initial * 20/100)
    elif type_voyageur == 2:
        rabais = (prix_initial * 10/100)
    
    if nombre_vol == 1:
        rabaisSup = (prix_initial * 10/100)
    elif nombre_vol >= 2 and nombre_vol <= 4:
        rabaisSup = (prix_initial * 15/100)
    else:
        rabaisSup = (prix_initial * 20/100)
    
    prix_initial = prix_initial - rabais - rabaisSup
    return prix_initial


def main():
    prix_initial = int(input("Prix initial : "))
    type_voyageur = int(input("Type de voyageur : "))
    nombre_vol = int(input("Nombre de vols : "))

    print(f"Prix effectif : {calcul(prix_initial, type_voyageur, nombre_vol)}")

if __name__ == "__main__":
    main()