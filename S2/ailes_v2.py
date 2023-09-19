def rabais_voyageur(type_voyageur, prix_initial):
    if type_voyageur == 1:
        return prix_initial * 20 / 100
    elif type_voyageur == 2:
        return prix_initial * 10 / 100
    else:
        return 0
    

def rabais_supplement(vol_effectue, prix_initial):
    if vol_effectue == 1:
        return prix_initial * 10/100
    elif 2 <= vol_effectue <= 4:
        return prix_initial * 15/100
    elif vol_effectue >= 5:
        return prix_initial * 20/100
    else:
        return 0
    

def prix_final(prix_initial, rabais, rabais_supplementaire):
    return prix_initial - rabais - rabais_supplementaire


def main():
    prix_effectif = int(input("Prix initial : "))
    type_voyageur = int(input("Type de voyageur : "))
    vol_effectue = int(input("Nombre de vol effectué : "))

    rabais = rabais_voyageur(type_voyageur, prix_effectif)
    rabais_supplementaire = rabais_supplement(vol_effectue, prix_effectif)

    prix_effectif = prix_final(prix_effectif, rabais, rabais_supplementaire)
    print("Prix effectif : ", prix_effectif, "CHF")

if __name__ == "__main__":
    main()