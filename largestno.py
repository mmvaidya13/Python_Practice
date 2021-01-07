a, b, c = input("Enter 3 no.: ").split()
if a > b and a > c:
    print("%d is grater" % int(a))
elif b > a and b > c:
    print("%d is Greater" % int(b))
elif c > a and c > b:
    print("%d is Greater" % int(c))
elif a == b == c:
    print("All have equal value")
else:
    print("Invalid")
