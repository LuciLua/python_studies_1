from os import name
import cv2
import numpy as np
from matplotlib import pyplot as plt
import pyautogui
import pandas as pd

list = ['morango', 'maca', 'uva', 'pera']
index = ['mo', 'ma', 'u', 'p']

s1 = pd.Series(list, index=index, name='Frutas')

# print(list)
print(s1.str.upper())
print(s1.count(), s1.name)
print(s1[2], 'Ocupando a posicao [2]')

print(pd.Series('test', range(10)))
print(pd.Series( 32, range(10)))

gasesNobresA = pd.Series([4.003, 20.180, 39.95, 83.798, 132.293, 222])

print(gasesNobresA)


# y = pyautogui.position()
# y = np.arange(10,100,5)

# x = np.arange(0,1000,1)

# plt.plot(x, x**2) #função

# plt.show()

# plt.scatter(x,y)

# dados = pd.read_csv('graficos\athlete_events.csv')
# print(dados.head())