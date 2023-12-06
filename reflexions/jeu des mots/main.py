#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 14:51:50 2022

@author: pc
"""
with open("liste_francais.txt", "r")  as liste :
    liste = liste.readlines()
    mots5 = []
    for mot in liste :
        if len(mot) == 6:
            mots5.append(mot.lower())
            '''
            for lettre in range(len(mot)):
                if mot[lettre] in ['à', 'â', 'ä'] :
                    mot[lettre] = 'a'
                if mot[lettre] in ['é', 'è', 'ê', 'ë'] :
                    mot[lettre] = 'e'
                if mot[lettre] in ['î', 'ï'] :
                    mot[lettre] = 'i'
                if mot[lettre] in ['ô', 'ö'] :
                    mot[lettre] = 'o'
                if mot[lettre] in ['ù', 'û', 'ü'] :
                    mot[lettre] = 'u'
                if mot[lettre] in ['ÿ'] :
                    mot[lettre] = 'y'
            '''

print(mots5[1])
            
guess = input("quel mot avez-vous ? ")
interdit1 = int(input("quelle est la premiere lettre interdite ? "))-1
interdit2 = int(input("quelle est la deuxième lettre interdite ? "))-1
lettre_interdite1 = guess[interdit1]
lettre_interdite2 = guess[interdit2]

for mot in mots5 :
    compteur = 0
    lettres_pareils = []
    for lettre in range(5):
        if guess[lettre] == mot[lettre]:
            compteur += 1
            lettres_pareils.append(lettre)
    if compteur == 2 :
        if mot[interdit1] != lettre_interdite1 and mot[interdit2] != lettre_interdite2 :
            if abs(lettres_pareils[0] - lettres_pareils[1]) == 1:
                mot = mot[:5]
                print('(' + mot + ')\n')
            else :
                print(mot)
                