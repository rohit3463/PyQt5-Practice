from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QLineEdit,QGridLayout
import sys

class Button(QPushButton):
	def __init__(self,title,parent):
		super().__init__(title,parent)
		self.setAcceptDrops(True)

	def dragEnterEvent(self,e):
		if e.mimeData().hasFormat('text/plain'):
			e.accept()
		else:
			e.ignore()

	def dropEvent(self,e):
		self.setText(e.mimeData().text())

class App(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		grid = QGridLayout()

		btn = Button('Title',self)

		lEdit = QLineEdit('',self)

		lEdit.setDragEnabled(True)

		grid.addWidget(btn,1,0)
		grid.addWidget(lEdit,2,0)

		self.setLayout(grid)

		self.setWindowTitle('drag and drop')
		self.setGeometry(300,300,300,350)
		self.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = App()
	sys.exit(app.exec_())