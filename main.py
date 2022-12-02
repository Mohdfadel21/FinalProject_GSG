

class Account:
    __balance=None

    def setBalance (self, balance):
        self.__balance=balance

    def GetBalance (self):
        return self.__balance



    def __init__(self, initBalance):
        self.__balance=initBalance
        print("Creating Account\n" , "Account Balance : " , self.__balance)
        print("")

    def deposit(self, amount):
        self.__balance += amount
        print("deposit : " , amount , ": True")

    def withdraw (self, amount ):

        if amount <= self.__balance:
            self.__balance -= amount
            print("withdraw : " , amount , ": True")

        else :
            print("withdraw : " , amount , ": False")