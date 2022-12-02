from  Bank import Bank2
import Customer
from main import Account

Bank_obj =  Bank2()
moh = (Customer)
moh=Bank_obj.add_cust("Mohammed", "fadel")
moh.set_account( Account (500))
moh.get_account().withdraw(150)
moh.get_account().deposit(1000)
moh.get_account().withdraw(47.62)
moh.get_account().withdraw(400)
moh.get_account().GetBalance()
print("Customer " , moh.cast_name() , " has a balance of " , moh.get_account().get_account())


Ahmed = (Customer)
Ahmed=Bank_obj.add_cust("Mohammed", "fadel")
Ahmed.set_account( Account (500))
Ahmed.get_account().withdraw(150)
Ahmed.get_account().deposit(1000)
Ahmed.get_account().withdraw(47.62)
Ahmed.get_account().withdraw(400)
Ahmed.get_account().GetBalance()
print("Customer " , Ahmed.cast_name() , " has a balance of " , Ahmed.get_account().get_account())




#____________________________

tim = (Customer)
Bank_obj.add_cust("Tim", "Soley")
tim.SetAccount( Account(10055))
maria = (Customer)
maria.Bank_obj.addCustomer("Maria", "Soley")
maria.SetAccount(tim.GetAccount());
print("Maria shares her account with her husbond")

tim.set_account( Account (10055))
tim.get_account().withdraw(1054)
tim.get_account().deposit(200)
tim.get_account().withdraw(42.62)
tim.get_account().withdraw(150)
print("Customer " , tim.cast_name() , " has a balance of " , tim.get_account().get_account())

maria.set_account( Account (10055))
maria.get_account().withdraw(1054)
maria.get_account().deposit(200)
maria.get_account().withdraw(42.62)
maria.get_account().withdraw(150)
print("Customer " , maria.cast_name() , " has a balance of " , maria.get_account().get_account())
print("Customer " , tim.cast_name() , " has a balance of " , tim.get_account().get_account())