# AGOSTA LOIC

# Procédures et fonctions
''' Cette procédure modifie toutes les données erronées de la liste des pourcentages reçue en paramètre :
        - les valeurs négatives, ou supérieures à 100, sont mises à 0.
        - les valeurs inférieures à 1 doivent être multipliées par 100. '''


def corriger_donnees(lst_pourcentages):
    pass


''' Cette fonction retourne la moyenne des valeurs de la liste des pourcentages reçue en 
paramètre sans prendre en compte les valeurs nulles. '''


def moyenne_sans_0(lst_pourcentages):
    ''' A CODER '''


''' Cette procédure affiche le pays ayant le pourcentage le plus proche du pourcentage recherché '''


def afficher_pays_le_plus_proche(lst_pays, lst_pourcentages, pourcentage_recherche):
    pass


''' Cette procédure affiche les nb premières valeurs non nulles de la liste des pourcentages, 
puis indique le nombre de valeurs affichées. '''


def afficher_nb_donnees(lst_pourcentages, nb):
    ''' A CODER '''


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
