from tkinter import *

W = 600
H = 400

Win = Tk()
c = Canvas(Win, width=W, height=H, bg="white")
c.pack()

R = 40

block = c.create_rectangle(50, 50, 50 + R, 50 + R, fill="blue", outline="blue")

is_pressed = False

def motion(event):
    global is_pressed
    x, y = event.x, event.y
    is_inside_block = c.coords(block)[0] <= x <= c.coords(block)[2] and c.coords(block)[1] <= y <= c.coords(block)[3]
    if is_pressed and is_inside_block:
        c.coords(block, x - R / 2, y - R / 2, x + R / 2, y + R / 2)

def press_on(event):
    global is_pressed
    is_pressed = True
    
def press_off(event):
    global is_pressed
    is_pressed = False

Win.bind("<Button-1>", press_on)
Win.bind("<ButtonRelease-1>", press_off)
Win.bind("<Motion>", motion)

Win.mainloop()
