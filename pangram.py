l = input("Enter string: ")
l = l.lower()
l = l.replace(' ', '')
b = []
for i in l:
    if i.isalpha():
        if i not in b:
            b.append(i)
if len(b) == 26:
    print("Pangram")
else:
    print("Not Pangram")
