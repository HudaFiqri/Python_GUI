import tkinter

# buat dulu frame-nya
frame = tkinter.Tk()
frame.title("Tkinter Frame 1")

# terus buat button-nya dan masukin ke dalam frame
button = tkinter.Label(frame, text="hello world")
button.pack()

# biar dia keluar dia harus di looping
frame.mainloop()