from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QGridLayout,QStatusBar
from PyQt5.QtCore import Qt
import sys

class App(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		grid = QGridLayout()
		self.statusbar = QStatusBar(self)

		btn1 = QPushButton('Button 1',self)
		btn1.resize(btn1.sizeHint())
		btn2 = QPushButton('Button 2',self)
		btn2.resize(btn2.sizeHint())
		grid.setSpacing(10)

		grid.addWidget(btn1,1,0)
		grid.addWidget(btn2,1,1)
		grid.addWidget(self.statusbar,3,0,Qt.AlignBottom)

		btn1.clicked.connect(self.buttonClicked)
		btn2.clicked.connect(self.buttonClicked)

		self.setGeometry(300,300,300,350)
		self.setWindowTitle('Event Sender')

		self.setLayout(grid)

		self.show()

	def buttonClicked(self):

		sender = self.sender()
		self.statusbar.showMessage(sender.text() + ' was pressed')

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = App()

	sys.exit(app.exec_())
