class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self):
        cash = float(input("Money to be deposited: "))
        self.balance += cash

    def withdraw(self):
        amount = float(input("Money to be withdrawn: "))
        if self.balance >= amount:
            self.balance = self.balance - amount
            print("You withdrew ", amount)
        else:
            print("\n Insufficient balance  ")


name = input()
money = float(input())
b = BankAccount(name, money)
b.deposit()
b.withdraw()