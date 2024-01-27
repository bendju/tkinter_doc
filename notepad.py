from tkinter import *
from tkinter import filedialog

BLACK = '#1c1c1c'
run = False


class MyMenu(Menu):
    def __init__(self, file_text):
        super().__init__()
        self.file_text = file_text
        self.file_menu = Menu(self, tearoff=0)
        self.add_cascade(label="file", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=quit)
        self.file_type = [ ('Text File', '.txt'), ('All Files', '.*')]

    def open_file(self):
        filepath = filedialog.askopenfilename(title="Open File", filetypes=self.file_type)
        file = open(filepath, 'r')
        self.file_text.text.insert(END, file.read())
        file.close()


    def save_file(self):
        file = filedialog.asksaveasfile(defaultextension='.txt', filetypes=self.file_type)
        if file is None:
            return

        file.write(str(self.file_text.text.get(1.0, END)))
        file.close()


class TextBox(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.pack()
        self.text = Text(self, font=(None, 13), width=1000, height=500)
        self.text.pack()


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title('App')
        self.geometry('1020x500')
        self.resizable(width=False, height=False)
        self.textbox = TextBox(self)
        self.menu = MyMenu(self.textbox)
        self.config(menu=self.menu)


app = App()
app.mainloop()