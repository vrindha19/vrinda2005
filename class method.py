# class method

# The @classmethod decorator is a built-in function decorator that is an expression that gets evaluated after your function is defined. 
# The result of that evaluation shadows your function definition. A class method receives the class as an implicit first argument,
#  just like an instance method receives the instance

# A class method is a method that is bound to the class and not the object of the class.

# They have the access to the state of the class as it takes a class parameter that points to the class and not the object instance.

# It can modify a class state that would apply across all the instances of the class. 
# For example, it can modify a class variable that will be applicable to all the instances.


# class Student:
#     name = 'vrinda' 
#     def __init__(self):
#         self.age = 20  #

#     @classmethod
#     def tostring(cls):
#         print('Student Class Attributes: name=',cls.name)

# Student.tostring()  



# class MyClass:
#     def __init__(self, value):
#         self.value = value
 
#     def get_value(self):
#         return self.value
 
# # Create an instance of MyClass
# obj = MyClass(10)
 
# # Call the get_value method on the instance
# print(obj.get_value()) 

