from tkinter import *

def change_color():
    button['bg'] = 'yellow'

window = Tk()
window.title("Special Midterm Exam in OOP")
window.geometry("500x300")

button = Button(window, text="Click to Change Color", command=change_color)
button.place(x=150, y=100)

window.mainloop()
