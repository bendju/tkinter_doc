from tkinter import *

def create_win():
    new_window = Toplevel() #kapcsolodik a fo hoz
    #app_2 = Tk() ##uj ablak teljesen kulon vannak
app = Tk()

Button(app, text='create window', command=create_win)
app.mainloop()