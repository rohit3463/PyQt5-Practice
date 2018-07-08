from PyQt5.QtWidgets import QMainWindow,QPushButton,QApplication,QDesktopWidget,QToolTip
from PyQt5.QtGui import QIcon,QFont
import sys

class Example(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUi()
	def initUi(self):
		QToolTip.setFont(QFont('SansSerif',10))
		self.statusBar().showMessage('Hello,World!')
		
		btn = QPushButton('Button',self)
		btn.setToolTip('this is a <b>QPushButton</b>')
		btn.resize(btn.sizeHint())
		btn.clicked.connect(QApplication.instance().quit)
		btn.move(50,50)
		self.setGeometry(300,300,400,400)
		self.setWindowTitle('A simple Window')
		self.setWindowIcon(QIcon('images.png'))
		self.setToolTip('this is a <b>Simple</b> Window')
		self.center()
		self.show()
	def center(self):
		qr = self.frameGeometry()

		cp = QDesktopWidget().availableGeometry().center()

		qr.moveCenter(cp)

		self.move(qr.topLeft())

app = QApplication(sys.argv)

window = Example()

sys.exit(app.exec_())