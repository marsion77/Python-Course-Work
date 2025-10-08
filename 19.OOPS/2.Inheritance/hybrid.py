# Hybrid Inheritance

# A combination of multiple types (multiple + multilevel).


class Bank:
    def __init__(self):
        print("Bank created")

class Customer(Bank):
    def __init__(self):
        super().__init__()
        print("Customer created")

class SavingsAccount(Customer):
    def __init__(self):
        super().__init__()
        print("SavingsAccount created")

class PremiumSavings(SavingsAccount, Bank):
    def __init__(self):
        super().__init__()
        print("PremiumSavings created")

p = PremiumSavings()
