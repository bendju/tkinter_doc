from tkinter import *

app = Tk()
"""
hotIMage = PhotoImage(file='val.png')
hotlabel = Label(image=hotIMage)
hotlabel.pack()
"""
def submit():
    print(f'the temleture is {scale.get()} c')

scale = Scale(app,
              from_=100,
              to=0,
              length=600,
              showvalue=0,
              orient=VERTICAL,
              font=('Consolas', 20),
              tickinterval=10,
              bg='black',
              fg='red',
              activebackground='red',
              troughcolor='blue'
              )
scale.set(scale['from'] / 2)
button = Button(app, text='submit', command=submit)

scale.pack()
button.pack(pady=10)
app.mainloop()