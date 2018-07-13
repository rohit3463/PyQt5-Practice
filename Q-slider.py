from PyQt5.QtWidgets import QWidget,QApplication,QSlider,QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import sys

class App(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):

		sld = QSlider(Qt.Horizontal,self)
		sld.setFocusPolicy(Qt.NoFocus)
		sld.setGeometry(30,40,100,30)
		sld.valueChanged[int].connect(self.changeValue)

		self.label = QLabel(self)
		self.label.setPixmap(QPixmap('Mute.png'))
		self.label.setGeometry(160,40,80,30)

		self.setGeometry(300,300,280,170)
		self.setWindowTitle('QSlider')
		self.show()

	def changeValue(self, value):

		if value == 0:
			self.label.setPixmap(QPixmap('Mute.png'))
		elif value > 0 and value <= 30:
			self.label.setPixmap(QPixmap('Min.ico'))
		elif value > 30 and value <= 80:
			self.label.setPixmap(QPixmap('Med.png'))
		else:
			self.label.setPixmap(QPixmap('Max.ico'))



if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = App()
	sys.exit(app.exec_())

