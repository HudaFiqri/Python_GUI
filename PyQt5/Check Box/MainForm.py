import PyQt5.QtWidgets
import OtherMain

Label = PyQt5.QtWidgets.QLabel
CheckBox = PyQt5.QtWidgets.QCheckBox
Button = PyQt5.QtWidgets.QPushButton

class MainForm(PyQt5.QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.Main()

    def Main(self):

        ###Application Module
        self.resize(230, 160)
        self.setWindowTitle("Main Form")

        ###label
        #label
        self.label1 = Label("Silahkan Pilih:")
        self.label1.setGeometry(10, 5, 100, 30)
        self.label1.setParent(self)

        ###Check Box
        #Check 1
        self.check1 = CheckBox("Check 1 Checked")
        self.check1.setText("Check 1 Checked")
        self.check1.setGeometry(10, 30, 150, 30)
        self.check1.setParent(self)

        #Check 2
        self.check2 = CheckBox()
        self.check2.setText("Check 2 Checked")
        self.check2.setGeometry(10, 55, 150, 30)
        self.check2.setParent(self)

        #Check 3
        self.check3 = CheckBox()
        self.check3.setText("Check 3 Checked")
        self.check3.setGeometry(10, 80, 150, 30)
        self.check3.setParent(self)

        ###button
        #button 1
        self.button1 = Button("Confirm")
        self.button1.setGeometry(10, 120, 100, 30)
        self.button1.pressed.connect(self.button1Press)
        self.button1.setParent(self)

        #button 2
        self.button2 = Button("Close")
        self.button2.setGeometry(120, 120, 100, 30)
        self.button2.pressed.connect(self.button2Press)
        self.button2.setParent(self)


    def button1Press(self):
        ###Other Application Call Module
        self.CallOtherApp = OtherMain.OtherMain()

        ###Add Choice Answer
        if self.check1.isChecked():
            self.CallOtherApp.TextOutput.append("Check 1 Is Checked")
        if self.check2.isChecked():
            self.CallOtherApp.TextOutput.append("Check 2 Is Checked")
        if self.check3.isChecked():
            self.CallOtherApp.TextOutput.append("Check 3 Is Checked")

        ###Show Other Application
        self.CallOtherApp.show()

    def button2Press(self):
        self.close()