import PyQt5.QtWidgets

class MainForm(PyQt5.QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.Main()

    def Main(self):

        ###Application Module
        self.resize(400, 130)
        self.setWindowTitle("Main Window")

        ###Label
        #Label1
        self.Label1 = PyQt5.QtWidgets.QLabel("Masukkan Input Angka:")
        self.Label1.setGeometry(10, 5, 105, 30)
        self.Label1.setParent(self)

        ###Dialog
        #Dialog Input
        self.DialogInput = PyQt5.QtWidgets.QLineEdit()
        self.DialogInput.setGeometry(10, 30, 380, 30)
        self.DialogInput.setParent(self)

        ###ProgressBar
        #Progress1
        self.Progress = PyQt5.QtWidgets.QProgressBar()
        self.Progress.setValue(0)
        self.Progress.setGeometry(10, 65, 380, 20)
        self.Progress.setParent(self)

        ###Button
        #Button1
        self.Button1 = PyQt5.QtWidgets.QPushButton()
        self.Button1.setText("Confirm!")
        self.Button1.setGeometry(10, 90, 100, 30)
        self.Button1.pressed.connect(self.Button1Press)
        self.Button1.setParent(self)

        #Button2
        self.Button2 = PyQt5.QtWidgets.QPushButton()
        self.Button2.setText("Close")
        self.Button2.setGeometry(120, 90, 100, 30)
        self.Button2.pressed.connect(self.Button2Press)
        self.Button2.setParent(self)

    def Button1Press(self):
        TextInput = self.DialogInput.text()
        self.Progress.setValue(int(TextInput))
        self.DialogInput.clear()

    def Button2Press(self):
        self.close()