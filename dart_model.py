# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 15:18:37 2023

@author: RM275199
"""
import math
import random
from math import pi
from math import atan
import matplotlib.pyplot as plt

Aire_totale = pi*340*340/4
Aire_gros_centre = pi*31.8*31.8/4
Aire_petit_centre = pi*12.7*12.7/4
Aire_une_valeur = (Aire_totale - Aire_gros_centre)/20
Aire_tous_les_doubles = Aire_totale - pi*(162*162)
Aire_un_double = Aire_tous_les_doubles/20
Aire_tous_les_triples = pi*(214.8*214.8/4-206.8*206.8/4)
Aire_un_triple = Aire_tous_les_triples/20 
Aire_tous_les_simples = Aire_totale - Aire_tous_les_doubles - Aire_tous_les_triples - Aire_gros_centre
Aire_un_simple = Aire_tous_les_simples/20
Aire_25 = Aire_gros_centre - Aire_petit_centre

rayon_tot = 1
larg_dbl_trpl = 8/170
rayon_centre = 12.7/2/170
rayon_demi_centre = 31.8/2/170
rayon_trpl_ext = 107.4/170


def dist_o(x,y):
    return math.sqrt(x**2+y**2)


def multiplier(x, y):
    dist = dist_o(x,y)

    if dist <= rayon_centre :
        return (0,50)
    elif dist <= rayon_demi_centre:
        return (0,25)
    elif dist <= rayon_trpl_ext-larg_dbl_trpl:
        return (1,0)
    elif dist <= rayon_trpl_ext:
        return (3,0)
    elif dist <= rayon_tot-larg_dbl_trpl:
        return (1,0)
    elif dist <= rayon_tot:
        return (2,0)
    else:
        return (0,0)

def angl(x,y):
    if x >= 0:
        if y <= 0 :
            return atan(y/x)+2*pi
        else:
            return atan(y/x)
    else :
        return atan(y/x)+pi
    
def prop_angl(x,y):
    return int(10*angl(x,y)/(pi))

value_order = [6,13,4,18,1,20,5,12,9,14,11,8,16,7,19,3,17,2,15,10]

def angle_value(x,y):
    a = prop_angl(x,y)
    for i in range(20):
        if a <= i :
            return value_order[i]

def value(x,y):
    val = angle_value(x,y)
    multi = multiplier(x,y)
    return val*multi[0]+multi[1]
    
def random_unif():
    return 2*random.random()-1, 2*random.random()-1

def test_1():
    for _ in range(50):
        (x, y) = random_unif()
        print("La flechette est tombée au coordonnées ({},{}) ce qui donne le score de {}".format(x,y, value(x,y)))

def test_2(n=100000):
    av_score = 0
    for _ in range(n):
        (x,y) = random_unif()
        av_score += value(x,y)/n
    print(av_score)

import numpy as np
plt.style.use('_mpl-gallery')

# make data:
np.random.seed(3)
x = 0.5 + np.arange(8)
y = np.random.uniform(2, 7, len(x))

# plot
fig, ax = plt.subplots()


def test_3():
    x=[]
    y=[]
    for i in range(100):
        x.append(random.normalvariate(7, 1))
        y.append(i)
        plt.plot(x)
        ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

test_3()
