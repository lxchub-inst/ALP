def echanger(a, b):
    c = a
    a = b
    b = c
    return a, b


a = 5
b = 10

print("a =", a)
print("b =", b)

a, b = echanger(a, b)

print("a =", a)
print("b =", b)