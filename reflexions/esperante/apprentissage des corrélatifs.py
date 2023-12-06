#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 18:18:42 2023

@author: pc
"""
import random
dictionnaire = {
    '   iu' : "quelqu'un",
    '   io' : "quelque chose",
    '   ia' : "une sorte de",
    '   ie' : "quelque part",
    '   iam' : "un jour, une fois",
    '   iel' : "d'une certaine manière",
    '   ial' : "pour une certaine raison",
    '   iom' : "un peu",
    '   ies' : "de quelqu'un",
    '  kiu' : "qui/quel(le)",
    '  kio' : "quoi, que",
    '  kia' : "quel(le) (sorte de)",
    '  kie' : "où",
    '  kiam' : "quand",
    '  kiel' : "comment/comme",
    '  kial' : "pourquoi",
    '  kiom' : "combien",
    '  kies' : "de qui/dont",
    '  tiu' : "celui-là/ce",
    '  tio' : "cela",
    '  tia' : "tel(le), cette sorte de",
    '  tie' : "là",
    '  tiam' : "alors",
    '  tiel' : "ainsi, tellement",
    '  tial' : "pour cette raison",
    '  tiom' : "autant",
    '  ties' : "de celui-là",
    '  ciu' : "chacun/chaque",
    '  cio' : "tout",
    '  cia' : "chaque sorte de",
    '  cie' : "partout",
    '  ciam' : "toujours",
    '  ciel' : "de toute manière",
    '  cial' : "pour toutes raisons",
    '  ciom' : "le tout",
    '  cies' : "de tous",
    'neniu' : "personne/aucun",
    'nenio' : "rien",
    'nenia' : "nulle sorte de",
    'nenie' : "nulle part",
    'neniam' : "jamais",
    'neniel' : "en aucune façon",
    'nenial' : "pour aucune raison",
    'neniom' : "rien du tout",
    'nenies' : "de personne"
    }

explications = {
    "   i"  : "l'indéfini",
    "  ki" : "l'interrogatif et le relatif",
    "  ti" : "le démonstratif",
    "  ci" : "le collectif",
    "neni" : "le négatif",
    "u   " : "l'individualité",
    "o   " : "la chose",
    "a   " : "la qualité",
    "e   " : "le lieu",
    "am  " : "le temps",
    "el  " : "la manière",
    "al  " : "la cause",
    "om  " : "la quantité",
    "es  " : "la possession"
    
    }


def quiz(n=10):
    compteur = 0
    for i in range(n):
        mot = random.choice(tuple(dictionnaire.keys()))
        print(dictionnaire[mot].strip())
        reponse = input(" se dit : ")
        if reponse.strip()  == mot.strip() :
            print("\n\n OUI ! \n")
            compteur += 1
        for key in dictionnaire :
            if key.strip() == reponse.strip():
                reponse = key
        
        else :
            print("\n\n non c'etait " + mot + "\n")
            for key in explications:
                comptep = 0
                comptes = 0
                for lettre in range(4):
                    if mot[lettre] == key[lettre]:
                        comptep +=1
                for lettre in range(2):
                    if mot[4+lettre] == key[lettre]:
                        comptes +=1
                if comptep == 4 :
                    print("le préfixe "+ key + " caractérise " + explications[key] + "\n")
                if comptes == 2 :
                    print("le sufixe " + key + " caractérise " + explications[key] + "\n")
                        
            
    print("Vous avez une note de " + str(compteur) + "/" + str(n))
    
        
quiz()














































