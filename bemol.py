liste_note = ["Do", "Re", "Mi", "Fa", "Sol", "La", "Si"]
liste_altérations = ["fa", "do", "sol", "ré", "la", "mi", "si"]
SAUT_NOTE = 4
TYPE_BEMOL = "b"
TYPE_DIESE = "#"


def recap_notes(type_notes, nb_notes):

    dico_notes = {"do": "C", "ré": "D", "mi": "E", "fa": "F", "sol": "C", "la": "A", "si": "B"}

    for i in range(len(liste_note)):
        gamme_notes = altertaions_gamme(type_notes, nb_notes)
        print("La gamme avec", i+1, type_notes, "est gamme", gamme_notes, "en anglais", dico_notes[gamme_notes])


def diese(nb_notes):
    ele_notes = 0
    note_bemol = ""

    while nb_notes > 0:
        if (ele_notes + SAUT_NOTE) < len(liste_note):
            ele_notes = ele_notes + SAUT_NOTE
        else:
            ele_notes = ele_notes + SAUT_NOTE - len(liste_note)

        note_bemol = liste_note[ele_notes]
        nb_notes = nb_notes - 1
    return note_bemol

def bemol(nb_notes):
    ele_notes = 0
    notes_diese = ""

    while nb_notes > 0:
        if (ele_notes - SAUT_NOTE) >= 0:
            ele_notes = ele_notes - SAUT_NOTE
        else:
            ele_notes = len(liste_note) + ele_notes - SAUT_NOTE

        notes_diese = liste_note[ele_notes]
        nb_notes = nb_notes - 1
    return notes_diese


def altertaions_gamme(type_notes, nb_notes):
    print("Les notes altérées sont : ", end=" ")
    notes_debut = 0
    notes_fin = nb_notes
    notes_etapes = 1

    if type_notes == TYPE_BEMOL:
        notes_debut = len(liste_altérations) - 1
        notes_fin = len(liste_altérations) - nb_notes - 1
        notes_etapes = -1

    for ele_notes in range(notes_debut, notes_fin, notes_etapes):
        print(liste_altérations[ele_notes], end=" ")


def type_alteration(type_note, nb_notes):
    nb_diese = ""
    if type_note == TYPE_DIESE:
        nb_diese = diese(nb_notes)
    else:
        nb_diese = bemol(nb_notes)
    return nb_diese

def main():
    type_notes = input("Type de signe (# ou b) : ")
    nb_notes = int(input("Nombre d'altérations : "))
    gamme_note = type_alteration(type_notes, nb_notes)
    print("Pour les", nb_notes, "altérartions de type", type_notes, ", la gamme de base est",
          gamme_note)
    altertaions_gamme(type_notes, nb_notes)
    print("\n Récpap de #")
    print(recap_notes(type_notes, nb_notes))
    print("\n")
    print("Récap de b")
    print(recap_notes(type_notes, nb_notes))


main()
