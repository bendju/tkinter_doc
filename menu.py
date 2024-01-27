from tkinter import *

def openfile():
    print("file opened")

def savefile():
    print("file has ben saved")

app = Tk()

#openimage = PhotoImage(file='file.png')
menubar = Menu()
app.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0, font=("MV Boli", 15))
menubar.add_cascade(label="file", menu=filemenu)
filemenu.add_command(label="Open", command=openfile) #image=openimage, compound='left'
filemenu.add_command(label="save", command=savefile)
filemenu.add_separator()
filemenu.add_command(label="exit", command=quit)

editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='edit', menu=editmenu)


app.mainloop()