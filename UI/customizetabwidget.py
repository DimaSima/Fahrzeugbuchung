from PyQt5.QtWidgets import QVBoxLayout,QLabel,QWidget, QHBoxLayout, QCalendarWidget, QToolButton
from PyQt5.QtCore import Qt, QDate, QSize
from PyQt5.QtGui import QFont

from UI.vehiclepopup import VehiclePopUp

class CustomizeTabWidget(QWidget):
	def __init__(self, vehicle):
		super().__init__()
		vbox = QVBoxLayout()
		self.calendar = QCalendarWidget()
		self.calendar.setGridVisible(False)
		self.calendar.selectionChanged.connect(self.calendar_date)
		self.calendar.showToday()
		self.calendar.setMinimumDate(QDate.addDays(QDate.currentDate(),-7))
		self.calendar.setMaximumDate(QDate.addDays(QDate.currentDate(),+7))
		self.calendar.activated.connect(self.openVehiclePopUp)		# double click event
		self.calendar.setNavigationBarVisible(False)

		self.vehicle = vehicle

		fn = self.calendar.font()
		fn.setPointSize(10)
		self.calendar.setFont(fn)

		self.label = QLabel()

		vbox.addWidget(self.calendar)
		vbox.addWidget(self.label)

		self.setLayout(vbox)


	def openVehiclePopUp(self):
		self.vPopUp = VehiclePopUp(self.vehicle)
		self.vPopUp.show()

	def calendar_date(self):
		dateselected = self.calendar.selectedDate()
		date_in_string = str(dateselected.toPyDate())

		self.label.setText("Date Is : " + date_in_string)


	def setNavigationBarSize(self,width,height):
		prev_button = self.calendar.findChild(QToolButton, "qt_calendar_prevmonth")
		next_button = self.calendar.findChild(QToolButton, "qt_calendar_nextmonth")
		for btn in (prev_button, next_button):
			btn.setIconSize(QSize(width, height))


