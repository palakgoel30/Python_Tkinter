from tkinter import *

main_window = Tk()
main_window.title("Lets Start Tkinter")
main_window.minsize(width = 400,height = 200)
main_window.maxsize(width=800,height=500)
#Button
b1 = Button(main_window,text = "Submit")
b1.place(x= 350,y = 300)
# Entry
b2 = Entry(main_window,width=70,bd = 6,font = ("calibri,20"))
#b2.grid(row=5,column = 9)
b2.place(x = 60,y = 80)
main_window.mainloop()