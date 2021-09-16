'''
dengan adanya ukuran maximum dan minimum, dapat dilakukan penguncian ukuran yang sudah ditentukan

ditulis pada: 26-02-2021
direvisi pada: 02-03-2021
'''

from PyQt5.QtWidgets import *

class MainApp(QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry(10, 10, 500, 450)
        self.setWindowTitle('Main App')
        self.setMinimumSize(300, 250)
        self.setMaximumSize(700, 650)

app = QApplication([])

module = MainApp()
module.show()

app.exec()