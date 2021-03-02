'''
dengan menggunakan frame kita bisa membuat yang namanya tampilan responsif dengan mudah

ditulis pada: 02-03-2021
'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MainApp(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Frame')

        self.setGeometry(QRect(10, 10, 500, 500))

        self.MainFrame()

    def MainFrame(self):

        # import dulu widgetnya
        widget = QWidget(self)

        # terus buat vertikal layoutnya
        self.verlay = QVBoxLayout(self)
        self.verlay.setContentsMargins(0, 0, 0, 0)
        self.verlay.setSpacing(0)

        # baru buat framenya
        self.frame = QFrame(widget)
        self.frame.setStyleSheet(
            'background-color: grey'
        )
        # lalu tambahkan framenya di layout dan coba di running maka tampilan akan responsif
        self.verlay.addWidget(self.frame)

app = QApplication([])

module = MainApp()
module.show()

app.exec()
