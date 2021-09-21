from tkinter import *

window = Tk()

frm = Frame(window, bg='red')
frm.pack(ipadx=10, ipady=10)

label = Label(frm, text='value')
label.pack()



window.mainloop()