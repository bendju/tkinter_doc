from tkinter import *

def dosometing(event):
    # print('You pressed: ' + event.keysym)
    label.config(text=event.keysym)
app = Tk()

label = Label(app, font=('Helventica', 100))
label.pack()
app.bind("<Key>", dosometing)  #Key
app.mainloop()