# Exercice 1 : les constantes dont vous avez besoin, c'est kdo

# Constantes pour les les options de menus
MAINS = ["1. Big Mac", "2. Mc Nuggets (6)", "3. Cheese Royal", "4. Mc Chicken"]
SIDES = ["1. Frites", "2. Patatos", "3. Salade Verte"]
DRINKS = ["1. Coca Cola", "2. Coca Zero", "3. Eau gazeuse", "4. Thé froid"]

# Constantes pour calories
MAINS_CAL = [498, 257, 504, 393]
SIDES_CAL = [435, 389, 90]
DRINKS_CAL = [175, 1, 0, 80]

# Constantes pour le surplus
SURPLUS_CAL = 0.25


# Exercice 2 écrivez une fonction qui affiche le contenu de la liste passée en paramètre (ze_liste)
def show_list_items(ze_list):
    for i in range(len(ze_list)):
        print(ze_list[i])


# Exercice 3 écrivez une fonction qui retourne l'index de la valeur la plus grande
# de la liste passée en paramètre (ze_liste)
def get_index_of_max(ze_list):
    max_index = 0
    for i in range(len(ze_list)):
        if ze_list[i] > ze_list[max_index]:
            max_index = i
    return max_index


def get_index_of_min(ze_list):
    min_index = 0
    for i in range(len(ze_list)):
        if ze_list[i] < ze_list[min_index]:
            min_index = i
    return min_index


# Exercice 3 écrivez une fonction qui affiche le choix le plus calorique et le moins calorique
# selon les listes, cette fonction APPELLE les fonctions min et max !
def show_max_min_choice(cal_list, dish_list):
    max_calories = get_index_of_max(cal_list)
    min_calories = get_index_of_min(cal_list)

    print("Le choix le plus calorique est", dish_list[max_calories])
    print("Le choix le moins calorique est", dish_list[min_calories])


def get_user_choices():
    # Demande à l'utilisateur de choisir un plat principal
    print("\nChoisissez un plat :")
    show_list_items(MAINS)  # décommentez appel de la fonction de l'exercice 2
    # ajouter partie exercice 3
    show_max_min_choice(MAINS_CAL, MAINS)
    main_choice = int(input("Entrez le numéro correspondant : "))

    # Demande à l'utilisateur de choisir un accompagnement
    print("\nChoisissez un accompagnement :")
    show_list_items(SIDES)  # décommentez appel de la fonction de l'exercice 2
    # ajouter partie exercice 3
    show_max_min_choice(SIDES_CAL, SIDES)
    side_choice = int(input("Entrez le numéro correspondant : "))

    # Demande à l'utilisateur de choisir une boisson
    print("\nChoisissez une boisson :")
    show_list_items(DRINKS)  # décommentez appel de la fonction de l'exercice 2
    # ajouter partie exercice 3
    show_max_min_choice(DRINKS_CAL, DRINKS)
    drink_choice = int(input("Entrez le numéro correspondant : "))

    return main_choice, side_choice, drink_choice  # retour des valeurs saisies


def get_tot_calories(main_course, side, drink):
    # Exercice 4 : Calcul des calories en fonction des choix de l'utilisateur sans effet papillon
    return MAINS_CAL[main_course - 1] + SIDES_CAL[side - 1] + DRINKS_CAL[drink - 1]


def get_tot_calories_with_butterfly(main_choice, side_choice, drink_choice):
    surplus = 0
    main_choice_calories = get_index_of_max(MAINS_CAL)
    side_choice_calories = get_index_of_max(SIDES_CAL)
    original_calories = MAINS_CAL[main_choice - 1] + SIDES_CAL[side_choice - 1] + DRINKS_CAL[drink_choice - 1]

    # Vérifiez si l'utilisateur a choisi les options les plus caloriques pour le plat principal et l'accompagnement
    if main_choice - 1 == main_choice_calories and side_choice - 1 == side_choice_calories:
        surplus = original_calories + (original_calories * SURPLUS_CAL)
    else:
        surplus = original_calories
    return surplus


def get_combinations(options, options_calories, current_combo, index, total_calories, max_calories):
    if index == len(options):
        if total_calories < max_calories:
            return [current_combo]
        else:
            return []

    option_combinations = []
    for i in range(len(options[index])):
        option = options[index][i]
        option_calories = options_calories[index][i]

        new_combo = current_combo + [option]
        new_total_calories = total_calories + option_calories

        option_combinations += get_combinations(options, options_calories, new_combo, index + 1, new_total_calories,
                                                max_calories)

    return option_combinations


def get_item_under_300_calories():
    list_options = []
    max_callories = 300

    for i in range(len(MAINS_CAL)):
        if MAINS_CAL[i] < max_callories:
            list_options.append(MAINS[i])
    for j in range(len(SIDES_CAL)):
        if SIDES_CAL[j] < max_callories:
            list_options.append(SIDES[j])
    for k in range(len(DRINKS_CAL)):
        if DRINKS_CAL[k] < max_callories:
            list_options.append((DRINKS[k]))
    return list_options


# Procédure main()
def main():
    main_choice, side_choice, drink_choice = get_user_choices()

    # Exercice 4 appel de la fonction get_tot_calories
    total_calories = get_tot_calories(main_choice, side_choice, drink_choice)
    total_calories_with_butterfly = get_tot_calories_with_butterfly(main_choice, side_choice, drink_choice)

    # Exercice 4 affichage du résultat
    print("\n Calories total de votre menu", total_calories, "kcal")
    print("\n Calories total de votre menu", total_calories_with_butterfly, "kcal")

    print("\n Les options qui font moins de 300 calories sont : ")
    show_list_items(get_item_under_300_calories())

# Appel de la procédure main()
if __name__ == "__main__":
    main()
