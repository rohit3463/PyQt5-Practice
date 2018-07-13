from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtCore import pyqtSignal,QObject
import sys

class Communicate(QObject):

	closeApp = pyqtSignal()

class App(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):

		self.c = Communicate()

		self.c.closeApp.connect(self.close)

		self.setGeometry(300,300,300,350)

		self.setWindowTitle('Emit Signal')

		self.show()

	def mousePressEvent(self,event):

		self.c.closeApp.emit()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()

	sys.exit(app.exec_())