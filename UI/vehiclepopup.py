from PyQt5.QtWidgets import QVBoxLayout,QLabel,QWidget, QHBoxLayout, QCalendarWidget, QToolButton, QLineEdit, QPushButton
from PyQt5.QtCore import Qt, QDate, QSize
from PyQt5.QtGui import QFont

from UI.customizepushbutton import CustomizePushButton


class VehiclePopUp(QWidget):
	def __init__(self, vehicle, selectedDate):
		super().__init__()
		"""Data values"""
		self.vehicle = vehicle
		self.selectedDate = selectedDate
		""" Popup values"""
		self.x=100
		self.y=100
		self.width=500
		self.height=500
		self.setGeometry(self.x,self.y,self.width,self.height)
		self.setMinimumSize(self.width, self.height)
		self.setWindowTitle('Fahrzeugbuchung für das Fahrzeug: ' + self.vehicle.getModel())

		WindowLayout=QVBoxLayout()

		self.label = QLabel("Datum: "+self.selectedDate)
		WindowLayout.addWidget(self.label)
		WindowLayout.addStretch(1)

		firstCol = self.createNewColumn("VIN: ", vehicle.getVin(), "Neue Vin einfügen", "Vin speichern")

		WindowLayout.addLayout(firstCol)

		self.setLayout(WindowLayout)



	def createNewColumn(self,labelText, labelValue, placeHolderText, btnText):
		firstCol = QHBoxLayout()
		vinLabel = QLabel(labelText+str(labelValue))
		line = QLineEdit(self)
		line.setPlaceholderText(placeHolderText)
		vinBtn = CustomizePushButton(btnText)
		firstCol.addWidget(vinLabel)
		firstCol.addWidget(line)
		firstCol.addWidget(vinBtn)

		return firstCol

