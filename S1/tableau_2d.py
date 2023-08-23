import numpy as np


def tab_pythagore(nb_lignes, nb_colonnes):
    tableau = np.empty((nb_lignes, nb_colonnes), dtype=int)
    for i in range(nb_lignes):
        for j in range(nb_colonnes):
            tableau[i, j] = i * j
    return tableau


# Exemple d'utilisation
tableau = tab_pythagore(13, 13)
print(tableau)
