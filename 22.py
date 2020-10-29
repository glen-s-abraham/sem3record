"""Abstraction"""
class Computer:
	def __init__(self):
		self.__maxprice=900
	def sell(self):
		print("Selling price ",self.__maxprice)
	def setMaxprice(self,amount):
		self.__maxprice=amount

mac=Computer()
mac.sell()
mac.__maxprice=1000#private member not accessible from outside class
mac.sell()
mac.setMaxprice(1000)
mac.sell()			