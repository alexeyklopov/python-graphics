from tkinter import *

Win1 = Tk()
c = Canvas(Win1, width=800, height=500, bg='#292727')
c.pack()


def menu():
    global b1, b2
    c.config(width=400, height=500, )
    c.create_text(195, 150, text="PONG", fill='black', font=("Calibri", 80))
    c.create_text(205, 142, text="PONG", fill='white', font=("Calibri", 80))
    b1 = Button(text="PLAY", bg='white', font=("Calibri", 30), fg='black', bd=0, width=7, height=0, command=START)
    b1.place(x=140, y=250)
    b2 = Button(text="EXIT", bg='white', font=("Calibri", 30), fg='black', bd=0, width=7, height=0, command=EXIT)
    b2.place(x=140, y=350)
    c.create_rectangle(128, 255, 255, 320, fill='black')
    c.create_rectangle(128, 355, 255, 420, fill='black')
    c.create_rectangle(50, 50, 350, 450, outline='white', width=8)


def START():
    global b1, b2
    c.delete("all")
    b1.destroy()
    b2.destroy()
    game()


def MENU():
    global ls, rs
    c.delete("all")
    ls.destroy()
    rs.destroy()
    menu()


def EXIT():
    Win1.destroy()


def game():
    global lp, rp, point, ls, rs, scoreleft, scoreright
    scoreleft = 0
    scoreright = 0
    c.config(width=800, height=600)
    ls = Label(text=scoreleft, bg='#292727', fg='white', font=("Calibri", 80))
    ls.place(x=290, y=20)
    rs = Label(text=scoreright, bg='#292727', fg='white', font=("Calibri", 80))
    rs.place(x=440, y=20)
    c.create_rectangle(45, 134, 755, 566, outline='white', width=8)
    c.create_line(400, 138, 400, 566, fill='white', width=8, dash=(10, 2))
    point = c.create_rectangle(400, 300, 410, 310, fill='red')
    lp = c.create_line(61, 220, 61, 220 + 60, fill='white', width=8)
    rp = c.create_line(739, 220, 739, 220 + 60, fill='white', width=8)
    Win1.bind('<w>', up_lp)
    Win1.bind('<s>', down_lp)
    Win1.bind('<Up>', up_rp)
    Win1.bind('<Down>', down_rp)
    Win1.after(100, motion)


def up_lp(event):
    if c.coords(lp)[1] > 150:
        c.move(lp, 0, -30)


def down_lp(event):
    if c.coords(lp)[3] < 550:
        c.move(lp, 0, 30)


def up_rp(event):
    if c.coords(rp)[1] > 150:
        c.move(rp, 0, -30)


def down_rp(event):
    if c.coords(rp)[3] < 550:
        c.move(rp, 0, 30)


x = 5
y = 5


def motion():
    global x, y, point, scoreleft, scoreright, ls, rs
    if c.coords(point)[0] < 70 and c.coords(point)[3] > c.coords(lp)[1] and c.coords(point)[1] < c.coords(lp)[3]:
        x = -x
        c.move(point, x, y)
    elif c.coords(point)[2] > 739 and c.coords(point)[3] > c.coords(rp)[1] and c.coords(point)[1] < c.coords(rp)[3]:
        x = -x
        c.move(point, x, y)
    elif c.coords(point)[0] < 45:
        x = -x
        scoreright += 1
        rs.config(text=scoreright)
        l = 400 - c.coords(point)[0]
        t = 250 - c.coords(point)[1]
        c.move(point, l, t)
    elif c.coords(point)[1] < 134:
        y = -y
        c.move(point, x, y)
    elif c.coords(point)[2] > 755:
        x = -x
        scoreleft += 1
        ls.config(text=scoreleft)
        l = -400 + c.coords(point)[0]
        t = 250 - c.coords(point)[1]
        c.move(point, -l, t)
    elif c.coords(point)[3] > 566:
        y = -y
        c.move(point, x, y)
    else:
        c.move(point, x, y)
    if (scoreleft != 2 and scoreright != 2):
        Win1.after(10, motion)
    else:
        scoreleft = scoreright = 0
        MENU()


menu()