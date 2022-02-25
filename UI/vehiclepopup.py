from PyQt5.QtWidgets import QVBoxLayout,QLabel,QWidget, QHBoxLayout, QCalendarWidget, QToolButton
from PyQt5.QtCore import Qt, QDate, QSize
from PyQt5.QtGui import QFont


class VehiclePopUp(QWidget):
	def __init__(self, vehicle):
		super().__init__()
		self.vehicle = vehicle
		self.x=100
		self.y=100
		self.width=500
		self.height=300
		self.setGeometry(self.x,self.y,self.width,self.height)
		self.setMinimumSize(self.width, self.height)

		WindowLayout=QVBoxLayout()

		self.label = QLabel("Another Window")
		WindowLayout.addWidget(self.label)
		self.setLayout(WindowLayout)
