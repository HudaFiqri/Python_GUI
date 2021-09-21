import tkinter

window = tkinter.Tk()

#akan memunculkan label mengarah dari kiri dulu
label1 = tkinter.Label(window, text='label left 1')
label1.pack(side=tkinter.LEFT)

label2 = tkinter.Label(window, text='label left 2')
label2.pack(side=tkinter.LEFT)

#akan memunculkan label mengarah dari kanan dulu
label3 = tkinter.Label(window, text='label right 1')
label3.pack(side=tkinter.RIGHT)

label4 = tkinter.Label(window, text='label right 2')
label4.pack(side=tkinter.RIGHT)

window.mainloop()