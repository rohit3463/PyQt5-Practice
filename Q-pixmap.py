from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QGridLayout
from PyQt5.QtGui import QPixmap
import sys

class App(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		grid = QGridLayout()

		pixmap = QPixmap('images.png')

		self.lbl = QLabel(self)

		self.lbl.setPixmap(pixmap)

		grid.addWidget(self.lbl,1,0)

		self.setLayout(grid)

		self.setGeometry(300,300,300,350)

		self.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = App()
	sys.exit(app.exec_())