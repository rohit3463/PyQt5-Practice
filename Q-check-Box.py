from PyQt5.QtWidgets import QWidget,QApplication,QCheckBox
from PyQt5.QtCore import Qt 
import sys

class App(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		self.ch = QCheckBox('check me',self)
		self.ch.toggle()
		self.ch.stateChanged.connect(self.titlehide)

		self.setGeometry(300,300,300,350)
		self.setWindowTitle('check box for title hide')
		self.show()

	def titlehide(self,state):

		if state == Qt.Checked:
			self.setWindowTitle('check box for title hide')

		else:
			self.setWindowTitle('')

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = App()
	sys.exit(app.exec_())