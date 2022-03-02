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
		self.width=700
		self.height=700
		self.LINESIZE = 200
		self.BUTTONSIZE = 150

		self.setGeometry(self.x,self.y,self.width,self.height)
		self.setMinimumSize(self.width, self.height)
		self.setWindowTitle('Fahrzeugbuchung für das Fahrzeug: ' + self.vehicle.getModel())

		WindowLayout=QVBoxLayout()

		self.label = QLabel("Datum: "+self.selectedDate)
		WindowLayout.addWidget(self.label)
		WindowLayout.addStretch(1)

		# VIN Column
		vinCol = QHBoxLayout()
		vinLabel = QLabel("VIN: "+str(vehicle.getVin()))
		vinLine = QLineEdit(self)
		vinLine.setPlaceholderText("Neue Vin einfügen")
		vinLine.setMaximumWidth(self.LINESIZE)
		vinBtn = QPushButton("Vin speichern")
		vinBtn.setMaximumWidth(self.BUTTONSIZE)
		vinBtn.clicked.connect(lambda: vinLabel.setText("VIN: "+vinLine.text()))
		vinCol.addWidget(vinLabel)
		vinCol.addWidget(vinLine)
		vinCol.addWidget(vinBtn)

		# MIB SW Column
		mib_sw_Col = QHBoxLayout()
		mib_sw_Label = QLabel("MIB SW: "+str(vehicle.getMIBSW()))
		mib_sw_line = QLineEdit(self)
		mib_sw_line.setPlaceholderText("Neue MIB SW einfügen")
		mib_sw_line.setMaximumWidth(self.LINESIZE)
		mib_sw_Btn = QPushButton("MIB SW speichern")
		mib_sw_Btn.setMaximumWidth(self.BUTTONSIZE)
		mib_sw_Btn.clicked.connect(lambda: mib_sw_Label.setText("MIB SW: "+mib_sw_line.text()))
		mib_sw_Col.addWidget(mib_sw_Label)
		mib_sw_Col.addWidget(mib_sw_line)
		mib_sw_Col.addWidget(mib_sw_Btn)

		# Add all Layouts
		WindowLayout.addLayout(vinCol)
		WindowLayout.addLayout(mib_sw_Col)


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


