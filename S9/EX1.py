L10_INT = [-3, -1, 0, 1, 1, 4, 6, -1, 7, 8]


# Exercice 1
def premier_liste(liste):
    liste = L10_INT
    return liste[0]


def dernier_liste(liste):
    liste = L10_INT
    return liste[-1]


def avant_dernier_liste(liste):
    liste = L10_INT
    return liste[-2]


def main():
    print(premier_liste(L10_INT))
    print(dernier_liste(L10_INT))
    print(avant_dernier_liste(L10_INT))


if __name__ == "__main__":
    main()
