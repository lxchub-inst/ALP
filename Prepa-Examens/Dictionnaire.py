DICTIONNAIRE = {"Michel": 0, "Robert": 1, "Jean": 2, "Pierre": 3, "Paul": 4, "Jacques": 5, "Marie": 6, "Anne": 7}


def dic():
    print("Impression uniquement des clés du dictionnaire :")
    for ele_keys in DICTIONNAIRE:
        print(ele_keys)

    print("\n")
    print("Impression uniquement des valeurs du dictionnaire :")

    for ele_keys in DICTIONNAIRE:
        print(DICTIONNAIRE[ele_keys])

    print("\n")
    print("Impression des clés et des valeurs du dictionnaire :")
    for ele_keys in DICTIONNAIRE:
        print(ele_keys, ":", DICTIONNAIRE[ele_keys])

    print("\n")
    print("Impression des clés et des valeurs du dictionnaire :")

    for ele_keys, ele_values in DICTIONNAIRE.items():
        print(ele_keys, ":", ele_values)

    print("\n")
    print("Impression du dictionnaire forme pair avec des conditions")
    for ele_keys, ele_values in DICTIONNAIRE.items():
        if ele_values % 2 == 0:
            print(ele_keys, ":", ele_values)

    print("\n")
    print("Impression du dictionnaire avec des conditions de recherche (clé)")
    for ele_keys, ele_values in DICTIONNAIRE.items():
        if ele_keys == "Robert":
            return print(ele_keys, ":", ele_values)
        else:
            return print("La clé", ele_keys, "n'est pas dans le dictionnaire")

    print("\n")
    print("Impression du dictionnaire avec des conditions de recherche (valeur)")
    for ele_keys, ele_values in DICTIONNAIRE.items():
        if ele_values == 99:
            return print(ele_keys, ":", ele_values)
        else:
            return print("L'élément", ele_values, "n'est pas dans le dictionnaire")


def main():
    dic()


main()
