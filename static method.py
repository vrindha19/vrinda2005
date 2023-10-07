# static method


# class MyClass:
#     def __init__(self, value):
#         self.value = value
 
#     @staticmethod
#     def get_max_value(x, y):
#         return max(x, y)
 
# # Create an instance of MyClass
# obj = MyClass(10)
 
# print(MyClass.get_max_value(20, 30))  
 
# print(obj.get_max_value(20, 30)) 

# A class method takes cls as the first parameter while a static method needs no specific parameters
# In general, static methods know nothing about the class state. They are utility-type methods that take some parameters and work upon those parameters. 
#  the other hand class methods must have class as a parameter.

# Static methods are functions defined in a class that do not have access to the class object or any instance of that class. 
# 's a method that is a member of the class but has no reference to anything in the class.
# A method is made static be adding the @staticmethod decoration. Static methods do not take self or cls as the first parameter. 


