"""Division By zero error"""
a=int(input("Enter Number1?"))
b=int(input("Enter Number2?"))
try:
	print("Division reuslt: ",a/b)
except ZeroDivisionError:
	print("Cannot divide number by zero")	