#Caliculate the are of rectangle
#Area =Length* Breadth
# Length=float(input('Enther the Length in Meters:'))
# Breath=float(input("Enter the  breath in Meters:"))
# print(f"Area of Rectangle for length {Length} M and Breath {Breath} M is :",float(Length*Breath) ,"MTS")

#Program to increment and Decrement a variable

# age=int(input("Enter a number :"))
# #If Int is not specifiedd then the entered number is considered as string and will through error
# age +=5
# print(age)

#Program to convert Temp convert temperature from Celsius to Fahrenheit
#formula for conversion is: F = (C * 9/5) + 32 .
# temp_celcius=float(input("Enter temerature in Celsius:"))
# print("Fahrenheit is:",(temp_celcius * 9/5)+32)

#Write a Python program to calculate the simple interest given the principal
#amount, rate, and time (in years).
#Simple Interest =PTR/100
# Principle_Amount=int(input("Enter the Principle Amount :"))
# Duration=float(input("Enther the Duration of time in years :"))
# Rate=float(input("Enter the % of interest :"))
# print(f"Simple Interest is Rs: {Principle_Amount*Duration*Rate/100} Per/Year")


#Write a Python program to concatenate two strings and display the result. The
# #strings should be taken as input from the user.
# First_Name=str(input("Enter the Fist name of a candidate :"))
# Last_Name=str(input("Enter the Last name of a candidate :"))
# print(f"Full name of the candidate is : {First_Name} {Last_Name}")

#Write a Python program to convert a distance from kilometers to miles.
# #1 KM=0.621371 Miles
# KMS=float(input("Enter the KMS travelled :"))
# print(f"Mr Been has travelled a distance of {KMS*0.621371} Miles") 

#Create a program that takes user input for their name and age

# Candidate_name=str(input("Enter the name :"))
# Candidate_age=int(input("Entrer the age of the person:"))
# print(f"Thank you {Candidate_name} for providing your name and age  {Candidate_age} .Welcome  to the Python Life Training.")

#Create a list called numbers that contains integers from 1 to 10.
list_1=[1,2,3,4,5,6,7,8,9,10]
Num_search=int(input("Enter the number:"))
print(Num_search  in list_1)
Num_search2=int(input("Enter the number:"))
print(Num_search2  not in list_1)