import tkinter
from tkinter.constants import RAISED

window = tkinter.Tk()
window.geometry("300x400")

frame1 = tkinter.Frame(window, borderwidth=2)

btn1_frame1 = tkinter.Label(window, text='Head')

btn1_frame1.pack()
frame1.pack()

frame2 = tkinter.Frame(window, relief="raised")
frame2.pack()

window.mainloop()