x = -4
y = -2
if x > 0:
    if y > 0:
        print("I")
    else:
        print("IV")
else:
    if y > 0:
        print("II")
    else:
        print("III")

# Résultat attendu: III


print(5 + 10) # 15
print(3 * 7, (17 - 2) * 8) # 21, 120
print(2 ** 4) # 16
print(37 / 2) # 18.5
print(37 // 3) # 12
print(37 % 3) # 1



x = 5
y = -1
if x > 0 and y > 0:
    print("Quadrant 1")
elif x > 0 and y < 0:
    print("Quadrant 4")
elif y > 0:
    print("Quadrant 2")
else:
    print("Quadrant 3")

# Résultat attendu: Quadrant 4



jour = (input("Entrez un jour de la semaine : "))
heure = int(input("Entrez une heure : "))

if jour == "samedi":
    print("False")
elif jour != "samedi":
    if heure > 12:
        print("True")
    else:
        print("False")




temp = int(input("Entrez la température : "))
if temp <= 0:
    print("Gla gla")
elif temp > 100:
    print("Vapeur")
else:
    print("Liquide")




temp_processeur = int(input("Entrez la température du processeur : "))
type_sys = input("Entrez le type de système : ")
if temp_processeur > 80 or type_sys == "WINDOWS" and type_sys == "vista":
    print("True")
else:
    print("False")


moyenne = float(input("Entrez la moyenne : "))
renvois = int(input("Entrez le nombre de renvois : "))
if not(moyenne < 4 or renvois > 3):
    print("True")
else:
    print("False")