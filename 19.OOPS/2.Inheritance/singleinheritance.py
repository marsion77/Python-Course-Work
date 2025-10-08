# Inheritance is a mechanism in object-oriented programming where one class can derive properties and behaviors (methods and attributes) from another class.
# It allows code reuse, makes programs modular, and reduces redundancy.
# Single Inheritance:   One child inherits from one parent.

# Parent class
class Bank:
    def __init__(self, balance):
        self.balance = balance
        print(f"Bank initialized with balance: {self.balance}")

# Child class
class SavingsAccount(Bank):
    def __init__(self, balance, interest_rate):
        super().__init__(balance)  # call parent constructor
        self.interest_rate = interest_rate
        print(f"SavingsAccount initialized with interest rate: {self.interest_rate}")

# Create object
s1 = SavingsAccount(7000, 5)
