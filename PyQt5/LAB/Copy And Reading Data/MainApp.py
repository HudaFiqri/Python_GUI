from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MainApp(QWidget):

    def __init__(self):
        super().__init__()
        self.label1()
        self.label2()
        self.text1()
        self.text2()
        self.btnRead()
        self.btnClear()
        self.setGeometry(10, 10, 500, 490)
        self.show()

    def label1(self):
        self.label = QLabel('Data Tulisan')
        self.label.setGeometry(10, 10, 100, 30)
        self.label.setParent(self)

    def label2(self):
        self.label = QLabel('Data Yang Dibaca')
        self.label.setGeometry(10, 80, 150, 30)
        self.label.setParent(self)

    def text1(self):
        self.text1 = QLineEdit()
        self.text1.setGeometry(10, 40, 480, 30)
        self.text1.setPlaceholderText('Masukkan Data')
        self.text1.setParent(self)

    def text2(self):
        self.text2 = QTextBrowser()
        self.text2.setGeometry(10, 110, 480 ,300)
        self.text2.setParent(self)

    def btnRead(self):
        self.read = QPushButton('Read Data')
        self.read.setGeometry(10, 420, 240, 60)
        self.read.clicked.connect(self.btnReadClick)
        self.read.setParent(self)

    def btnClear(self):
        self.write = QPushButton('Clear Data')
        self.write.setGeometry(260, 420, 230, 60)
        self.write.clicked.connect(self.btnClearClick)
        self.write.setParent(self)

    def btnReadClick(self):
        self.text2.append(self.text1.text())
        self.text1.setText('')

    def btnClearClick(self):
        self.text2.setText('')

app = QApplication([])
module = MainApp()
app.exec()