from tkinter import *

app = Tk()

canvas = Canvas(app, height=500, width=500)
# blueline = canvas.create_line(0,0, 500,500, fill='blue', width=5)
# redline = canvas.create_line(0,500, 500,0, fill='red', width=5)
# canvas.create_rectangle(50, 50, 250, 250, fill='purple')
# canvas.create_polygon(250,0, 500,500, 0,500, fill='yellow', outline="black", width=5)
points = [250,0, 500,500, 0,500]
# canvas.create_polygon(points, fill='yellow', outline="black", width=5)
# canvas.create_arc(0,0, 500, 500, style=CHORD, start=180, extent=180) #fill='green'
canvas.create_arc(0,0, 500,500, fill='red', extent=180, width=10)
canvas.create_arc(0,0, 500,500, fill='white',start=180, extent=180, width=10)
canvas.create_oval(190,190, 310,310, fill='white', width=10)
canvas.pack()

app.mainloop()