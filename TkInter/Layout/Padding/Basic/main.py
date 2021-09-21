import tkinter

window = tkinter.Tk()

"""
pady = untuk mengatur jarak atas dan bawah
padx = untuk mengatur jarak kanan dan samping
"""

label1 = tkinter.Label(window, text="value 1", bg='red')
label1.pack(padx=10, pady=10)

label2 = tkinter.Label(window, text="value 2", bg='yellow')
label2.pack(padx=10, pady=10)

window.mainloop()