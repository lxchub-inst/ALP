# AGOSTA LOIC

# Procédures et fonctions
''' Cette procédure modifie toutes les données erronées de la liste des pourcentages reçue en paramètre :
        - les valeurs négatives, ou supérieures à 100, sont mises à 0.
        - les valeurs inférieures à 1 doivent être multipliées par 100. '''


def corriger_donnees(lst_pourcentages):
    for elements in range(len(lst_pourcentages)):
        if lst_pourcentages[elements] < 0 or lst_pourcentages[elements] > 100:
            lst_pourcentages[elements] = 0
        if lst_pourcentages[elements] < 1:
            lst_pourcentages[elements] *= 100
    return lst_pourcentages


''' Cette fonction retourne la moyenne des valeurs de la liste des pourcentages reçue en 
paramètre sans prendre en compte les valeurs nulles. '''


def elements(lst_pourcentages):
    somme_element = 0
    for element in range(len(lst_pourcentages)):
        if lst_pourcentages[element] != 0:
            somme_element += lst_pourcentages[element]
    return somme_element


def moyenne_sans_0(lst_pourcentages):
    return elements(lst_pourcentages) / 6


''' Cette procédure affiche le pays ayant le pourcentage le plus proche du pourcentage recherché '''


def afficher_pays_le_plus_proche(lst_pays, lst_pourcentages, pourcentage_recherche):
    ele_pays = 0
    ele_pourcentage = 0
    for ele_pourcentages in range(len(lst_pourcentages)):
        if lst_pourcentages[ele_pourcentages] != 0:
            # GPT pour cette ligne
            if abs(lst_pourcentages[ele_pourcentages] - pourcentage_recherche) < abs(ele_pourcentage -
                                                                                     pourcentage_recherche):
                ele_pourcentage = lst_pourcentages[ele_pourcentages]
                ele_pays = lst_pays[ele_pourcentages]
    print("Le pays le plus proche est", ele_pays, "avec", ele_pourcentage, "%")


''' Cette procédure affiche les nb premières valeurs non nulles de la liste des pourcentages, 
puis indique le nombre de valeurs affichées. '''


def afficher_nb_donnees(lst_pourcentages, nb):
    nb_valeur = 0
    # GPT pour cette ligne
    lst_valeurs = []
    for ELEMENTS in range(len(lst_pourcentages)):
        if lst_pourcentages[ELEMENTS] != 0:
            # GPT pour cette ligne
            lst_valeurs.append(round(lst_pourcentages[ELEMENTS]))
            nb_valeur += 1
        if nb_valeur == nb:
            break
    print("Les", nb_valeur, "valeurs de pourcentages affichés sont", lst_valeurs)


# Procédure main()
''' Cette procédure permet de tester les 4 procédures/fonctions ci-dessus :
    elle commence par remplir la liste des pourcentages ainsi que la liste des pays, 
    avant d'appeler vos 4 procédures/fonctions. 
    Pour les tests, vous devez avoir une liste de pourcentages ainsi qu'une liste de pays contenant respectivement au 
    minimum 10 valeurs réelles et 10 chaînes de caractères. 
    
    Vous n'avez pas le droit de modifier cette procédure. '''


def main():
    nb = int(input("Entrez un nombre: "))
    pourcentage_recherche = float(input("Entrez un pourcentage recherché: "))
    pourcentages = [33, 0, 26.5, 0.28, 1234, 0.4, 0, -1, 29, 0.325]
    pays = ["France", "Suisse", "Irlande", "Italie", "Norvège", "Angleterre", "États-Unis", "Colombie", "Canada",
            "Suède"]
    corriger_donnees(pourcentages)
    print("-- Résultats après correction de la liste des pourcentages --")
    print("Réduction moyenne:", moyenne_sans_0(pourcentages))
    afficher_pays_le_plus_proche(pays, pourcentages, pourcentage_recherche)
    afficher_nb_donnees(pourcentages, nb)


# Appel de la procédure main()
if __name__ == "__main__":
    main()
