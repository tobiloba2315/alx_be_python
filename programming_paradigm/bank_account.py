class BankAccount:
 def __init__(self, initial_balance=0):
  self.account_balance = initial_balance


def deposit(self, amount):
 self.account_balance += amount


def withdraw(self, amount):
 if amount <= self.account_balance:
  self.account_balance -= amount
 return True
 return False


def display_balance(self):
 print(f"Current Balance: ${self.account_balance:.2f}")

 # main-0.py
# Command-line interface for BankAccount operations

import sys
from bank_account import BankAccount

account = BankAccount()

if len(sys.argv) < 2:
    print("Usage: python main-0.py <operation> [amount]")
    print("Operations: deposit, withdraw, balance")
    sys.exit()

operation = sys.argv[1].lower()

if operation == "deposit":
    if len(sys.argv) != 3:
        print("Usage: python main-0.py deposit <amount>")
        sys.exit()
    try:
        amount = float(sys.argv[2])
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
        account.display_balance()
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")

elif operation == "withdraw":
    if len(sys.argv) != 3:
        print("Usage: python main-0.py withdraw <amount>")
        sys.exit()
    try:
        amount = float(sys.argv[2])
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds!")
        account.display_balance()
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")

elif operation == "balance":
    account.display_balance()

else:
    print("Unknown operation. Use deposit, withdraw, or balance.")
