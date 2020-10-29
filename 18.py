"""Package arithmetic function"""
from Arithmetics import *

i=0
while i!=6:
	print("\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Remainder\n6.Exit")
	i=int(input("Enter Option"))
	num1=int(input("Enter number1?"))	
	num2=int(input("Enter number2?"))
	if i==1:
		print(add(num1,num2))
	if i==2:
		print(sub(num1,num2))
	if i==3:
		print(mul(num1,num2))
	if i==4:
		print(div(num1,num2))
	if i==5:
		print(mod(num1,num2))
	if i==6:
		break				