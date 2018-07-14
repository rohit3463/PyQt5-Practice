from PyQt5.QtWidgets import QWidget,QApplication,QComboBox,QLabel,QGridLayout
import sys

class App(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		grid = QGridLayout()

		self.lbl = QLabel("UBUNTU",self)

		combo = QComboBox(self)
		combo.addItem("Ubuntu")
		combo.addItem("Mandriva")
		combo.addItem("Fedora")
		combo.addItem("Arch")
		combo.addItem("Gentoo")

		combo.activated[str].connect(self.onActivated)

		grid.addWidget(self.lbl)
		grid.addWidget(combo)

		self.setLayout(grid)

		self.setGeometry(300,300,300,350)
		self.setWindowTitle('Q-combobox')
		self.show()

	def onActivated(self,text):
		self.lbl.setText(text)
		self.lbl.adjustSize()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = App()
	sys.exit(app.exec_())