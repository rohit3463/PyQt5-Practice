from PyQt5.QtWidgets import QMainWindow,QApplication,QAction,QMenu
import sys

class App(QMainWindow):
	def __init__(self):
		super().__init__()

		self.initUi()

	def initUi(self):

		menubar = self.menuBar()
		fileMenu = menubar.addMenu(' File')
		
		impMenu = QMenu(' Import',self)
		impAct = QAction(' Import mail',self)
		impMenu.addAction(impAct)

		newAct = QAction(' New',self)

		fileMenu.addAction(newAct)
		fileMenu.addMenu(impMenu)

		self.setGeometry(300,300,300,200)
		self.setWindowTitle('Simple menu')
		self.show()

if __name__ == '__main__' :
	app = QApplication(sys.argv)

	window = App()

	sys.exit(app.exec_())
