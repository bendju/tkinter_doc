from tkinter import *
from tkinter import ttk

app = Tk()

notebook = ttk.Notebook(app)

tab1 = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1, text="tab 1")
notebook.add(tab2, text="tab 2")
notebook.pack(expand=True, fill='both')

Label(tab1, text='hello asbdaibhasidb', width=50, height=25).pack()
Label(tab2, text='bye ndisbfbisdbfibsdifb', width=50, height=25).pack()
app.mainloop()