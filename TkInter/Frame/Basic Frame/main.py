import tkinter
from tkinter.constants import BOTH, BOTTOM, LEFT, RIGHT

window = tkinter.Tk()
window.geometry("300x400")

window_frame1 = tkinter.Frame(window)
window_frame1.pack()

window_frame2 = tkinter.Frame(window)
window_frame2.pack()

btn_top_1 = tkinter.Button(window_frame1, text="Top Button 1")
btn_top_1.pack(side=LEFT)

btn_top_2 = tkinter.Button(window_frame1, text="Top Button 2")
btn_top_2.pack(side=LEFT)

btn_bottom_1 = tkinter.Button(window_frame2, text="Bottom Button 1")
btn_bottom_1.pack(side=BOTTOM)

btn_bottom_2 = tkinter.Button(window_frame2, text="Bottom Button 2")
btn_bottom_2.pack(side=BOTTOM)

window.mainloop()