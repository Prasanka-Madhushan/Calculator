from tkinter import*
import math

root = Tk()
blank_space = " "
root.title (50 * blank_space + "My Calculator")
root.resizable(width= FALSE, height= FALSE)
root.geometry("438x573+460+40")

coverFrame = Frame (root, bd= 20, pady=2, relief=RIDGE)
coverFrame.grid()

coverMainFrame = Frame (coverFrame, bd= 10, pady=2, bg='navyblue', relief=RIDGE)
coverMainFrame.grid()

MainFrame = Frame (coverMainFrame, bd= 5, pady=2, relief=RIDGE)
MainFrame.grid()

root.mainloop()