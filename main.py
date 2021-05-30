from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import pygame
import json
#import function





#declare the window variable
window =Tk()

#give a suitable name to the window
window.title("Mediaplayer")
window.iconbitmap("icon.ico")

#Set it's height and width
window.geometry("400x300")

#give a background color to the window
window.configure(bg='#1a1b1c')

# core functions 
# All core function starts with underscore("_")
Song_number = 0
Song_location = {}

def _quit():
    window.quit()
    window.destroy()
    exit()

def _openfile():
    Song_loc = fd.askopenfilename(title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))
    song_name= Song_loc.split('/')[-1].split('.')[0]    
    Song_location[song_name] = Song_loc
    Song_location['Now_playing'] = song_name
    # Now_playing = song_name
    # Song_number+=1
    playlist.insert(END,song_name)

def play():
    print("play")
    song = playlist.get(ACTIVE)
    song_to_play = Song_location[song]
    pygame.mixer.music.load(song_to_play)
    pygame.mixer.music.play(loops=0)


def pause():
    print("pause")
    # Stop Song From Playing
    pygame.mixer.music.stop()
    playlist.selection_clear(ACTIVE)

def replay():
    print("replay")
    song_to_play = Song_location[Song_location['Now_playing']]
    pygame.mixer.music.load(song_to_play)
    pygame.mixer.music.play(loops=0)

def delete():
    print("delete")
    # Delete Currently Selected Song
    playlist.delete(ANCHOR)
    # Stop Music if it's playing
    pygame.mixer.music.stop()



    
pygame.mixer.init()# initialise the pygame

#initilize frame
master_frame = Frame(window)
master_frame.pack(pady=20)

playlist = Listbox(master=master_frame, bg="#1a1b1c", fg="white", width=60, selectbackground="#d6d6d6", selectforeground="black")
playlist.grid(row=0, column=0)


# Define Player Control Button Images
play_btn_img = PhotoImage(file='icons/play.png')
pause_btn_img =  PhotoImage(file='icons/pause.png')
replay_btn_img =  PhotoImage(file='icons/replay.png')
add_btn_img =  PhotoImage(file='icons/add.png')
delete_btn_img =  PhotoImage(file='icons/delete.png')

# Create Player Control Frame
controls_frame = Frame(master_frame)
controls_frame.grid(row=1, column=0, pady=0)


# Create Player Control Buttons
play_button = Button(controls_frame, image=play_btn_img, borderwidth=0, command=play)
pause_button = Button(controls_frame, image=pause_btn_img, borderwidth=0, command=pause)
replay_button = Button(controls_frame, image=replay_btn_img, borderwidth=0, command=replay)
add_button = Button(controls_frame, image=add_btn_img, borderwidth=0, command=_openfile)
delete_button =  Button(controls_frame, image=delete_btn_img, borderwidth=0, command= delete)


add_button.grid(row=0, column=4, padx=10)
play_button.grid(row=0, column=0, padx=10)
replay_button.grid(row=0, column=2, padx=10)
pause_button.grid(row=0, column=1, padx=10)
delete_button.grid(row=0, column=3, padx=10)


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

