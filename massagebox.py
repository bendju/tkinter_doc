from tkinter import *
from tkinter import messagebox

app = Tk()

def click():
    #messagebox.showinfo(title='virus', message='virus')
    #messagebox.showwarning(title='warning', message='virus')
    #messagebox.showerror(title='virus', message='virus')
    """
    if messagebox.askokcancel(title='ask ok canceled', message='hjjjjjj'):
        print('yes')
    else:
        print('no')

    if messagebox.askretrycancel(title='ask ok canceled', message='hjjjjjj', icon='warning):
        print('yes')
    else:
        print('no')

    if messagebox.askyesno(title='yes or no', message='change'):
        print('ok')
    else:
        print('no')

    answer = messagebox.askquestion(title='ask question', message='do you like pie')
    if (answer == 'yes'):
        print('yeeeee')
    else:
        print('why??')

    print(messagebox.askyesnocancel(title='change', message='like code?'))
    """
button = Button(app, command=click, text='click me')
button.pack()
app.mainloop()