class Bank:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance = amount

    def withdraw(self, amount):
        try:
            if int(self.balance) > 0 and int(self.balance) >= int(amount):
                self.balance = int(self.balance) - int(amount)
            else:
                raise Exception("Zero Balance or Withdraw amount greater then balance")
        except Exception as a:
            print(a)

    def display(self):
        print("Balance: ", self.balance)


b = Bank()
t = 'y'
while t == 'y':
    print("Select operation:\n 1.Deposit\n2.Withdraw\n3.Display\n")
    o = input("Enter option: ")
    if o == '1':
        a = input("Enter deposit amount: ")
        b.deposit(a)
    elif o == '2':
        a = input("Enter deposit amount: ")
        b.withdraw(a)
    elif o == '3':
        b.display()
    else:
        print("Invali option")
    t = input("Do you want to continue(y/n): ")
