# 1 Write a program to check whether the entered number is postive or negative

# num=int(input("enter the number"))
# if num==0:
#     print("zero")
# elif num>0:
#     print("number is postive")
# else:
#     print("number is negative")

# 2 Write a program to  swap two variables.

# a=int(input("Enter the first number"))
# b=int(input("Enter the second number"))
# c=a
# a=b
# b=c
# print("the value of the first number after swapping is:",a)
# print("the value of the second number after swapping is:",b)

# 3 Write a program to  Determine If Year Is Leap Year

# year=int(input("Enter the year:"))
# if (year%4==0 and year%100!=0) or (year%400==0):
#     print(year,"is a leap year.")
# else:
#     print(year,"is a not leap year."

# 4   Write a program check whether the given number is odd or even.

# num = int(input("Enter a number: "))
# if (num % 2) == 0:
#    print("{0} is Even".format(num))
# else:
#    print("{0} is Odd".format(num))

# 5. Write a program to print the fibonocci series.

# n=10
# num1=0
# num2=1
# next_number=num2
# count=1
# while count <=n:
#     print(next_number,end=" ")
#     count += 1
#     num1,num2 = num2, next_number
#     next_number = num1 + num2
# print()

# 6.Write a program to  generate following pyramid or triangle like  given below using for loop.

# A 

# rows=int(input("Enter number of rows:"))
# for i in range(rows,0,-1):
#     for j in range (0,i):
#         print("*",end=" ")
#     print("\n")

# B

# n=5
# for i in range(n):
#     for j in range(0,i+1):
#         print("*",end=" ")

#     print("\n")
# for i in range(n):
#     for j in range(0,i-1):
        
#         print("*",end=" ")
#     print("\n")


# 7 Write a program to print the prime numbers between given interval.

# lower=900
# upper=1000
# print("print number between ",lower,"and","and",upper,",are:")
# for num in range (lower,upper+1):
#     if num>1:
#         for i in range(2,num):
#             if(num%i)==0:
#                 break
#         else:
#             print(num)

# 8 Write a program for Printing Odd numbers between 1 and 50 and calculate the sum of that numbers.

# max = 50

# for num in range(1, max+1, 2):
#     print("{0}".format(num))

# 9 Write a program to find the factorial of the given number.

# n = int(input("Enter the number:"))
# factorial = 1

# if n >= 1:

#               for i in range (1, n+1):

#                              factorial = factorial *i

# print("factorial of the given number is:",factorial)

# 10 .Write a program to Check if the given string  is Palindrome or not.

# my_str = 'computer'
# my_str = my_str.casefold()

# rev_str = reversed(my_str)

# if list(my_str) == list(rev_str):
#    print("The string is a palindrome.")
# else:
#    print("The string is not a palindrome.")

# 11  Write a program to find sum of all integers greater than 100 and less than 200 that are divisible by 7.

# int i, sum=0;
#    printf("Numbers between 100 and 200, divisible by 7 : \n");
#    for(i=101;i<200;i++)
#    {
#      if(i%9==0)
#      {
#        printf("% 5d",i);
#        sum+=i;
#      }
#    }
#    printf("\n\nThe sum : %d \n",sum);
# }

# begin 	= 1
# end 	= 200
# for cnt in range(begin, end+1):
# 	if( cnt%7==0 and cnt%5!=0 ):
# 		print
		

        

# 12 .Write a program to Display Multiplication Table

# num=12
# for i in range(1,11):
# 	print(num,'x',i,'=',num*i)

# 13 Write a program to calculate the area and perimeter of a rectangle..

# l=int(input("Length : "))
# w=int(input("Width : "))
# area=l*w
# perimeter=2*(l+w)
# print("Area of Rectangle : ",area)
# print("Perimeter of Rectangle : ",perimeter)


# 14 .  Write a program to find the sum of n' Natural Numbers.


# num=16
# if num<0:
#     print("Enter a postive number")
# else:
#     sum=0
#     while (num>0):
#         sum+=num
#         num-=1
#     print("The sun is ",sum)


# 15 . Write a program to find whether given no. is Armstrong or not

# num = int(input("Enter 3-digit number : "))
 
# sum = 0
# temp = num

# while temp > 0:
#     digit = temp % 10
#     sum += digit * digit * digit
#     temp = temp//10
 
# if sum==num:
#     print('It is an Armstrong number')
# else:
    # print('It is not an Armstrong number')


# 16.  Write a program to find the largest among 3 numbers

# print("Enter three Numbers: ")
# numOne = int(input())
# numTwo = int(input())
# numThr = int(input())

# if numOne>numTwo:
#     if numTwo>numThr:
#         large = numOne
#     else:
#         if numThr>numOne:
#             large = numThr
#         else:
#             large = numOne
# else:
#     if numTwo>numThr:
#         large = numTwo
#     else:
#         large = numThr

# print("\nLargest Number =", large)

# 17 Write a program to remove all punctuations from given string.

# import string
# str = "Remove. punctuations @from a% given string?"
# print("Original String :\n\t",str)
# for c in string.punctuation:
# 	str = str.replace(c,"")
# print("After removing Punctuations :\n\t",str)

#  18  Write a program to  Display Triangle as follow : # 1

# 2 2

# 3 3 3

# 4 4 4 4...

# depth = 5
# for number in range(depth):
#     for i in range(number):
#         print(number, end=" ")
#     print(" ")

# 19  Write a program to count the no:of each vowel in a given string.

# string = "GeekforGeeks!"
# vowels = "aeiouAEIOU"
 # count = sum(string.count(vowel) for vowel in vowels)
# print(count)


# 20 Program to perform Addition,Subtraction,Multiplication and division on Complex-No's.


# def addComplex( x1, x2):
#     return x1 + x2
 
# # Driver's code
# x1 = complex(2, 3)
# x2 = complex(1, 2)
# print( "Addition is : ", addComplex(x1, x2))



#  21 . Find Value of the following expressions

# num_1=10
# num_2=11

# num3=num_1 %num_2
# print(num3)

 
# num_4=num_1 - num_2
# print(num_4)

# num_5=num_1*num_2
# print(num_5)



# 22.  Find the results of the following expressions (True or False)
# num_1 = 10

# num_2 = 11
# num_1 % num_2
# num_1 - num_2
# num_1 * num_2


# num_1=7
# num_2=6

# # Add two numbers
# sum = num_1 + num_2

# # Display the sum
# print('The sum of {0} and {1} is {2}'.format(num_1, num_2, sum))


# 23. find the results of the following expression (true or false)


# num_1=3
# num_2=4

# true

# num1=(num_1<num_2)and(num_1!=num_2)
# print(num1)

# true

# num2=(num_2>=num_1)or(num_1>num_2)
# print(num2)

# true

# num3=not(num_1==num_2)
# print(num3)




# 24.   Output of the following while loop

# i=1

# while (i<6):

#     i = i +1

# print(i) 


#  25 . Select the correct option

# customer_num =5

# invoice_num =1212

# print("Invoice No(s):")

# while(customer_num >0):

#      print("INV -", invoice_num)

#      invoice_num = invoice_num +3

#      customer_num = customer_num -1


# option

# A
#  INV-1212 INV-1215 INV-1218

# 26. Write a python function to add ‘python’ at the end of a given string and return the new string. If the given string already ends with ‘python’ then add ‘java’. If the length of the given string is less than 5, then add ‘php’.# Use the keyword def to declare the function and follow this up with the function name

# def modify_str(input_string):
#     if (input_string.endswith("python")):
#         return input_string +"java"
#     elif len(input_string)<5:
#         return input_string+"php"
#     else:
#         return input_string+"python"
# input_str="Hello"
# result=modify_str(input_str)
# print(result)
# input_str="python"
# result=modify_str(input_str)
# print(result)
# input_str="programming"
# result=modify_str(input_str)
# print(result)





