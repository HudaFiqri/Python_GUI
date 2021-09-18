import tkinter

window = tkinter.Tk()

label1 = tkinter.Label(window, text='value 1')
label1.grid(row=0, column=0)

label2 = tkinter.Label(window, text='value 2')
label2.grid(row=1, column=1)

label3 = tkinter.Label(window, text='value 3')
label3.grid(row=2, column=2)

window.mainloop()