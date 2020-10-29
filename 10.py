"""Calculator using functions"""

def add(a,b):
	return a+b

def subtract(a,b):
	return a-b	

def multipy(a,b):
	return a*b	

def divide(a,b):
	return a/b	

def remainder(a,b):
	return a%b	

i=0
while i!=6:
	print("\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Remainder\n6.Exit")
	i=int(input("Enter Option"))
	num1=int(input("Enter number1?"))	
	num2=int(input("Enter number2?"))
	if i==1:
		print(add(num1,num2))
	if i==2:
		print(subtract(num1,num2))
	if i==3:
		print(multipy(num1,num2))
	if i==4:
		print(divide(num1,num2))
	if i==5:
		print(remainder(num1,num2))
	if i==6:
		break					
