# Épreuve du 21.09.2022
# Exercice 1 – Sapin de Noël


# Imports
from turtle import *
import turtle as np

# Procédures et fonctions
def Sapin(longueur, angle, nombre_fleche, couleur):
    np.left(90)
    couleur_default = "green"
    if longueur > 100 or angle > 90:
        print("La longeur ou l'angle est trop grand pour être affiché correctement !")
        breakpoint()
        exitonclick()
    else:
        for i in range(nombre_fleche):
            if i % 3 == 2:
                np.color(couleur)
            else:
                np.color(couleur_default)
            forward(longueur)
            right(180-angle)
            forward(longueur)
            backward(longueur)
            right(angle*2)
            forward(longueur)
            backward(longueur)
            right(180-angle)
    np.done()
# Procédure main()


def main():
    nombre_fleche = int(input("Entrez le nombre de fleche du sapin : "))
    longeur = int(input("Entrez la longeur du sapin : "))
    angle = int(input("Entrez l'angle du sapin : "))
    couleur = input("Entrez la couleur du sapin : ")

    Sapin(longeur, angle, nombre_fleche, couleur)
    hideturtle()  # pour ne pas voir la tortue (à ne pas supprimer)
    np.exitonclick()  # pour fermer la fenêtre graphique (à ne pas supprimer)


# Appel de la procédure main()
if __name__ == "__main__":
    main()
