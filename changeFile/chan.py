import os
import argparse
import sys
from time import sleep
import tkinter as tk
from turtle import width
import pyautogui
from playsound import playsound 

# os.mkdir()

# argparse.ArgumentParser()

# Create Tk from tk
window = tk.Tk()

# RESIZE: none
window.resizable(0, 0)

window.anchor('center')

# Window: propreties
window_width = 300    
window_height = 200
windows_backgroundColor = '#3D3E4A'
backgroundColor_default = windows_backgroundColor
fontColor_default = '#fff'

canvas1 = tk.Canvas(
    window, 
    width=window_width,
    height=window_height,
    bg=windows_backgroundColor,
    relief='groove',
)

# Windows: title
window.title("Dankap0z v0.0.1 Alpha")

# Join all elements?
canvas1.pack()

current_directory = os.getcwd() 
full_path = current_directory + '\\result'

def createDirectory():
    if os.path.isdir(full_path):
        print("[...] directory already exists")
    else:
        os.makedirs(full_path)
        print("[...] directory created at " + full_path)


def takeScreenShot():
    
    sleep(2)
    playsound('take.wav') 
    window.resizable=True
    
    screenshot = pyautogui.screenshot()
    print("[...] Screenshot was taken")
    return screenshot
    
def saveScreenShot():
    takeScreenShot().save(full_path + '\\screenshot.png')
    print("[...] Screenshot was saved")
    

# main function
def run():
    createDirectory()
    saveScreenShot()
    
half_width = window_width/2
half_heigth = window_height/2

# Label: title
label1 = tk.Label(
    window, 
    text='Run here:', 
    bg = backgroundColor_default,
    foreground=fontColor_default,
    anchor='center'
)
label1.config(font=('helvetica', 16))
canvas1.create_window(half_width, (half_heigth - 20), window=label1)

# button
button1 = tk.Button(
    window,
    width=20,
    command=run,
    text='Run',
    anchor='center',
)
canvas1.create_window(half_width, (half_heigth + 20), window=button1)


# Start tk window
window.mainloop()
