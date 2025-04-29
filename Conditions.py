# Will practive the If ,elif,else conditions in this file
# Age=int(input("Enter your age"))
# if Age>18:
#     print(f'Your age is {Age}')
#     print(".Your are elegible for voting.")
# print("out of if block statement")

#If else

# age=int(input("Enter the age :"))
# if age>18:
#     print(f"Your age is {age} Years.\n Your are elegible for voting")
# else:
#     print(f"Your age is {age} Years and is below age criteria for voting") 


# #Elif --When we want to check the multipe conditions one by one .
# age=int(input("Enter age :"))
# Gender=str(input("Please enter the gender Male Or Female:"))
# if age>21 and Gender=='Male':
#     print(f"Your age is {age} Years Male.\n Your are elegible for marriage")
# elif age>18 and Gender=='Female':
#     print(f"Your age is {age} Years Female.\n  Your are elegible for marriage") 
# else:
#     print(f"Your  {age} years {Gender} .Your not eligible for marriage  as per Govt Rules.")

#Nested Ifelse--Useful when we are taking a series of Conditions -decisions

# user_name=str(input("Enter the Usename :"))
# user_pwd=str(input("Enter the User password :"))
# if user_name=="Ramesh":
#     if user_pwd=="Ramesh@123":
#         print(f"Login successful \n logged as {user_name}")
#     else:
#         print(f"Invalid Password")
# else:
#     print(f"Invalid Username")

#shorthand iF
# number=int(input("Enter the number:"))
# if number%2==0:
#     print(f"Given {number} is a even number")
# else:
#     print(f"Given {number} is not a even number")


# number=int(input("Enter the number:"))
# print(f"Given {number} is a even number") if number%2==0 else  print(f"Given {number} is not a even number")


# #Vowel Checker:
# list1=['a','A','e','E','i','I','o','O','u','U']
# vowel_serch=str(input("Enter the character:"))
# if vowel_serch in list1:
#     print(f"{vowel_serch} is a vowel.")
# else:
#     print(f"{vowel_serch} is not a vowel")

# #Number Classifier
# number=int(input("Enter the number:"))
# if number>0:
#     print(f"{number} is positive value")
# elif number<0:
#     print(f"{number} is a negative value")
# else:
#     print(f"Provided value is ZERO")

# Perform +,-.* and / operations 
num1=int(input("enter the num1:"))
num2=int(input("enter the num2:"))

operatot=input("Enter any Operator + Or - or 8 or / :")
if operatot=="+":
    print(f"Sum of 2 numbers {num1} and {num2} is {num1+num2}")
elif operatot=="-":
    print(f"Substraction of 2 numbers {num1} and {num2} is {num1-num2}")
elif operatot=="*":
    print(f"Product of 2 munbers {num1} and {num2} is {num1*num2}")
elif operatot=="/":
    print(f"Division of 2 numbers {num1} and {num2} is {num1/num2}")
else:
    print("Invalid Operation")

