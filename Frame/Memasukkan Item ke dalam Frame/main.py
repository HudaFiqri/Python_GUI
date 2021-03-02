'''
dengan cara ini bisa dengan mudah membuat pengelompokkan layout mau yang seperti apa

ditulis pada: 02-03-2021
'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MainApp(QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry(QRect(10, 10, 500, 500))

        # buat dulu tampilan vertical layoutnya
        self.verlay = QVBoxLayout(self)
        self.verlay.setContentsMargins(0, 0, 0, 0)
        self.verlay.setSpacing(0)

        # terus tambahkan frame untuk didalamnya
        self.mainFrame = QFrame(self)
        self.mainFrame.setStyleSheet(
            'background-color: grey;'
        )
        self.mainFrame.setGeometry(QRect(50, 60, 200, 200))
        # masukkan frame ke dalam layout
        self.verlay.addWidget(self.mainFrame)

        # masukkan button ke dalam frame
        self.btn = QPushButton(self.mainFrame)
        self.btn.setGeometry(QRect(10, 10, 130, 30))
        self.btn.setText('Button on Frame')

app = QApplication([])

module = MainApp()
module.show()

app.exec()
