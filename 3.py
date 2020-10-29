"""Sum of digits"""
number=int(input("Enter number?"))
sum_of_digits=0
while(number!=0):
	digit=number%10
	sum_of_digits+=digit
	number=number//10
print("Sum ",sum_of_digits)	
