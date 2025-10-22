from abc import ABC, abstractmethod


# Abstract Class
class ATM(ABC):
    @abstractmethod
    def enter_pin(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass

class SBI(ATM):
    # @property
    def enter_pin(self):
        print("PIN Entered Successfully")
    
    # @property
    def withdraw(self):
        print("Withdrawn Successfully")


a = SBI()
a.enter_pin()
a.withdraw()
