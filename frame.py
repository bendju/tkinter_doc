from tkinter import *

app = Tk()

frame = Frame(app, bg='pink', bd=5, relief=RAISED)
frame.pack(side=BOTTOM)
frame.place(x=0, y=0)

Button(frame, text='W', font=('Consolas', 25), width=3).pack(side=TOP)
Button(frame, text='A', font=('Consolas', 25), width=3).pack(side=LEFT)
Button(frame, text='S', font=('Consolas', 25), width=3).pack(side=LEFT)
Button(frame, text='D', font=('Consolas', 25), width=3).pack(side=LEFT)
app.mainloop()