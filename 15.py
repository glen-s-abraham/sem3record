"""user defined Exception"""

class Error(Exception):
	def __init__(self,value):
		self.value=value
	def __str__(self):
		return(repr(self.value))

try:
	raise Error(6)
except Error as err:
	print("Error occured",err.value)
