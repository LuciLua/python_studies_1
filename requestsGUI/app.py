from doctest import master
import tkinter as tk
from turtle import bgcolor, color
import pyautogui
import time
import msvcrt
import keyboard
import requests

from tkinter import Text
from PIL import ImageTk, Image

# Default values for arguments
status = '???'
method = 'get'
path = 'http://google.com'
value = "defaultValue"
key = "defaultValue"
cookies = False
content = False
headers = False


def app():
    print("app is running")


def check():
    print('check click')


def definesMethod():
    return


window = tk.Tk()
window.resizable(width=False, height=False)

width = 800
height = 470

halfWidth = width/2
halfHeight = height/2

# SCREEN PROPS
canvas = tk.Canvas(
    window, width=width, height=height,
    bg='#332233', relief='raised',
    highlightthickness=0  # bordas da janela
)

# Window config
window.title("L4Dev Requests v0.0.1 Alpha")
window.geometry('800x470')

# PACK
canvas.pack(fill="both", expand=True)

# Create welcome screen

def welcome():
    # urlLabel.destroy()
    # urlInput.destroy()
    # methodInput.destroy()
    # methodLabel.destroy()
    # headerOption.destroy()
    # contentOption.destroy()
    # cookiesOption.destroy()
    # sendBtn.destroy()
    
    path = urlInput.get()
    method = methodInput.get()
    status = requests.get(path).status_code
    
    # Status result
    statusLabelResult = tk.Label(
    window, text=status,
    bg='#332233',
    foreground='#55ff55'
    )
    
    canvas.create_window(550, 100, window=statusLabelResult, anchor="nw", width=50)

    print('status: ', status)
    print('path: ' + path)
    print('method: ' + method)

    if (method == 'post'):
        result = requests.post(path).content
    if (method == 'get'):
        result = requests.get(path).content

    textResult.insert('1.0', result)


# Add a welcome message
textResult = Text(
    foreground='#fff', background='#221122',
    highlightthickness=0, highlightbackground='#221111',
    padx=15, pady=15,
)

canvas.create_window(
    400, 350,
    width=805, height=250,
    window=textResult)

# Define Entry Boxes
urlInput = tk.Entry(window, width=27)
urlInput.config(border=0, font='12')

methodInput = tk.Entry(window, width=27)
methodInput.config(border=0, font='12')

# Add the entry boxes to the canvas
canvas.create_window(190, 70, anchor="nw", window=urlInput)
canvas.create_window(68, 130, anchor="nw", window=methodInput)


# Define Label Boxes
# URL [LABEL]
urlLabel = tk.Label(window, text='Url:', bg='gray90')
urlLabel.config(font=('helvetica', 10),  bg='#332233', foreground="#fff")
# METHOD [LABEL]
methodLabel = tk.Label(window, text='Method', bg='gray90')
methodLabel.config(font=('helvetica', 10), bg='#332233', foreground="#fff")

# Add the label boxes to the canvas
# URL
canvas.create_window(80, 40, window=urlLabel)
canvas.create_window(190, 70, window=urlInput)
# METHOD
canvas.create_window(90, 100, window=methodLabel)

# OPTIONS
headerOption = tk.Checkbutton(
    window, text='Header',
    bg='#332233',
    variable=1, onvalue=1, offvalue=0, command=check)

contentOption = tk.Checkbutton(
    window, text='Content',
    bg='#332233',
    variable=2, onvalue=2, offvalue=0, command=check)

cookiesOption = tk.Checkbutton(
    window, text='Cookies',
    bg='#332233',
    variable=3, onvalue=3, offvalue=0, command=check)

# PUT OPTIONS ON SCREEN
canvas.create_window(100, 180, window=headerOption)
canvas.create_window(200, 180, window=contentOption)
canvas.create_window(300, 180, window=cookiesOption)



# Status
statusLabel = tk.Label(
    window, text='Status: ',
    bg='#332233',
    foreground='#554455'
)
canvas.create_window(500, 100, window=statusLabel, anchor="nw", width=50)

# # Status result
# statusLabelResult = tk.Label(
#     window, text=status,
#     bg='#332233',
#     foreground='#55ff55'
# )
# canvas.create_window(550, 100, window=statusLabelResult, anchor="nw", width=50)

# Define Button
sendBtn = tk.Button(
    text='Send', bg='#443344', fg='white',
    font=('helvetica', 12, 'bold'),
    command=welcome,
    highlightthickness=0,
    border=0
)

# Add the button to the canvas
canvas.create_window(500, 50, window=sendBtn, anchor="nw", width=200)


# RUN
window.mainloop()
