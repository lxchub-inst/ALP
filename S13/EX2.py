PRIX = {"bananes": 4, "pommes": 2, "oranges": 1.5, "poires": 3}
STOCK = {"bananes": 100,"pommes": 290, "oranges": 50, "poires": 120}


def stock_fruit(nom_fruit):
    for ele_keys in STOCK:
        if ele_keys == nom_fruit:
            return print("Le stock de", nom_fruit, "est de", PRIX[ele_keys], "unités")
        else:
            return print("Le fruit", nom_fruit, "n'est pas dans le stock")


def calcul_prix_stock():
    for ele_keys in PRIX:
        print(ele_keys, ":", STOCK[ele_keys] * PRIX[ele_keys], "CHF")

def main():
    nom_fruit = input("Nom du fruit : ")
    stock_fruit(nom_fruit)
    calcul_prix_stock()


main()