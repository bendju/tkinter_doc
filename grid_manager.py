from tkinter import *

app = Tk()

firstlabel = Label(app, text='First name :  ', width=20)
firstlabel.grid(row=0, column=0)
firstentry = Entry(app)
firstentry.grid(row=0, column=1)

lastlabel = Label(app, text='First name :  ')
lastlabel.grid(row=1, column=0)
lastentry = Entry(app)
lastentry.grid(row=1, column=1)

submitbutton = Button(app, text='submit')
submitbutton.grid(row=2, column=0, columnspan=2)

app.mainloop()