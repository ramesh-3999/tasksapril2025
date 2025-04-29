# sample="Python life"
# print(sample[3:8])
# print(sample[-1])
# print(sample[-6:])
# print(sample[10:6:-1])
# print(sample[9:6:-1])

#string Methods
# message="Hello, World!"
# conv_obj=message.upper()
# print(message)
# print(conv_obj)
# conv_obj=message.lower()
# print(conv_obj)
#Lowe and Upper case mainly used in Gmail

#count
# cnt=message.count('o')#Count the Occurance of O
# print(cnt)
# #Strip
# message=("   Hi This is ramesh and I am learning Python    ")
# new_message=message.strip()
# print(new_message)
# print(len(message))
# print(len(new_message))
# new_message=message.lstrip()
# print(new_message)
# print(len(message))
# print(len(new_message))
# new_message=message.rstrip()
# print(new_message)
# print(len(message))
# print(len(new_message))
# #split-its separator a  string to LIST sub string
# data="ramesh,Suresh,Rajesh"
# date1=data.split(',')
# #data="1,2,3,4,5,6"
# date1=data.split(',')
# print(date1)
# new_string=data.replace('ramesh','Ramesh')
# print(new_string)

#Starts with and ends with
# email_list=["r@gmail.com","a@gmail.com","m@gmail.com","e@gmail.com","k@outlook.com","b@yahoo.com"]
# # new_list=[]
# # for i in email_list:
# #     if i.endswith('@gmail.com'):
# #      new_list.append(i)
# # print(new_list)

# new_list=[i for i in email_list if i.endswith('@gmail.com')]
# print(new_list)

# string_1="12345"
# string_2="ramesh@123"
# is_numeric=string_1.isdigit()
# print(is_numeric)
# is_numeric=string_1.isalpha()
# print(is_numeric)
# is_numeric=string_1.isalnum()
# print(is_numeric)
# str_name="this is my reverse string"
# str_obj=str_name[::-1]
# str_obj=str_name.capitalize()
# str_obj=str_name.replace(' ','_')
# str_obj=form
# print(str_obj)


input_str = "Hello world , this is python code!"
new_string=input_str.casefold()
print(new_string)
new_string=new_string.title()
print(new_string)
