import PyQt5.QtWidgets

class main_form(PyQt5.QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
        self.main_button()

    def main_button(self):
        
        self.button = PyQt5.QtWidgets.QPushButton("click me!")
        self.button.setGeometry(10, 10, 100, 30)
        #trigger agar saat click button akan tertutup
        self.button.clicked.connect(self.ClickButton)
        self.button.setParent(self)

    def ClickButton(self):
        self.close()