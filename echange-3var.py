def echanger(a, b, c):
    d = b
    b = a
    a = c
    c = d
    return a, b, c


a = 5
b = 10
c = 15

print("a =", a)
print("b =", b)
print("c =", c)

a, b, c = echanger(a, b, c)

print("a =", a)
print("b =", b)
print("c =", c)
