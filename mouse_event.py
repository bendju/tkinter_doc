from tkinter import *

def doSometing(event):
    print('valami  ' + str(event.x) + str(event.y) )
app = Tk()

#app.bind('<Button-1>', doSometing) #left mouse click
# app.bind('<Button-2>', doSometing) #gorgo katt
# app.bind('<Button-3>', doSometing) #right mouse click
# app.bind('<Enter>', doSometing) #enter the window
# app.bind('<Leave>', doSometing) #leave the window
app.bind('<Motion>', doSometing) #motion

app.mainloop()