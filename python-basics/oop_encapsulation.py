# Object Oriented Programming
## Access Modifiers
### 1. public - accessible within and outside the class (attributes & methods)
### 2. Private  - accessible only inside the class
### 3. Protected - accesssible only class and its subclass
# 1. Encapsulation - wrapping the data (attributes & methods) called
# 2. Abstraction
# 3. Inheritance
# 4. Polymorphism
class BankAccount:
    def __init__(self,name,savingbalance,spendingbalance):
        self.name=name # public attribute
        self._savingbalance=savingbalance # protected attribute -> this is for developer so that he/she can understand that it is protected but it can be accesible outside the class because python enforce this but not apply mondary that protected attribute can't be access from the outside the class
        self.__spendingbalance=spendingbalance # private attribute -> this can't be accessible from outside the class (data mangling)


    def get_spending_balance(self):
        return self.__spendingbalance

    def add_spending_balance(self,new_balance):
        self.__spendingbalance+=new_balance
        return self.__spendingbalance
u1=BankAccount('ashrith',7000,300)
print(u1.name,u1._savingbalance,u1.get_spending_balance(),u1.add_spending_balance(3000),u1._BankAccount__spendingbalance) # this is accessible because it is protected attribute
# to access any private access u1._BankAccount__spendingbalance
