stack=[]
i=0
while i!=4 :
	print("1.Push\n2.Pop\n3.Print Stack\n4.Exit")
	i=int(input("Enter Option?"))
	if i==1:
		element=input("Enter Elemet to push? ")
		stack.insert(0,element)
	if i==2:
		if len(stack)>0:
			element=stack.pop(0)
			print("popped element",element)
		else:	
			print("Empty Stack")	
	if i==3:
		print(stack)
	if i==4:
		break		
		