class my_account:
    def __init__(self,name,account_number,password):
        self.name = name
        self.account_number = account_number
        self.__password = password


     # Getter
    def getpassword(self):
        return self.__password
    
    def setpassword(self):
        return self.__password


account = my_account("Abhi",123,"python")

print(account.name)
print(account.account_number)
print(account.getpassword())


