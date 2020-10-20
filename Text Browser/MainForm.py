import PyQt5.QtWidgets

class MainForm(PyQt5.QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.Main()

    def Main(self):

        #app module
        self.resize(400, 300)
        self.setWindowTitle("Main Window")

        ###label
        #label1
        self.label1 = PyQt5.QtWidgets.QLabel("Masukkan Text")
        self.label1.setGeometry(10, 10, 100, 30)
        self.label1.setParent(self)

        ###text dialog
        #Text Input
        self.TextInput = PyQt5.QtWidgets.QLineEdit()
        self.TextInput.setGeometry(10, 40, 380, 30)
        self.TextInput.returnPressed.connect(self.TextInputValue)
        self.TextInput.setParent(self)

        #Text Output
        self.TextOutput = PyQt5.QtWidgets.QTextBrowser()
        self.TextOutput.setGeometry(10, 80, 380, 170)
        self.TextOutput.setParent(self)

        ###button
        #button 1
        self.Button1 = PyQt5.QtWidgets.QPushButton("Clear")
        self.Button1.setGeometry(10, 260, 100, 30)
        self.Button1.setToolTip("clear text")
        self.Button1.clicked.connect(self.Button1Click)
        self.Button1.setParent(self)

        #button 2
        self.Button2 = PyQt5.QtWidgets.QPushButton("Close")
        self.Button2.setGeometry(120, 260, 100, 30)
        self.Button2.setToolTip("close program")
        self.Button2.clicked.connect(self.Button2Click)
        self.Button2.setParent(self)

    ###function of module
    #text input module
    def TextInputValue(self):
        Text = self.TextInput.text()
        self.TextOutput.setText(Text)
        self.TextInput.clear()

    #button clear module
    def Button1Click(self):
        self.TextOutput.clear()

    #button close module
    def Button2Click(self):
        self.close()