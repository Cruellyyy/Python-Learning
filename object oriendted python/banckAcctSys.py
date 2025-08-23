class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def show_balance(self):
        print(f"Balance of the account \"{self.owner}\" is {self.balance}")
    def deposite(self, amount):
        self.balance = self.balance + amount
        print(f"Balance in the account \"{self.owner}\" is {self.balance}")     
    def withdraw(self, amount):
         self.balance = self.balance - amount
         print(f"{amount} has been withdrawen. Balance in the account \"{self.owner}\" is {self.balance}")  

AccountDetails = [BankAccount("Arsh Khan", 5000),
                    BankAccount("Prince Nagda", 6000),
                    BankAccount("Anvesh Bhatta", 7000),
                    BankAccount("Aniket Patidar", 8000), 
                    BankAccount("Anshul Bhoshi", -8000)
                    ]

owner_name = input("Enter the name of the account owner ")

account_found = False
for BanckAccount in AccountDetails:
    if (BanckAccount.owner.lower() == owner_name.lower()):
        account_found = True
        print("\n1. Show Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        choice = int(input("Enter your choice (1-3): "))
        
        if (choice == 1):
            BanckAccount.show_balance()
        elif (choice == 2):
            amount = int(input("Enter the amount u waana deposite "))
            BankAccount.deposite(amount)
        elif (choice == 3):
            amount = int(input("Enter the amount u wanna withdraw "))
            BankAccount.withdraw(amount)
        else:
            print("invalid choice")
            break