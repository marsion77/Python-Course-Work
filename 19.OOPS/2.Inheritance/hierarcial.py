# Hierarchical Inheritance

# Multiple children inherit from the same parent.

class Bank:
    def __init__(self):
        print("Bank created")

class SavingsBank(Bank):
    def __init__(self):
        super().__init__()
        print("SavingsBank created")

class CurrentBank(Bank):
    def __init__(self):
        super().__init__()
        print("CurrentBank created")

s = SavingsBank()
c = CurrentBank()
