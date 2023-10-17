RELEVES = [11.8, 14.4, 18.6, 16.5, 11.5, 12.3, 9.1]


def moyenne_liste(RELEVES):
    moyenne = 0
    somme = 0
    for i in range(len(RELEVES)):
        somme += RELEVES[i]
        moyenne = somme / len(RELEVES)
    return moyenne


def main():
    print("La moyenne est de :", moyenne_liste(RELEVES))


if __name__ == "__main__":
    main()