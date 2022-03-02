import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QToolBar
from PyQt5.QtWidgets import QAction, QTabWidget
from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QStackedWidget,QWidget, QHBoxLayout, QMenuBar
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtCore import Qt, QSize

from UI.customizelabel import CustomizeLabel
from UI.customizetabwidget import CustomizeTabWidget
from UI.customizepushbutton import CustomizePushButton

from Data.vehicles import Vehicles

class Window(QWidget):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.x=100
        self.y=100
        self.width=1300
        self.height=910
        self.setGeometry(self.x,self.y,self.width,self.height)
        self.setMinimumSize(self.width, self.height)
        self.setStyleSheet("background:rgb(255,255,255)")
        self.setWindowTitle('Fahrzeugbuchungs - Tool')

        self.maintext = CustomizeLabel("Eximia Engineering GmbH")

        self.exitBtn = CustomizePushButton("Beenden")
        self.exitBtn.closeApplication()

        self.goBackBtn = CustomizePushButton("Zurück")

        self.StackedWidget=QStackedWidget()
        self.CalendarWindow = CalendarWindow()
        self.StackedWidget.addWidget(self.CalendarWindow)

        WindowLayout=QVBoxLayout()
        WindowLayout.addWidget(self.maintext)
        WindowLayout.addWidget(self.StackedWidget)

        btnLayout = QHBoxLayout()
        btnLayout.addWidget(self.goBackBtn)
        btnLayout.addStretch(1)
        btnLayout.addWidget(self.exitBtn)

        WindowLayout.addLayout(btnLayout)

        self.setLayout(WindowLayout)



class CalendarWindow(QWidget):
    """CalendarWindow"""
    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QVBoxLayout(self)
        
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tabs.setFont(QFont("Arial", 10, QFont.Bold))
        
        # Add tabs
        self.createVehiclesTab()

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)


    def createVehiclesTab(self):
        all_vehicles = Vehicles().getAllVehicles()

        for v in all_vehicles:
            v_tab = CustomizeTabWidget(v)
            self.tabs.addTab(v_tab, v.getModel())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    win = Window()
    win.show()
    sys.exit(app.exec_())