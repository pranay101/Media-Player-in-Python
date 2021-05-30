from tkinter import *
#import function


#core functions
def _quit():
    window.quit()
    window.destroy()
    exit()


#declare the window variable
window =Tk()

#give a suitable name to the window
window.title("Mediaplayer")

#Set it's height and width
window.configure(width = 700, height=500)

#give a background color to the window
window.configure(bg='#1a1b1c')



#creating menu bar
menuBar = Menu(window)

#initialize menu bar
window.config(menu=menuBar)

#File menu
filemenu = Menu(menuBar, tearoff=0,)
filemenu.add_command(label="Open")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=_quit)
menuBar.add_cascade(label="File", menu = filemenu)

#Help menu
helpmenu = Menu(menuBar, tearoff=0)
helpmenu.add_command(label="About Mediaplayer")
helpmenu.add_separator()
helpmenu.add_command(label="Rate us on Github")
helpmenu.add_separator()
helpmenu.add_command(label="Help")
menuBar.add_cascade(label='Help', menu = helpmenu)

#calling main
window.mainloop()

