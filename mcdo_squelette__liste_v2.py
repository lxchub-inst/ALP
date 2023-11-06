# Constantes pour les les options de menus
MAINS = ["1. Big Mac", "2. Mc Nuggets (6)", "3. Cheese Royal", "4. Mc Chicken"]
SIDES = ["1. Frites", "2. Patatos", "3. Salade Verte"]
DRINKS = ["1. Coca Cola", "2. Coca Zero", "3. Eau gazeuse", "4. Thé froid"]

# Constantes pour calories
MAINS_CAL = [498, 257, 504, 393]
SIDES_CAL = [435, 389, 90]
DRINKS_CAL = [175, 1, 0, 80]

CAT_MAINS = 1
CAT_SIDES = 2
CAT_DRINKS = 3

LIST_ORDER_J = ["1. Big Mac","1. Frites","1. Coca Cola", "2. Mc Nuggets (6)", "3. Salade Verte", "2. Patatos",
                "2. Coca Zero", "4. Mc Chicken", "4. Thé froid"]
LIST_CAL_ORDER_J = [498, 435, 175, 257, 90, 389, 1, 393, 80]
LIST_CAT_ORDER_J = [CAT_MAINS, CAT_SIDES, CAT_DRINKS, CAT_MAINS, CAT_SIDES, CAT_SIDES, CAT_DRINKS, CAT_MAINS, CAT_DRINKS]


LIST_ORDER_A = ["1. Big Mac","1. Coca Cola", "2. Mc Nuggets (6)", "3. Salade Verte", "4. Mc Chicken", "4. Thé froid"]
LIST_CAL_ORDER_A = [498, 175, 257, 90, 393, 80]
LIST_CAT_ORDER_A = [CAT_MAINS, CAT_DRINKS, CAT_MAINS, CAT_SIDES, CAT_MAINS, CAT_DRINKS]


def order_recap(list_orders, list_cals, list_cat, cat_calcul):
    total_calories = 0
    for i in range(len(list_orders)):
        if list_cat[i] == cat_calcul:
            total_calories += list_cals[i]
    return total_calories


def test_order_recap():
    print("Pour la liste de A, mains : ")
    print(order_recap(LIST_ORDER_A, LIST_CAL_ORDER_A, LIST_CAT_ORDER_A, CAT_MAINS))
    print("Pour la liste de J, drinks :")
    print(order_recap(LIST_ORDER_J, LIST_CAL_ORDER_J, LIST_CAT_ORDER_J, CAT_DRINKS))


def show_list_items(ze_list):
    for i in range(len(ze_list)):
        print(ze_list[i])


def get_index_of_max(ze_list):
    val_max = 0
    for i in range(len(ze_list)):
        if ze_list[i] > ze_list[val_max]:
            val_max = i
    return val_max


def get_index_of_min(ze_list):
    val_min = 0
    for i in range(len(ze_list)):
        if ze_list[i] < ze_list[val_min]:
            val_min = i
    return val_min


def show_max_min_choice(cal_list, dish_list):
    val_max = get_index_of_max(cal_list)
    val_min = get_index_of_min(cal_list)

    print("Choix le plus calorique ", dish_list[val_max])
    print("Choix le moins calorique ", dish_list[val_min])

def get_user_choices():
    # Demande à l'utilisateur de choisir un plat principal
    print("\nChoisissez un plat :")
    show_list_items(MAINS)
    show_max_min_choice(MAINS_CAL, MAINS)
    main_choice = int(input("Entrez le numéro correspondant : "))

    # Demande à l'utilisateur de choisir un accompagnement
    print("\nChoisissez un accompagnement :")
    show_list_items(SIDES)
    show_max_min_choice(SIDES_CAL, SIDES)
    side_choice = int(input("Entrez le numéro correspondant : "))

    # Demande à l'utilisateur de choisir une boisson
    print("\nChoisissez une boisson :")
    show_list_items(DRINKS)
    show_max_min_choice(DRINKS_CAL, DRINKS)
    drink_choice = int(input("Entrez le numéro correspondant : "))

    return main_choice, side_choice, drink_choice


def get_tot_calories(main_course, side, drink):
    # Calcul des calories en fonction des choix de l'utilisateur
    return MAINS_CAL[main_course - 1] + SIDES_CAL[side - 1] + DRINKS_CAL[drink - 1]


# Procédure main()
def main():
    main_choice, side_choice, drink_choice = get_user_choices()

    tot_cal = get_tot_calories(main_choice, side_choice, drink_choice)

    print("\nCalories totales de votre menu :", tot_cal, "kcal")

    test_order_recap()


# Appel de la procédure main()
if __name__ == "__main__":
    main()
