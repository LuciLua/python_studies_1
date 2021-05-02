import tkinter as tk
import pyautogui, time, msvcrt, keyboard


def start_flood():
    f = open(entry1.get(), 'r')
    while True:
        for word in f:
            pyautogui.typewrite(word)
            pyautogui.press("enter")
            if keyboard.is_pressed("q"):
                print("Canceled")
                break
        print("Success!")
        break

window = tk.Tk()
window.resizable(0, 0)


canvas1 = tk.Canvas(window, width=300, height=350, bg='gray90', relief='raised')
window.title("L4Dev Flood v0.0.1 Alpha")
window.geometry('300x270')
canvas1.pack()

label1 = tk.Label(window, text='Flood Machine:', bg = 'gray90')
label1.config(font=('helvetica', 16))
canvas1.create_window(150, 35, window=label1)

label2 = tk.Label(window, text='digite nome do arquivo:', bg='gray90')
label2.config(font=('helvetica', 10))
canvas1.create_window(150, 80, window=label2)

label3 = tk.Label(window, text=' (com a extensão | ex: file.txt)', bg='gray90')
label3.config(font=('helvetica', 10))
canvas1.create_window(150, 100, window=label3)

entry1 = tk.Entry(window, width=27)
canvas1.create_window(150, 120, window=entry1)

button1 = tk.Button(text='     Start    ', bg='green', fg='white', font=('helvetica', 12, 'bold'), command=start_flood)
canvas1.create_window(150, 180, window=button1)

window.mainloop()