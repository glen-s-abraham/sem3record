"""Factors using function"""
def getFactors(number):
	factors=[]
	for i in range(1,number+1):
		if number%i==0:
			factors.append(i)
	return factors		

number=int(input("Enter Number?"))
factors=getFactors(number)
print("Factors of number are ",factors)	