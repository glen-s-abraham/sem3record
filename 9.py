"""List operations"""
uset=set()
i=0
while i!=6:
	print("\n1.Add to set\n2.Remove from set\n3.Print set\n4.Count Elements of set\n5.Find element in set\n6.Clear set and Exit")
	i=int(input("Enter Option\n"))
	if i==1:
		element=input("EnterElement:")
		uset.add(element)	
	elif i==2:
		print(uset)
		pos=input("Enter element to delete")
		uset.discard(pos)
	elif i==3:
		print(uset)	
	elif i==4:	
		print(len(uset))
	elif i==5:
		pos=input("Enter element  to find in set")
		if pos in uset:
			print("Element found")
	elif i==6:					
		uset.clear()
		break		