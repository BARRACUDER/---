import numpy as np
from mss import *
import cv2
import pyautogui as gui
from matplotlib import pyplot as plt

import time
# gui.sleep(0.5)
def viewImage(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

with mss() as sct:
    sct.shot()
image=cv2.imread("monitor-1.png")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

arr = np.array(gray_image)
plt.imshow(arr,cmap='gray')
plt.show()
print(arr)
