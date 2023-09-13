from tkinter import *

main_window = Tk()
main_window.title("Lets Start Tkinter")
main_window.minsize(width=400, height=200)
main_window.maxsize(width=800, height=500)

f1 = Frame()
f1.pack()
f2 = Frame()
f2.pack(side = BOTTOM)
l1 = Label(f1,text = 'Learning !!!!!!')
l1.pack()
l2 = Label(f2,text = 'End !!!!!!!!!!!!!!!!')
l2.pack()
main_window.mainloop()