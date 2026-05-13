'''CLASS deep diving
(1) ENCAPSULATION
(2) INHERITANCE
(3) POLIMORPHISM
'''

print("==== ENCAPSULATION ====")
'''
C++ JAVA > public private protected
PHP Typescript > public private protected
Python >  public  __private  _protected
'''
# ENCAPSULATION > public  __private  _protected


class Account():
    # state
    desciprtion = "This class makes bank accounts"

    # constructor
    def __init__(self, owner, amount):
        self.__owner = owner
        self.__amount = amount

    # method
    def get_balance(self):
        print(f"The owner {self.__owner} has {self.__amount} usd")

    def deposit(self, amount):
        print("deposit:", amount)
        self.__amount += amount

    def withdraw(self, amount):
        print("withdraw:", amount)
        self.__amount -= amount
        
        
    @property     # property decorator > getter methodni belgilash uchun ishlatiladi
    def holder(self):
        return self.__owner
    
    @holder.setter   # setter decorator > setter methodni belgilash uchun ishlatiladi
    def holder(self, new_owner):
        print("holder.setter:", new_owner)
        self.__owner = new_owner
    
    
    def change_ownership(self, new_owner):
        print("change ownership to:", new_owner)
        self.__owner = new_owner

my_account = Account("JUSTIN", 1000)
my_account.get_balance()


print("----------")

my_account.deposit(3500)
my_account.withdraw(400)
my_account.get_balance()


print("----------")

try:
    result = my_account.__amount
    print("result:", result)
except Exception as err:
    print("No target state found:", err)


# getter va setter methodlari orqali private statega murojaat qilish mumkin
print("owner before:", my_account.holder)  # state 
# my_account.change_ownership("SIMON")
my_account.holder = "SIMON"  # holder.setter stateni call qilish
print("owner after:", my_account.holder)  # state