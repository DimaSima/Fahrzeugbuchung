

class Vehicle:
	def __init__(self, name): 
		self.name = name
		self.vin = 0
		self.mib_sw = None
		self.mib_hw = None


	def getName(self):
		return self.name

	def getVin(self):
		return self.vin
		
