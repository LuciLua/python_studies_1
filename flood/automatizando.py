import tkinter as tk
import pyautogui, time, msvcrt, keyboard



def start_flood():
    f = open(entry1.get(), 'r')
    while True:
        for word in f:
            pyautogui.typewrite(word)
            pyautogui.press("enter")
            if keyboard.is_pressed("q"):
                pyautogui.alert("cancelado")
                break
        pyautogui.alert("Flodado com sucesso! Se deseja Floodar dnovo aperte ENTER")
        break

window = tk.Tk()

canvas1 = tk.Canvas(window, width=300, height=350, bg='gray90', relief='raised')
canvas1.pack()

label1 = tk.Label(window, text='Flood Machine:', bg = 'gray90')
label1.config(font=('helvetica', 12))
canvas1.create_window(150, 80, window=label1)

label2 = tk.Label(window, text='digite nome do arquivo:', bg='gray30')
label2.config(font=('helvetica', 10))
canvas1.create_window(150, 80, window=label1)

entry1 = tk.Entry(window, width=27)
canvas1.create_window(150, 120, window=entry1)

button1 = tk.Button(text='      Iniciar Flood    ', bg='green', fg='white', font=('helvetica', 12, 'bold'), command=start_flood)
canvas1.create_window(150, 180, window=button1)

window.mainloop()