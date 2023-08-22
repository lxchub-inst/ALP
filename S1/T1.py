import turtle as np


def rectangle(longeur, largeur):
    # Boucle sur la longueur du rectangle
    for i in range(2):
        np.forward(longeur)
        np.left(90)
        np.forward(largeur)
        np.left(90)
    np.done()
    np.hideturtle()


def main():
    longeur = int(input("Entrer la longeur du rectangle: "))
    largeur = int(input("Entrer la largeur du rectangle: "))
    rectangle(longeur, largeur)


if __name__:
    main()
