import os
import tkinter as tk
import pyautogui
import ctypes

from playsound import playsound
from time import sleep
from datetime import datetime

# minimize window
# ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

# Create Tk from tk
window = tk.Tk()

# RESIZE: none
window.resizable(0, 0)
window.anchor('center')

# directories
current_dir = os.getcwd()
screenshots_path = current_dir + '\\screenshots'

backgroundImage = current_dir + '\\assets\\background.png'
closeImage = current_dir + '\\assets\\close.png'

# colors
background = '#1e1e1e'
backgroundHover = '#222224'
primaryColor = '#0089d2'
cancelColor = '#a5272b'

# Window: propreties
window_width = 220
window_height = 150
half_width = window_width/2
half_heigth = window_height/2

windows_backgroundColor = background
backgroundColor_default = windows_backgroundColor
fontColor_default = '#fff'

canvas1 = tk.Canvas(
    window,
    width=window_width,
    height=window_height,
    bg=windows_backgroundColor,
    relief='groove',
    highlightthickness=0
)

# Windows: title
title = 'prints_machine v1.0.0 Alpha'
window.title(title)

# remove the tab
# but this stops de/iconify  
window.overrideredirect(1)

# window center
window.eval('tk::PlaceWindow . center')

# listen a sound effect
def playSound(type):
    assets_path = current_dir + '\\assets'
    if type == 'take':
        file_path = assets_path + '\\take.wav'
    elif type == 'directory':
        file_path = assets_path + '\\open.wav'
    else:
        file_path = assets_path + '\\destroy.wav'
    playsound(file_path)


# if not exist: create. If already, just print a messasge
def createDirectory():
    if os.path.isdir(screenshots_path):
        print("[...] directory already exists")
    else:
        os.makedirs(screenshots_path)
        print("[...] directory created at " + screenshots_path)

# take a screenshot
def takeScreenShot():
    window.overrideredirect(0)
    window.iconify()
    sleep(.3)
    screenshot = pyautogui.screenshot()
    playSound('take')
    print("[...] Screenshot was taken")
    sleep(.2)
    window.deiconify()
    window.overrideredirect(1)  
    return screenshot


def saveScreenShot():
    date = (datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f'))
    if os.path.isfile(screenshots_path + '\\screenshot.png'):
        # If screenshot.png already exists
        takeScreenShot().save(screenshots_path + '\\screenshot_%s.png' % date)
    else:
        # If screenshot.png not exists
        takeScreenShot().save(screenshots_path + '\\screenshot.png')

    print("[...] Screenshot was saved")


# main function
def run():
    createDirectory()
    saveScreenShot()

def close():
    window.destroy()

def minimize():
    window.iconify()
    
def directory():
    playSound('directory')
    os.path.realpath(screenshots_path)
    os.startfile(screenshots_path)

# Label: title
label1 = tk.Label(
    window,
    width=30,
    text=title,
    bg=backgroundColor_default,
    foreground=fontColor_default,
    justify='center',
)
label1.config(font=('Poppins', 7))
canvas1.create_window(80, (half_heigth - 55), window=label1)

# button: Take a Photo
button1 = tk.Button(
    window,
    width=10,
    command=run,
    text='📸 Take',
    anchor='center',
    background=primaryColor,
    border=0,
    foreground='#fff'
)
canvas1.create_window(half_width, (half_heigth), window=button1)

# button: open Directory
button1 = tk.Button(
    window,
    width=10,
    command=directory,
    text='📁 Directory',
    anchor='center',
    background='#2f3539',
    border=0,
    foreground='#fff'
)
canvas1.create_window(half_width, (half_heigth + 30), window=button1)

# button: minimize
button3 = tk.Button(
    window,
    width=3,
    height=0,
    command=minimize,
    text='-',
    anchor='center',
    border=0,
    background=background,
    highlightbackground=background,
    activeforeground='#fff',
    foreground='#fff',
    activebackground=backgroundHover,
)
button3.config(font=('Poppins', 12))
canvas1.create_window((window_width - 50), 20, window=button3)

# button: close
button2 = tk.Button(
    window,
    width=3,
    height=0,
    command=close,
    text='X',
    anchor='center',
    border=0,
    background=background,
    highlightbackground=background,
    activeforeground='#fff',
    foreground='#fff',
    activebackground=backgroundHover
)
button2.config(font=('Poppins', 12))
canvas1.create_window((window_width - 20), 20, window=button2)

# Join all elements?
canvas1.pack()

# Start tk window
window.mainloop()
