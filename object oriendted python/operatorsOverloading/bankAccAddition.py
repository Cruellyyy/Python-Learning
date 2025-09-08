class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def __add__(self, otherAcc):
        return BankAccount(self.balance + otherAcc.balance)
    def __str__(self):
        return f"BankAccount(balance={self.balance})"
    
Acc1 = BankAccount(299334)
Acc2 = BankAccount(200432)

print(Acc1 + Acc2)
