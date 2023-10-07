# super function

# class Emp():
#     def __init__(self,id,name,Add):
#         self.id = id
#         self.name=name
#         self.Add=Add
# class freelance(Emp):
#     def __init__(self,id,name,Add,Emails):
#         super().__init__(id,name,Add)
#         self.Emails = Emails
# Emp_1= freelance(156,"vrinda","palakkad","vrindam363@gmail.com")
# print('The ID is:',Emp_1.id)
# print('The name is:',Emp_1.name)
# print('The Address is:',Emp_1.Add)
# print('The Emails is:',Emp_1.Emails)


# supper keyword

# class Rectangle(object):
#     def __init__ (self,length,width):
#         self.length=length
#         self.width=width
#     def area(self):
#         print('iii')
#         return 2 * self.length +2 * self.width
# class square(Rectangle):
#     def __init__(self,length):
#         super(). __init__(length,length)

# s=square(1)
# print(s.area())
        
# class Rectangle(object):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         print("iii")
#         return self.length * self.width

#     def perimeter(self):
#         return 2 * self.length + 2 * self.width

# # Here we declare that the Square class inherits from the Rectangle class
# class Square(Rectangle):
#     def __init__(self, length):
#         super().__init__(length, length)  #onl   
# s = Square(1)

# print(s.area())
    
