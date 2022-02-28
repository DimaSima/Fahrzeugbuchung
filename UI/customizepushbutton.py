from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QVBoxLayout,QLabel,QWidget, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class CustomizePushButton(QWidget):
	def __init__(self,text):
		super().__init__()
		self.text = text
		self.initUI()


	def initUI(self):
		self.btn = QPushButton(self.text,self)
		self.btn.setFont(QFont("Arial", 14, QFont.Bold))
		self.btn.setStyleSheet("QPushButton {background-color:rgb(51,65,82); color:white;}")
		self.btn.setMaximumWidth(200)

		btnLayout=QHBoxLayout()
		btnLayout.addWidget(self.btn)

		self.setLayout(btnLayout)


	def closeApplication(self):
		self.btn.clicked.connect(QApplication.instance().quit)
