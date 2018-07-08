from PyQt5.QtWidgets import QWidget,QApplication,QGridLayout,QLabel,QLineEdit,QTextEdit
import sys

class App(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		grid = QGridLayout()

		self.setLayout(grid)
		grid.setSpacing(10)

		title = QLabel('Title')
		author = QLabel('Author')
		review = QLabel('Review')

		titleEdit = QLineEdit()
		authorEdit = QLineEdit()
		reviewEdit = QTextEdit()

		grid.addWidget(title,1,0)
		grid.addWidget(titleEdit,1,1)
		grid.addWidget(author,2,0)
		grid.addWidget(authorEdit,2,1)
		grid.addWidget(review,3,0)
		grid.addWidget(reviewEdit,3,1,5,1)

		self.setGeometry(300,300,300,300)
		self.setWindowTitle('grid with position indexing')
		self.show()

if __name__ == '__main__':

	app = QApplication(sys.argv)

	window = App()

	sys.exit(app.exec_())
