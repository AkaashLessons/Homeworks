from errors import NegativeInputError, NegativeBalanceError
class BankAccount:
    def __init__(self,owner,bank_name,balance):
        self.owner = owner
        self.bank_name = bank_name
        self.balance = balance
        
    def deposit(self):
        money = float(input("please deposit the amount of money you would like: "))
        if money < 0:
            raise NegativeInputError
        else:
            self.balance = self.balance + money
            print("this is your new balance %d" %self.balance)
            
    def withdraw(self):
        money = float(input("please withdraw yout money: "))
        if money < 0:
            raise NegativeInputError
        elif money > self.balance:
            raise NegativeBalanceError
        else:
            self.balance = self.balance - money
            print("this is your new balance %d" %self.balance)
