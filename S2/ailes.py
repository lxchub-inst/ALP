def saisir_prix_initial():
    return int(input("Veuillez entrer un prix initial: "))

def saisir_type_voyageur():
    return int(input("Veuillez entrer le N° du type de voyageur: "))

def saisir_vol_effectue():
    return int(input("Veuillez entrer le nombre de vol effectué: "))

def rabais_voyageur(type_voyageur, prix_initial):
    if type_voyageur == 1:
        return prix_initial * 20 / 100
    elif type_voyageur == 2:
        return prix_initial * 10 / 100
    else:
        return 0

def rabais_supplement(vol_effectue, prix_initial):
    if vol_effectue == 1:
        return prix_initial * 10 / 100
    elif 2 <= vol_effectue <= 4:
        return prix_initial * 15 / 100
    elif vol_effectue >= 5:
        return prix_initial * 20 / 100
    else:
        return 0

def prix_final(prix_initial, rabais, rabais_supplementaire):
    return prix_initial - rabais - rabais_supplementaire

def main():
    prix_initial = saisir_prix_initial() # int(input("Veuillez entrer un prix initial: "))
    type_voyageur = saisir_type_voyageur() # int(input("Veuillez entrer le N° du type de voyageur: "))
    vol_effectue = saisir_vol_effectue() # int(input("Veuillez entrer le nombre de vol effectué: "))

    rabais = rabais_voyageur(type_voyageur, prix_initial)
    rabais_supplementaire = rabais_supplement(vol_effectue, prix_initial)

    prix_effectif = prix_final(prix_initial, rabais, rabais_supplementaire)
    
    print(f"Prix effectif : {prix_effectif} CHF")

if __name__ == "__main__":
    main()
