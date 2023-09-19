"""" 
Nom : AGOSTA LOIC
Version : 1.0
"""

def a(x, y):
    print('a(', x, ',', y, ')')
    y = x + 1
    print("y", y)
    b(x, y)
    print("x", x)
    print("y", y)

def b(x, y):
    print('b')
    print("y", y)
    print("x", x)
    x += 1
    print("x", x)

x = 10
y = -1
a(x, 5)
print("x", x)
print("y", y)

""" 
Partie A

# Stock a(10, 5)
a, 10, 5
# Stock y = 10 + 11
y, 11
# Stock b(10, 11)
b 
y, 11
x, 10
# Stock x += 1 = 11
x, 11

x, 10
y, -1
"""

def b(a):
    print('b(', a, ')')
    return a + a

def z(a):
    print('z(', a, ')')
    return a - 10

def a(c, d):
    print('a(', c, ',', d, ')')
    x = 0
    if c < d:
        x = b(c)
    elif c > d:
        x = b(d)
    else:
        x = z(c)
    print(x)
    return x

x = 10
x += a(x, 6)
y = a(x, x)
print("x", x)
print("y", y)

""" 
Partie B
# Stock x = 10
a, 10, 6
b, 6 # Stock 12 en attente
12 # Stock 12 en attente

# x += a(x, 6)
# -> 10 + 12 = 22
x, 22

a, 22, 22
z, 22 # Stock 12 en attente
12 # Stock 12 en attente

# y = 12
y, 12
"""