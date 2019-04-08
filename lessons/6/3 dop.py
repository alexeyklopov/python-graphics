from tkinter import *
import random
A=500
#####
Win = Tk()
c = Canvas(Win, width=A, height=A, bg='white')
c.pack()

label = Label(text="Я молодец", font="Arial 15", bg='green')
i=0
while i<100:
    xx=random.randint(0, A-60)
    yy=random.randint(0, A-60)
    Label(text="Я молодец", font="Arial 15", bg='green').place(x=xx, y=yy)
    i+=1