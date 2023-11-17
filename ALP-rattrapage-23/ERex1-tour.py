# AGOSTA LOIC


# Imports
from turtle import *

# Constantes


# Procédures et fonctions
def aller_a_position_initiale():
    penup()
    goto(-100, -300)
    pendown()

def input_longueurs():
    return int(input('Saisir la longueur des côtés: ')), int(input('Saisir la longueur limite: '))


def input_couleurs():
    return input('Saisir une liste de 2 couleurs séparées par un espace (p.ex. green red): ').split()


# Procédure main()
def main():
    aller_a_position_initiale()
    ''' A CODER '''


# Appel de la procédure main()
if __name__ == '__main__':
    main()
