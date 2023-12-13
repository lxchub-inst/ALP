tableau_2d = [
#     0    1    2	 3	  4    5 	6
    ['a', 'b', 'c', '1', '2', '3', '@'],
    ['A', 'B', 'C', '4', '5', '6', '#'],
    ['d', 'e', 'f', '7', '8', '9', '$'],
    ['D', 'E', 'F', '!', '@', '#', '%'],
    ['g', 'h', 'i', '0', '&', '*', '-'],
    ['j', 'k', 'l', 'm', 'n', 'o', '?']
]

mot_de_passe = ''
# print(tableau_2d[5][3])

# print(len(tableau_2d))

# print(len(tableau_2d[0]))

for i in range(len(tableau_2d)):
    for j in range(len(tableau_2d[0])):
        if j == len(tableau_2d[0]) - 1:
            print(tableau_2d[i][j], end="")
        else:
            print(tableau_2d[i][j], "- ", end="")

    print()

# vous pouvez ici essayer de
# générer un mdp en vous basant sur les caractères de la première colonne à chaque fois
print("Mot de passe généré:", mot_de_passe)