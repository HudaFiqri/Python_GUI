from tkinter import *

window = Tk()

list = Listbox(window)
list.insert(1, 'value 1')
list.insert(2, 'value 2')
list.insert(3, 'value 3')
list.pack()

window.mainloop()