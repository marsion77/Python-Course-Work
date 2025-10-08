# Multiple Inheritance

# One child inherits from multiple parents.


class Bank:
    def __init__(self, balance):
        self.balance = balance
        print(f"Bank balance: {self.balance}")

class Customer:
    def __init__(self, name):
        self.name = name
        print(f"Customer name: {self.name}")

class PremiumAccount(Bank, Customer):
    def __init__(self, name, balance, perks):
        Bank.__init__(self, balance)
        Customer.__init__(self, name)
        self.perks = perks
        print(f"PremiumAccount perks: {self.perks}")

p1 = PremiumAccount("Alice", 10000, ["Free ATM", "Cashback"])
