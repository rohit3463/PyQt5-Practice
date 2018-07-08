from PyQt5.QtWidgets import QMainWindow,QApplication,QMenu,QAction 
from PyQt5.QtGui import QIcon 
import sys

class App(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.statusbar = self.statusBar()
		self.statusbar.showMessage('Ready')

		menubar = self.menuBar()
		viewMenu = menubar.addMenu('View')

		viewStatAct = QAction('View statusbar',self,checkable=True)
		viewStatAct.setChecked(True)
		viewStatAct.triggered.connect(self.toggleMenu)

		viewMenu.addAction(viewStatAct)

		self.setGeometry(300,300,300,200)
		self.setWindowTitle('toggle status bar menu')
		self.show()

	def toggleMenu(self,state):

		if state:
			self.statusbar.show()
		else:
			self.statusbar.hide()

if __name__ == '__main__':
	app = QApplication(sys.argv)

	window = App()

	sys.exit(app.exec_())