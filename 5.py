"""Fibonacci series with recursion"""
def fibonacci(number):
	if number==1:
		return 0
	elif number==2:
		return 1
	else:
		return fibonacci(number-1)+fibonacci(number-2) 			

number=int(input("Enter number?"))
for i in range(1,number+1):
	print(fibonacci(i))		