"""List operations"""
ulist=[]
i=0
while i!=9:
	print("\n1.Add to list\n2.Remove from list\n3.Print List\n4.Count Element of list\n5.Find element index\n6.Sort List\n7.Reverse\n8.Delete list\n9.Exit")
	i=int(input("Enter Option\n"))
	if i==1:
		element=input("EnterElement:")
		pos=input("Enter postion to add element leave blank to append to end:")
		if(pos):
			ulist.insert(int(pos),element)
		else:
			ulist.append(element)	
	elif i==2:
		print(ulist)
		pos=input("Enter postion to remove element leave blank to remove from end:")
		if(pos):
			ulist.pop(int(pos))
		else:
			ulist.pop()
	elif i==3:
		print(ulist)	
	elif i==4:	
		pos=input("Enter element  to count")
		print(ulist.count(pos))
	elif i==5:
		pos=input("Enter element  to find index of")
		print(ulist.index(pos))
	elif i==6:
		ulist.sort()					
	elif i==7:
		ulist.reverse()	
	elif i==8:
		ulist.clear()
		break		