import tkinter
from tkinter import Label, font

window = tkinter.Tk()

def windowLabel():
    # panggil variable entry ke sini
    entryStr = entry.get()

    entryLabelOutput = tkinter.Label(
        window,
        # baru panggil lagi output variable dari entry buat di keluarkan saat di klik
        text=f"{entryStr}"
    )
    entryLabelOutput.pack()

tkString = tkinter.StringVar()

entry = tkinter.Entry(
    window,
    font='ubuntu',
    textvariable=tkString
)
entry.pack()

btnShowConsole = tkinter.Button(
    window,
    text='Console',
    font='ubuntu',
    # command buat ngeluarin output ke terminal
    command=lambda:print(entry.get())
)
btnShowConsole.pack()

btnShowWindow = tkinter.Button(
    window,
    text='App',
    font='ubuntu',
    command=windowLabel
)
btnShowWindow.pack()

btnClose = tkinter.Button(
    window,
    text="exit",
    font="ubuntu",
    command=lambda:exit()
)
btnClose.pack()

window.mainloop()