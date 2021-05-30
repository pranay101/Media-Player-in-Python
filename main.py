from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import pygame
#import function





#declare the window variable
window =Tk()

#give a suitable name to the window
window.title("Mediaplayer")
window.iconbitmap(r"icon.ico")

#Set it's height and width
window.geometry("400x300")

#give a background color to the window
window.configure(bg='#1a1b1c')

# core functions 
# All core function starts with underscore("_")
def _quit():
    window.quit()
    window.destroy()
    exit()

def _openfile():
    Song_location = fd.askopenfilename(title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))
    song_name= Song_location.split('/')[-1].split('.')[0]    
    
    playlist.insert(END,song_name)

    
pygame.mixer.init()# initialise the pygame

#initilize frame
master_frame = Frame(window)
master_frame.pack(pady=20)

playlist = Listbox(master=master_frame, bg="#1a1b1c", fg="white", width=60, selectbackground="#d6d6d6", selectforeground="black")
playlist.grid(row=0, column=0)

name="prana prajapat"
playlist.insert(END,name)





#creating menu bar
menuBar = Menu(window)

#initialize menu bar
window.config(menu=menuBar)

#File menu
filemenu = Menu(menuBar, tearoff=0,)
filemenu.add_command(label="Add Music", command=_openfile)
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

