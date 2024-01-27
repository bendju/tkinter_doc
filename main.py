from tkinter import *


app = Tk()
###########################ablak####################
app.title('ablak')                                 #
app.geometry('400x400')                            #
#app.resizable(width=False, height=False)           #
#app.destroy()
#app.iconphoto(True, image)
app.configure(bg='black')
######################image########################
#image = PhotoImage(file='')
################BUTTON##############################
def button_com():
    print('parancs')
button = Button(app,
                text='button',
                width=40,
                height=40,
                bg='red',
                fg='black',
                state="active",
                command=button_com,
                font=('Arial', 12),
                compound='top',
                activeforeground='black',
                activebackground='red') #image=image

#button.pack(pady=20)
######################Label#########################

label = Label(master=app,
              text='Label',
              fg='red',
              bg='green',
              width=10,
              height=10,
              font=('Arial', 12, 'bold'),
              padx=10,
              bd=10,
              relief=RAISED
              )# image=photo_varrible, compound='top'

#label.pack(pady=20)
label.configure(text='red')
#######################frame#########################
frame = Frame(app,
              width=20,
              height=20,
              bg='red',
              )
#########################checkbutton########################
checkvar = IntVar()
def check_com():
    if checkvar.get() == 1:
        print('aktiv a faszom')
    else:
        print('nem jo')
checkbox = Checkbutton(app,
                       text='ez nem az',
                       bg='black',
                       fg='red',
                       activeforeground='red',
                       activebackground='black',
                       width=20,
                       height=20,
                       command=check_com,
                       variable=checkvar,
                       onvalue=1,
                       offvalue=0,
                       font=('Arial', 20),
                       )#image and compound is working
#checkbox.pack()
######################radiobutton#############
food = ['pizza', 'hamburger', 'hotdog']
def order():
    if (x.get()==0):
        print('pizza')

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(app, text=food[index],
                              variable=x,
                              value=index,
                              padx=25,
                              font=('Impact', 10),
                              indicatoron=0,
                              width=100,
                              command=order
                              )#image and compound is working
    radiobutton.pack(anchor=W)

######################entry####################
def submit():
    username = entry.get()
    print(username)
    entry.config(state=DISABLED)
def delete():
    entry.delete(0, END)

def backspace():
    entry.delete(len(entry.get())-1, END)

entry = Entry(app,
              font=('Arial', 50),
              fg='green',
              bg='black',
              show='*')

entry.insert(0, 'spongebob')
entry.pack(side=LEFT)
Button(app, text='submit', command=submit).pack(side=RIGHT)
Button(app, text='delete', command=delete).pack(side=RIGHT)
Button(app, text='backspace', command=backspace).pack(side=RIGHT)
################################################################x
app.mainloop()
