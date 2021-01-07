hist = input("Enter list separated by SPACE: ").split()
for i in hist:
    for j in range(0, int(i)):
        print("*", end='')
    print("\n", end='')
