

class Vehicle:
	def __init__(self, model, vin, kennzeichen, mib_sw): 
		self.model = model
		self.vin = vin
		self.kennzeichen = kennzeichen
		self.mib_sw = mib_sw
		self.mib_hw = None


	def getModel(self):
		return self.model

	def getVin(self):
		return self.vin

	def getKennzeichen(self):
		return self.kennzeichen
		
