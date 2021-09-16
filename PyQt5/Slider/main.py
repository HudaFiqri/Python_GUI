'''
PyQt5 slider.

sumber referensi: https://zetcode.com/pyqt/qslider/
ditulis pada: 27-02-2021
'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MainApp(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Slider')
        self.setGeometry(10, 10, 300, 250)

        self.label1()
        self.label2()
        self.slider1()
        self.slider2()

    def label1(self):
        self.label = QLabel('Horizontal Slider')
        self.label.setGeometry(10, 10, 120, 30)
        self.label.setParent(self)

    def label2(self):
        self.label2 = QLabel('Vertical Slider')
        self.label2.setGeometry(10, 60, 100, 30)
        self.label2.setParent(self)

    def slider1(self):
        # untuk slider secara default dia akan menampilkan tampilan vertical
        # jadi untuk membuatnya menjadi horizontal perlu menggunakan module QtCore
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setGeometry(10, 30, 280, 30)
        self.slider.setParent(self)

    def slider2(self):
        self.slider = QSlider(Qt.Vertical)
        self.slider.setGeometry(10, 90, 20, 150)
        self.slider.setParent(self)

app = QApplication([])

module = MainApp()
module.show()

app.exec()