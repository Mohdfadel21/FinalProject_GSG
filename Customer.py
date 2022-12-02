from main import Account



__firstname=None
__lastname=None
__account=Account (500)
def __init__(self, first,last):
        self.__firstname=first
        self.__lastname = last
        print("Creating the customer " , first , " " , last)


def set_Firstname(self, firstname):
        self.__firstname = firstname

def get_Firstname (self):
        return self.__firstname

def set_lastname(self, lastname):
        self.__lastname = lastname

def get_lastname(self):
        return self.__lastname

def set_account(self, account):

         self.__account = account


def get_account(self):
        return self.__account



def cast_name (self):
        return "[",self.__lastname,",", self.__firstname,"]"



