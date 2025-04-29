#Code to buit a ATM using class

class activity():
    def __init__(self,name,branch,location,accttype):
        self.name=name
        self.__branch=branch
        self.location=location
        self._accttype=accttype
        self.balance=0
        self.transaction=[]
        print(f"\nWelcome to {self.name} ATM,{self.location}")
    def main_menu(self):  
        print('''
         1. Deposit
         2. Withdraw
         3. Balance_enquiry
         4. Pin change
         5. Exit''')
    def deposit(self):
         amount=int(input("Enter the amount to be deposited:"))
         if  amount> 0:
          self.balance+=amount
          self.transaction.append({amount})
          print(f"\n₹ {amount} credited to your {self._accttype}account.")
         else:
          print("Invalid Amount")
         
    def withdraw(self):
        #global balance
        amount=int(input("\nEnter the amount to withdraw:"))
        if self.balance<amount:
         print("Insufficient balance in account.")
        else:
         self.balance -=amount
         self.transaction.append({amount})
         print(f"₹ {amount} withdrawl from your {self._accttype} account.")
    def pinchange(self):
        pin=int(input("Enter the current pin:"))
        if pin>1000 and pin<10000:
           newpin=int(input("Enter new pin:"))
           if newpin==pin:
            print("Old pin not accepted.")
           else:
            print("New pin updated succesfully.") 
        else:
           print("Invalid pin)")
    def start(self):
        while True:
            self.main_menu()
            choice = input("Enter your option (1-5): ")

            if choice == '1':
                self.deposit()
            elif choice == '2':
                self.withdraw()
            elif choice == '3':
                self.bal_enquiry()
            elif choice=='4':
               self.pinchange()
            elif choice == '5':
                print(f"Thank you for using the {self.name} ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
class bal(activity):         
    def bal_enquiry(self):
        print(f"\nYour account balance is: ₹{self.balance} .You checked your balance at {self.__branch} branch")
        #print(self.newpin)
obj=bal("HDFC","VRTR","Varthur","savings")
obj.start()
