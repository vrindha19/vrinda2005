# 1 Write a program to find the transpose of a matrix.

# X = [[12,7],
#     [4 ,5],
#     [3 ,8]]

# result = [[0,0,0],
#          [0,0,0]]


# for i in range(len(X)):
   
#    for j in range(len(X[0])):
#        result[j][i] = X[i][j]

# for r in result:
#    print(r)


# 2. Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

# x = "SPECTRUM SOFTWARE SOLUTION"
# capitalized_string = x.capitalize()
# print(capitalized_string)

# 3. Write a program to implement all built-in methods of list.

# Method 	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

# 4. Write a program to read dictionary values through keyboard and merge two dictionaries.

# dict1 = {'a': 10, 'b': 8}
# dict2 = {'d': 6, 'c': 4}
# dict3 =  (dict1, dict2)
# print(dict3)

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# z = (x, y)
# print(x,y,z)

# 5 Write a program to demonstrate all built-in methods of dictionary.

# Method 	Description

# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary

# 6  Write a program to find the sum of all the elements in a list.

# Table of Contents

#     Summing a list in Python
#     Using sum() function
#     TypeError
#     sum list elements using for loop
#     Using while () loop
#     Using Recursion
#     Sum numbers only in a list with various data types
#     Sum List Ignore Nan
#     Sum List Ignore None
#     Sum List Elements that meet a Condition
#     Sum List Slice
#     Sum List of Tuples Element-Wise
#     Sum List of Lists

# total = 1
# list1 = [11, 5, 17, 18, 23]
# for ele in range(1, len(list1)):
#     total = total + list1[ele]
# print("Sum of all elements in given list: ", total)

# 7. With a given integral number n, write a program to generate a dictionary that contains(i,i*i) such that i is an integral number between 1 and n. And then the program should print the dictionary.

# number = int(input("Type a number: "))

# numberDict = {}
# for i in range(1, number+1):
#     numberDict[i] = i*i

# print(numberDict)

# n=int(input("Input a number "))
# y= dict()

# for i in range(1,n+1):
#     y[i]=i*i

# print(y) 

# 8. Write a program that accepts a sentence and calculate the number of letters & digits

# str = input("Input a string: ")

# d=l=0

# for c in str:

#     if c.isdigit():

#         d=d+1

#     elif c.isalpha():

#         l=l+1

#     else:

#         pass

# print("Letters", l)

# print("Digits", d)


# 9.Write a program to implement filter(), map() and reduce() .

# def add(x):  
#     return x + 1  
  
  
# def multiply(x):  
#     return x * 2  
  

# def apply(func, x):  
#     return func(x)  

# result1 = apply(add, 3)  # 
# result2 = apply(multiply,3)# 
# print(result1,result2)

# map

# def myfunc(n):
#   return len(n)

# x = map(myfunc, ('apple', 'banana', 'cherry')) 
# print(x)

# filter

# ages = [5, 12, 17, 18, 24, 32]

# def myFunc(x):
#   if x < 12:
#     return False
#   else:
#     return True

# my_def = filter(myFunc, ages)

# for x in my_def:
#   print(x) 

# reduce 

# The reduce()  is a really useful function for performing some computation on a list and
# returning the result. It applies a rolling computation to sequential pairs of values in a list.
# The reduce()  will transform a given list into a single value by applying a given function continuously to all elements. 
# It basically keeps operating on pairs of elements until there are no more elements left.

# 10. Write a program to implement List Comprehension .

# numbers = [1, 2, 3, 4, 5]
# squared = [x ** 2 for x in numbers]
# print(squared)


# 11. Write a program to implement Dictionary Comprehension ..

# x={'vrinda':18,'midhun':24,'mrudhula':20,'manoop':17}
# print(x)

# 12. Write a program to find the largest and smallest element from a list.

# The min() and max() are built-in functions of Python programming language to find the smallest and the largest elements in any iterable.
#  These functions come in handy when working with any iterables like lists, tuples, sets, and dictionaries in Python.


    # / C program to find the smallest and largest element in an array. ​
    # int main() {
    # printf(“\nEnter the number of elements : “); scanf(“%d”,&n);
    # printf(“\nInput the array elements : “); ...
    # scanf(“%d”,&a[i]); ...
    # large=small=a[0]; ...
    # for(i=1;i<n;++i) ...
    # large=a[i];
# x=('smal')
# larg = l[0] 

# for num in l:
#     if num > larg:
#         larg = num
#     if num < small:
#         smallest = num

# print("Largest:", larg)
# print("Smallest:", smal

l=eval(input("Enter a list of numbers"))
# [4,7,9,10,45,21,46,67,23] --- input
print("min=",min(l))
print("max=",max(l))













# 13. Write a Python program to print the numbers of a specified list after removing even numbers from it. 















# 14. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30

















# 15. Write a Python program to insert a given string at the beginning of all items in a list. 















# 16.  Write a Python program to iterate over two lists simultaneously

















