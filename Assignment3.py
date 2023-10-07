# 1. Write a program to define a function that can accept an integer number as    input and print the "It is an even number" if the number is even, otherwise print "It is odd".

# num=int(input("Enter a number:"))
# mod=num%2
# if mod >0:
#     print("This is an odd number.")
# else:
#     print("This is an even number.")


# 2. Write a program to define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.

# dic={}

# for i in range(1,21):
#     dic[i] = i**2

# print(dic)


# 3. Write a program to take a string as input and return a string with vowels removed.(implement List Comprehesion)

# def remove_vowels(string):
#     vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#     result = ""
#     for char in string:
#         if char not in vowels:
#             result += char
#     return result

# input_string = "Hello, World!"
# output_string = remove_vowels(input_string)
# print(output_string)  


# 4. Write a program to display Powers of 2  using Anonymous functions?(lambda,map).

# num = int (input ("Enter the number of terms: "))

# result = list (map (lambda x: 2 ** x, range (num)))

# print ("The total number of terms are:", num)

# for i in range (num):

#               print ("2 raised to the power”, i, “is", result [i])



# 5. Write a program to implement bubble-sort algorithm

# def bubbleSort(array):
#     for i in range(len(array)):
#         for j in range(0, len(array) - i - 1):
#             if array[j] > array[j + 1]:
#               temp = array[j]
#               array[j] = array[j+1]
#               array[j+1] = temp
# data = [-2, 45, 0, 11, -9]

# bubbleSort(data)

# print('Sorted Array in Ascending Order:')
# print(data)


# 6. Write a program to implement binary-search algorithm

# def binarySearch(array, x, low, high):

    
#     while low <= high:

#         mid = low + (high - low)//2

#         if array[mid] == x:
#             return mid

#         elif array[mid] < x:
#             low = mid + 1

#         else:
#             high = mid - 1

#     return -1


# array = [3, 4, 5, 6, 7, 8, 9]
# x = 4

# result = binarySearch(array, x, 0, len(array)-1)

# if result != -1:
#     print("Element is present at index " + str(result))
# else:
#     print("Not found")



# 7. Write a program to take two list of same length as input and return a dictionary with one as keys and other as values.

# def test(keys, values):
#   return dict(zip(keys, values))

# x = ['a', 'b', 'c', 'd', 'e', 'f']
# y = [1, 2, 3, 4, 5]     
# print("Original lists:")
# print(x)
# print(y)
# print("\nCombine the values of the said two lists into a dictionary:")
# print(test(x,y))


# 8. Write a program to print fibonocci series using recursion.


# def my_fibo(n):
#    if n <= 1:
#        return n
#    else:
#        return(my_fibo(n-1) +my_fibo(n-2))

# nterms = 10

# # # check if the number of terms is valid
# if nterms <= 0:
#    print("Plese enter a positive integer")
# else:
#    print("Fibonacci sequence:")
#    for i in range(nterms):
#        print(my_fibo(i))


# 9. Write a program to find the factorial of a number using recursion.


# def Fibonacci(n):
 
    
#     if n < 0:
#         print("Incorrect input")
 
    
#     elif n == 0:
#         return 0
 
    
#     elif n == 1 or n == 2:
#         return 1
 
#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)
 
 

# print(Fibonacci(9))




# 10. Program to implement concept of decorator to calculate the time needed to execute one or more function in a program.



# def my_decorator(func): 
#     def wrapper_function(*args, **kwargs): 
#         print("*"*10) 
#         func(*args,  **kwargs) 
#         print("*"*10) 
#     return wrapper_function 
  
  
# def say_hello(): 
#     print("Hello Geeks!") 
  
# @my_decorator
# def say_bye(): 
#     print("Bye Geeks!") 
  
  
# say_hello = my_decorator(say_hello) 
# say_hello() 
# say_bye() 


# 11. Write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.(implement generator).

         
      
# def numgenterator(n):
#     for i in range(n+1):
#         if i%5==0 and i%7==0:
#             yield i
# n=int(input("enter number"))
# values=[]
# for i in numgenterator(n):
#     values.append(str(i))
# print(",".join(values))

  
#  12 . Write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.(implement generator)

# for even_numbers in range(4,15,2):
  
#     print(even_numbers,end=' ')

# def my_generator(n):
#     value = 0
#     values = input("Input some comma seprated numbers : ")
#     list = values.split(",")
#     while value < n:
#         yield value
#         value +=2
# for value in my_generator(20):
#     print(value)

  
# 13. Write a program to implement Insertion-Sort algorithm in python.


# def insertionSort(arr):
#     n = len(arr)  
#     if n <= 1:
#         return  
 
#     for i in range(1, n): 
#         key = arr[i]  
#         j = i-1
#         while j >= 0 and key < arr[j]: 
#             arr[j+1] = arr[j]  # 
#             j -= 1
#         arr[j+1] = key  

# arr = [12, 11, 13, 5, 6]
# insertionSort(arr)
# print(arr)


# 14. Program to implement Linear-Search Algorithm.

# def linearSearch(array, n, x):

    
#     for i in range(0, n):
#         if (array[i] == x):
#             return i
#     return -1


# array = [2, 4, 0, 1, 9]
# x = 1
# n = len(array)
# result = linearSearch(array, n, x)
# if(result == -1):
#     print("Element not found")
# else:
#     print("Element found at index: ", result)



# 15.  Program to implement Selection-Sort Algorithm.

# def selectionSort(array, size):
   
#     for step in range(size):
#         min_idx = step

#         for i in range(step + 1, size):
         
#             
#             if array[i] < array[min_idx]:
#                 min_idx = i
         
#         
#         (array[step], array[min_idx]) = (array[min_idx], array[step])


# data = [-2, 45, 0, 11, -9]
# size = len(data)
# selectionSort(data, size)
# print('Sorted Array in Ascending Order:')
# print(data)


# 16. Write a Python program to find the second smallest number in a list using function.

# def my_len(list1):
#     length = len(list1)
#     list1.sort()
#     print("Largest element is:", list1[length-1])
#     print("Smallest element is:", list1[0])
#     print("Second Largest element is:", list1[length-2])
#     print("Second Smallest element is:", list1[1])
 
# list1=[12, 45, 2, 41, 31, 10, 8, 6, 4]
# Largest = my_len(list1)



