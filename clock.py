from tkinter import *
import tkinter
from datetime import datetime

import pyglet
pyglet.font.add_file('digital-7.ttf')


cor1 = "#3d3d3d"  # black
cor2 = "#21c25c"  # green

root = Tk()
root.title("")
root.geometry('430x180')
root.resizable(width=FALSE, height=FALSE)
root.configure(background=cor1)


def clock():
    time = datetime.now()

    hour = time.strftime("%H:%M:%S")
    weekday = time.strftime("%A")
    day = time.day
    month = time.strftime("%b")
    year = time.strftime("%Y")
    l1.config(text=hour)
    l1.after(200, clock)
    l2.config(text=weekday + " " + str(day) + "/" + str(month) + "/" + (year))


l1 = Label(root, font=('digital-7 80'), bg=cor1, fg=cor2)
l1.grid(row=0, column=0, sticky=NW, padx=5)

l2 = Label(root,  font=('digital-7 20'), bg=cor1, fg=cor2)
l2.grid(row=1, column=0, sticky=NW, padx=5)

clock()

root.mainloop()