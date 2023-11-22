d = {'nom': 'Dupuis', 'prenom': 'Jacque', 'age': 30}


def correction_dictionnaire(d):
    for ele_keys in d:
        if ele_keys == "prenom":
            d[ele_keys] = "Jacques"
    return d


def main():
    print(correction_dictionnaire(d))


main()