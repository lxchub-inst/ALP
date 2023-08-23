nb1 = int(input("Entrez un nombre : "))
dv1 = int(input("Entrez un diviseur : "))

while dv1 == 0:
    print("Le diviseur ne peut pas être égal à 0 !")
    dv1 = int(input("Entrez un diviseur : "))
    if dv1 != 0:
        print(f"{nb1} / {dv1} = {nb1 / dv1}")
        break
