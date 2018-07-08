from PyQt5.QtWidgets import QWidget,QApplication,QLCDNumber,QSlider,QVBoxLayout
from PyQt5.QtCore import Qt 
import sys

class App(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		lcd = QLCDNumber(self)
		sld = QSlider(Qt.Horizontal,self)

		vbox = QVBoxLayout()
		vbox.addWidget(lcd)
		vbox.addWidget(sld)

		self.setLayout(vbox)
		sld.valueChanged.connect(lcd.display)

		self.setGeometry(300,300,300,350)
		self.setWindowTitle('Signal and slot')
		self.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
