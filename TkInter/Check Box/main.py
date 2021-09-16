import tkinter

window = tkinter.Tk()

chk1 = tkinter.Checkbutton(window, text="hello world")
chk2 = tkinter.Checkbutton(window, text="hello world2")

chk1.pack()
chk2.pack()

window.mainloop()