import PyQt5.QtWidgets
import PyQt5.QtCore

class Main_Form(PyQt5.QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.Main()

    def Main(self):
        self.resize(220, 90)
        self.setWindowTitle('Other Window')
        
        self.label = PyQt5.QtWidgets.QLabel("Click The Button For Close")
        self.label.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
        self.label.setGeometry(10, 10, 200, 30)
        self.label.setParent(self)

        self.button = PyQt5.QtWidgets.QPushButton("Click Me")
        self.button.setGeometry(45, 50, 125, 30)
        self.button.clicked.connect(self.ButtonClick)
        self.button.setParent(self)

    def ButtonClick(self):
        self.close()