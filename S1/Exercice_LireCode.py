# def z(z):
#     print("z(z)")
#     print("z", z)
#     y(z*2)
#     print("z", z)


# def y(z):
#     print("y(z)")
#     print("z", z)
#     z -= 1
#     print("z", z)


# print("=== A ===")
# z(4)


# def x(y):
#     print("x(y)")
#     print("y", y)
#     return y+1


# def y(z):
#     print("y(z)")
#     print("z", z)
#     z *= x(z)  # z = z * x(z)
#     print("z", z)


# print("=== B ===")
# z = 2
# y(z)
# print("main")


# def a(x):
#     print('a(', x, ')')
#     return x*x


# def b(x, y):
#     print('b(', x, ',', y, ')')
#     print(a(x*y))
#     print(a(y))


# def c(x, y):
#     print('c(', x, ',', y, ')')
#     b(y+2, x)


# print("=== C ===")
# c(2, 2)

def f3(n):
    print("f3")
    print("n", n)
    if n < 10:
        n += 2
    else:
        n += 1
    return n

def f2(a):
    print("f2")
    print("a", a)
    if a % 2 == 0:
        a += f3(a)
        print("a", a)
    if a >= 5:
        a = f3(a)
        print("a", a)

def f1(hello):
    print("f1")
    a = 3
    if hello < 2*a:
        f2(hello-a)
    else:
        f2(a-hello)
print("=== D ===")
f1(5)