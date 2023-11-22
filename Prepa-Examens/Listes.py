LISTE_CHIFFRE = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
LISTE_MOT = ["Michel", "Robert", "Jean", "Pierre", "Paul", "Jacques", "Marie", "Anne", "Sophie", "Julie"]
LISTE_METIER = ["Boulanger", "Pâtissier", "Boucher", "Charcutier", "Cuisinier", "Traiteur", "Boucher", "Boulanger",
                "Pâtissier", "Cuisinier"]
LISTE_ERREUR = [33, 0, 26.5, 0.28, 1234, 0.4, 0, -1, 29, 0.325]


def liste_totale():
    print("Impression d'une liste totale :")
    for ele_nom in LISTE_MOT:
        print(ele_nom)


def liste_condition():
    print("\n")
    print("Impression de deux listes en parallèle :")
    for ele_nom in LISTE_MOT:
        for ele_metier in LISTE_METIER:
            if ele_nom == "Michel":
                return print(ele_nom, "est", ele_metier)


def liste_parallele():
    print("\n")
    print("Impression de deux listes en parallèle avec condition :")
    for ele_nom in range(len(LISTE_MOT)):
        for ele_metier in range(len(LISTE_METIER)):
            if LISTE_MOT[ele_nom] == "Michel" and LISTE_METIER[ele_metier] == "Boulanger":
                return print(LISTE_MOT[ele_nom], "est", LISTE_METIER[ele_metier])


def correction_donnes():
    print("\nCorrection des données d'une liste")
    for ele_chiffre in range(len(LISTE_ERREUR)):
        if LISTE_ERREUR[ele_chiffre] < 0 or LISTE_ERREUR[ele_chiffre] > 100:
            LISTE_ERREUR[ele_chiffre] = 0
        elif LISTE_ERREUR[ele_chiffre] < 1:
            LISTE_ERREUR[ele_chiffre] *= 100
            LISTE_ERREUR[ele_chiffre] = int(LISTE_ERREUR[ele_chiffre])
    return LISTE_ERREUR


def main():
    print("Avant la correction d'une liste")
    print(LISTE_ERREUR)
    correction_donnes()
    print("Après la correection d'une liste")
    print(LISTE_ERREUR)


main()
