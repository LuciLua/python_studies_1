import cv2
import numpy as np
from matplotlib import pyplot as plt

iA = cv2.imread('imagem.png')
iB = cv2.imread('img.jpg')

# IMREAD_COLOR - 1
# IMREAD_UNCHAGED = -1

iResult = iA

# a = cv2.imshow("Altered", iResult)

# cv2.imshow('image', iA)


plt.imshow(iA, cmap = 'gray', interpolation='bicubic')

plt.plot([900, 400], [80, 600], 'r', linewidth=2)
plt.show()

cv2.imwrite('imagem', iA)


cv2.waitKey(0)
cv2.destroyAllWindows()