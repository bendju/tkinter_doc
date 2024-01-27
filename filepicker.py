from tkinter import *
from tkinter import colorchooser

def click():
    """
    color = colorchooser.askcolor()
    colorhex = color[1]
    print(colorhex)
    app.config(bg=colorhex)
    """
    app.config(bg=colorchooser.askcolor()[1])
app = Tk()
app.geometry('420x420')
button = Button(text='click me', command=click)
button.pack()
app.mainloop()