from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QGridLayout
import sys

class App(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		grid = QGridLayout()

		names = ['Cls','Bck','','Close',
				  '7','8','9','/',
				  '4','5','6','*',
				  '3','2','1','-',
				  '0','.','=','+']

		positions = [(i,j) for i in range(5) for j in range(4)]

		for position,name in zip(positions, names):
			if name == '':
				continue
			button = QPushButton(name)
			grid.addWidget(button,*position)

		self.setWindowTitle('Calculator')
		self.setLayout(grid)
		self.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
