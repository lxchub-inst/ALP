"""
Suite à la votation d'hier sur la nouvelle constitution pour Genève, le canton va reverser aux communes le Fonds Réservé pour l'Adoption de la Nouvelle Constitution. Ce FRANC sera réparti en fonction du nombre de votants par commune, et du score réalisé, selon les critères suivants :

les communes reçoivent l'un des montants de base suivants, selon le nombre de votes :
    - toutes les communes recevront au minimum CHF 5'000.-
        - ou alors CHF 8'000.- s'il y a plus de 1000 votants
        - ou alors CHF 12'000.- s'il y a plus de 2000 votants
    - selon le score réalisé, un montant peut être rajouté au montant de base :
        - 2'000.- de plus si le OUI l'a emporté
            - et un montant supplémentaire de CHF 4'000.- est encore versé s'il y a eu plus de 65% de OUI.
"""

def montant_final(nb_oui, nb_non, nb_votants):
    nb_votants = nb_oui + nb_non
    argent = 0
    if((nb_votants) > 1000 and (nb_votants) <= 2000):
            argent += 8000
    elif((nb_votants) > 2000):
            argent += 12000
    else:
        argent += 5000

    if(nb_oui > nb_non):
            argent += 2000 

    if(100*nb_oui/(nb_votants) > 65):
            argent += 4000
    return argent

def main():
    nb_oui = int(input("Nombre de oui : "))
    nb_non = int(input("Nombre de non : "))
    nb_votants = nb_oui + nb_non
    montant_final(nb_oui, nb_non, nb_votants)

    print(f"Le montant pour cette commune ayant {nb_oui} de OUI et {nb_non} de NON sera de : {montant_final(nb_oui, nb_non, nb_votants)} CHF")

if __name__ == "__main__":
    main()