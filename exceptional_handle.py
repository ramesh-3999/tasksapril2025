#Exeception/Errort handling
'''In general we will come across 3 types of errors
1.Syntex errors
2.Runtime errors
3.Logical errors'''

# num1=int(input("Enter the numeber1:"))
# num2=int(input("Enter the numeber2:"))
# print(num1+num2)
# print(num1-num2)
# try:
#     print(num1/num2)
# except:
#     print("some error")    
# print(num1*num2)

#try and except

# list_1=[10,20,30,40]
# print(list_1[0])
# print(list_1[1])
# try:
#    print(list_1[5])
# except:
#    print("List range error")
# print(list_1[3])

#else block

# list_1=[10,20,30,40]
# print(list_1[0])
# print(list_1[1])
# try:
#     #print(list_1[5])#When we wuse this else will not execute as we dont see index 5 in list
#    print(list_1[2])#When we use this else will execute as we have index 2 in list
# except:
#    print("List range error")
# else:   
#  print(list_1[3])

 #finally
# list_1=[10,20,30,40]
# print(list_1[0])
# print(list_1[1])
# try:
#    print(list_1[5])
#    #print(list_1[2])
# except:
#    print("List range error")
# else:   
#  print(list_1[3])
# finally:
#   print("Final block execution")

#Displaying the specific error
# list_1=[0,20,30,40]
# print(list_1[0])
# print(list_1[1])
# try:
#    print(list_1[5])
#    #print(list_1[2])
# except ValueError as e:
#    print(e)
# else:   
#  print(list_1[3])
# finally:
#   print("Final block execution")

#exception -This is base class for all errors
a=10
b=0
try:
 div=a/b
 print(div)
except Exception as r:
 print(r)

list_1=[0,20,30,40]
print(list_1[0])
print(list_1[1])
try:
   print(list_1[5])
   #print(list_1[2])
except Exception as e:
   print(e)
else:   
 print(list_1[3])
finally:
  print("Final block execution")
