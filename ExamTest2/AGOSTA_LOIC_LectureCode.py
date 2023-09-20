"""" 
Nom : AGOSTA LOIC
Version : 1.0
"""

def t():
    c()
    print("Do")
    c()

def q():
    print("Ré")

def c():
    q()
    print("Mi")

print("Fa")
d = True
e = 4
if e < 4:
    print("Sol")
    t()
else:
    e -= 1
    if d == False or e <= 3:
        print("La")
        c()
    elif d == True and e >= 3:
        t()
    else:
        q()
    print("Si")

""" 
Partie A

Fa
La
Ré
Mi
Si
"""

def f(a, b):
    print(a-b)

def g(a, b, c):
    if a < 5:
        h(b + 5)
    else:
        h(a + 2)
    print(c * 2)
    f(b, a)
    x = 5

def h(a):
    b = a + 2
    print(b)

b = 5
x = 6
g(4, b, 6)
print(x)

"""
Partie B
# Stockage des valeurs
# g(4, 5, 6)
# Maj h(b + 5) = h(10)
# b = 10 + 2
12
# print(6 * 2)
12
# f(5, 4)
1
# x = 6
6
"""

def i(u):
    print('i(', u, ')')
    return k(u + 1)

def j(v):
    print('j(', v, ')')
    return 5

def k(w):
    print('k(', w, ')')
    v = j(w - 1)
    print('v', v)
    return v - 1

print(i(3) + 2)

"""
Partie C

# Stockage des valeurs
# i(3) = i(u)
i, 3 # Stockage de k(4) = k(w)
k, 4 # Stockage de j(3) = j(w - 1)
j, 3 # Stockage de 5
# v = 5
v, 5 # Stockage de v - 1 = 4
# Stockage de 4 + 2 = 6
6
"""