import tkinter

window = tkinter.Tk()

enterStr = tkinter.StringVar()

enter = tkinter.Entry(window, textvariable=enterStr)
enter.pack()

btn = tkinter.Button(
    window,
    text="Click Me!",
    # untuk memasukkan value ke dalam entry maka gunakan set()
    command=lambda:enterStr.set("hello world")
)
btn.pack()

window.mainloop()