#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jeu de Hex

@author: pc
"""
import numpy as np


"""
class joueur(numeros):
    def __init__(self):
        self.numeros =numeros
"""
        
def afficher_plateau(plateau):
    print('')
    for lignes in range(plateau.shape[0]):
        print('  '*lignes, end='')
        for colonnes in range(plateau.shape[1]):
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
    coup = input("donner la case (de la forme ligne x colonne) : ")
    x = int(coup[1])
    y = int(coup[0])
    while plateau[x][y] != 0:
        print("case déjà prise !")
        coup = input("donner la case (de la forme ligne x colonne) : ")
        x = int(coup[1])
        y = int(coup[0])
    plateau[x][y]=joueur
    return plateau

def test_victoire(plateau, joueur):
    for lignes in range(plateau.shape[0]):
        if plateau[lignes][1]==1:
            pass


def main():
    fin = False
    plateau = np.zeros((12,12))
    afficher_plateau(plateau)
    while not fin :
        plateau = coup(1, plateau)
        afficher_plateau(plateau)
        plateau = coup(2, plateau)
        afficher_plateau(plateau)

main()

