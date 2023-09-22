# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 16:13:39 2023

@author: RM275199
"""

with open('1million_pi.txt', 'r') as f:
    doc = f.read()
    
        
def trouver_chaine_repeter(texte, n):
    # Créer un dictionnaire pour stocker les indices de début de chaque occurrence de la chaîne
    occurrences = {}
    
    # Parcourir le texte
    for i in range(len(texte) - n + 1):
        sous_chaine = texte[i:i + n]
        
        # Vérifier si la sous-chaîne existe déjà dans le dictionnaire des occurrences
        if sous_chaine in occurrences:
            # Si oui, vérifier si la distance entre les occurrences est supérieure ou égale à n
            if i - occurrences[sous_chaine] >= n:
                return sous_chaine  # Retourner la première sous-chaîne qui se répète
        else:
            # Si la sous-chaîne n'existe pas encore dans le dictionnaire, l'ajouter avec son index
            occurrences[sous_chaine] = i
    
    return None  # Si aucune sous-chaîne n'est trouvée qui se répète

for i in range(100) :
    print(trouver_chaine_repeter(doc, i))

