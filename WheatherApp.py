'''
Program:WheatherApp.py
Author:Everett Bassett
Last date modified: 5/17/22

The purpose of this program is to call data from
the OpenWheatherMap API to return wheather conditions
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
import tkinter as tk
import requests
from tkinter import messagebox

HEIGHT = 500
WIDTH = 600


def test_function(entry):
	print("This is the entry:", entry)

# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
# a4aa5e3d83ffefaba8c00284de6ef7c3

# def API call
def format_response(weather):
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']

		final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s' % (name, desc, temp)
	except:
		final_str = 'There was a problem retrieving that information'

	return final_str

# def NAV to menu.py
# destroy root at nav
def mainMenu():
    root.destroy()
    import menu.py

# def popup function for quit button
def popup():
    response = messagebox.askokcancel("Skate Conditions?", "Click Ok to close, cancel to return to menu.")
    #Label(root, text=response).pack()
    if response == 1:
        command=root.destroy()
    else:
        Label(root, text="Skate Conditions").pack()

# def output for API
def get_weather(city):
	weather_key = 'a4aa5e3d83ffefaba8c00284de6ef7c3'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
	response = requests.get(url, params=params)
	weather = response.json()

	label['text'] = format_response(weather)


# initilize window
root = tk.Tk()
root.title("Skate Conditions") # title 
root.iconbitmap('nuclear.ico') # mushroom cloud image

# initilize canvas for widget placement
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# add background image for window
background_image = tk.PhotoImage(file='landscape.png') # cartoon landscape image
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# create frame for entry
frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

# initialize entry
entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

# create button to callback api from entry
button = tk.Button(frame, text="Skate Conditions", font=40, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

# create quit button to close program
button2 = tk.Button(root, text="Quit", font=40, command=popup)
button2.pack()

# create nav button to return to main menu
button3 = tk.Button(root, text="Main Menu", font=40, command=mainMenu)
button3.pack()

# create lower frame for output
lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

root.mainloop()
