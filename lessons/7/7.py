from tkinter import *

## Размеры холста:
W = 600  # ширина
H = 400  # высота

Win = Tk()
c = Canvas(Win, width=W, height=H, bg='black')
c.pack()

pong_label = Label(text="PONG", font="Arial 50", bg="black", fg="white")
pong_label.place(x=W/2-100, y=50)

play_button = Button(text="Play", font="Arial 30", bg="black", fg="white", width=4, height=1)
play_button.place(x=W/2-50, y=150)

exit_button = Button(text="Exit", font="Arial 30", bg="black", fg="white", width=4, height=1)
exit_button.place(x=W/2-50, y=250)

Win.mainloop()