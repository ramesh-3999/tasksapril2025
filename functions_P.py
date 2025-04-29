#Practicing the functions 
#syntex
# def function_name():# Definition of a function 
#     print("This is sample code for function")# Block od code in the function function_name()
#  #If we donot call the function it will be compilead and reside inside the code   
# function_name()# To execute the code inside the function we will call the function.Here we called the function
'''A FUNCTION CAN BE REUSED ANY NUMBER OF TIMES'''


# def add():
#     a=20 #Block of code for function add.Here we can take dynamic inputs using input function
#     b=30 #Block of code for function add.Here we can take dynamic inputs using input function
#     print("Sum of a and b is:",a+b)#Block of code for function add
# add()

#Passing the Parameters(Variables) & Arguments(Values) to the function definition
# def add(a,b):#Function definition with Parameters a anb b
#     print(a+b)# Block of code to be executed in function call
# add( a=int(input("Enter argunent for a:")),
#     b=int(input("enter argument for b:")))# passing the values dynmically at the time of function call

# def emp_details(a,b):
#     print(f"Employe name is {a} and empid is {b}")
# emp_details('Ramesh',1193)


# def nums(a,b):
#     return a*b# Return used to exit from the function and sends the valu to caller,Function will ends after return
# obj=nums(3,5)#Return value can be stored in a object
# nums(3,5)#Return valus sent to the caller--> 'nums'
# print(nums)# prints the position of the caller
# print(nums(5,6))#Prints the return value userd in function block

'''DEFAULT PARAMETERS'''
# def emp_details(name=None,empid=None,dept=None):
#     print(name,empid,dept)
# emp_details("Ramesh",123,"IT")#Aguments are passed  
# emp_details("Suresh",124)#Only 2 arguments are passed and the 3rd argument it will take default from def dept=None
# emp_details("Mahesh")#Only 1 arguments are passed and the 2nd,3rd argument it will take default  from def empid=None,dept=None
# emp_details()#No argumentsa are passed  and it will take all 3 default valus from def emp_details

# def emp_details(name,empid=None,dept=None):
#     print(name,empid,dept)
# emp_details()   
#TypeError: emp_details() missing 1 required positional argument: 'name'---->
'''None is a special constant that represents Null or Absance of Argument'''

'''Arbitary arguments --It will allow any number of arguments  and 
 returns output in a tuple '''
# def my_list(*a):# Arbitary  arguments are represented with *Parameter --->*a
#     print(a)
# my_list("Ramesh","Suresh","Mahesh",1,1,2,[1,2,3])

'''keywords arguments --It will allow any number of arguments   in key=value and 
 returns output in a dictionary '''
# def my_fun(**a):#Keywors are represented as **Parameter
#     print(a)
# my_fun(Ramesh=1,Rajesh=2,Suresh=3)

'''VARIABLES'''
'''Global and Local variables'''

#Local variables
# def myfun(a):
#     a=a*10
#     print(a)
# myfun(5)
# print(a)#This cannot be used as 'a' is a local variable

#Global variables
# b=20
# def myfun(a):
#     result=a*b
#     print(result)
# myfun(5)
# print(b*5)

'''With import we can use all the functions in the import file with filename.functionname'''
# import func_imp
# func_imp.add(5,5)
# func_imp.mul(5,5)
# func_imp.expo(5,3)

'''To avoid calling func_imp(module).function) we use all  that is '*' 
syntex is --> from module(func_imp) import *    Here module is .py file'''
#from func_imp import *

from random import *
Lottery_list=[]
registration_list={1:"Ramesh",2:"Mahesh",3:"Panya",4:"Ahanya",5:"Rishi",6:"Nandu",7:"Riyansh",8:"Juhita",9:"Juvas",10:"Jitendra"}
while len(Lottery_list) < 3:
    num = randint(1, 10)
    if num not in Lottery_list:
        Lottery_list.append(num)
# Selected candidates
for num in Lottery_list:
    if num in registration_list:
        print(f"Hi {registration_list[num]}, congratulations! Your H1B Application is selected. We will send you a confirmation mail.")

print("\nSelected Numbers:", Lottery_list)
# #print(Lottery_list)
# print("out put for choice function")
# print(choice(["Ramesh","Suresh","Rajesh"]))

# from datetime import datetime
# date_time=datetime.now()
# print(date_time)

# #OS Module --To interact with Operating System
# import os
# print(os.getcwdb())

# #import sys# Tis modules gives the details about the Python software 
# from sys import *
# print(argv)
# print(version)
# print(copyright)

balance=10000
def credit(amount):
    balance+=amount
    print(balance)
credit(500)
# '''We will get error as we are using global variable balance inside the function ,
# Here we have to declare the global variable name inside the function'''
# #UnboundLocalError: cannot access local variable 'balance' where it is not associated with a value

'''Here we got the output as we mentioned the global key word and variable in side the function'''
balance=10000
def credit(amount):
    global balance
    balance+=amount
    print(balance)
credit(500)

# import math
# #Task 1: Add Function
# def add(a,b):
#     sum=a+b
#     print(sum)
# add(4,5)  

# num=int(input(":Enter the number:"))
# print(math.sqrt(num))

# num=int(input(":Enter the number:"))
# print(math.factorial(num))

#Find max valu in a list
def my_max(my_list):
    #my_list=[23,24,54,32,61,27,16]
    max=my_list[0]
    for i in my_list:
        if i>max:
            max=i
           # break
    print("max value is:",max)
my_max([23,24,54,32,61,27,16])

#Reverse a string
def rev(a):
    return a[::-1]
print(rev("hello"))

#Prime number checking
def is_prime(n):
    if n <= 1:
        return False  # 0 and 1 are not prime numbers
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return print(f"{n} is not a prime number")#False
    return print(f"{n} is a prime number")#False#True
a=int(input("Enternumber:"))   
is_prime(a)

#Fibonacci Function

def febo(n):
    febon=[]
    a,b=0,1
    while a<n:
        febon.append(a)
        a,b=b,a+b
    print(febon)
n=int(input("Enternumber:"))        
febo(n)

# #Palindrome Function
def palin(a):
    b=a[::-1]
    if a==b:
        print(f"The word  {a} is a palindrom")
    else:
        print(f"The word  {a} is not a palindrom")
    #print(b)
a=str(input("Enter a string:"))
palin(a)       

#Sum of square of a given list
def squares_sum(num_list):
    sqr_sum=0
    for i in num_list:
        sum=i**2
        sqr_sum+=sum
    print(f"The sum of squares of a list {num_list} is :",sqr_sum)
numbers=input("Enter the numbers separate by ,:")
num_list = [int(i) for i in numbers.split(',')] 
squares_sum(num_list)    

#Average of a given list

def avg_val(num_list):
    sum=0
    leng_list=len(num_list)
    for i in num_list:
        sum+=i
    print(f" Average of {num_list} is ",int(sum/leng_list))
numbers=input("Enter the numbers separate by ,:")
num_list = [int(i) for i in numbers.split(',')] 
avg_val(num_list) 