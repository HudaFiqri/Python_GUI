import PyQt5.QtWidgets
import MainForm

app_module = PyQt5.QtWidgets.QApplication([])

app = MainForm.MainForm()
app.show()

app_module.exec()