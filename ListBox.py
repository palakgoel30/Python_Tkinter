from tkinter import *

main_window = Tk()
main_window.title("Lets Start Tkinter")
main_window.minsize(width=400, height=200)
main_window.maxsize(width=800, height=500)

lb1 = Listbox(main_window, width=15, height=10)
list1 = ["Palak", "Sweeta", "Rita"]
for i in list1:
    lb1.insert(END, i)
lb1.pack()


def deletion():
    lb1.delete(ANCHOR)


b1 = Button(main_window, text='Remove', command=deletion)
b1.pack()
main_window.mainloop()
