from PyQt5.QtWidgets import QWidget,QApplication,QAction,qApp,QMenu,QToolBar
from PyQt5.QtGui import QIcon 
import sys

class App(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.toolbar = QToolBar(self)


		exitAct = QAction(QIcon('images.png'),'Exit',self)
		exitAct.setShortcut('Ctrl+Q')
		exitAct.triggered.connect(qApp.quit)

		self.toolbar.addAction(exitAct)

		self.setGeometry(300,300,300,200)
		self.setWindowTitle('toolbar for exit')
		self.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = App()

	sys.exit(app.exec_())