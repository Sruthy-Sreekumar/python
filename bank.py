class Bank_Account:
 def __init__(self):
  self.balance=0
  print("Hello,welcome to deposit & withdrawal machine")
 def deposit(self):
  amount=float(input("Enter the amount to be deposited:"))
  self.balance=amount
  print("Amount deposited:",amount)
 def withdraw(self):
  amount=float(input("Enter the amount to be withdrawn:"))
  if(self.balance>=amount):
   self.balance=self.balance-amount
   print("You withdrew:",amount)
  else:
   print("Insufficient balance")
 def display(self):
   print("Net available balance=",self.balance)
l=Bank_Account()
l.deposit()
l.withdraw()
l.display()
   
