from PyQt5.QtWidgets import QMainWindow,QAction,QApplication,qApp,QMenu,QTextEdit
from PyQt5.QtGui import QIcon 
import sys

class App(QMainWindow):
	def __init__(self):

		super().__init__()
		self.initUI()

	def initUI(self):
		textEdit = QTextEdit()
		self.setCentralWidget(textEdit)

		exitAct = QAction(QIcon('images.png'),'Exit',self)
		exitAct.setShortcut('Ctrl+Q')
		exitAct.triggered.connect(qApp.quit)

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(exitAct)

		toolbar = self.addToolBar('Exit')
		toolbar.addAction(exitAct)

		self.setGeometry(300,300,350,250)
		self.setWindowTitle('Main window')
		self.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = App()

	sys.exit(app.exec_())


