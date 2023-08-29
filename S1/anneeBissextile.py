# # initialisation des variables
# annee=2015
# bissextile=False

# # instructions conditionnelles SANS opérateurs booléans
# if annee % 4 == 0:
#     bissextile = True
# else:
#     if annee % 100 == 0:
#         bissextile = True
#     else:
#         if annee % 400 == 0:
#             bissextile = True
#         else:
#             bissextile = False
# if bissextile == True:
#     print('Bissextile')
# else:
#     print('Non bissextile')

"""" 
Savoir par un autre algorithme si une année est bissextile ou non
"""

def bissextile(annee, diviseur):
    while diviseur == 0:
        print("Le diviseur ne peut pas être nul ! \n")
        diviseur = int(input('Entrez un autre diviseur disponible (4, 100, 400) : \n'))

    if diviseur == 4:
        bissextile = annee % diviseur == 0
    elif diviseur == 100:
        bissextile = annee % diviseur == 0
    elif diviseur == 400:
        bissextile = annee % diviseur == 0
    else:
        pass
        return

    if bissextile:
        print("\n L'année est bissextile")
    else:
        print("\n L'année n'est pas bissextile")


def main():
    annee = int(input('Entrez une année : '))
    diviseur = int(input('Entrez un diviseur (4, 100, 400) : '))

    bissextile(annee, diviseur)

if __name__ == '__main__':
    main()
