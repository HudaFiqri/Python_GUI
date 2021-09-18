import tkinter
from typing import Text

window = tkinter.Tk()

txtArea = tkinter.Text(window, width=30, height=10)
txtArea.pack()

window.mainloop()