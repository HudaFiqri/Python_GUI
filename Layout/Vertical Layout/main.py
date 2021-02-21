'''
menentukan tampilan dengan vertical layout

sumber referensi: https://pythonpyqt.com/pyqt-box-layout/
ditulis pada: 21-02-2021
'''

from PyQt5.QtWidgets import *

class MainApp(QWidget):

    def __init__(self):
        super().__init__()
        self.MainUI()
        self.setGeometry(10, 10, 200, 150)
        self.setWindowTitle('Frame Vertical')

    def MainUI(self):

        btn1 = QPushButton('Click Me!!! Button 1')
        btn1.setGeometry(10, 10, 0, 30)

        btn2 = QPushButton('Click Me!!! Button 2')
        btn1.setGeometry(10, 10, 0, 30)

        herlay = QVBoxLayout(self)
        herlay.addWidget(btn1)
        herlay.addWidget(btn2)

app = QApplication([])

module = MainApp()
module.show()

app.exec()