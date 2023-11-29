NOMS = ['Londa','Lenita','Beatrice','Kendrick','Genny','Rolf','Meridith','Hilton','Phylis','Candis','Ron','Lecia','Jacquelyn','Gonzalo','Herlinda','Morgan','Han','Sanjuanita','Allie','Fernande','Anna','Gracia','Lula','Merlyn','Tandy','Adah','Ozella','Laureen','Ricky','Miki']
NB_PLONGEES = [20,120,15,150,5,20,30,60,100,8,20,15,30,79,130,66,24,110,8,23,20,77,60,22,30,80,50,20,10,29]


def nom_plongeur(nom):
    for ele_noms in range(len(NOMS)):
        if NOMS[ele_noms] == nom:
            return print(nom, "a fait", NB_PLONGEES[ele_noms], "plongées")
        else:
            return print("Le nom", nom, "n'est pas dans la liste")


def dico():
    dico = {}
    for nom in range(len(NOMS)):
        dico[NOMS[nom]] = NB_PLONGEES[nom]
    return dico


def meilleur_nom_plongeur():
    dic_plongeur = {'nom': '', 'nb_plongees': 0}
    for i in range(len(NOMS)):
        nom = NOMS[i]
        nb_plongees = NB_PLONGEES[i]
        if nb_plongees > dic_plongeur['nb_plongees']:
            dic_plongeur['nom'] = nom
            dic_plongeur['nb_plongees'] = nb_plongees
    return dic_plongeur


def main():
    nom = input("Nom du plongeur : ")
    nom_plongeur(nom)
    print("\n")
    print("Dicionnaire des plongeurs :")
    print(dico())
    print("\n")
    print("Le meilleur plongeur est :")
    print(meilleur_nom_plongeur())


main()