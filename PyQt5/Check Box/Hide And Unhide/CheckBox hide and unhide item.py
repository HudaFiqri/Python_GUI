'''
menampilkan item dan menampilkan item pada Check Box

sumber referensi: https://www.tutorialspoint.com/pyqt/pyqt_qcheckbox_widget.htm
ditulis pada: 01-03-2021
'''
from PyQt5.QtWidgets import *

class MainApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('main app')
        self.setGeometry(10, 10, 500, 500)

        self.btn1()
        self.dialog1()

    def btn1(self):
        self.btn1 = QCheckBox()
        self.btn1.setGeometry(10, 10, 150, 30)
        self.btn1.setText('expanding check')
        self.btn1.clicked.connect(self.btnClick)
        self.btn1.setParent(self)

    def dialog1(self):
        self.dialog1 = QTextBrowser()
        self.dialog1.setGeometry(10, 50, 480, 1)
        self.dialog1.setParent(self)

    def btnClick(self):

        if self.btn1.isChecked() == True:
            self.dialog1.setGeometry(10, 50, 480, 440)

        elif self.btn1.isChecked() == False:
            self.dialog1.setGeometry(10, 50, 480, 1)


app = QApplication([])
module = MainApp()
module.show()
app.exec()