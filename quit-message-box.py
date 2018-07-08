from PyQt5.QtWidgets import QWidget,QApplication,QToolTip,QPushButton,QMessageBox
from PyQt5.QtGui import QFont,QIcon 
import sys

class App(QWidget):
	def __init__(self):
		super().__init__()
		self.initUi()
	def initUi(self):
		QToolTip.setFont(QFont('SansSerif',10))
		self.setGeometry(300,300,400,400)
		self.setWindowTitle('this is a <b>Simple</b> window')
		self.setWindowIcon(QIcon('images.png'))
		self.setToolTip('this is a simple window')

		self.show()
	def closeEvent(self,event):
		reply = QMessageBox.question(self,'Message','Are you sure , you want to quit?',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)

		if reply == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()

app = QApplication(sys.argv)

window = App()

sys.exit(app.exec_())
