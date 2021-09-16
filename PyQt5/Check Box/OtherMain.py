import PyQt5.QtWidgets

class OtherMain(PyQt5.QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.Main()

    def Main(self):
        
        ###Aplication Module
        self.resize(400,300)
        self.setWindowTitle("Hasil Checkbox")

        ###Text
        #Text Output
        self.TextOutput = PyQt5.QtWidgets.QTextBrowser()
        self.TextOutput.setGeometry(10, 10, 380, 280)
        self.TextOutput.setParent(self)