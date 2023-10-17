def ma_liste(val_min, val_max):
    liste_nombre = [55, 43, 122]
    nombre_element = 0
    for i in range(len(liste_nombre)):
        if val_min < liste_nombre[i] < val_max:
            nombre_element += 1
    return nombre_element


def main():
    print(ma_liste(-3, 1))


if __name__ == "__main__":
    main()
