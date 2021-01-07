def prim(a):
    f = False
    for i in range(2, int(a / 2)):
        if a % i == 0:
            f = True
            break
        else:
            f = False

    if f: return True
    return f


print(prim(2))
