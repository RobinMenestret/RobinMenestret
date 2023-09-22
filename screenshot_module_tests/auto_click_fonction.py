# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 11:38:46 2023

@author: RM275199
"""

"""
This programme has for goal to take a picture as input and when this picture
appears on the screen, the mouse go to click it
"""

import pyautogui
import time
from pynput.mouse import Controller, Button
import cv2
import numpy as np
from threading import Thread


file = {'pic_1' : 0.0485,
        'pic_2' : 0.005,
        'pic_3' : 0.003,
        'pic_4' : 0.0025,
        'pic_5' : 0.0035
        }

def matchTemplate(pic_test, screen, mouse):
    pic = cv2.imread('data/input_pic/' + pic_test + '.jpg')
    screen = cv2.imread('data/screens/' + screen + '.jpg')
    image =  cv2.matchTemplate(screen, pic, cv2.TM_SQDIFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(image)

    #print(pic_test + " : " + str(int(min_val*10000)/10000))
    if min_val < file[pic_test] :
        #print("It appears in {} with a score of {}.".format(min_loc, min_val))
        mouse.position = (min_loc[0]+40, min_loc[1]+20)
        mouse.press(Button.left)
        mouse.release(Button.left)
        mouse.position = (1850, 512)
    return False, min_loc



def main():
    stop = False
    mouse = Controller()

    while True:
        screenshot = pyautogui.screenshot()
        screenshot.save('data/screens/screenshot.jpg')
        threads = []
        for i in range(5):
            threads.append(Thread(target=matchTemplate, args = ['pic_'+str(i+1), 'screenshot', mouse]))
            #stop, min_loc = matchTemplate('pic_'+str(i+1), 'screenshot')
        for i in range(5):
            threads[i].start()
        for i in range(5):
            threads[i].join()
            



main()

