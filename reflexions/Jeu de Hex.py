# -*- coding: utf-8 -*-

"""
Jeu de Hex

@author: pc
"""
import numpy as np
from random import randint
import time
import pygame
import math

#Variables Pygame
WHITE = (255, 255, 255)
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

screen_width = math.sqrt(3)*16*50+100
screen_height = 950
   

# fonctions pour le jeu en terminal 
def afficher_plateau(plateau):
    print('')
    for lignes in range(plateau.shape[0]-1):
        print('  '*lignes, end='')
        for colonnes in range(plateau.shape[1]-1):
            if colonnes == 0:
                if lignes == 10 or lignes == 11:
                    print(lignes, end=' ')
                else:
                    print(lignes, end='  ')
            elif lignes == 0:
                if colonnes == 10 or colonnes == 11:
                    print(colonnes, end=' ')
                else:
                    print(colonnes, end='  ')
            else:
                print(int(plateau[lignes][colonnes]), end='  ')
        print('\n')

        
def coup(joueur, plateau):
    coup = input("Joueur " + str(joueur) + ", donner la case (de la forme ligne x colonne) : ")
    x=int(coup.split('x')[1])
    y=int(coup.split('x')[0])
            
    while plateau[x][y] != 0:
        print("case déjà prise !")
        coup = input("Joueur " + str(joueur) + ", donner la case (de la forme ligne x colonne) : ")
        x=int(coup.split('x')[1])
        y=int(coup.split('x')[0])
    plateau[x][y]=joueur
    return plateau, x, y

def coup_auto(joueur, plateau):

    x = randint(1,11)
    y = randint(1,11)
    compteur=0
    while plateau[x][y] != 0:
        #print("case déjà prise !")
        compteur+=1
        x = randint(1,11)
        y = randint(1,11)
    plateau[x][y]=joueur
    return plateau

# Fonctions de test de victoire
         
def test_cases_autour(plateau, case_actuelle, joueur, cases_parentes):
    ligne = case_actuelle[0]
    colonne = case_actuelle[1]
    plateau[ligne][colonne] = - abs(plateau[ligne][colonne])
    cases_parentes.append(case_actuelle)
    if joueur == 1:
        if ligne == plateau.shape[0]-2:
            return True
    else:
        if colonne == plateau.shape[1]-2:
            return True
    if  plateau[ligne-1][colonne] == joueur :
        return test_cases_autour(plateau, (ligne-1, colonne), joueur, cases_parentes)
    elif plateau[ligne-1][colonne+1] == joueur :
        return test_cases_autour(plateau, (ligne-1, colonne+1), joueur,cases_parentes)
    elif plateau[ligne][colonne-1] == joueur :
        return test_cases_autour(plateau, (ligne, colonne-1), joueur, cases_parentes)
    elif plateau[ligne][colonne+1] == joueur :
        return test_cases_autour(plateau, (ligne, colonne+1), joueur, cases_parentes)
    elif plateau[ligne+1][colonne-1] == joueur :
        return test_cases_autour(plateau, (ligne+1, colonne-1), joueur, cases_parentes)
    elif plateau[ligne+1][colonne] == joueur :
        return test_cases_autour(plateau, (ligne+1, colonne), joueur, cases_parentes)
    else :
        cases_parentes.pop()
        if cases_parentes == []:
            return False
        else :
            return test_cases_autour(plateau, cases_parentes.pop(), joueur, cases_parentes)
        

def test_victoire(plateau_actuel, joueur):
    plateau=plateau_actuel.copy()
    test_case = False
    if joueur == 1:
        for colonne in range(plateau.shape[1]-1):
            #print(plateau[1][colonne+1])
            if plateau[1][colonne+1]==joueur:
                 test_case = test_cases_autour(plateau, (1, colonne+1), joueur, [])
            if test_case:
                return True, joueur
        return False, joueur
    else :
        for ligne in range(plateau.shape[0]-1):
            #print(plateau[ligne+1][1])
            if plateau[ligne+1][1]==joueur:
                 test_case = test_cases_autour(plateau, (ligne+1, 1), joueur, [])
            if test_case:
                return True, joueur
        return False, joueur
    
#Fonctions d'affichage pygame

def grille_pygame(screen):
    bord1 = [(50+50*math.sqrt(3)*(21/4),75*(12)-12.5),(50+50*math.sqrt(3)*(10/2),100+75*(11)),(50-25*math.sqrt(3),100),(50-25*math.sqrt(3),50)]
    bord2 = []
    bord3 = [(50+43*math.sqrt(3)*50/4,25+150/4),(50+11*math.sqrt(3)*50,25),(50,25),(50-25*math.sqrt(3),50)]
    bord4 = []
    for j in range(11):
        bord1.append((50+50*math.sqrt(3)*(j/2),75+75*j))
        bord1.append((50+50*math.sqrt(3)*(j/2),50+75*(j+1)))
        bord3.append((50+50*math.sqrt(3)*(j),75))
        bord3.append((50+50*math.sqrt(3)*(j)+25*math.sqrt(3),50))
        for i in range(12):
            pygame.draw.line(screen, BLACK, (50+50*math.sqrt(3)*(i+j/2),75+75*j),(50+50*math.sqrt(3)*(i+j/2),50+75*(j+1)))
            pygame.draw.line(screen, BLACK, (50+50*math.sqrt(3)*(j+i/2),75+75*i),(50+50*math.sqrt(3)*(j+i/2)+25*math.sqrt(3),50+75*(i)))
    for j in range(12):
        for i in range(12):
            pygame.draw.line(screen, BLACK, (50+50*math.sqrt(3)*(j+i/2),75+75*i),(50+50*math.sqrt(3)*(j+i/2)-25*math.sqrt(3),50+75*(i)))
    for sommets in bord1:
        bord2.append((screen_width-sommets[0], screen_height-sommets[1]))
    for sommets in bord3:
        bord4.append((screen_width-sommets[0], screen_height-sommets[1]))
    pygame.draw.polygon(screen, RED, bord1)
    pygame.draw.polygon(screen, RED, bord2)
    pygame.draw.polygon(screen, BLUE, bord3)
    pygame.draw.polygon(screen, BLUE, bord4)
    

def coord_to_hex(x,y):
    return 50+50*math.sqrt(3)*(x+y/2),75+75*y

def hexagone(screen, point, joueur):
    x = point[0]
    y = point[1]
    x, y = coord_to_hex(x,y)
    if joueur == 1:
        color = BLUE
    elif joueur == 2:
        color = RED
    else:
        color = WHITE
    pygame.draw.polygon(screen, color, [(x,y),(x,y+50),(x+math.sqrt(3)*25,y+75),(x+math.sqrt(3)*50,y+50),(x+math.sqrt(3)*50,y),(x+math.sqrt(3)*25,y-25)])
    
    
def clear_grille(screen, plateau):
    for i in range(11):
        for j in range(11):
            hexagone(screen, (i,j), 0)
                
def cursor_to_table(x, y):
    y = (y-62.5)//75
    x = (x-50-(y)*math.sqrt(3)*25)//(math.sqrt(3)*50)
    return x, y
    
    
def main():
    fin = False
    plateau = np.zeros((13,13))
    afficher_plateau(plateau)
    gagnant = None
    joueur = 1
    pygame.init()

    screen = pygame.display.set_mode((screen_width,screen_height))
    screen.fill(BLACK)
    clear_grille(screen, plateau)
    grille_pygame(screen)
    launched = True
    pygame.display.flip()
    while launched:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE :
                    launched = False         
                    print("Partie interrompue !")
            if event.type == pygame.QUIT :
                launched = False        
                print(" Partie interrompue !")
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
                print(x,y)
                x, y = cursor_to_table(x,y)
                x, y = int(x)+1, int(y)+1
                print(x,y)
                if x > 0 and x < 12 and y > 0 and y < 12 and plateau[y][x] == 0:
                    plateau[y][x]=joueur       
                    afficher_plateau(plateau)
                    hexagone(screen, (x-1,y-1), joueur)
                    pygame.display.flip()
                    fin, gagnant = test_victoire(plateau, joueur)
                    joueur = 3-joueur
                if fin :
                    launched = False
                    time.sleep(0.5)
                    print("La partie est terminée ! Le vainqueur est le joueur " + str(gagnant))
    pygame.quit()
    


main()

