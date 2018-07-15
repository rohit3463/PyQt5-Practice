from PyQt5.QtWidgets import QWidget,QApplication,QPushButton
from PyQt5.QtCore import QMimeData,Qt 
from PyQt5.QtGui import QDrag
import sys

class Button(QPushButton):
	def __init__(self,title,parent):
		super().__init__(title,parent)

	def mouseMoveEvent(self,e):
		if e.buttons() != Qt.RightButton:
			return

		drag = QDrag(self)
		data = QMimeData()
		drag.setMimeData(data)
		drag.setHotSpot(e.pos() - self.rect().topLeft())

		dropAction = drag.exec_(Qt.MoveAction)

	def mousePressEvent(self,e):
		super().mousePressEvent(e)

		if e.buttons() == Qt.LeftButton:
			print("Press")

class App(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.btn = Button('hello',self)

		self.setAcceptDrops(True)

		self.setWindowTitle('drag button to move')
		self.setGeometry(300,300,300,350)
		self.show()

	def dragEnterEvent(self,e):
		e.accept()

	def dropEvent(self,e):
		position = e.pos()
		self.btn.move(position)
		e.setDropAction(Qt.MoveAction)
		e.accept()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = App()
	sys.exit(app.exec_())

