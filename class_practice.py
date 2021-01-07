class Parent:
    def __init__(self, name, add):
        self.name = name
        self.address = add

    def cal(self, n):
        print("Organiston: :", int(n) / 10)


class Child(Parent):
    def __init__(self, name, add, pno):
        super(Child, self).__init__(name, add)
        self.name = name
        self.address = add
        self.no = pno

    def cal(self, n):
        super(Child, self).cal(n)
        print("Employee: ", int(n) / 5)


c = Child("cds", "bsada", 9845156820)
print(c.name, c.address, c.no)
c.cal(100)
