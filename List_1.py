# my_list=[10,20,30,40,50,60]
# print(my_list[-6])

# #slicing
# my_list=[10,20,30,40,50,60]
# print(my_list[-6:-1])


# my_list=[10,20,30,40,50,60]
# print(my_list[:])
# print(my_list[:8])
# print(my_list[0:])
# print(my_list[::1])
# print(my_list[::-1])

# my_list=[10,20,30,40,50,60]
# #print(my_list[8:2:-1])
# print(my_list[6:2:-1])

#List Methods
#list_1=[1,2,3,4,5,6]
# list_1.append(7)
# list_1.extend([8,9,10,1,2,1,1,1])
# copy_list=list_1.copy()
# print(list_1) 
# print(copy_list)
# # list_1.clear()
# # print(list_1)
# print(list_1.count(1))
# print(list_1.index(10))
# list_1.remove(1)
# print(list_1)
# #list_1.pop(1)#Removes eliment in specified index position
# # Object is preated on pop  ,so it will be used for further where as not possible in remove
# obj=list_1.pop(10)
# print(obj)
# print(list_1)
# list_1.insert(6,"Ramesh")
# print(list_1)
# print(len(list_1))
# list_1.reverse()
# print(list_1)
# list_1.remove("Ramesh")
# list_1=[1,2,7,9,3,4,5,6]
# list_1.sort()
# print(list_1)
# list_1.sort(reverse=True)
# print(list_1)

#Nested List 
# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# print(matrix[0][1])
# print(matrix[1][0])

# #LIST COMPREHENSIONS
# empty_list=[]
# sum=0
# for i in range(1,8):
#     result=i**2
#     sum+=result
#     empty_list.append(result)
# print(empty_list)
# print(f"Sum of square in a given range is {sum}")

#[exp FOR item in iterable range]
# result=[i**2 for i in range(1,6)]
# print(result)
# print([i**2 for i in range(1,6)])#List comprehension 
# list_1=[]
# for i in range(1,10):
#     if i%2==0:
#         list_1.append(i)
# print(list_1)

# print([i for i in range(1,10) if i%2==0])
#Remove the duplicates from index using element
# lst= [1,2,3,4,1,1,3,5,1] 
# empty_lst=[]
# for i in lst:
#     if i!=1:
#         empty_lst.append(i)
# print(empty_lst)


#Remove the duplicates from index using Index value for the specific element 1
# lst= [1,2,3,4,1,1,3,5,1,0] 
# empty_lst=[]
# for i in lst:
#     if lst.index(i)!=0:#Here 0 is not the element its a Index position of 1
#         empty_lst.append(i)
# print(empty_lst)

# Progran to find the even numbers in a range and result in list 
# print([i for i in range(10) if i%2==0])

# lst=[1,2,3,4,5,6]
# lst.reverse() #Using reverse method
# result=lst[::-1] # using Slice method
# print(lst)
# print(result)

#Program to find common elements in 2 lists list1 and list2
# list1=[1,2,3,4,5]
# list2=[4,5,6,7,8]
# comm_list=[]
# for i in list1:
#     for j in list2:
#          if i==j:
#           comm_list.append(i)
# print(comm_list)

# list1=[1,1,2,3,4,4,5,6]
# new_set=(set(list1))
# print(new_set)
# print(list(new_set))

#Find unique elements using loop condition
# list1=[1,1,2,3,4,4,5,6]
# new_lst=[]
# for i in list1:
#           if i not in new_lst:
#             new_lst.append(i)
# print(new_lst)

#Concatinate 2 lists
# list1=[1,1,2,3,4,4,5,6]
# list2=[8,8,8,8,8,8,8]
# new_list1=[list1+list2]#Adding to different list values in 1 list
# new_list=[list1]+[list2]#Adding to diiferent lists in 1 list
# print(new_list)
# print(new_list1)

#program to repeat the list 3 times and print the result
# list1=[1,2,3]
# new_list=list1*3
# print(new_list)

#Program to remove emenents at even
# list1=[1,2,3,4,5,6,7,8,9]
# noneven_list=[]
# for i in list1:
#     if i%2!=0:
#         noneven_list.append(i)
# print(noneven_list)


# list1=[1,2,3,4,5,6,7,8,9]
# print([i for i in list1 if i%2!=0])

# print([i for i in range(10) if i!=0 and i%2!=0])

#program to insert the 10,11 and 12 at begining of the list
# list1=[1,2,3,4,5,6,7,8,9]
# list1.insert(0,10)
# list1.insert(1,11)
# list1.insert(2,12)
# print(list1)

#List of seq num from 1 to 10
# new_list=[i for i in range(1,11)]
# print(new_list)

#List of even num from 1 to 10
# new_list=[i for i in range(1,11) if i%2==0]
# print(new_list)

#program to find the word length
new_list=["apple","banana","papaya","strawberry"]
print("Element wise name and length \n")
for i in new_list:
    len_str=len(i)
    print(f"Length of '{i}' is :",len_str)
print()

new_list=["apple","banana","papaya","strawberry"]
print(F"Lengths of elements in new_list:")
print([len(i) for i in new_list])



