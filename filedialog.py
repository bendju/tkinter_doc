"""
from tkinter import *
from tkinter import filedialog

def openfile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\tbeni\\Documents\\program",
                                          title='Open file',
                                          filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    file = open(filepath, 'r')
    print(file.read())
    file.close()

app = Tk()

button = Button(app, text='open', command=openfile)
button.pack()
app.mainloop()
"""

from tkinter import *
from tkinter import filedialog

def savefile():
    file = filedialog.asksaveasfile(initialdir='C:\\Users\\tbeni\\Documents\\program',
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("text file", ".txt"),
                                        ("HTML file", ".html"),
                                        ("all file", ".*")
                                    ])
    if file is None:
        return

    filetext = str(text.get(1.0, END))
    file.write(filetext)
    file.close()
app = Tk()

button = Button(app, text='save', command=savefile)
button.pack()
text = Text(app)
text.pack()
app.mainloop()