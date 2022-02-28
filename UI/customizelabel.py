from PyQt5.QtWidgets import QVBoxLayout,QLabel,QWidget, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont




class CustomizeLabel(QWidget):
    def __init__(self,text):
        super().__init__()
        self.text = text
        self.initUI()

    def initUI(self):
        label = QLabel(self)
        label.setText(self.text)
        label.setAlignment(Qt.AlignCenter)
        label.setFont(QFont("Arial", 14, QFont.Bold))

        labelLayout=QHBoxLayout()
        labelLayout.addWidget(label)

        self.setLayout(labelLayout)
        #self.show()