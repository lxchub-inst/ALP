def calcul_pieces():
    pass


def main():
    prix_unitaire = int(input("Entrer un prix unitaire : "))
    nb_pieces = int(input("Entrer un nombre de pieces : "))
    print(f"Pour {nb_pieces} pièces à {prix_unitaire}€ : \n - Prix avant rabais : {prix_unitaire * nb_pieces}€ \n - Prix après rabais : {prix_unitaire * nb_pieces} \n - Montant du rabais : ")


if __name__ == '__main__':
    main()
