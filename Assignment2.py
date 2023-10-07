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

# l=eval(input("Enter a list of numbers"))
# [4,7,9,10,45,21,46,67,23] --- input
# print("min=",min(l))
# print("max=",max(l))


# 13. Write a Python program to print the numbers of a specified list after removing even numbers from it. 


# list = [11, 22, 33, 44, 55]
# # print("specified list:")
# print(list)
# for i in list:
#     if i % 2 == 0:
#         list.remove(i)
# print("List after removing EVEN numbers:")
# print(list)



# 14. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30


# def printValues():
# 	l = list()
# 	for i in range(1,30):
# 		l.append(i**2)
# 	print(l[:5])
# 	print(l[-5:])
	
# printValues()




# 15. Write a Python program to insert a given string at the beginning of all items in a list. 


# def mylist(list, str):
 
#     str += '{0}'
#     list = [str.format(i) for i in list]
#     return(list)
 
 
# list = [1, 2, 3, 4]
# str = 'apple'
# print(mylist(list, str))




# 16.  Write a Python program to iterate over two lists simultaneously

# Iterating over single lists, refers to using for loops for iteration over a single element of a single list at a particular step whereas in iterating over multiple lists simultaneously,
#  we refer using for loops for iteration over a single element of multiple lists at a particular step. 


# import itertools
 
# num = [1, 2, 3]
# color = ['red', 'while', 'black']
# value = [255, 256]
# for (a, b, c) in zip(num, color, value):
#      print (a, b, c)


# 17  . Write a Python program to add a key to a dictionary.


 # dict = {'name': 'vrinda', 'place': 'palakkad'}
# print("keys to the dictionary:")
 
# print (dict)


#  18. Write a Python script to concatenate following dictionaries to create a new one.


# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic4 = {}
# for d in (dic1, dic2, dic3): dic4.update(d)
# # print(dic4)


# 19. Write a Python program to iterate over dictionaries using for loops.

# You can loop through a dictionary by using a for loop.
# When looping through a dictionary, the return value are the keys of the dictionary,
# but there are methods to return the values as well.

# dict_1 = {'ID':123,'NAME':'sana','PLACE':'kochi','AGE':19}

# for key, value in dict_1.items():
#     print(key, value)



#  20.  Write a Python program to sum all the items in a dictionary.


# def Sum(myDict):
 
#     list = []
#     for i in myDict:
#         list.append(myDict[i])
#     final = sum(list)
 #     return final
 
# dict = {'a': 100, 'b': 200, 'c': 300}
# print("Sum :", Sum(dict))


# 21.   Create a dictionary to hold information about pets. Each key is an animal's name, and each value is the kind of animal.Eg : {'Dog':'Willie'}

    # Put at least 3 key-value pairs in your dictionary.
    # Use a for loop to print out a series of statements such as "Willie is a dog."

# 1. Create a dictionary named pets to hold information about pets. Each key is
      # an animal’s name, and each value is the type of animal.
# 2. Put at least 5 key-value pairs in your dictionary.
# 3. Use a for loop to go through the dictionary.
#        a. Print out a series of statements such as:
#             Willie is dog
 # 4. Change one of the values in your dictionary.
#               a. Print out your dictionary with the change.
# 5. Add a new key-value pair to your dictionary.
# a. Print out your dictionary with the new key-value pair added.
# 6. Remove one of the key-value pairs from your dictionary.
#          a. Print out your dictionary to show the change.
# 7. Print out the dictionary’s keys.
# 8. Print out the dictionary’s values


# 22.  Write a python function to create and return a new dictionary from the given dictionary (subject: mark).

# Create a new dictionary with subject having marks more than 50.

# marks = {English: 40,'Maths': 60, 'Hindi: 30,'Chemistry': 46,'Physics': 70}

# mylist={'ENGLISH':40,'MATHS':60,'HINDI':30,'CHEMISTRY':46,'PHYSICS':70}

# for i in range(1):
#     print('marks','subject')

#     print(mylist)
# def markdict(orginal_dict):
#     passed_subject={}
#     for subject,mark in orginal_dict.items():
# if mark>50:
#             passed_subject[subject]=mark
#     return passedsubject
# sample_dict={"English":40,"maths":60,"Hindi":30,"Chemistry":46,"Physics":70}
# passed_subject_dict=ma_rkdict(sample_dict)
# print(passed_subject_dict


# 23.  Write a python function which accepts a sentence and finds the number of letters and digits in the sentence.

# It should return a dictionary in which the key should be letter count and value should be digit count.
# Ignore the spaces or any other special character in the sentence

# s = input("Input a string")
# d=l=0
# for c in s:
#     if c.isdigit():
#         d=d+1
#     elif c.isalpha():
#         l=l+1
#     else:
#         pass

# print("Letters", l)
# print("Digits", d)

# str_1=input("input a string")
# d=a=0
# for i istn r_1:
#     if i.isdigit():
#         d=d+1
#     elif i.isalpha():
#         a=a+1
#     else:
#         pass
# print("letters",a)
# print("digital",d)


# 24 . Write a Python function which generates and retrnus a dictionary where the keys are numbers between 1 and n (both inclusive) and the values are square of keys.


# d=dict()
# n=43
# for i in range(1,n+1):
#     d[i]=i**2
# print(d)









