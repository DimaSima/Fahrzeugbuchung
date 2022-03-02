
from enum import Enum
import pandas as pd

from Data.vehicle import Vehicle

class Models(Enum):
	J1 = 1
	_992 = 2 
	E3 = 3



class Vehicles:
	def __init__(self):
		self.allVehicles = []

		self.excelData = pd.read_excel('Fahrzeuge.xlsx')
		self.allVehiclesModel = self.excelData.loc[:,'Model']
		self.countAllVehicles = len(self.allVehiclesModel)
		self.allVehiclesVIN = self.excelData.loc[:,'VIN']
		self.allVehiclesKennzeichen = self.excelData.loc[:,'Kennzeichen']
		self.allVehiclesMIBSW = self.excelData.loc[:,'MIB SW']

		self.loadAllVehicles()



	def loadAllVehicles(self):
		#for v in self.allVehiclesName:
		#	vehicleModel = Vehicle(v)
		#	self.allVehicles.append(vehicleModel)

		for i in range(self.countAllVehicles):
			model = self.allVehiclesModel[i]
			vin = self.allVehiclesVIN[i]
			kennzeichen = self.allVehiclesKennzeichen[i]
			mib_sw = self.allVehiclesMIBSW[i]
			vehicleModel = Vehicle(model,vin,kennzeichen,mib_sw)
			self.allVehicles.append(vehicleModel)


	def getAllVehicles(self):
		return self.allVehicles

	#def getSpecificVehicle(self,name):
	#	return list(filter(lambda x: x == name, for v in self.allVehicles.getName())

