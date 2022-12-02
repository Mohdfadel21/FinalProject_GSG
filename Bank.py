import Customer
class Bank2:
      __custno= 0
      allcustomer=None
      def __init__(self):
          allcustomer= Customer[7]
          pass

      def get_custno(self):
         return self. __custno







      def add_cust(first_input="m", last_input="l",self=None):
         first_input = input("add your first name")
         last_input = input("add your last name")
         if first_input.isdigit() or first_input.isspace() or last_input.isdigit() or last_input.isspace():
              print("error input")
              exit()
         else:
             allcustomer = Customer[self.__custno]
             allcustomer.insert(self.__custno, first_input, last_input)
             print(allcustomer[0])
             self.__custno += 1
             return allcustomer[self.__custno - 1]


      def getCustomer(self,index):
           return self.allcustomer[index]
