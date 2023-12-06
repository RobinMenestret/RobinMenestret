import pygame, sys
from pygame.locals import *
import random, time, math
import json
import requests

#-----------------------------------------------------------------------------
scale_screen = 0.8
screen_w = 1000 * scale_screen
screen_h = 961 * scale_screen

def chg_base(x,y):
    x = (63.25 * x + 367) * screen_w / 1000
    y = (-91.5 * y + 4712)* screen_h / 961
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
    return chg_base(coords[0], coords[1]), ville

def afficher_ville(ville):
    response = requests.get('https://geo.api.gouv.fr/communes?nom=' + ville + '&fields=nom,centre')
    dictionnaire = response.json()
    for city in dictionnaire:
        if city.get('nom').lower() == ville:
            coords = city.get('centre').get('coordinates')
    print(dictionnaire)
    print(coords)
    return chg_base(coords[0], coords[1])
    
#-----------------------------------------------------------------------------

def modes(mode=1):
    k,Liste=0,[]
    mode_prefecture = mode
    if mode_prefecture :
        f = open('Prefectures.txt', 'r', encoding='utf-8')
    else :
        f = open('Villes.txt', 'r', encoding='utf-8')
    for word in f:
        if word[0]!='#':
            if k%3==0:
                l=[word[:-1]]
            else:
                l.append(int(word))
                if k%3==2:
                    Liste.append(l)
            k+=1
    return k,Liste

#MODES : 0 = play, 1 = edit, 2 = result, 3 = newgame, 4 = finalscore, 5 = display all cities, 6 = None, 7 = Display city on the input
def main(GAMES=20,MODE=3, VILLE = 'Vesdun'):
    k, Liste = modes(1)
    pygame.init()

    FPS = 60
    FramePerSec = pygame.time.Clock()

    BLUE  = (0, 0, 255)
    RED   = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    N=len(Liste)


    font_small = pygame.font.SysFont("arial", 30)

    if MODE == 1:
        background = pygame.image.load("fonddecarte.jpg")
    else:
        background = pygame.image.load("fonddecarte.jpg")
        
    SCREEN_WIDTH  = screen_w
    SCREEN_HEIGHT = screen_h

    DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    DISPLAYSURF.fill(WHITE)
    pygame.display.set_caption("Game")

    jack = pygame.image.load("Jack.png")
    text1 = font_small.render("T'es mauvais Jack !", True, BLACK)
    text2 = font_small.render("Tu sais pas jouer !", True, BLACK)
    #time.wait(5)
    #pygame.QUIT()
    SCORE = 0
    NGAMES=0
    
    while True:
        if MODE == 3:
            l=Liste[random.randint(0,N-1)]
            MODE=0
        for event in pygame.event.get(): 
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                (xd,yd)=pygame.mouse.get_pos()
                if MODE == 1:
                    print(xd,yd)
                elif MODE == 0:
                    MODE = 2
                    start=time.time()
                    SCORE-=int(-100*math.exp(-((xd-l[1])**2+(yd-l[2])**2)/400))
        if MODE!=6:
            background = pygame.transform.scale(background, (DISPLAYSURF.get_width(), DISPLAYSURF.get_height()))
            DISPLAYSURF.blit(background, (0,0))
        if MODE == 0 or MODE == 2:
            city=font_small.render(l[0], True, BLACK)
            DISPLAYSURF.blit(city, (4,0))
            score=font_small.render(str(SCORE), True, BLACK)
            DISPLAYSURF.blit(score, (700,0))
            game=font_small.render(str(NGAMES+1)+'/'+str(GAMES), True, BLACK)
            DISPLAYSURF.blit(game, (4,30))
        if MODE == 2:
            pygame.draw.circle(DISPLAYSURF, BLUE, (l[1],l[2]), 3)
            pygame.draw.line(DISPLAYSURF, RED, (xd-4,yd),(xd+4,yd))
            pygame.draw.line(DISPLAYSURF, RED, (xd,yd-4),(xd,yd+4))
            if time.time()-start>3:
                MODE=3
                NGAMES+=1
                if NGAMES == GAMES:
                    MODE=4
        elif MODE == 4:  
            DISPLAYSURF.fill(WHITE)
            score=font_small.render('Score : '+str(SCORE), True, BLACK)
            scm=int(100*SCORE/GAMES)/100
            score2=font_small.render('Score moyen par tour: '+str(scm), True, BLACK)
            DISPLAYSURF.blit(score, (200,300))
            DISPLAYSURF.blit(score2, (200,330))
            if scm<50:
                DISPLAYSURF.blit(jack, (200,400))
                DISPLAYSURF.blit(text1, (300,410))
                DISPLAYSURF.blit(text2, (300,450))
        elif MODE == 5:
            for l in Liste:
                pygame.draw.circle(DISPLAYSURF, BLACK, (l[1],l[2]), 3)
            MODE = 6
#-----------------------------------------------------------------------------
        elif MODE == 7:
            ville = input("Nom de la ville : ").lower()
            VILLE=ville
            x,y = afficher_ville(VILLE)
            city=font_small.render(VILLE, True, BLACK)
            DISPLAYSURF.blit(city, (4,0))
            pygame.draw.circle(DISPLAYSURF, BLUE, (x,y), 3)
            MODE = 6
        elif MODE == 8:
            [x,y] , ville = ville_random()
            city=font_small.render(ville, True, BLACK)
            DISPLAYSURF.blit(city, (4,0))
            pygame.draw.circle(DISPLAYSURF, BLUE, (x,y), 3)
            MODE = 6
            
#-----------------------------------------------------------------------------
        pygame.display.update()
        FramePerSec.tick(FPS)

main(MODE=7)

#idee : recuperer la liste de toutes les villes et villages de france avec leurs coordonnées geographiques pour faire un quiz
#idee : Donner deux villes de reference et une troisieme et dire si celle-ci est au dessu ou en dessous de la droite passant par les deux premieres