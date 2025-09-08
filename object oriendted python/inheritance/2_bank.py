'''class Account():
    def __init__(self, acc_no, owner, balance=0):
        self.acc_no = acc_no
        self.owner = owner
        self.balance = balance
    def deposite(self, value):
        self.balance = self.balance + value
        print(f"Ur balance is {self.balance}")
    def withdraw(self, value):
        self.balance  = self.balance - value
        print(f"Balance remaining = {self.balance}")
    def __str__(self):
        print(self.balance) 
              

class SavingAcc(Account):
    def __init__(self, acc_no, owner, balance):
        super().__init__(acc_no, owner, balance)
    def deposite(self, value):
        super().deposite(value)
    def withdraw(self, value):
        if not ((self.balance - value) <= -5000):
            super().withdraw(value)
        else: print("Ur balance is lower than -5000 ruppees, u cannot withdraw")
    def __str__(self):
        super().__str__()

class CurrentAcc(Account):
    def __init__(self, acc_no, owner, balance):
        super().__init__(acc_no, owner, balance)
    def deposite(self, value):
        super().deposite(value)
    def withdraw(self, value):
        negativeLimit = -5000
        if not (self.balance <= negativeLimit):
            if not (value >= 10000):
                super().withdraw(value)
            else: print("U cannot withdraw more than 10,000 at one time")
        else: print("Ur account has reached maximum negtive limit, u cannot withdraw more")
    def __str__(self):
        super().__str__()

currentAccList = [CurrentAcc(28930, "Arsh", 99002)]
savingAccList = [SavingAcc(28931, "Arsh", 99499)]

def logic():
    while True:
        if name.lower() == i.owner.lower():
            print("")
            method= int(input("1. Deposit \n2. Withdraw \n3. Show balance \n4. Logout\n"))
            if method == 1:
                value = int(input("Enter the deposit amount"))
                i.deposite(value)
            elif method == 2:
                value = int(input("Enter the withdraw amount"))
                i.withdraw(value)
            elif method == 3:
                i.__str__()
            elif method == 4:
                break

while True:
    print("")
    name = input("Enter the name of acc owner")
    accType = int(input("1. Saving acc \n2. Current acc\n"))
    if accType == (1):
        for i in currentAccList:
            logic()
    elif accType == (2):
        for i in savingAccList:
            logic()'''

class Account:
    def __init__(self, acc_no, owner, balance=0):
        self.acc_no = acc_no
        self.owner = owner
        self.balance = balance

    def deposit(self, value):
        self.balance += value
        print(f"Deposit successful. Balance = {self.balance}")

    def withdraw(self, value):
        self.balance -= value
        print(f"Withdrawal successful. Balance = {self.balance}")

    def __str__(self):
        return f"Account No: {self.acc_no} | Owner: {self.owner} | Balance: {self.balance}"


class SavingAcc(Account):
    def withdraw(self, value):
        if self.balance - value >= -5000:
            super().withdraw(value)
        else:
            print("❌ Withdrawal denied: Balance cannot go below -5000.")


class CurrentAcc(Account):
    def withdraw(self, value):
        if self.balance - value < -5000:
            print("❌ Withdrawal denied: Account has reached maximum negative limit (-5000).")
        elif value > 10000:
            print("❌ Withdrawal denied: Cannot withdraw more than 10,000 at once.")
        else:
            super().withdraw(value)


# Accounts
currentAccList = [CurrentAcc(28930, "Arsh", 99002)]
savingAccList = [SavingAcc(28931, "Arsh", 99499)]


def logic(user, account):
    while True:
        if user.lower() == account.owner.lower():
            method = int(input("\n1. Deposit \n2. Withdraw \n3. Show balance \n4. Logout\n"))
            if method == 1:
                value = int(input("Enter the deposit amount: "))
                account.deposit(value)
            elif method == 2:
                value = int(input("Enter the withdraw amount: "))
                account.withdraw(value)
            elif method == 3:
                print(account)
            elif method == 4:
                print("Logging out...")
                break


while True:
    print("")
    name = input("Enter the name of acc owner: ")
    accType = int(input("1. Saving acc \n2. Current acc\n"))

    if accType == 1:
        for acc in savingAccList:
            logic(name, acc)
    elif accType == 2:
        for acc in currentAccList:
            logic(name, acc)
