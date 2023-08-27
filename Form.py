from tkinter import *

window = Tk()
window.title("Registration Form")
window.minsize(width=400, height=200)
window.maxsize(width=500, height=250)

l1 = Label(window, text='Enter your name')
l1.place(x=5, y=7)

e1 = Entry(window, width=20, bd=1)
e1.place(x=150, y=7)

l2 = Label(window, text='Enter your phn number')
l2.place(x=5, y=40)

e2 = Entry(window, width=20, bd=1)
e2.place(x=150, y=40)

b1 = Button(window, text="Submit")
b1.place(x=150, y=80)

window.mainloop()
