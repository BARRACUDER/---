
from mss import mss
import cv2
import pyautogui
import time
import numpy as np
class coordinates():
    replaybutton = (697, 360)


def restartGame():
    pyautogui.click(coordinates.replaybutton)
    # pyautogui.keyDown('down')


def press_space():

    pyautogui.keyDown('space')
    time.sleep(0.08)
    #pyautogui.keyDown('down')
    #time.sleep(0.04)
    pyautogui.keyUp('space')
    #pyautogui.keyUp('down')
    # print("jump")


def imageGrab():
    with mss() as sct:
        sct.shot()
    image = cv2.imread(r'C:\Users\User\PycharmProjects\pythonProject\monitor-1.png')
    gray_image = cv2.cvtColor(image[360:390 ,430:647], cv2.COLOR_BGR2GRAY)
    a = np.array(gray_image)
    print(sum(sum(a)))
    return a


restartGame()
while True:
    if sum(sum(imageGrab() ))!= 48806:
        press_space()