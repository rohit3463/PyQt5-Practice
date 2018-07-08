from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtCore import Qt 
import sys

class App(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):

		self.setGeometry(300,300,300,350)
		self.setWindowTitle('Event handler')
		self.show()

	def keyPressEvent(self,e):

		if e.key() == Qt.Key_Escape:
			self.close()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = App()
	sys.exit(app.exec_())