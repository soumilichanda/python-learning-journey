class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def display(self):
        print(f"Account Holder : {self.account_holder}")
        print(f"Current Balance: ${self.balance}")


# Example usage:
acc = BankAccount("Munmun", 1000.0)
acc.display()

print("\n--- Transactions ---")
acc.deposit(500)
acc.withdraw(200)

print("\n--- Final Account Status ---")
acc.display()