from tkinter import *

main_window = Tk()
main_window.title("Lets Start Tkinter")
main_window.minsize(width=400, height=200)
main_window.maxsize(width=800, height=500)

# variable for getting text
v = StringVar()

# Entry
b2 = Entry(main_window, width=20, bd=6, font=("calibri",20),textvariable = v)
# b2.grid(row=5,column = 9)
b2.place(x=60, y=80)

#output in Label
l1 = Label(main_window,text = "              ",bg = "pink",fg = 'black')
l1.place(x = 150,y = 150)

def outLabel():
    x = v.get()
    print(x)
    l1.config(text = x)

# Button
b1 = Button(main_window, text="Submit",command = outLabel)
b1.place(x=350, y=300)


main_window.mainloop()
