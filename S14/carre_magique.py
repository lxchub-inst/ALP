def est_magique(mon_carre_de_3par3):
    # Vérification des valeurs uniques de 1 à 9
    valeurs_uniques = []
    for ligne in mon_carre_de_3par3:
        for valeur in ligne:
            if valeur not in valeurs_uniques and 1 <= valeur <= 9:
                valeurs_uniques.append(valeur)
            else:
                return False

    # Vérification des sommes des lignes, colonnes et diagonales
    somme_magique = 15

    # Vérification des lignes et colonnes
    for i in range(3):
        if sum(mon_carre_de_3par3[i]) != somme_magique or sum(mon_carre_de_3par3[j][i] for j in range(3)) != somme_magique:
            return False

    # Vérification des diagonales
    if sum(mon_carre_de_3par3[i][i] for i in range(3)) != somme_magique or sum(mon_carre_de_3par3[i][2 - i] for i in range(3)) != somme_magique:
        return False

    # Si toutes les vérifications passent, le carré est magique
    return True

# Test de la fonction avec les données fournies
carre1 = [[6, 1, 8], [7, 5, 3], [2, 9, 4]]
carre2 = [[6, 7, 2], [1, 5, 9], [8, 3, 4]]
carre3 = [[6, 7, 5], [1, 2, 9], [8, 3, 4]]
carre4 = [[4, 3, 8], [1, 5, 9], [2, 7, 6]]

print(est_magique(carre1))  # Output: True
print(est_magique(carre2))  # Output: True
print(est_magique(carre3))  # Output: False
print(est_magique(carre4))  # Output: False
