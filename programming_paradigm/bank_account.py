# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance  # private attribute for encapsulation

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        return f"Current Balance: ${self.__account_balance}"
# Example usage:
if __name__ == "__main__":
    account = BankAccount(100)
    print(account.display_balance())  # Current Balance: $100
    account.deposit(50)
    print(account.display_balance())  # Current Balance: $150
    success = account.withdraw(30)
    print("Withdrawal successful:", success)  # Withdrawal successful: True
    print(account.display_balance())  # Current Balance: $120
    success = account.withdraw(200)
    print("Withdrawal successful:", success)  # Withdrawal successful: False
    print(account.display_balance())  # Current Balance: $120