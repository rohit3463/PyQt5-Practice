from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QGridLayout
from PyQt5.QtCore import Qt 
import sys

class App(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setGeometry(300,300,300,350)
		self.setWindowTitle('Mouse Event handler')

		x =0
		y =0

		self.text = "x:{0},y:{1}".format(x,y)
		self.label = QLabel(self.text,self)
		grid = QGridLayout()
		grid.addWidget(self.label,0,0,Qt.AlignTop)

		self.setMouseTracking(True)

		self.setLayout(grid)

		self.show()

	def mouseMoveEvent(self, e):
		x = e.x()
		y = e.y()

		text = "x:{0},y:{1}".format(x,y)
		self.label.setText(text)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = App()
	sys.exit(app.exec_())