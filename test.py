# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 09:35:19 2023

@author: RM275199
"""

from pynput.mouse import Controller, Button
from time import sleep, time

import random

mouse = Controller()

mouse.position = (300, 400)
t1 = time()
while time()-t1 < 30000:
    print(mouse.position)
    print(int(time()-t1))
    (x, y) = mouse.position
    #mouse.press(Button.left)
    #mouse.release(Button.left)
    #mouse.position = (x + random.randint(-1, 1),y + random.randint(-1, 1))
    if int(time()-t1)%10 == 0:
        mouse.position = (995, 125)
        mouse.press(Button.left)
        mouse.release(Button.left)
        sleep(1)
        mouse.position = (629,303)
        mouse.press(Button.left)
        mouse.release(Button.left)
    sleep(1)