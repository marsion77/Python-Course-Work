
from marks import BankAccount

acc = BankAccount("Alice", 1000)

acc.deposit(500)
acc.withdraw(300)
print("Current balance:", acc.balance())
acc.withdraw(1500)
