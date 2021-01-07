l1 = ['a', 'b', 'c', 'd']
l2 = ['1', '2', '4', '3']


def ov():
    for i in l1:
        if i in l2:
            return True
        else:
            return False


print(ov())
