"""Check odd or even using function"""
def isEven(number):
	if number%2==0:
		return True
	return False	

number=int(input("Enter number?"))
if isEven(number):print("Even")
else:print("Odd")	

