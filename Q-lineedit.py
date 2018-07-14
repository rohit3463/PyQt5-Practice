from PyQt5.QtWidgets import QWidget,QApplication,QLineEdit,QLabel,QGridLayout
import sys

class App(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		grid = QGridLayout()

		self.lbl = QLabel(self)

		self.lineedit = QLineEdit()

		self.lineedit.textChanged[str].connect(self.onChange)

		grid.addWidget(self.lbl,1,0)
		grid.addWidget(self.lineedit,2,0)

		self.setLayout(grid)
		self.setWindowTitle('line_edit')
		self.adjustSize()
		self.show()

	def onChange(self,text):
		self.lbl.setText(text);
		self.lbl.adjustSize()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    window = App()
    sys.exit(app.exec_())
