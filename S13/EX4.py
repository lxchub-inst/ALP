CHAINE = "Comment AlleZ-Vous MainteNanT ?"


def decomposotion_chaine(chaine):
    dic_maj = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0,
               "F": 0, "G": 0, "H": 0, "I": 0, "J": 0,
               "K": 0, "L": 0, "M": 0, "N": 0, "O": 0,
               "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0,
               "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0,
               "Z": 0}

    for ele_chaine in chaine:
        if ele_chaine.isupper():
            dic_maj[ele_chaine] += 1

    for ele_key, ele_value in dic_maj.items():
        if ele_value != 0:
            print(f"{ele_key} : {ele_value * '*'} ({ele_value})")


def main():
    decomposotion_chaine(CHAINE)

main()