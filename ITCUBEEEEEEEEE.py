
# 541 572
# 1286 352 поле динозаврика
# 595 536
# 639 498 рядом с динозавриком
import numpy as np
from mss import *
import cv2
import pyautogui as gui
import time
gui.sleep(0.5)
def viewImage(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

with mss() as sct:
    sct.shot()
image=cv2.imread("monitor-1.png")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
megaimage=gray_image[352:572,541:1286]
viewImage(megaimage, "black")
image_crs=megaimage
print(image_crs)

# def jump():
#     gui.keyDown("space")
#     gui.sleep(0.5)
#     gui.keyUp("space")      
