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
# Command Line Interaction Script for BankAccount

import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Starting with an initial balance of $100

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw or balance")
        sys.exit(1)

    # Parse command and optional amount
    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: $67.0")

    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: $50.0")
        else:
            print("Insufficient funds.")

    elif command == "balance":
        account.display_balance()

    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
