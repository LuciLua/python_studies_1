import tkinter as tk
from turtle import bgcolor, color
import pyautogui
import time
import msvcrt
import keyboard
import requests

# Default values for arguments
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


window = tk.Tk()
window.resizable(0, 0)

# SCREEN PROPS
canvas = tk.Canvas(
    window, width=800, height=470,
    bg='#332233', relief='raised')
window.title("L4Dev Requests v0.0.1 Alpha")
window.geometry('800x470')
canvas.pack()

# URL
urlLabel = tk.Label(window, text='Url:', bg='gray90')
urlLabel.config(font=('helvetica', 10),  bg='#332233', foreground="#fff")
urlInput = tk.Entry(window, width=27)
# PUT URL ON SCREEN
canvas.create_window(80, 40, window=urlLabel)
canvas.create_window(150, 70, window=urlInput)

# METHOD
urlLabel = tk.Label(window, text='Method', bg='gray90')
urlLabel.config(font=('helvetica', 10), bg='#332233', foreground="#fff")
urlInput = tk.Entry(window, width=27)
# PUT METHOD ON SCREEN
canvas.create_window(90, 100, window=urlLabel)
canvas.create_window(150, 130, window=urlInput)

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

# SEND [BTN]
sendBtn = tk.Button(
    text='Send', bg='green', fg='white',
    font=('helvetica', 12, 'bold'),
    command=app)
# PUT SEND BTN ON SCREEN
canvas.create_window(200, 250, window=sendBtn)

# RUN
window.mainloop()
