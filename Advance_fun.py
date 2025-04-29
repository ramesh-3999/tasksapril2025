'''Advance functions'''
# def add(a,b):
#     return a+b
# print(add(5,5))

# #lambda function
# # Syntex----->lambda arguments:Expression
# result =lambda a,b:a+b
# print(result(20,30))

# result=lambda a,b,c:a+b+c
# print(result(25,35,50))

# result=lambda a,b:a**b
# print(result(5,2))

#Filter function
# list1=[1,1,13,17,1,51,61,89,91,0,2]
# def even(a):
#     return a%2==0
# obj=filter(even,list1)
# print(list(obj))

#lambda arg:exp
#filter(fun:iter)
# list1=[1,1,13,17,1,51,61,89,91,0,2]
# result=filter(lambda a:a%2==0,list1)
# print(list(result))

#map
# list1=[10,12,13,14,15,16,17,18,19,20]
# def square(a):
#     return a**2
# result=map(square,list1)
# print(list(result))

# 2 or more lists 

# list1=[10,12,13,14,15,16,17,18,19,20]
# list2=[31,1,1,1,1,11,1,11,1,1]
# def square(a,b):
#     return a**2
# result=map(square,list1,list2)
# print(list(result))
'''
Here the index position of the list2 is pointing to the value in list1 of same index '''


#Use lambda for above map function
#lambda arg:exp
#map (function,iterable,....)
# list1=[10,12,13,14,15,16,17,18,19,20]
# result=map(lambda a:a**2,list1)
# print(list(result))

#reduce
#syntex reduce(function,iterable)
# This is mainly used to perform the rolling sum 
# from functools import reduce
# list1=[1,2,3,4,5]
# def roll(a,b):
#     return a+b
# result=reduce(roll,list1)
# print(result)

#syntex reduce(function,iterable)
#lambda arg:exp
# from functools import reduce
# list1=[1,2,3,4,5]
# print(reduce(lambda a,b:a+b,[1,2,3,4,5]))
#print(reduce(lambda a,b:a+b,list1))

#generator Function
# list1=[1,2,3,4,5,6,7,8,9]
# def yield_fun(lst):
#     for a in lst:
#      if a%2==0:
#         yield f"{a} is even number"
#      elif a%2!=0:
#         yield f"{a} is not even number"
# for result in yield_fun(list1):
#     print(result)

from functools import reduce
lst=['a','A','e','E','i','I','o','O','u','U']
strg=input("Enter a string : ")
#print(reduce(lambda a,b:a+b,[1,2,3,4,5]))
vowel_count=reduce(lambda count, ch:count+(1 if ch.lower() in lst else 0),strg)
print("No of vowels in a ",strg, vowel_count)
# refuce(fun,iterable)
