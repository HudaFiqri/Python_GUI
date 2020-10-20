import MainButton
import PyQt5.QtWidgets

app_module = PyQt5.QtWidgets.QApplication([])

app = MainButton.main_form()
app.show()

app_module.exec()