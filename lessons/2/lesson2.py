from tkinter import *

## ������� ������:
W = 600  # ������
H = 400  # ������

## ������� ������:
D = 10

## ��������� ��������� ������:
X_START = 150
Y_START = 100

## �������� ����������� �������:
RACKET_SPEED = 10

Win=Tk()
c = Canvas(Win, width=W, height=H, bg='black')
c.pack()

## ��������� ����:
c.create_rectangle(30, 30, W - 30, H - 30, outline='white', width=8)
c.create_line(W / 2, 30, W / 2, H - 30, fill='white', width=8, dash=(100, 10))

## ������� � �����:
ball = c.create_rectangle(X_START, Y_START, X_START + D, Y_START + D, fill='white')
left_racket = c.create_line(50, 150, 50, 200, fill='white', width=10)
right_racket = c.create_line(W - 50, 150, W - 50, 200, fill='white', width=10)

## ������� ��� �������� �������:
def move_up_left_racket(event):
    c.move(left_racket, 0, -RACKET_SPEED)
    
def move_down_left_racket(event):
    c.move(left_racket, 0, RACKET_SPEED)
    
def move_up_right_racket(event):
    c.move(right_racket, 0, -RACKET_SPEED)
    
def move_down_right_racket(event):
    c.move(right_racket, 0, RACKET_SPEED)


## ��������� ������� ������:
Win.bind('w', move_up_left_racket)
Win.bind('s', move_down_left_racket)
Win.bind('<Up>', move_up_right_racket)
Win.bind('<Down>', move_down_right_racket)

Win.mainloop()
