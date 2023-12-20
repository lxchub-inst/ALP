from fis_cup_data import *

def points(placement):
    if placement not in DIC_POINTS:
        return 0
    else:
        return DIC_POINTS[placement]
def question1():
    print("=== Question 1 ===")
    print(points(99))


def question2():
    print("=== Question 2 ===")


def question3():
    print("=== Question 3 ===")
    #skieuses = ['Jessica Richer', 'Claire Martin', 'Julie Durand', 'Jessica Durand', 'Céline Martin']
    #for skieuse in skieuses:
    #    afficher_moyenne_placements(skieuse)


def question4():
    print("=== Question 4 ===")


def main():
    question1()
    question2()
    question3()
    question4()


if __name__ == '__main__':
    main()
