from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtGui import QPainter,QFont,QColor
from PyQt5.QtCore import Qt 
import sys

class App(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.text = "rohit3463"
		self.setGeometry(500,500,500,550)
		self.setWindowTitle('paint the widget')
		self.show()

	def paintEvent(self,event):
		qp = QPainter(self)

		self.drawText(event,qp)
		qp.end()

	def drawText(self,event,qp):
		qp.setPen(QColor(255,0,0))
		qp.setFont(QFont('Decorative',10))
		qp.drawText(event.rect(),Qt.AlignCenter,self.text)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = App()
	sys.exit(app.exec_())


