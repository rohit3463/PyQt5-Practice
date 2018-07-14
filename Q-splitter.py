from PyQt5.QtWidgets import QWidget,QApplication,QSplitter,QStyleFactory,QFrame,QHBoxLayout
from PyQt5.QtCore import Qt
import sys

class App(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		hbox = QHBoxLayout(self)

		f1 = QFrame(self)
		f1.setFrameShape(QFrame.StyledPanel)
		f1.setStyleSheet("QFrame {background-color:red}")

		f2 = QFrame(self)
		f2.setFrameShape(QFrame.StyledPanel)
		f2.setStyleSheet("QFrame {background-color:blue}")

		f3 = QFrame(self)
		f3.setFrameShape(QFrame.StyledPanel)
		f3.setStyleSheet("QFrame {background-color:yellow}")

		splitter1 = QSplitter(Qt.Horizontal)
		splitter1.addWidget(f1)
		splitter1.addWidget(f2)

		splitter2 = QSplitter(Qt.Vertical)
		splitter2.addWidget(splitter1)
		splitter2.addWidget(f3)
		splitter2.setSizes([150,150])

		hbox.addWidget(splitter2)

		self.setLayout(hbox)

		self.setGeometry(300,300,300,350)
		self.setWindowTitle('Q-splitter')
		self.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = App()
	sys.exit(app.exec_())