from tkinter import *

window = Tk()
window.geometry("500x300")
window.minsize(width=100, height=60)
window.maxsize(width=500, height=300)

frm1 = Frame(window)
frm1.pack()

label1 = Label(frm1, text="hello world")
label1.pack()

btn1 = Button(frm1, text='Click Me!')
btn1.pack()

window.mainloop()