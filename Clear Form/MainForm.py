import PyQt5.QtWidgets
import PyQt5.QtCore

QtWidgets = PyQt5.QtWidgets
QtWidget = QtWidgets.QWidget
QApplication = QtWidgets.QApplication

Label = QtWidgets.QLabel
Button = QtWidgets.QPushButton
Dialog = QtWidgets.QTextEdit
LineEdit = QtWidgets.QLineEdit

class Main_Form(QtWidget):
    
    def __init__(self):
        super().__init__()
        self.main()

    def main(self):
        
        self.resize(330, 120)
        self.setWindowTitle("main window")

        ##label
        self.label = Label("Masukkan Kata")
        self.label.setGeometry(10, 5, 310, 30)
        self.label.setParent(self)

        ###dialog
        self.line = LineEdit()
        self.line.setText("")
        self.line.setGeometry(10, 39, 310, 30)
        self.line.setParent(self)

        ###button
        #button clear
        self.ButtonClear = Button('Clear')
        self.ButtonClear.setGeometry(10, 80, 150, 30)
        self.ButtonClear.clicked.connect(self.line.clear)
        self.ButtonClear.setParent(self)

        #button close
        self.ButtonClose = Button('Close')
        self.ButtonClose.setGeometry(170, 80, 150, 30)
        self.ButtonClose.clicked.connect(self.Button_Close)
        self.ButtonClose.setParent(self)

    def Button_Close(self):
        self.close()