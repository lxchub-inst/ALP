# Les employés de la compagnie (type de voyageur n°1) bénéficient d'un rabais de 20% sur le prix de base du billet, 
# les membres du club Cigogne (type n°2) obtiennent un rabais de 10% sur le prix de base du billet, 
# les autres voyageurs (type n°3) n'obtiennent pas de rabais.

# De plus, si le voyageur a déjà volé avec la compagnie lors de l'année courante, il bénéficie d'un rabais supplémentaire (sur le prix de base) 
# proportionnel au nombre de vols effectués; celui ci se monte à 10% pour un vol, à 15% pour 2, 3, ou 4 vols et à 20% pour 5 vols ou plus.

def calcul():
    pass

def main():
    prix_initial = int(input("Prix initial : "))
    type_voyageur = input("Type de voyageur : ")
    nombre_vol = int(input("Nombre de vols : "))
    calcul()

if __name__ == "__main__":
    main()