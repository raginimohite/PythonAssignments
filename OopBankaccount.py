class BankAccount:

    ROI = 10.5

    def __init__(self,Name,Amount):
        self.name = Name
        self.amount = Amount

    def Display(self):
        print("Account holder name:",self.name)
        print("Current balance:",self.amount)

    def Deposite(self,money):
        self.amount = self.amount+money
        print("Amount deposite:",money)
        print("updated balance:",self.amount)

    def Withdraw(self,money):
        if money <= self.amount:
            self.amount = self.amount - money
            print("Amount withdraw:",money)
            print("Remaining balance:",self.amount)
        else:
            print("Insufficient balance")

    def CalculateInterest(self):
        Interest = (self.amount * BankAccount.ROI)/100
        return Interest
    
obj1 = BankAccount("Amar:",50000)

obj1.Display()
obj1.Deposite(10000)
obj1.Withdraw(15000)
print("Interest = ",obj1.CalculateInterest())

