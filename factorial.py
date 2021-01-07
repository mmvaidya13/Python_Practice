def fac(a):
    t = 1
    for i in range(1, a + 1):
        t = t * i
    return t


for i in range(1, 20 + 1):
    print(i, fac(i))
