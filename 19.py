queue=[]
i=0
while i!=4 :
	print("1.Enqueue\n2.Dequeue\n3.Print Queue\n4.Exit")
	i=int(input("Enter Option?"))
	if i==1:
		element=input("Enter Elemet to add? ")
		queue.append(element)
	if i==2:
		
		if len(queue)>0:
			element=queue.pop(0)
			print("popped element",element)
		else:	
			print("Empty Queue")	
	if i==3:
		print(queue)
	if i==4:
		break		
		