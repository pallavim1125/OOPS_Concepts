class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance!")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")


# Child Class 1
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"Interest Added: {interest}")


# Child Class 2
class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance, overdraft_limit):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw_with_overdraft(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrawn with overdraft: {amount}")
        else:
            print("Overdraft limit exceeded!")
# Savings Account Object
sa = SavingsAccount("Pallavi", 10000, 5)
sa.display_balance()
sa.deposit(2000)
sa.add_interest()
sa.withdraw(3000)
sa.display_balance()

print("---------------------")

# Current Account Object
ca = CurrentAccount("Riya", 5000, 2000)
ca.display_balance()
ca.withdraw_with_overdraft(6000)
ca.display_balance()
ca.withdraw_with_overdraft(3000)
