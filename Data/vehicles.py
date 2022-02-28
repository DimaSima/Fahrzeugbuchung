
from enum import Enum

from Data.vehicle import Vehicle

class Models(Enum):
	J1 = 1
	_992 = 2 
	E3 = 3



class Vehicles:
	def __init__(self):
		self.allVehicles = []
		self.allVehiclesName = ["J1", "992", "E3", "Macan"]
		self.countAllVehicles = len(self.allVehiclesName)

		self.loadAllVehicles()



	def loadAllVehicles(self):
		for v in self.allVehiclesName:
			vehicleModel = Vehicle(v)
			self.allVehicles.append(vehicleModel)


	def getAllVehicles(self):
		return self.allVehicles

	#def getSpecificVehicle(self,name):
	#	return list(filter(lambda x: x == name, for v in self.allVehicles.getName())

