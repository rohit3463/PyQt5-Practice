from PyQt5.QtWidgets import QWidget,QApplication,QHBoxLayout,QVBoxLayout,QPushButton
import sys

class App(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		okbutton = QPushButton('OK')
		cancelbutton = QPushButton('Cancel')

		Hbox = QHBoxLayout()
		Hbox.addStretch(1)
		Hbox.addWidget(okbutton)
		Hbox.addWidget(cancelbutton)

		Vbox = QVBoxLayout()
		Vbox.addStretch(1)
		Vbox.addLayout(Hbox)

		self.setLayout(Vbox)

		self.setGeometry(300,300,300,350)
		self.setWindowTitle('Layouts and Stretch')

		self.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = App()

	sys.exit(app.exec_())