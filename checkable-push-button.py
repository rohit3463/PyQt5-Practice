from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QFrame,QGridLayout,QHBoxLayout
from PyQt5.QtGui import QColor
import sys

class App(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):\

		self.col = QColor(0,0,0)

		grid = QGridLayout()
		hbox = QHBoxLayout()

		red = QPushButton('Red',self)
		green = QPushButton('green',self)
		blue = QPushButton('blue',self)

		red.setCheckable(True)
		green.setCheckable(True)
		blue.setCheckable(True)

		self.frame = QFrame(self)

		red.clicked[bool].connect(self.change_col)
		green.clicked[bool].connect(self.change_col)
		blue.clicked[bool].connect(self.change_col)

		hbox.addWidget(red)
		hbox.addWidget(green)
		hbox.addWidget(blue)

		grid.addLayout(hbox,1,0)
		grid.addWidget(self.frame,2,0)

		self.frame.setStyleSheet("QFrame {background-color : %s}" %self.col.name())

		self.setLayout(grid)

		self.setGeometry(300,300,300,350)
		self.setWindowTitle('change frame color')
		self.show()

	def change_col(self,pressed):

		source = self.sender()
		if pressed:
			val = 255
		else:
			val = 0

		if source.text() == 'Red':
			self.col.setRed(val)
		elif source.text() == 'blue':
			self.col.setBlue(val)
		elif source.text() == 'green':
			self.col.setGreen(val)

		self.frame.setStyleSheet("QFrame {background-color : %s}" %self.col.name())

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = App()
	sys.exit(app.exec_())







