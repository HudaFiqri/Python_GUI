'''
spin box pada pytq5

sumber referensi: https://www.tutorialspoint.com/pyqt/pyqt_qspinbox_widget.htm
ditulis pada: 26-02-2021
'''

# import module yang dibutuhkan
from PyQt5.QtWidgets import *

class MainApp(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setGeometry(10, 10, 200, 250)
        self.setWindowTitle('Spin Box App')

        self.label1()
        self.label2()

        self.spin1()
        self.spin2()

    def label1(self):
        self.label1 = QLabel('Spin 1')
        self.label1.setGeometry(10, 5, 100, 30)
        self.label1.setParent(self)

    def label2(self):
        self.label2 = QLabel('Spin 2')
        self.label2.setGeometry(10, 80, 100, 30)
        self.label2.setParent(self)

    def spin1(self):
        self.spin = QSpinBox()
        self.spin.setGeometry(10, 35, 180, 30)
        self.spin.setRange(0, 100)
        self.spin.setParent(self)

    def spin2(self):
        self.spin = QSpinBox()
        self.spin.setGeometry(10, 110, 180, 30)
        self.spin.setRange(0, 100)
        self.spin.setValue(50)
        self.spin.setParent(self)

app = QApplication([])

module = MainApp()
module.show()

app.exec()