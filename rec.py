s = 10


def a(s):
    if s == 1:
        return 1
    else:
        s = s + a(s - 1)
        return s


print(a(s))
