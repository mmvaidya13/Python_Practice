s = input("Enter String: ")
t = list()
p = ''
for i in range(len(s)):
    t.append(s[i])
i = 0
for i in range(0, len(s) + 1):
    e = t[i]
    if t[i] == 'a' or t[i] == 'e' or t[i] == 'i' or t[i] == 'o' or t[i] == 'u' or t[i] == 'A' or t[i] == 'E' or t[
        i] == 'I' or t[i] == 'O' or t[i] == 'U':
        continue
    else:
        i += 1
        t.insert(i, 'o')
        i += 1
        t.insert(i, e)
    i = i + 1
    p = str("".join(t))

print(p)
