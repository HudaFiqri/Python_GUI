import tkinter
from tkinter.constants import HORIZONTAL

window = tkinter.Tk()

# das horizontal slider
slide1 = tkinter.Scale(window, from_=0, to=100)
slide1.pack()

# das vertical slider
slide2 = tkinter.Scale(window, from_=0, to=100, orient=HORIZONTAL)
slide2.pack()

window.mainloop()