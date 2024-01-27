from tkinter import *
from tkinter.ttk import *
import time

app = Tk()
def start():
    GB = 100
    download = 0
    speed = 1
    while download < GB:
        time.sleep(0.05)
        bar['value']+= (speed/GB) * 100
        download += speed
        percent.set(str(int(download/GB * 100)) + '%')
        text.set(str(download) + '/' + str(GB) + 'GB completed')
        app.update_idletasks()

percent = StringVar()
text = StringVar()

bar = Progressbar(app, orient=HORIZONTAL, length=300)
bar.pack(pady=10)

percenlabel= Label(app, textvariable=percent)
percenlabel.pack()

tasklabel= Label(app, textvariable=text)
tasklabel.pack()

button = Button(app, text='download', command=start)
button.pack()
app.mainloop()