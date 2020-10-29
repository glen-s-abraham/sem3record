"""Multi level"""
class Student(object):
	studentCount=0
	def getStudent(self,rollno,name,course):
		self.rollno=rollno
		self.name=name
		self.course=course
		Student.studentCount+=1
	def displayStudent(self):
		print("Roll No:",self.rollno)
		print("Name   :",self.name)
		print("Course :",self.course)	

class Test(Student):
	def getMarks(self,marks):
		self.marks=marks
	def displayMarks(self):
		print("Marks  :",self.marks)

class Result(Test):
	def calculateGrade(self):
		if self.marks>480:self.grade="Distinction"
		elif self.marks>360:self.grade="First Class"
		elif self.marks>240:self.grade="Second Class"
		else:self.grade="Failed"
		print("Result:",self.grade)

r=int(input("Enter rollno?"))
n=input("Enter name?")
c=input("Enter Course?")
m=int(input("Enter Marks?"))

stud=Result()
stud.getStudent(r,n,c)
stud.getMarks(m)
stud.displayStudent()
stud.displayMarks()
stud.calculateGrade()	
