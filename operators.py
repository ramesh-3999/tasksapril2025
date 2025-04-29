#Addition Operator +
# num1=int(input("Enter the num1:"))
# num2=int(input("Enter the num2:"))
# #Result=num1+num2
# print('Sum of 2 numbers is:',num1+num2)

# #Substraction Operator -
# num1=int(input("Enter the num1 :"))
# num2=int(input("Enter the num2 :"))
# print('Substraction of number is :',num1-num2)#num1-Left Operand,Num2 -Right Operand

# #Multiplication Operator *
# num1=int(input("Enter the 1st number :"))
# num2=int(input("Enter the 2nd  number:"))
# print("Product of given numbers ",num1,"and",num2,"is :",num1*num2)

#Division Operator /---Always return Quotient ,
# num1=int(input("Enter the num1 value:"))
# num2=int(input("Enter the num2 value:"))
# Result=num1/num2
# print(Result)

# # //(Floor Division)---Always gives the real part and discards decimal value
# num1=int(input("Enter the num1 value:"))
# num2=int(input("Enter the num2 value:"))
# Result=num1//num2
# print(Result)

# #Modulus Operator % --Always gives the remainder
# num1=int(input("Enter the num1 value:"))
# num2=int(input("Enter the num2 value:"))
# result=num1%num2
# print("reminder is :",result)

# #Exponential Operator ** Left oerand is Base and Right Operand is Exponential
# num1=int(input("Enter the num1 value:"))
# num2=int(input("Enter the num2 value:"))
# result=num1**num2
# print("reminder is :",result)
#Compound Assignment operator +=,-+,*=
# num1=10
# num1 +=10
# print(num1)
# num1=10
# num1 -=10
# print(num1)
# num1=int(input("Enter number:"))
# num1 *=10
# print(num1)

# #Comparison operators ==,<,>,<=,>=
# num1 =100
# num2=200
# print(num1==num2)
# print(num1!=num2)
# print(num1>num2)
# print(num1>=num2)
# print(num1<num2)
# print(num1<=num2)

#Logical operators
# user_name=str(input("Enter User name:"))
# pass_wd=str(input("Enter password:"))
# print(user_name=="ramesh" and pass_wd=="ramesh@123")
# print(user_name=="ramesh" or pass_wd=="ramesh@123")

# #Identity Operator
# num1=123456
# num2=12345
# print(num1 is num2)
# print(num1 is not num2)

# #Membership operators IN and NOT IN
# list_1=[1,2,3,4,5,"Ramesh"]
# print(1 not in list_1)
# print("ramesh" not in list_1)# Here ramesh & Ramesh is different
# print("Ramesh" in list_1)

#Discount Caliculator
#F""-Fstrings are used to print the output in redable format along with the numbers
product_Cost =10000
discount=10
result=product_Cost*(discount/100)
product_Cost-=result
print(f"Discount given {discount} %  Final discount {result} and total cost after discount is Rs.{product_Cost} ")