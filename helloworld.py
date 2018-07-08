from PyQt5.QtWidgets import QMainWindow,QPushButton,QApplication,QDesktopWidget,QToolTip
from PyQt5.QtGui import QIcon,QFont
import sys

class Example(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUi()
	def initUi(self):
		self.statusBar().showMessage('Hello,World!')
		self.setGeometry(300,300,400,400)
		self.setWindowTitle('A simple Window')
		self.setWindowIcon(QIcon('images.png'))
		self.show()

if __name__ == '__main__':

	app = QApplication(sys.argv)

	window = Example()

	sys.exit(app.exec_())