import tkinter
from typing import Text

window = tkinter.Tk()

def radConf():
    tkinter.Label.config()

rad1 = tkinter.Radiobutton(window, text="hello world 1", value=1)
rad2 = tkinter.Radiobutton(window, text="hello world 2", value=2)
rad3 = tkinter.Radiobutton(window, text="hello world 3", value=3)

rad1.pack()
rad2.pack()
rad3.pack()

window.mainloop()