stri = input("Enter string: ")
stri = stri.replace(" ", '')
stri = stri.lower()

if stri == stri[::-1]:
    print("Palindrome")
else:
    print("Not Pali")
