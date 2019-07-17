from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QPainter,QColor,QBrush
import sys

class App(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setGeometry(500,500,500,500)
		self.setWindowTitle('Q-Paint-Rect')
		self.show()

	def paintEvent(self,event):
		qp = QPainter(self)
		self.drawRectangles(qp)
		qp.end()

	def drawRectangles(self,qp):
		col = QColor(120,212,126)

		qp.setPen(col)

		qp.setBrush(QColor(255,0,0))
		qp.drawRect(10,15,90,60)

		qp.setBrush(QColor(0,255,0))
		qp.drawRect(130,15,90,60)

		qp.setBrush(QColor(0,0,255))
		qp.drawRect(250,15,90,60)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = App()
	sys.exit(app.exec_())