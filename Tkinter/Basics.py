from tkinter import *
window = Tk() #creating the screen/window

#layout manager: pack, grid, place

window.geometry("500x500")
window.title("Basic Calculator")

def greet():
    label1.config(text = f"I am {e1} learning app development", bg = "pink", fg = "black")

label1 = Label(window, text="Hi, this is KInjal", font=("Arial", 20), bg = "purple", fg = "white")
label1.pack(pady = 10, padx = 10, ipadx = 10, ipady = 10, side = "top", fill = "x")

label2 = Label(window, text="I'm in grade 12", font=("Arial", 20), bg = "light blue", fg = "white")
label2.pack(pady = 10, padx = 10, ipadx = 10, ipady = 10, side = "right", fill = "y")


submit = Button(window, text = "submit", bg = "blue", fg = "white", command = greet)
submit.pack(pady = 10, padx = 10, ipadx = 10, ipady = 10, side = "left")

e1 = Entry(window, font=("Arial", 20))

window.mainloop() #Just like a while true