"""Polymorphism"""

class Parrot:
	def fly(self):
		print("Parrot can fly")
	def swim(self):
		print("Parrot can't swim")

class Penguin:
	def fly(self):
		print("Penguins can't fly")
	def swim(self):
		print("Penguins can swim")			

def func(obj): 
       obj.fly() 
       obj.swim()

obj_parrot=Parrot()
obj_penguin=Penguin()

func(obj_parrot)
func(obj_penguin)       		