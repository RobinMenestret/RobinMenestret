# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 14:10:49 2023

@author: RM275199
"""

import math

x = math.sqrt(2)
x_name = "racine(2)"

def approx_const(x, x_name = "value", prec = 100):
    val = 1
    h, b = 0,0
    for i in range(prec):
        for j in range(prec):
            try :
                if abs(x-i/j) < val :
                    val = abs(x-i/j)
                    h = i
                    b = j
            except :
                pass
                
    print(x_name + " : " + str(h) + "/" + str(b) +" = "+ str(h/b))

x = math.exp(1)
x_name = "racine(2)"    

approx_const(x, "e")