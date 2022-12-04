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

# Window: propreties
window_width = 300
window_height = 200
windows_backgroundColor = '#1e1e1e'
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
window.title("prints_machine v0.1.0 Alpha")

# Join all elements?
canvas1.pack()

# remove the border
# window.overrideredirect(1)

# window center
window.eval('tk::PlaceWindow . center')

current_dir = os.getcwd()
screenshots_path = current_dir + '\\screenshots'

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


def takeScreenShot():
    window.iconify()
    sleep(.2)
    screenshot = pyautogui.screenshot()
    print("[...] Screenshot was taken")
    sleep(.4)
    window.deiconify()
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
    playSound('take')
    createDirectory()
    saveScreenShot()

def close():
    playSound('close')
    window.destroy()

def directory():
    playSound('directory')
    os.path.realpath(screenshots_path)
    os.startfile(screenshots_path)


half_width = window_width/2
half_heigth = window_height/2

# Label: title
label1 = tk.Label(
    window,
    text='Take photos',
    bg=backgroundColor_default,
    foreground=fontColor_default,
    anchor='center',
)
label1.config(font=('Poppins', 16))
canvas1.create_window(half_width, (half_heigth - 50), window=label1)

# button: Take a Photo
button1 = tk.Button(
    window,
    width=20,
    command=run,
    text='Take',
    anchor='center',
    background='#49ceff'
)
canvas1.create_window(half_width, (half_heigth + 10), window=button1)

# button: open Directory
button1 = tk.Button(
    window,
    width=20,
    command=directory,
    text='Directory',
    anchor='center',
    background='#ffcd42'
)
canvas1.create_window(half_width, (half_heigth + 40), window=button1)

# button: Destroy
button1 = tk.Button(
    window,
    width=20,
    command=close,
    text='Close',
    anchor='center',
    background='#e33c2f'
)
canvas1.create_window(half_width, (half_heigth + 70), window=button1)

# Start tk window
window.mainloop()
