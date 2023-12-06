import pygame, sys
from pygame.locals import *
import random, time, math
import json
import requests

#-----------------------------------------------------------------------------
def chg_base(x,y):
    x=63.25*x+367
    y=-91.5*y+4712
    return x, y

def random_code_postal():
    code_postal=''
    for i in range(5):
        code_postal+=str(random.randint(0,9))
    return code_postal


def random_correct_city():
    code_postal=random_code_postal()
    reponse = requests.get('https://geo.api.gouv.fr/communes?code=' + str(code_postal) + '&fields=nom,centre').json()
    while reponse == []:
        code_postal=random_code_postal()
        reponse = requests.get('https://geo.api.gouv.fr/communes?code=' + str(code_postal) + '&fields=nom,centre').json()
    #print(reponse)
    return reponse
    

def ville_random():
    dictionnaire = random_correct_city()
    for city in dictionnaire:
        ville = city.get('nom')
        coords = city.get('centre').get('coordinates')
    print(ville)
    return chg_base(coords[0], coords[1])





print(ville_random())