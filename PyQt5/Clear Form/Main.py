import MainForm
import PyQt5.QtWidgets

app_module = PyQt5.QtWidgets.QApplication([])

app = MainForm.Main_Form()
app.show()

app_module.exec()