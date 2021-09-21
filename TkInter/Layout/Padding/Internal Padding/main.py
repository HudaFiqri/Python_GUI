import tkinter

window = tkinter.Tk()

label1 = tkinter.Label(window, text='With ipadx', bg='red')
# mengatur lebar
label1.pack(ipadx=20)

label2 = tkinter.Label(window, text='With ipady', bg='blue')
# mengarur tinggi
label2.pack(ipady=10)

window.mainloop()