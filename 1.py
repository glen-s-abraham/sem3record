"""Second largest of 3 numbers"""
numbers=[]
numbers.append(int(input("number 1?")))
numbers.append(int(input("number 2?")))
numbers.append(int(input("number 3?")))
print("2nd largest Among",numbers,"is")
large_index=numbers.index(max(numbers))
second_largest=0
for i in range(3):
	if i==large_index:
		continue
	if numbers[i]>second_largest:
		second_largest=numbers[i]
print(second_largest)		
