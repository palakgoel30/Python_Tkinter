from tkinter import *  # Step1

main_window = Tk()  # Step2 assinging tk object to main window variable
main_window.title("Lets Starts Tkinter")  # Adding title
main_window.minsize(width=400, height=200)  # Initialize the minimum size of gui window
main_window.maxsize(width=800, height=500)  # Initialize the maximum size of gui window

# Different types of Widgets
# LABEL
l1 = Label(main_window, text="Music Music !!",bg = 'Black',fg = 'white')
l1.pack()
#l1.grid(row=8, column=5)  # Use grid for l1 label
#l1.place(x=50,y =70)
image1= PhotoImage(file="C:/Users/gpala/Desktop/Palak/Code/Python_Tkinter/images/logo.png")

l2 = Label(main_window, image = image1)
l2.pack()
#l2.place(x=10, y=70)
#l2.grid(row=4, column=5)
main_window.mainloop()  # Step4 creates a main loop
