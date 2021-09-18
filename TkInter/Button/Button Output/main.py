from tkinter import *

window = Tk()

# syntax untuk ngeluarkan output diterminal
def BtnClick():
    print('hello world')
    exit()

# syntax untuk ngeluarkan output diprogram
def BtnClick2():
    BtnLabel = Label(window, text="Hello Comerade")
    BtnLabel.pack()

btn1 = Button(window, text="click me! 1", command=BtnClick)
btn1.pack()

btn2 = Button(window, text="click me! 2", command=BtnClick2)
btn2.pack()

window.mainloop()