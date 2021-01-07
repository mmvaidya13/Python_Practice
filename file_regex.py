import re

lis = input("Enter fruit Name: ").split()
i = 0
l = list()
fi = open("fruit.txt", 'r+')
while i < len(lis):
    if not re.findall(r"[\W0-9]", lis[i]):
        # fi.write(lis[i]+" ")
        l.append(lis[i])
    i += 1

l.sort()
for i in l:
    fi.write(i + " ")
fi.seek(0)
print(fi.read())
fi.close()
