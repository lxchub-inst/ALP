print('=== Start A ===')
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
if  e < 4:
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
print('=== End A ===')


print('=== Start B ===')
def f(a,b):
    print(a-b)
     
def g(a,b,c):
    if a < 5:
        h(b+5)
    else:
        h(a+2)
    print(c*2)
    f(b,a)
    x = 5

def h(a):
    b = a+2
    print(b)

b=5
x=6
g(4,b,"6")
print(x)
print('=== End B ===')


print('=== Start C ===')
def i(u):
    print('i(', u, ')')
    return k(u+1)
    
def j(v):
    print('j(', v, ')')
    return 5

def k(w):
    print('k(', w, ')')
    v = j(w-1)
    print('v', v)
    return v-1
    
print(i(3) + 2)
print('=== End C ===')


print('=== Start D ===')
def k(x):
    print("k(", x, ")")
    return x*3
    print(x)

def l(y,z):
    print("l(",y,",",z,")")
    y += k(z)
    a = m(y)
    print("a",a)

def m(x):
    print("m(", x, ")")
    if x >= 10:
        return x+5
    elif x >= 15:
        return x+10
    print("x",x)
    return x

x = 5
y = 10
z = 15
y += m(y)
l(z,y)
print('=== End D ===')