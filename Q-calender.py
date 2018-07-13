from PyQt5.QtWidgets import QWidget,QApplication,QCalendarWidget,QLabel,QGridLayout,QHBoxLayout,QVBoxLayout
from PyQt5.QtCore import QDate
import sys

class App(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		grid = QGridLayout()

		self.cal = QCalendarWidget()
		self.cal.clicked[QDate].connect(self.showDate)

		self.lbl = QLabel(self)

		date = self.cal.selectedDate()

		self.lbl.setText(date.toString())

		grid.addWidget(self.cal,1,0,5,0)
		grid.addWidget(self.lbl,6,0)

		self.setLayout(grid)

		self.setGeometry(400,500,400,500)

		self.setWindowTitle('Q-calender')

		self.show()

	def showDate(self,date):
		self.lbl.setText(date.toString())

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = App()
	sys.exit(app.exec_())