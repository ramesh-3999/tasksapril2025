# Mode =r
file=open("demo.txt",mode='r')#demo.txt file to be existed the the Current working directory
read_data=file.read()
print(read_data)
file.close()

#readline()
file=open("demo.txt",mode='r')
read_data=file.readline()#Reads first line of the file demo.txt
read_data1=file.readline()
# '''
# Reads secondline of the file demo.txt as the cursor ends at the 
# end of first line in above code'''
print(read_data)
print(read_data1)
file.close()

#readlines()--Reads file into list of substings 
#This concept is like a SPLIT method in data structures
file=open("demo.txt",mode='r')
read_date=file.readlines()
print(read_date)
file.close()

'''Mode='a' '''
#write()
#This is uded to appent (Add new content to existing information in a file)
file =open("demo.txt",mode='a')
write_data=file.write("\nfour")#It prints length of \n(1)+four(4)=5
print(write_data)
file.close()

vote_list=["Ramesh","Rajesh","Suresh"]#If we consider the list like this ,dat will concat and copy in 1 line
#This similar like Join concept in datastructures
vote_list=["\nRamesh","\nRajesh","\nSuresh"]
file=open("demo.txt",mode='a')
write_date=file.writelines(vote_list)
file.close()

#mode='w'
#In this mode data will override if file exists or it will create new file 
'''For existing file'''
file=open("demo.txt",mode='w')
write_data=file.write("Existing data truncated and this will be copied to this file")
file.close()
'''For new file'''
file=open("sample.txt",mode='w')
write_date=file.write("This will create the new file with name")
file.close()


# Mode =r+
file=open("demo1.txt",mode="r+")
read_data=file.read()
print(read_data)
write_date1=file.write("\nHi I am using  r+ mode")
write_date2=file.write("\nHello")
file.close()

#mode=w+
file=open("demo2.txt",mode="w+")
write_date=file.write("creating new file using w+ mode and writing data")
'''Every time data will be overwritten '''
print("cursor is at ",file.tell(),"place")#Prints the current position of cursor in a file demo2.txt
file.seek(0)#places the cursor in reqiured position i.e 0 in this case.
read_file=file.read()
print(read_file)
file.close()

#mode =a+

file=open("demo3.txt",mode="a+")
write_date=file.write("\ncreating new file using a+ mode and writing data")
'''Every time datas will be appended'''
print("cursor is at ",file.tell(),"place")#Prints the current position of cursor in a file demo2.txt
file.seek(0)#places the cursor in reqiured position i.e 0 in this case.
read_file=file.read()
print(read_file)#Id seek() is  not used then we will get blank spacea output
file.close()

'''rename a existing file'''
#To do some specific operation on file we have to import the 'os' module 
import os
exist_file_Name="New_demo.txt"
rename_file="demo.txt"
os.rename(exist_file_Name,rename_file)
print(f"file {exist_file_Name} has renamed to {rename_file}")

'''removing a file from location'''
import os
rem_file="demo_r.txt"
os.remove(rem_file)
cwd = os.getcwd()
print(f"file {rem_file} has removed from {cwd}")

'''Accessing files outside Current working Directory'''
import os
file= open("D:\\Python\\Python_Introduction.txt",mode='r')
#print("Exists:", os.path.exists(file))
read_file=file.read()
print(read_file)
file.close()