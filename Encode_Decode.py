key = {}
for i in range(97, 123):
    j = i + 13
    if j > 122:
        j = j % 123 + 97
    key[chr(i)] = chr(j)
    j += 1
for i in range(65, 91):
    j = i + 13
    if j > 90:
        j = j % 91 + 65
    key[chr(i)] = chr(j)
    j += 1

en = input("Enter string to Encode: ").replace(" ", '')
for i in en:
    for j in key:
        if i == j:
            print(key.get(j), end='')
print("\n")
de = input("Enter string to Decode: ").replace(" ", '')
for i in de:
    if i.isalpha():
        for j in key:
            if i == j:
                print(key.get(j), end='')
