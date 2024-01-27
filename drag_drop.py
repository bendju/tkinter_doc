from tkinter import *

def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)

app = Tk()

widget = Label(app,text='o', bg='red', width=10, height=10)
widget.place(x=0, y=0)

label_2 = Label(app, bg='blue', width=10, height=10)
label_2.place(x=100, y=100)

widget.bind('<Button-1>', drag_start)
widget.bind('<B1-Motion>', drag_motion)

label_2.bind('<Button-1>', drag_start)
label_2.bind('<B1-Motion>', drag_motion)

app.mainloop()