# list_1=[1,2.5,"ramesh",[2,3.5,"babu"]]
# print(type(list_1))
# list_1.append("Vegi")
# #list can be append --Mutable type
# print(id(list_1))
# list_1.append(2)
# print(list_1)

#tuples
# tuple_1=(1,2.5,"Ramesh",(4,5.5,"babu"))
# print(tuple_1)
# print(type(tuple_1))
# print(id(tuple_1))
#tuples cannot be appended -Immutable type

#set
#Its a unordered collection of unique elements(It will not allow duplicates even if we define in set)
# My_set={1,2,3.5,"coach",1,2,3.5,"coach"}
# print(My_set)
# print(type(My_set))
#Set cannot be appended


#Dictionary
#Keys.values--Keys(NumbersTuplesStrings)
emp_id={
    1:"Ramesh",#Item(KEY:VALUE)
    2:"Suresh",
    3:"Panya",
    4:"Ahanya",
    (1,2):"hi" 
}
print(emp_id)
print(type(emp_id))
conv_tuple=tuple(emp_id)
print(conv_tuple)
#conv_dict=dict(conv_tuple)
#print(conv_dict)


# list_1=[1,1,1,1,2,2,3,4,4,4,4,"Raj","Ram","Raj"]
# print(list_1)
# print(type(list_1))
# conv_set=set(list_1)
# print(conv_set)
# print(type(conv_set))
# conv_list=list(conv_set)
# print(conv_list)

