GAMME_BASE = ["do", "ré", "mi", "fa", "sol", "la", "si"]
LISTE_ALTERATIONS = ["fa", "do", "sol", "ré", "la", "mi", "si"]
SAUT = 4
TYPE_DIESE = "#"
TYPE_BMOL = "b"


# récap à l'aide d'un dico pour la traduction des notes en anglais
# def affiche_recap(type_alt):
#     dico_notes = {"do": "C", "ré": "D", "mi": "E", "fa": "F", "sol": "C", "la": "A", "si": "B"}
#
#     for i in range(len(GAMME_BASE)):
#         gamme = gamme_selon_alteration(i + 1, type_alt)
#         print(f"La gamme avec {i + 1} {type_alt} est {gamme}, en anglais {dico_notes[gamme]}")


# appelle le calcul selon bmol ou dièse en fonction du type voulu
def gamme_selon_alteration(nb_alt, type_alt):
    gamme = ""
    if type_alt == TYPE_BMOL:
        gamme = gamme_bemol(nb_alt)
    else:
        gamme = gamme_diese(nb_alt)

    return gamme


# affiche la liste des altérations selon leur type (la liste commence à l'envers pour les bémol)
def affiche_liste_alterations(nb_alt, type_alt):
    print("Les notes altérées sont : ", end="")
    debut = 0
    fin = nb_alt
    pas = 1
    if type_alt == TYPE_BMOL:
        debut = len(LISTE_ALTERATIONS) - 1
        fin = len(LISTE_ALTERATIONS) - nb_alt - 1
        pas = -1

    for i in range(debut, fin, pas):
        print(LISTE_ALTERATIONS[i], end=" ")


# calcule la gamme selon le nombre de dièses
def gamme_diese(nb_alt):
    i = 0
    note = ""
    while nb_alt > 0:
        if (i + SAUT) < len(GAMME_BASE):
            i = i + SAUT
        else:
            i = i + SAUT - len(GAMME_BASE)

        note = GAMME_BASE[i]
        nb_alt = nb_alt - 1

    return note


# calcule la gamme selon le nombre de bémols
def gamme_bemol(nb_alt):
    i = 0
    note = ""
    while nb_alt > 0:
        if (i - SAUT) >= 0:
            i = i - SAUT
        else:
            i = len(GAMME_BASE) + i - SAUT

        note = GAMME_BASE[i]
        nb_alt = nb_alt - 1

    return note


def main():
    type_alt = input("Entrez le type d'altération (# ou b) : ")
    nb_alt = int(input("Entrez le nombre d'altérations (entre 1 et 7) : "))
    gamme = gamme_selon_alteration(nb_alt, type_alt)

    print(f"Pour le {nb_alt} altérations de type {type_alt}, la gamme de base est {gamme}")
    affiche_liste_alterations(nb_alt, type_alt)
    # print("\n------------------")
    # affiche_recap("#")
    # print("\n------------------")
    # affiche_recap("b")


main()