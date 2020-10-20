import PyQt5.QtWidgets

Label = PyQt5.QtWidgets.QLabel
Button = PyQt5.QtWidgets.QPushButton
Radio = PyQt5.QtWidgets.QRadioButton
Massage = PyQt5.QtWidgets.QMessageBox

class MainForm(PyQt5.QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.Main()

    def Main(self):
        
        ###Application Module
        self.resize(230, 160)
        self.setWindowTitle("Main Window")

        ###Label
        #Label1
        self.Label1 = Label("Silahkan Pilih:")
        self.Label1.setGeometry(10, 5, 105, 30)
        self.Label1.setParent(self)

        ###Radio
        #Radio 1
        self.Radio1 = Radio("Radio 1")
        self.Radio1.setGeometry(10, 30, 100, 30)
        self.Radio1.setParent(self)

        #Radio 2
        self.Radio2 = Radio("Radio 2")
        self.Radio2.setGeometry(10, 55, 100, 30)
        self.Radio2.setParent(self)

        #Radio 3
        self.Radio3 = Radio("Radio 3")
        self.Radio3.setGeometry(10, 80, 100, 30)
        self.Radio3.setParent(self)

        ###Button
        #Button 1
        self.Button1 = Button("Confirm")
        self.Button1.setGeometry(10, 120, 100, 30)
        self.Button1.pressed.connect(self.Button1Press)
        self.Button1.setParent(self)

        #Button 2
        self.Button2 = Button("Close")
        self.Button2.setGeometry(120, 120, 100, 30)
        self.Button2.pressed.connect(self.Button2Press)
        self.Button2.setParent(self)

    def Button1Press(self):

        if self.Radio1.isChecked():
            Radio1Massage = Massage()
            Radio1Massage.setText("Radio 1 Is Checked")
            Radio1Massage.setWindowTitle("Alert!")
            Radio1Massage.setIcon(Massage.Information)
            Radio1Massage.setStandardButtons(Radio1Massage.Yes | Radio1Massage.No)
            Radio1Massage.exec()

        if self.Radio2.isChecked():
            Radio2Massage = Massage()
            Radio2Massage.setText('Radio 2 Is Checked')
            Radio2Massage.setWindowTitle("Alert!")
            Radio2Massage.setIcon(Radio2Massage.Information)
            Radio2Massage.setStandardButtons(Radio2Massage.Yes | Radio2Massage.No)
            Radio2Massage.exec()
        
        if self.Radio3.isChecked():
            Radio3Massage = Massage()
            Radio3Massage.setText("Radio 3 Is Checked")
            Radio3Massage.setWindowTitle("Alert!")
            Radio3Massage.setIcon(Radio3Massage.Information)
            Radio3Massage.setStandardButtons(Radio3Massage.Yes | Radio3Massage.No)
            Radio3Massage.exec()

    def Button2Press(self):
        self.close()