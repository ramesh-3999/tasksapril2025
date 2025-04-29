#Dictionary
# dict_1={}
# print(type(dict_1))
# dict_2=dict()
# print(type(dict_2))
# emp_date={
#     1:"Ramesh",
#     2:"Sunitha",
#     3:"Panya",
#     4:"Ahanya",
# }
# print(emp_date)
# emp_date_cpy=emp_date.copy()
# print(emp_date_cpy)
# print(emp_date.get(1))
# print(emp_date[2])
# print(emp_date.items())
# print(emp_date.keys())
# print(emp_date.values())#this will come in pandas topic as well
# #Emp_data_pop=emp_date.pop(1)
# print(emp_date)
# #print(Emp_data_pop)
# emp_data_1={
#     5:"Uma",
# }
# emp_data_1[5]="Uma Shankar"#Changing the value of existing key
# emp_data_1[6]="Rishi"
# emp_date.update(emp_data_1)
# print(emp_date)

#Task1-
# my_dict = {'name': 'python', 'age': 25}
# my_dict['city']='West Godavari'
# print(my_dict)

# #task2
# product_info = {'name': 'Laptop', 'brand': 'Dell', 'price': 1200}
# print(product_info['price'])

#task3-Dictionary Removal
# my_dict = {'name': 'python', 'age': 30, 'city': 'Bhimavaram'}
# my_dict.pop('city')
# print(my_dict)

#task4-Dictionary Keys
# my_dict = {'name': 'python', 'age': 25, 'city': 'Rajahmundry'}
# print(my_dict.keys())

#Task 5: Dictionary Values
# my_dict = {'name': 'python', 'age': 25, 'city': 'tanuku'}
# print(my_dict.values())

#Exercise 1: Dictionary Update

# emp_data={1:"Ramesh",2:"Sunitha",3:"Panya",4:"Ahanya",}
# emp_new_lst={5:"Uma"}
# emp_data.update(emp_new_lst)
# print(emp_data)

#Exercise 2: Dictionary Access
emp_data={1:"Ramesh",2:"Sunitha",3:"Panya",4:"Ahanya",}
print(emp_data[3])

# #Exercise 3: Dictionary Removal
# emp_data1={1:"Ramesh",2:"Sunitha",3:"Panya",4:"Ahanya",}
# print(emp_data1.pop(1))
# print(emp_data1)
# emp_data1[1]="Ramesh"
# print(emp_data1)

# #Exercise 4: Dictionary Keys
# print(emp_data1.keys())

# #Exercise 5: Dictionary Values

# print(emp_data1.values())