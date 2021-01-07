roman = input().upper()
li = {'I': 1, 'V': 5, 'X': 10, 'L': 50}
v = 0
for i in range(0, len(roman)):
    if i > 0 and li[roman[i]] > li[roman[i - 1]]:
        v += li[roman[i]] - 2 * li[roman[i - 1]]
    else:
        v += li[roman[i]]
print(v)
