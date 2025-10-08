# Multilevel Inheritance

# A child inherits from a parent, which itself inherits from a grandparent.


class Bank:
    def __init__(self):
        print("Bank created")

class SavingsBank(Bank):
    def __init__(self):
        super().__init__()
        print("SavingsBank created")

class PremiumSavings(SavingsBank):
    def __init__(self):
        super().__init__()
        print("PremiumSavings created")

p = PremiumSavings()
