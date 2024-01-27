from tkinter import *
def submit():
    input = text.get('0.1', END)
    print(input)

app = Tk()
text = Text(app,
            bg='light yellow',
            font=('Ink Free', 25),
            height=8,
            width=20,
            padx=20,
            pady=20,
            fg='purple')
text.pack()
button = Button(app, text='submit', command=submit)
button.pack()
app.mainloop()