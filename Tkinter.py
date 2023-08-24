from tkinter import * #Step1

main_window = Tk() #Step2 assinging tk object to main window variable
main_window.title("Lets Starts Tkinter") # adding title
main_window.minsize(width = 400, height= 200) # initailize the minimum size of gui window
main_window.maxsize(width=800,height=500) # initalize the maximum size of gui window
main_window.mainloop() #Step4 creates a mainloop