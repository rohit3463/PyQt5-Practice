from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
import sys,random

class App(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setWindowTitle('put dots')
		self.setGeometry(500,500,500,500)
		self.show()

	def paintEvent(self,event):
		qp = QPainter(self)
		self.drawDots(qp)
		qp.end()

	def drawDots(self,qp):
		qp.setPen(Qt.red)
		size = self.size()

		for i in range(1000):
			x = random.randint(1,size.width() - 1)
			y = random.randint(1,size.height() - 1)

			qp.drawPoint(x,y)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = App()
	sys.exit(app.exec_())