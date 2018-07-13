from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QFileDialog,QTextEdit,QStatusBar,QMenuBar,QGridLayout,QAction
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import sys

class App(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):

		grid = QGridLayout()

		self.txt = QTextEdit()

		self.st = QStatusBar()

		self.mn = QMenuBar(self)

		grid.addWidget(self.txt,1,0,9,0)
		grid.addWidget(self.st,10,0,Qt.AlignBottom)

		self.st.showMessage('hello')

		self.setLayout(grid)

		self.op = QAction(QIcon('images.png'),'open',self)

		self.op.setShortcut('Ctrl+o')

		self.op.triggered.connect(self.showDialog)

		filemenu = self.mn.addMenu('&File')

		filemenu.addAction(self.op)

		self.setGeometry(300,300,300,350)

		self.setWindowTitle('open a file')

		self.show()

	def showDialog(self):

		fname = QFileDialog.getOpenFileName(self,'Open File','/home')

		if fname[0]:

			f = open(fname[0],'r')

			with f:
				data = f.read()
				self.txt.setText(data)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = App()

	sys.exit(app.exec_())

