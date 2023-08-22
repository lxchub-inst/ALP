NB_MAX_PIECES = 100


def calcul_pieces(prix_piece, nombre_pieces, rabais=10/100):
    if nombre_pieces > NB_MAX_PIECES:
        prix_piece = prix_piece * rabais
    elif nombre_pieces >= NB_MAX_PIECES:
        prix_piece = prix_piece
    return prix_piece


def main():
    prix_unitaire = int(input("Entrer un prix unitaire : "))
    nb_pieces = int(input("Entrer un nombre de pieces : "))
    print(f"Pour {nb_pieces} pièces, le prix unitaire est de {prix_unitaire}€")
    print(f"- Prix avant rabais : {prix_unitaire} * {nb_pieces}€")
    print(f"- Montant du rabais : ")
    print(calcul_pieces(prix_unitaire, nb_pieces, rabais=10/100))


if __name__ == '__main__':
    main()
