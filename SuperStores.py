'''    
Creating a Program to build a Billing system for a Super Market
1.Available Items in the store
2.Adding the Items and the Qantity
3.Creating the final bill which icludes GST,Default discount and any Coupon codes in a Dot matrix format

'''
customer_name=input("Please Enter your name:")
print(
    '''      A1 Super Market
    Bengalore -560087''')
product_list=('''
1.Rice          30 Rs Per/Strip
2.Sugar         40 Rs Per/Kg
3.Oil           180 Rs Per/Ltr
4.Salt          30 Rs Per/Kg
5.Aata          45 Rs Per/Kg
6.Groundnuts    140 Rs Per/Kg
7.Exit''')
#Declaration
price=0#Initial value is 0 & this will be used in adding price ,when products are added to cart
Totalprice=0#Initially it will be 0 & Price will be added to this.
Finalprice=0#Initially it will be 0 & Total will be added to this.
pricelist = []# When a item/Product is added this List will append
discount=0
tax=0
ilist=[]#Items/Products will be added in cart are added to this list
plist=[]#Price of the Item will be added to this list
qlist=[]#Quantity of each item added to list for a selected products
#All the products are taken in a Dictionary as a Key:value pair
Products={'rice':60,'sugar':40,'oil':180,'salt':30,'aata':45,'groundnuts':140}
while True:
  option=input("enter 1 for Shopping OR 2 for Exit: ")
  if option=='2':
    print("Thanks you for Shopping with Us")
    break
  elif option=='1':
    print(product_list)
    while True:
      cust_choice=input("Enter 1 to buy or 2 to exit:")
      if cust_choice=='2':
        print("Thank you for shoppig with Us")
        break
      elif cust_choice=='1':
        item=input("Select the item from above list:").lower()
        while True:
          quantity=input("Enter quantity of selected item:")
          if quantity.isdigit():
            quantity=int(quantity)
            break
          else:
            print("Enter a valied Quantity")
        if item in Products:
          price=quantity*Products[item]
          pricelist.append((item,quantity,Products[item],price))
          Totalprice+=price
          ilist.append(item)
          qlist.append(quantity)
          plist.append(price)
        else:
          print(f"{item}] out of stocke.Sorry for inconvience")
    if Totalprice>0:
     tax=(Totalprice*12)/100
     Finalprice=tax+Totalprice
     if Finalprice>1000:
       discount=(Finalprice*5)/100
       Finalprice-=discount
    else:
      Finalprice
    print(25 * "=", "A1 Super Market", 25 * "=")
    print(28 * " ", "Bengalore")
    print("Name:", customer_name, 30 * " ")
    print(60 * "-")   
    print("sno", 10 * " ", 'items', 8 * " ", 'quantity',8 * " ",  'price')
    for i in range(len(pricelist)):
            #print(len(pricelist))
        print(i+1, 13 * " ",ilist[i], 8 * " ",qlist[i], 15 * " ",plist[i])  
    print(60 * "-")
    print(35 * " ", 'Total amount:', 'Rs', Totalprice)
    print("Tax amount", 35 * " ", 'Rs', tax)
    print("Discount amount", 30 * " ", '(-)Rs', discount)
    print(70* "-")
    print(35 * " ", 'Final amount:', 'Rs', Finalprice)
    print(70 * "-")
    print(20 * " ", "Thank you & Visit again")
    print(70 * "-")