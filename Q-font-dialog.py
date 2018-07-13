from PyQt5.QtWidgets import QWidget,QApplication,QFontDialog,QLabel,QPushButton,QGridLayout
import sys

class App(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):

		grid = QGridLayout()

		btn = QPushButton('Dialog',self)

		btn.clicked.connect(self.showDialog)

		self.lb = QLabel('Rohit Sethi',self)

		grid.addWidget(btn,1,0)

		grid.addWidget(self.lb,2,0)

		self.setLayout(grid)

		self.setGeometry(300,300,300,350)

		self.setWindowTitle('Change font')

		self.show()

	def showDialog(self):

		font,ok = QFontDialog.getFont()

		if ok:
			self.lb.setFont(font)

if __name__ =='__main__':

	app = QApplication(sys.argv)

	window = App()

	sys.exit(app.exec_())

