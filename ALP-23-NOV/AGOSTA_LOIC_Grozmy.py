# ER ALP 30-10-2023
################### NOM ET PRENOM ici !
###################


# Constante fournie -- NE PAS MODIFIER
NOMBRE_DE_CATEGORIES = 4


# Vos constantes ici


# Fonction fournie -- NE PAS MODIFIER !!
def arrondi2(montant):  # arrondi un nombre au centiÃ¨me pour l'afficher
    return format(montant, '.2f')


##############################################
# proc Ã©dures et fonctions Ã  complÃ©ter
# en supprimant pass et le remplaÃ§ant par votre code

# QUESTION 1
def total_achats(liste_achats):
    somme_achats = 0
    for ele_achats in range(len(liste_achats)):
        somme_achats += liste_achats[ele_achats]
    return somme_achats


def afficher_total_achats(liste_achats):
    return "Le montant total (sans réduction) est de", total_achats(liste_achats)


# QUESTION 2
def total_par_categorie(liste_achats, liste_categories):
    somme_cat_ = 0
    for ele_cat in range(len(liste_categories)):
        if liste_categories[ele_cat] == ele_cat:
            somme_cat_ += total_achats(liste_achats)
    return somme_cat_


def afficher_toutes_les_categories(liste_achats, liste_categories):
    for ele_cat in range(NOMBRE_DE_CATEGORIES):
        print("Le montant total pour la catégorie", ele_cat, "est de",
              total_par_categorie(liste_achats, liste_categories))


# QUESTION 3
def afficher_bons(liste_achats):
    pass


# QUESTION 4
def minimum():
    pass


def afficher_minimum(liste_achats):
    pass


# QUESTION 5
def reduction_au_dela():
    pass


def afficher_reduction_au_dela(liste_achats, limite):
    pass


# QUESTION 6
def reduction_par_deux(l):
    pass


def afficher_reduction_par_deux(liste_achats):
    pass


#################
# NE PAS MODIFIER LES PROCEDURES QUI SUIVENT
def test_global(liste_achats, liste_categories):
    print("Pour la liste d'achats suivante", liste_achats)
    afficher_total_achats(liste_achats)
    afficher_toutes_les_categories(liste_achats, liste_categories)

    afficher_bons(liste_achats)

    afficher_minimum(liste_achats)

    afficher_reduction_au_dela(liste_achats, 1000)
    afficher_reduction_au_dela(liste_achats, 500)

    afficher_reduction_par_deux(liste_achats)


def main():  # NE PAS MODIFIER !!
    # les trois jeux de donnÃ©es
    liste_1_achats = [138.50, 312.50, 312.50, 72, 283.40, 152, 135.20, 89.40, 37, 37]
    liste_1_categories = [1, 3, 3, 4, 2, 1, 1, 4, 3, 3]

    liste_2_achats = [138.50, 312.50, 312.50, 72]
    liste_2_categories = [1, 3, 3, 1]

    liste_3_achats = [37, 45.20, 12.50, 12.50, 12.50, 12.50]
    liste_3_categories = [3, 1, 2, 2, 2, 2]

    # exÃ©cution des procÃ©dures d'affichage avec les trois jeux de donnÃ©es
    test_global(liste_1_achats, liste_1_categories)
    print("\n-----------------------------------------------------------\n")
    test_global(liste_2_achats, liste_2_categories)
    print("\n-----------------------------------------------------------\n")
    test_global(liste_3_achats, liste_3_categories)


# Appel de la procÃ©dure main()
if __name__ == "__main__":
    main()
