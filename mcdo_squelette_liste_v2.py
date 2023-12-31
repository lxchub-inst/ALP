# Exercice 1 : les constantes dont vous avez besoin, c'est kdo

# Constantes pour les les options de menus
MAINS = ["1. Big Mac", "2. Mc Nuggets (6)", "3. Cheese Royal", "4. Mc Chicken"]
SIDES = ["1. Frites", "2. Patatos", "3. Salade Verte"]
DRINKS = ["1. Coca Cola", "2. Coca Zero", "3. Eau gazeuse", "4. Thé froid"]

# Constantes pour calories
MAINS_CAL = [498, 257, 504, 393]
SIDES_CAL = [435, 389, 90]
DRINKS_CAL = [175, 1, 0, 80]


# Exercice 2 écrivez une fonction qui affiche le contenu de la liste passée en paramètre (ze_liste)
def show_list_items(ze_list):
    for i in range(len(ze_list)):
        print(ze_list[i])


# Exercice 3 écrivez une fonction qui retourne l'index de la valeur la plus grande
# de la liste passée en paramètre (ze_liste)
def get_index_of_max(ze_list):
    val_max = 0
    for i in range(len(ze_list)):
        if ze_list[i] > ze_list[val_max]:
            val_max = i
    return val_max


# Exercice 3 écrivez une fonction qui retourne l'index de la valeur la plus plus petite
# de la liste passée en paramètre (ze_liste)
def get_index_of_min(ze_list):
    val_min = 0
    for i in range(len(ze_list)):
        if ze_list[i] < ze_list[val_min]:
            val_min = i
    return val_min


# Exercice 3 écrivez une fonction qui affiche le choix le plus calorique et le moins calorique
# selon les listes, cette fonction APPELLE les fonctions min et max !
def show_max_min_choice(cal_list, dish_list):
    choice_val_max = get_index_of_max(cal_list)
    choice_val_min = get_index_of_min(cal_list)

    print("Le choix le plus calorique c'est", dish_list[choice_val_max])
    print("Le choix le moins calorique, c'est ", dish_list[choice_val_min])


def get_user_choices():
    # Demande à l'utilisateur de choisir un plat principal
    print("\nChoisissez un plat :")
    show_list_items(MAINS)  # décommentez appel de la fonction de l'exercice 2
    show_max_min_choice(MAINS, MAINS_CAL)
    # ajouter partie exercice 3
    main_choice = int(input("Entrez le numéro correspondant : "))

    # Demande à l'utilisateur de choisir un accompagnement
    print("\nChoisissez un accompagnement :")
    show_list_items(SIDES)  # décommentez appel de la fonction de l'exercice 2
    show_max_min_choice(SIDES, SIDES_CAL)
    # ajouter partie exercice 3
    side_choice = int(input("Entrez le numéro correspondant : "))

    # Demande à l'utilisateur de choisir une boisson
    print("\nChoisissez une boisson :")
    show_list_items(DRINKS)  # décommentez appel de la fonction de l'exercice 2
    show_max_min_choice(DRINKS, DRINKS_CAL)
    # ajouter partie exercice 3
    drink_choice = int(input("Entrez le numéro correspondant : "))

    return main_choice, side_choice, drink_choice  # retour des valeurs saisies


# Exercice 4 : Calcul des calories en fonction des choix de l'utilisateur sans effet papillon
def get_tot_calories(main_course, side, drink):
    return MAINS_CAL[main_course - 1] + SIDES_CAL[side - 1] + DRINKS_CAL[drink - 1]


# Procédure main()
def main():
    main_choice, side_choice, drink_choice = get_user_choices()

    # Exercice 4 appel de la fonction get_tot_calories
    get_tot_calories(main_choice, side_choice, drink_choice)

    # Exercice 5 affichage du résultat
    print("Le nombre total de calories c'est ", get_tot_calories(main_choice, side_choice, drink_choice))


# Appel de la procédure main()
if __name__ == "__main__":
    main()
