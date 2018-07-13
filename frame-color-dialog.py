from PyQt5.QtWidgets import QWidget,QApplication,QFrame,QPushButton,QColorDialog
from PyQt5.QtGui import QColor
import sys

class App(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		col = QColor(0,0,0)
		self.frm = QFrame(self)
		self.btn = QPushButton('Dialog',self)

		self.btn.clicked.connect(self.showDialog)

		self.frm.setStyleSheet("QWidget {background-color: %s}" % col.name())

		self.frm.setGeometry(100,100,100,150)

		self.setGeometry(300,300,300,350)
		self.setWindowTitle('change frame color')
		self.show()

	def showDialog(self):

		col = QColorDialog.getColor()

		if col.isValid():
			self.frm.setStyleSheet("4QWidget {background-color: %s}" % col.name())

if __name__ == '__main__':

	app = QApplication(sys.argv)
	window = App()

	sys.exit(app.exec_())