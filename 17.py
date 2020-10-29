f1=input("Enter file1 to merge?")
f2=input("Enter file2 to merge?")
f3=input("Enter name of merged file?")
try:
	mergefile=open(f3,'w')
	file=open(f1,'r')
	for line in file:
		print("Writing:",line," to ",f3)
		mergefile.write(line)
	file.close()	
	file=open(f2,'r')
	for line in file:
		print("Writing:",line," to ",f3)
		mergefile.write(line)
	file.close()
	mergefile.close()
	mergefile=open(f3,'r')
	print("Contents of ",f3)
	for line in mergefile:
		print(line)	
except Exception:
	print("Files don't exist")	