NOTES = [3, 6, 5.5, 4.5, 2.5, 4, 5, 4, 3, 4, 2.5, 4.5, 5, 5, 4, 3]


def moyenne_notes(NOTES):
    moyenne = 0
    somme = 0
    for i in range(len(NOTES)):
        somme += NOTES[i]
        moyenne = somme / len(NOTES)
    return moyenne


def notes_inferieurs(NOTES):
    nombre_notes = 0
    for i in range(len(NOTES)):
        if NOTES[i] < 4:
            nombre_notes += 1
    return nombre_notes


def notes_la_plus_meilleur(NOTES):
    nombre_notes = 0
    for i in range(len(NOTES)):
        if NOTES[i] > NOTES[i - 1]:
            nombre_notes += 1
    return nombre_notes


def indice_position_meilleure_notes(NOTES):
    meilleure_note = NOTES[0]
    indice = 0

    for i in range(1, len(NOTES)):
        if NOTES[i] > meilleure_note:
            meilleure_note = NOTES[i]
            indice = i

    return indice


# Deuxipme méthode
def indice_position_meilleurs_notes(NOTES):
    meilleure_note = NOTES[0]  # Supposons que la première note est la meilleure initialement
    indice = 0  # L'indice initial de la meilleure note est 0

    for i in range(len(NOTES)):
        if NOTES[i] > meilleure_note:
            meilleure_note = NOTES[i]
            indice = i
        elif NOTES[i] == meilleure_note:
            # Si une note égale est trouvée, on conserve le premier indice trouvé
            indice = NOTES.index(meilleure_note, indice)

    return indice


def main():
    print("La moyenne est de :", moyenne_notes(NOTES))
    print("Le nombre de notes inférieurs à 4 est de :", notes_inferieurs(NOTES))
    print("La meilleure note c'est :", notes_la_plus_meilleur(NOTES))
    print("L'indice de la meilleure note c'est:", indice_position_meilleurs_notes(NOTES))
    print("L'indice de la meilleure note c'est:", indice_position_meilleure_notes(NOTES))


if __name__ == "__main__":
    main()