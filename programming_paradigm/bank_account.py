class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        self.account_balance += amount
        return True

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False
<<<<<<< HEAD
=======

    def display_balance(self):
           print(f"Current Balance: ${self.account_balance:.2f}")
>>>>>>> 3913ee7bb2026b71deb7b8509a1439b9a9ec729a
