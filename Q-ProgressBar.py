from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QProgressBar,QGridLayout
from PyQt5.QtCore import QBasicTimer
import sys

class App(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):

		grid = QGridLayout()

		self.pb = QProgressBar(self)

		self.btn = QPushButton('Start',self)

		self.btn.clicked.connect(self.doAction)

		self.timer = QBasicTimer()

		self.step = 0

		grid.addWidget(self.pb,1,0)
		grid.addWidget(self.btn,2,0)

		self.setLayout(grid)

		self.setGeometry(300,300,300,350)
		self.setWindowTitle('Progress Bar')
		self.show()

	def timerEvent(self,e):
		if self.step >= 100:
			self.timer.stop()
			self.btn.setText('Finished')
			return 

		self.step = self.step + 1
		self.pb.setValue(self.step)

	def doAction(self):
		if self.timer.isActive():
			self.timer.stop()
			self.btn.setText('Stop')

		else:
			self.timer.start(100,self)
			self.btn.setText('Stop')

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
