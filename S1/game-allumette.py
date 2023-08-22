def game_allumette():
    allu_depart = int(input("Joueur 1 prends : "))
    if allu_depart > 3:
        print("Le nombre max est 3 allumettes !")
    else:
        print(f"Joueur 1 : A pris {allu_depart} allumettes")
        allu_fin = 4 - allu_depart
        print(f"Ordinateur 1 : A pris {allu_fin} allumettes")
        allu_total = allu_depart - allu_fin
        if allu_total < 4:
            print("Ordi 1 : A gagné !")
        else:
            print("Ordi 1 : A perdu !")


def main():
    game_allumette()


if __name__ == '__main__':
    main()
