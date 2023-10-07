# overloading

# class human:
#     def sayhello(self,name = None):
#         if name is not None:
#             print('hello'+ name)
#         else:
#             print('hello')
# obj=human()
# obj.sayhello()
# obj.sayhello('sana')

# overriiding

# class parent:
#     def my_method(self):
#         print('calling parent method')
# class chlid(parent):
#     def my_method(self):
#         print('calling chlid method')
# obj=chlid()
# obj.my_method()

    
# class person

# class person:
#     _name=None
#     def __init__(self,name):
#         self._name=name
#     def _displayname(self):
#         print('name:',self.name)
# class student(person):
#     def __init__(self, name):
#             student. __init__(self,name)
# obj=student("vrinda")


#  protected

# class Person:
#    def __init__(self, name, age):
#       self._name = name
#       self._age = age
    
#    def _display(self):
#       print("Name:", self._name)
#       print("Age:", self._age)

# class Student(Person):
#    def __init__(self, name, age, roll_number):
#       super().__init__(name, age)
#       self._roll_number = roll_number
    
#    def display(self):
#       self._display()
#       print("Roll Number:", self._roll_number)

# s = Student("John", 20, 123)
# s.display()

# private

# class BankAccount:
#    def __init__(self, account_number, balance):
#       self.__account_number = account_number
#       self.__balance = balance
    
#    def __display_balance(self):
#       print("Balance:", self.__balance)

# b = BankAccount(1234567890, 5000)
# b.__display_balance()  

        
    


        
