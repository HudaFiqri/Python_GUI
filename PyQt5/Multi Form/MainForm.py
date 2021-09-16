import OtherForm
import PyQt5.QtWidgets
import PyQt5.QtCore

class MainForm(PyQt5.QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
        self.MainFormWindow()

    def MainFormWindow(self):
        
        self.resize(250, 160)
        self.setWindowTitle("Main Window")

        self.label = PyQt5.QtWidgets.QLabel("Click Button For Open New Form")
        self.label.setGeometry(10, 10, 250, 30)
        self.label.setAlignment(PyQt5.QtCore.Qt.AlignLeft)
        self.label.setParent(self)

        self.label2 = PyQt5.QtWidgets.QLabel('Click Button For Close Form')
        self.label2.setGeometry(10, 90, 250, 30)
        self.label2.setAlignment(PyQt5.QtCore.Qt.AlignLeft)
        self.label2.setParent(self)

        self.button = PyQt5.QtWidgets.QPushButton("Click Me! To Open")
        self.button.setGeometry(10, 39, 150, 30)
        self.button.clicked.connect(self.ButtonOpen)
        self.button.setParent(self)

        self.button2 = PyQt5.QtWidgets.QPushButton("Click Me! To Close")
        self.button2.setGeometry(10, 119, 150, 30)
        self.button2.clicked.connect(self.ButtonClose)
        self.button2.setParent(self)

    def ButtonOpen(self):
        self.Other_Form = OtherForm.Main_Form()
        self.Other_Form.show()

    def ButtonClose(self):
        self.close()
