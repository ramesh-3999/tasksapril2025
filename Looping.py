#Looping statements
# # FOR(Key word) Variable in sequence
# voter_list=["Ramesh","Rajesh","Suresh"]
# for i in voter_list:
#     print(f"{i} your elegible to vote")
#     number=int(input("Enter the number"))
#     if number%2==0:
#         print(f"{number} is a even number")
#     else:
#         print(f"{number} is a Odd number")


# num_list=[1,2,3,4,5]
# for i in num_list:
#     if i%2==0:
#         print(f"{i*2}\n")
#     else:
#         print(f"{i*3}")
# print("Out of for loop")

#Range()--Range is used to find the sequence 
# rng=range(10)
# for i in rng:
#     print(i)
#     print("Inside loop")
# print("Outside loop")

# rng=range(99,149+1)
# for i in rng:
#     print(i)
#     #print("Inside loop")
# print("Outside loop")

# rng=range(0,101,5)
# for i in rng:
#     print(i)
#     #print("Inside loop")
# print("Outside loop")

# rng=range(1,11)
# for i in rng:
#     print(f"2 X {i}={2*i}")
    
# num=int(input("Enter the multiplication Table: "))
# print(f"Multiplication table for {num}")
# for i in range(1,11):
#     print(f"{num} X {i}={num*i}")

# #Nested For Loop
# for i in range(1,6):
#     print(f"Table for {i} is :")
#     for j in range(1,11):
#         print(f"{i} X {j}={i*j}")
#     print()

#while loop 
#CTRL+E(To brak the continous execution of loop)
# while True:
#     user_Name=str(input("enter user name :"))
#     user_pwd=str(input("Enter the password:"))       
#     if user_Name=="Ramesh" and user_pwd=="ramesh@123":
#         print("Login successful")
#         break
#     print("Invalid Credentials")

#Nested While Loop

# outer=0
# while outer<2:
#     inner=0
#     while inner<2:
#         print(outer,inner)
#         inner+=1
#     outer+=1

#Caliculate the sum of squares
# sum=0
# for i in range(1,6):
#     result=i**2
#     sum +=result

# print(f"The sum of squares of given range of numbers is :{sum}")

# for i in range(1,601):
#     if i%2==0:
#         continue
#     print(i)

# number =[10,20,30,40,50]
# sum =0
# for i in number:
#     sum+=i
#     if sum<150:
#       print(f"sum of numbers at {i} is {sum}")
#     else:
#        print(f"Sum Exceeded than 150 for {i}")
#        break

# num=int(input("Enter the number:"))
# for i in range(5):
#     for j in range(1,11):
#       print(f"{i} X {j}={j*i}")
#     print()

#Program to find the sum of numbers in a given range
# sum=0
# for i in range(0,11):
#     if i%2==0:
#         sum+=i
#        # print(sum)
# print(sum)

#Program to find the sum of numbers till the given number
# temp=0
# sum=0
# num=int(input("Enter the number: "))
# for i in range(1,num+1):
#     if temp<=num:
#      temp +=1
#      #break
#      sum=sum+temp
# print(f"The sum of numbbers from 1 to {num} is :",sum)

#Display the numvers from the list
# lst=[1,2,3,4,5,6]
# for i in lst:
#     print(i)
# print("lst is of the type:",type(lst))
# print(type(i))

#Display numbers from -10 to -1 using for loop

# for i in range(-10,0):
#     print(i)

#Program to display all prime numbers in a rage

n=int(input("Enter the number:"))
for i in range(2, n):
        if i % 2 ==0 or i%3==0:
           print()# print(f"{i} Not a prime numbers") 
        else:
            print(f"{i} is a prime number")
   