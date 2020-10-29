"""File operations"""
i=0
while i!=5:
	print("1.Create File\n2.Write to file\n3.Append To file\n4.Read from file\n5.Exit")
	i=int(input("Enter Option?"))
	if i==1:
		fname=input("enter Filename:")
		try:
			file=open(fname,'x')
			print("Created")
		except Exception:
			print("File already present")	
	elif i==2:
		fname=input("enter Filename:")
		try:
			file=open(fname,'w')
			print("File Opened")
			fstr=input("Enter string to write to file:")
			file.write(fstr)
			file.close()
		except Exception:
			print("File Not Found")	
	elif i==3:
		fname=input("enter Filename:")
		try:
			file=open(fname,'a')
			print("File Opened")
			fstr=input("Enter string to write to file:")
			file.write(fstr)
			file.close()
		except Exception:
			print("File Not Found")	
	elif i==4:
		fname=input("enter Filename:")
		try:
			file=open(fname,'r')
			print("File Opened")
			for line in file:
				print(line)
			file.close	
		except Exception:
			print("File Not Found")							 
	elif i==5:
		break		