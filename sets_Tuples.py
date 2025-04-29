# set1={1,2,3,"Ram","Raj","Sai"}
# set2={1,2,3,"Ram","Raj","Sai"}
# print(set1)
# set1.add(5)
# print(set1)
# print(set2)
# set2.clear()
# print(set2)
# set3=set1.copy()
# print(set3)
# obj=set3.pop()
# print(obj)
# print(set3)
# set3.remove(3)
# print(set3)
# set3.update(set1)
# print(set3)

###SETS TOPIC
#Union
# set1={1,2,3,4,5}
# set2={4,5,6,7,8,9}
# set3=set1.union(set2)
# print(set3)

#Intersection
# set1={1,2,3,4,5}
# set2={4,5,6,7,8,9}
# set3=set1.intersection(set2)
# print(set3)

#Differenciate
# set1={1,2,3,4,5}
# set2={4,5,6,7,8,9}
# set3=set1.difference(set2)
# set4=set2.difference(set1)
# print(set3)
# print(set4)

#Symmetric Difference--Ignores the common elements in both sets
# set1={1,2,3,4,5}
# set2={4,5,6,7,8,9}
# set3=set1.symmetric_difference(set2)
# print(set3)

#Disjoint--Returns True any common elements else returs False
# set1={1,2,3,4,5}
# set2={4,5,6,7,8,9}
# print(set1.isdisjoint(set2))
# set4={1,2,3}
# set5={4,5,6,7,8,9}
# print(set4.isdisjoint(set5))

# #Super &Sub stets
# set1={1,2,3,4,5,6}
# set2={4,5,6}
# print(set1.issubset(set2))
# print(set2.issubset(set1))
# print(set1.issuperset(set2))
# print(set2.issuperset(set1))

#Frozen set---Changing a set from Mutable to Immutable
# set1={1,2,3,4,5}
# set2=frozenset(set1)
# set1.add(6)
# print(set1)
# set2.add(7)# throws error as -AttributeError: 'frozenset' object has no attribute 'add'

'''
Working on Tuples

Tuple is a ordered collection of elements .which allows int,string,sets,tuple ,list and duplicate elements

'''
# my_tuple=()
# # print(type(my_tuple))
# my_tuple=(1,2,3,"ram",(1,2),{3,4},[5,6],2,3)
# print(my_tuple)
# print(len(my_tuple))
# print(my_tuple.count(2))
# print(my_tuple.index(2))# this provides the Index value of a element 2 (first occurance)

# tuple1=(1,2,3)
# tuple2=(4,5,6)
# tuple3=tuple1+tuple2 #concatination
# print(tuple3)

# course=('python','java','sql')
# print('sql' in course)#Returns True if exists or False


# #uupacking in tuple
# Details=(20,30)
# length=Details[0]
# breath=Details[1]
# print(f"Area of rectangle is {length*breath} Meters") 

'''
Super store program'''
name=input("Enter your name :")
items_list=[("Apple",100),("potato",30),("Tomatos",20)]
sum=0
print(f"Hi {name} your bill is here")
print(f"Item           Price")
print("-"*20)
for i,j in items_list:
   sum+=j
   print(f"{i:15}{j:.2f}")
print("-"*20)
print(f"Total          {sum:.2f}")
