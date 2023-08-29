def facturation(prix_unitaire, quantite):
    prix_avant_rabais = prix_unitaire * quantite
    rabais = 0

    if quantite > 100:
        rabais = prix_avant_rabais * 10/100

    prix_apres_rabais = prix_avant_rabais - rabais

    resultat = {
        "prix_avant_rabais": prix_avant_rabais,
        "montant_rabais": rabais,
        "prix_apres_rabais": prix_apres_rabais
    }

    return resultat

def main():
    prix_unitaire = int(input("Veuillez entrer le prix unitaire: "))
    quantite = int(input("Veuillez entrer le nombre de pièces: "))
    
    resultat = facturation(prix_unitaire, quantite)

    print(f"Pour {quantite} pièces à {prix_unitaire} :")
    print(f"Prix avant rabais: {resultat['prix_avant_rabais']}")
    print(f"Montant du rabais: {resultat['montant_rabais']}")
    print(f"Prix à payer: {resultat['prix_apres_rabais']}")

if __name__ == "__main__":
    main()
