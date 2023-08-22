import turtle as np


def losange(longeur):
    # On crée une boucle sur la longeur du losange
    np.left(45)
    np.forward(longeur)
    # for i in range(4):
    #     np.forward(longeur)
    #     np.left(90)
    np.done()
    np.hideturtle()


def main():
    longeur = int(input("Entrer la longeur du losange: "))
    losange(longeur)
    pass


if __name__:
    main()
