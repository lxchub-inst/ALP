# Épreuve du 21.09.2022
# Exercice 1 – Sapin de Noël


# Imports
from turtle import *
import turtle as np

# Procédures et fonctions


def Sapin(longueur, angle):
    if longueur > 100 or angle > 90:
        print("La longueur doit être inférieure à 100 et l'angle doit être inférieur à 90 degrés.")
    else:
        np.left(90)
        np.forward(longueur)
        np.right(20)
        np.forward(longueur)
        np.back(longueur)
# Procédure main()


def main():
    longeur = int(input("Entrez la longeur du sapin : "))
    angle = int(input("Entrez l'angle du sapin : "))
    Sapin(longeur, angle)
    hideturtle()  # pour ne pas voir la tortue (à ne pas supprimer)
    np.exitonclick()  # pour fermer la fenêtre graphique (à ne pas supprimer)


# Appel de la procédure main()
if __name__ == "__main__":
    main()
