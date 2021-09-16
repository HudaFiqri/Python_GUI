import MainForm

app_module = MainForm.PyQt5.QtWidgets.QApplication([])

app = MainForm.MainForm()
app.show()

app_module.exec()