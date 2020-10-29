"""class Implementation"""
class Customer:
	def getData(self,name,accno,acctype,balance):
		self.name=name
		self.accno=accno
		self.acctype=acctype
		self.balance=balance
	def displayCustomer(self):
		print("Customer Name :",self.name)
		print("Account Number:",self.accno)
		print("Account Type  :",self.acctype)
		print("Balance Amount:",self.balance)
	def deposit(self,amount):
		self.balance+=amount	
	def withdrawal(self,amount):
		if self.balance-amount<0:print("Insufficient Funds")
		else:self.balance-=amount		
ch=0
while ch!=5:
	print("1.New Customer\n2.Deposit\n3.Withdrawal\n4.Display\n5.Exit")
	ch=int(input("Enter Option?"))
	if ch==1:
		obj=Customer()
		n=input("Enter name?")
		no=int(input("Enter accno?"))
		t=input("Enter Type(SB/C)?")
		b=int(input("Enter balance?"))
		obj.getData(n,no,t,b)
	elif ch==2:
		b=int(input("Enter Amount?"))
		obj.deposit(b)
	elif ch==3:
		b=int(input("Enter Amount?"))
		obj.withdrawal(b)	
	elif ch==4:
		obj.displayCustomer()	
	else:
		break	