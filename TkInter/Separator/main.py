from tkinter import *
from tkinter.font import BOLD
from tkinter.ttk import Separator

window = Tk()
window.geometry("400x200")

label1 = Label(window, text="value 1", relief=RAISED, bd=4)
label1.place(relx=0.3, rely=0.2, relwidth=0.3, relheight=0.2)

sep = Separator(window, orient='horizontal')
sep.place(relx=0, rely=0.50, relwidth=1, relheight=1)

label2 = Label(window, text="value 2", relief=RAISED, bd=4)
label2.place(relx=0.3, rely=0.6, relwidth=0.3, relheight=0.2)

window.mainloop()