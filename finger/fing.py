import tkinter as tk
from tkinter import *
import pyautogui, cv2
from PIL import Image, ImageTk

import numpy as np
from matplotlib import pyplot as plt

# Imagem
img = cv2.imread('finger.jpg')
cat = cv2.VideoCapture('finger.mp4')

# show img
plt.imshow(img)
plt.show()




cv2.waitKey(0)
cv2.destroyAllWindows()

# Imagem no tkinter
