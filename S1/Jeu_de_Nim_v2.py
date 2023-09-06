# Importation des modules
import random
import numpy as np

# Définition des constantes
ALLU_DEPART_MAX = 16
ALLU_DEPART_MIN = 4

# Définition des fonctions

def affichage_allumettes():
    allu_depart = random.choice([ALLU_DEPART_MIN, ALLU_DEPART_MAX])
    print("Bienvenue sur le Jeu de Nim !")
    print("Le but du jeu est de prendre la dernière allumette.")
    print("Pour cela, vous devez prendre entre 1 et 3 allumettes à chaque tour.")
    print("Le joueur qui prend la dernière allumette a perdu.")
    print("Bonne chance !")
    print("\n")
    print(f"Le nombre d'allumettes de départ est {allu_depart}.")
    return allu_depart


def blabla():
    pass

def choix_joueurs():
    nom_joueurs = ["Joueur", "Ordinateur"]
    depart_joueurs = random.choice(nom_joueurs)
    allu_depart = affichage_allumettes()
    allu_total = allu_depart

    while allu_total != 0:
        if depart_joueurs == nom_joueurs[0]:
            allu_joueur1 = 0
            while allu_joueur1 < 1 or allu_joueur1 > min(3, allu_total):
                allu_joueur1 = int(input("Joueur 1 : Combien d'allumettes voulez-vous prendre (entre 1 et 3) ? "))
                    
                if allu_joueur1 < 1 or allu_joueur1 > min(3, allu_total):
                        print(f"Vous ne pouvez prendre que 1, 2 ou 3 allumettes (maximum {min(3, allu_total)}) !") 
                        """ 
                        Si le joueur entre un nombre d'allumettes incorrect, on lui affiche un message d'erreur et on lui redemande de saisir un nombre d'allumettes
                        """

            allu_total -= allu_joueur1 # On retire le nombre d'allumettes que le joueur a pris au nombre d'allumettes restantes
                # affichage_allumettes(allu_total)
            print(f"Joueur 1 : A pris {allu_joueur1} allumettes")

        elif depart_joueurs == nom_joueurs[1]:
            allu_ordi = random.randint(1, min(3, allu_total)) # L'ordinateur prend un nombre d'allumettes aléatoire entre 1 et 3 (ou le nombre d'allumettes restantes si il en reste moins de 3)
            allu_total -= allu_ordi
            print(f"Ordinateur 1 : A pris {allu_ordi} allumettes")
        
        print(f"Il reste {allu_total} allumettes.")
        depart_joueurs = changement_joueurs(depart_joueurs, nom_joueurs)
    gagnant_jeu(depart_joueurs, nom_joueurs)
    
def changement_joueurs(depart_joueurs, nom_joueurs):
    return nom_joueurs[1] if depart_joueurs == nom_joueurs[0] else nom_joueurs[0]

def gagnant_jeu(depart_joueurs, nom_joueurs):
    if depart_joueurs == nom_joueurs[0]:
        print("Vous avez gagné !")
    else:
        print("L'ordinateur a gagné !")

def main():
    choix_joueurs()

if __name__ == '__main__':
    main()