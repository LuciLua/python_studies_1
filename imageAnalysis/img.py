import cv2
import numpy as np
from matplotlib import pyplot as plt

# Implementation of matplotlib function
import datetime

# image
imageA = cv2.imread('imagem.png')
plt.imshow(imageA)



# lines
# [x][y]
# plt.plot([100, 400], [200, 200], 'r', linewidth=1)
# plt.plot([150, 350], [100, 100], 'b', linewidth=1)
# plt.legend("12")


# dates
dates = datetime.date.today()
plt.title(dates)


plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()