from tkinter import *

## Размеры холста:
W = 600  # ширина
H = 400  # высота

## Диаметр мячика:
D = 10

## Начальное положение мячика:
X_START = 150
Y_START = 100

Win=Tk()
c = Canvas(Win, width=W, height=H, bg='black')
c.pack()

## Отрисовка поля:
c.create_rectangle(30, 30, W - 30, H - 30, outline='white', width=8)
c.create_line(W / 2, 30, W / 2, H - 30, fill='white', width=8, dash=(100, 10))

## Ракетки и мячик:
c.create_rectangle(X_START, Y_START, X_START + D, Y_START + D, fill='red')
c.create_line(50, 150, 50, 200, fill='white', width=10)
c.create_line(W - 50, 150, W - 50, 200, fill='white', width=10)

Win.mainloop()