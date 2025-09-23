

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount
        print(f"{amount} deposited. New balance: {self._balance}")

    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient funds!")
        else:
            self._balance -= amount
            print(f"{amount} withdrawn. New balance: {self._balance}")

    def balance(self):
        return self._balance
