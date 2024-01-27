from tkinter import *

def submit():

    food = []
    for i in listbox.curselection():
        food.insert(i, listbox.get(i))
    for i in food:
        print(i)
    #print(listbox.get(listbox.curselection()))

def add():
    listbox.insert(listbox.size(), entrybox.get())
    listbox.config(height=listbox.size())

def delete():
    for i in reversed(listbox.curselection()):
        listbox.delete(i)
    #listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size())

app = Tk()
listbox = Listbox(app,
                  bg='gray',
                  font=('Constantia', 35),
                  width=12,
                  selectmode=MULTIPLE
                  )
listbox.pack()
listbox.insert(1, 'pizza')
listbox.insert(2, 'fasz')
listbox.insert(3, 'picsa')
listbox.insert(4, 'soup')
listbox.config(height=listbox.size())

entrybox = Entry(app)
entrybox.pack()
addbutton = Button(app, text='add', command=add)
addbutton.pack()
submitbutton = Button(app, text='submit', command=submit)
submitbutton.pack()
deletebutton = Button(app, text='delete', command=delete)
deletebutton.pack()


app.mainloop()