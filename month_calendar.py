month = input("Enter Month: ")
dim = input("No. of days in Month: ")
dos = input("Day of week(0-6): ")
j = 0 + int(dos)
if 0 <= int(dos) <= 6:
    print("S  M  T  W  T  F  S")
    for i in range(0, int(dos)):
        print(" ", end='  ')
    for i in range(1, int(dim) + 1):
        print(i, end='  ')
        j = j + 1
        if j == 7:
            print("\n", end='')
            j = 0
else:
    print("Invalid value")
