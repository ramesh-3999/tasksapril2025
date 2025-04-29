#syntex
#class classname():
   #class body
# class details():#Class definition
#     name ="Ramesh"#Attribute
#     name2="Rajesh"#Attribute
#     def details1(self):#Method--Here we need to 'self' as first argument in method
#         print("This is first method")
#     def details2(self):#Method--Here we need to 'self' as first argument in method
#         print("This is second method")
# #Class binds attribute and methods in a single unit called blueprint 
# #Object creation
# #Object_name=classname()
# obj=details()# Object creation process is called an Instanciation
# print(obj.name)
# print(obj.name2)       
# obj.details1()
# obj.details2()

# class mobiles():
#     name="samsung"
#     color="Blue"
#     Storage="128 GB"
#     def calling(self):
#         print("Your calling from",self.name)
#     def camara(self):
#         print("Your accessing the camara")
#     def contact(self):
#         print("Your accessing the contact list")
# #OBJECT creation
# my_phone=mobiles()
# my_phone.calling()
# my_phone.camara()    
# print(my_phone.name)   


# Accessing the other methods in  a class using the 'self'
# class mobiles():
#     name="samsung"
#     color="Blue"
#     Storage="128 GB"
#     def calling(self):
#         print("Your calling from",self.name)
#     def camara(self):
#         print("Your accessing the camara")
#         self.calling()
#     def contact(self):
#         print("Your accessing the contact list")
#         self.calling()
#         self.camara()
# #OBJECT creation
# my_phone=mobiles()
# # my_phone.calling()
# # my_phone.camara()   
# my_phone.contact() 
# print(my_phone.name)  

# class mobiles():
#     name="samsung"
#     color="Blue"
#     Storage="128 GB"
#     def calling(self,brand):
#         print("Your calling from",brand)
#     def camara(self):
#         print("Your accessing the camara")
#         self.calling()
#     def contact(self):
#         print("Your accessing the contact list")
#         self.calling()
#         self.camara()
# #OBJECT creation
# my_phone=mobiles()
# # my_phone.calling()
# # my_phone.camara()   
# my_phone.calling("samsung") 
# #print(my_phone.name) 
# my_vivo=mobiles()
# my_vivo.calling("vivo") 

# class car():
#     def __init__(self,brandname,color,model):
#         self.brandname=brandname
#         self.color=color
#         self.model=model
#     def driving(self):
#         print("Your driving ",self.color,"color",self.brandname)
#     def engine(self):
#         print("Start On/Off")
# mycar=car("Hundai","Red",2025)
# mycar.driving()

'''Single Inheritance'''
# class key_phone():
#     def __init__(self,name,brand,model):
#         self.name=name
#         self.brand=brand
#         self.model=model
#     def calling(self,number):
#         print(" your calling from ",number)
#     def texting(self,number,message):
#         print(f"your sending {message} to {number}")
# class smart_phone(key_phone):
#     def app(self,appname):
#         print(f"using {appname} on {self.name}")
# #Object creation
# my_phone=smart_phone("Samsung_10","samsung","z series")
# my_phone.app("whatsapp")
# my_phone.calling(9885320901)
'''Polymorphism'''
'''Overloading 
1.Over loading 
    a.Operator Overloading 
    b.Method Overloading
2.Method overiding '''

#Operator over loading 
# class sample():
#     def add(self,a,b):#def
#         return print(a+b)#Here the Operator + used for int and string 
# obj=sample()
# obj.add(10,20)
# obj.add("Ramesh ","Babu")
#Method Over loading
# class sample():
#     def add(self,a,b):#def1
#         print(a,b)
#     def add(self,a,b,c):#def2
#         print(a,b,c)
# obj=sample()
# obj.add(20,30)
# obj.add(20,30,40)      
#Here its not calling the   def1 as Python will not directly support method over loading 
#Achieved using default paramenter values

# class sample():
#     def add(self,a=None,b=None,c=None):#def2
#         print(a,b,c)
# obj=sample()
# obj.add(1,2,3)
# obj.add(1,2)
# obj.add(1)
# obj.add()
# obj.add("Hi","Hello","Namasthe")
# obj.add("Hi","Hello")
# obj.add("Hi")
# obj.add()

#Method overloading
# class father():#Base Method
#     def details(self,a):
#         print("This is father class")
#         print(a)
# class child(father):#Derived Method
#     def details(self, a):
#         print("This is child class") 
#         print(a)      
# obj=child()
# obj.details("100 C")#Here we cannot access the base class directly
'''Super'''
'''To access the base class in method over riding whe use a key word called SUPER '''
# class father():#Base Method
#     def details(self,a):
#         print("This is father class")
#         print(a)
# class child(father):#Derived Method
#     def details(self, a):
#         print("This is child class") 
#         print(a)    
#         super().details(1234) #SUPER refers to base class
# obj=child()
# obj.details("100 C")#Here we cannot access the base class directly

#Encaptulation
'''It provides the ssecurity to data 
1.public-Any one can access
2.Protect--Only thoses classes access to specified with _(Single underscore)
3.Private--Only with in the class specified with __(Double unserscore)'''

'''ublic'''
# class gfather():
#     def __init__(self,a):
#         self.a=a
#         print(a)    
# obj=gfather("100cr")

# class gfather():
#     def __init__(self,a):
#         self.a=a
#         print(a)
# class father(gfather):
#     def display(self):
#         print(self.a)        
# obj=father("100cr")
# obj.display()
'''Protect'''
# class gfather():
#     def __init__(self,a):
#         self._a=a
#         print(a)
# class father(gfather):
#     def display(self):
#         print(self._a)
# obj=father("100cr")
# obj.display()

'''Private'''
# class gfather():
#     def __init__(self,a):
#         self.__a=a
#         print(a+10)
# class father(gfather):
#     def display(self):
#         print(self.__a)
# obj=father(1000)#Only this base call method will run
# obj.display()#It will through an error as we are calling the public data in base class __

'''Data abstraction'''
'''Hiding the Implementation but showing the only essential adn necessary information
A class is a abstract when it takes the argument as import method 'ABC' .
Import syntex: from abc import ABC,abstract method
If we define any methods in abstract class then it should be implemented in derived class'''

from abc import ABC, abstractmethod
class payment(ABC):
    @abstractmethod#This is called as decorators
    def payment_processing(self):
       # print(f" this is base class")
        pass
class gpay(payment):
    def payment_processing(self,amount):#Same method definition as like in base class
        print(f"Processing {amount} using Gpay")
class phonepay(payment):
    def payment_processing(self,amount):#Same method definition as like in base class
        print(f"Processing {amount} using Phonepay")
obj=gpay()
obj.payment_processing(1000)
obj=phonepay()
obj.payment_processing(5000)

