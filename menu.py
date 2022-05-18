'''
Program:menu.py
Author:Everett Bassett
Last date modified: 5/17/22

The purpose of this program is to serve as the main menu
for The Skate Bomb application

The user will be able to launch the Skate Condition application
or close the entire program

The Skate Bomb application serves as a tool for skateboards to
better plan their skate trip by checking the current whether 
conditions at the skate spot of their choosing

Once the user launches the Skate Condition window by selecting
it from the main menu, the user is then asked to input the
city name, or zip code of the location they plan to skate.
The program then returns the current wheather condition, 
temperature, and name of the city entered.
'''
# import tkinter all
# import PIL 
# import messagebox

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image


# intitialize window
root = Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title("The Skate Bomb :: MAIN") # title
root.iconbitmap('nuclear.ico') # mushroom cloud


# define quit command message
def popup():
    response = messagebox.askokcancel("Quit The Skate Bomb?", "Click Ok to close, cancel to return to menu.")
    #Label(root, text=response).pack()
    if response == 1:
        command=root.destroy()
    else:
        Label(root, text="Main Menu").pack()

def nextPage():
    root.destroy()
    import WheatherApp.py

background_image = PhotoImage(file='skateboard.png') # skateboarder image
background_label = Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# welcome message
label_welcome = Label(root, text="Welcome to The Skate Bomb!")
label_welcome.pack()

# create LabelFrame for main menu
frame = LabelFrame(root, text="Main Menu", padx=100, pady=100, bd=10)
frame.pack(padx=10, pady=10)

# create nav for main menu frame
# create weather app button
# create kill button
btn1 = Button(frame, text="Get Skate Conditions", command=nextPage)
btn1.grid(row=0, column=0)
btn2 = Button(frame, text="Quit", command=popup)
btn2.grid(row=1, column=0)

root.mainloop()
