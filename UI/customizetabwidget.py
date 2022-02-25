from PyQt5.QtWidgets import QVBoxLayout,QLabel,QWidget, QHBoxLayout, QCalendarWidget
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QFont



class CustomizeTabWidget(QWidget):
	def __init__(self):
		super().__init__()
		vbox = QVBoxLayout()
		self.calendar = QCalendarWidget()
		self.calendar.setGridVisible(True)
		self.calendar.selectionChanged.connect(self.calendar_date)
		self.calendar.showToday()
		self.calendar.setMinimumDate(QDate.addDays(QDate.currentDate(),-5))
		self.calendar.setMaximumDate(QDate.addDays(QDate.currentDate(),+5))

		#self.label =QLabel("Hello")
		#self.label.setFont(QFont("Sanserif", 15))
		#self.label.setStyleSheet('color:red')

		vbox.addWidget(self.calendar)
		#vbox.addWidget(self.label)

		self.setLayout(vbox)

	def calendar_date(self):
		dateselected = self.calendar.selectedDate()
		date_in_string = str(dateselected.toPyDate())

		#self.label.setText("Date Is : " + date_in_string)

