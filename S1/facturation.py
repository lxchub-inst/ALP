def facturation(prix_unitaire, quantite,):
    rabais = 0
    if quantite <= 100:
        rabais = prix_unitaire
    elif quantite > 100:
        rabais = prix_unitaire * 90/100
    return rabais

def main():
    prix_unitaire = int(input("Prix unitaire : "))
    quantite = int(input("Quantité : "))
    prix_avant_rabais = prix_unitaire * quantite
    prix_apres_rabais = facturation(prix_unitaire, quantite) * quantite

    print(f"Pour {quantite} articles, à {prix_unitaire}")
    print(f" - Prix avant rabais : {prix_avant_rabais}")
    print(f" - Montant du rabais : {prix_avant_rabais - prix_apres_rabais}")
    print(f" - Prix après rabais : {prix_apres_rabais}")

if __name__ == "__main__":
    main()