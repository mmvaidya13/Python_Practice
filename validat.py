import re

usr = input("Enter Username: ")
pas = input("Enter Password: ")
print()
if re.findall(r"\W", pas) == [] and re.findall(r"[\W0-9]", usr) == []:
    print("Done")
else:
    print("Enter valid string")
