import matplotlib.pyplot as plt
import numpy as np

import pickle



# (pour le jeu du pendu c'est plus bas)
# --------------- JEU AVEC FLORIAN -------------------
 
def main():
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
                    
# ------------------- Programme proportion de voyelle max -------------------                   
                    
def le_mot_avec_le_de_voyelles(n = 20):
    with open("liste_francais.txt", "r") as liste :
        liste = liste.readlines()
        voyelle = ['a', 'e', 'i', 'o', 'u', 'y', 'à', 'â', 'ä', 'é', 'è', 'ê', 'ë', 'î', 'ï', 'ô', 'ö', 'ù', 'û', 'ü', 'ÿ']
        mot_opti = ' '
        prop = 0
        for mot in liste :
            ajout = 0
            for lettre in mot :
                if lettre == '-' :
                    ajout +=1
            if len(mot) == n+1+ajout:
                nb_v = 0.0
                nb_l = -1.0
                for lettre in mot :  
                    if lettre == "-" :
                        nb_l -= 1
                    for voy in voyelle :
                        if lettre == voy :
                            nb_v += 1
                            break
                    nb_l += 1
                if nb_v > 0 :
                    if prop <= nb_v/nb_l :
                        prop = nb_v/nb_l
                        #print(mot)
                        mot_opti = mot
                
        print(mot_opti)
        print(str(int(prop*n)) + '/' + str(n))
        






##############################################################################
###########################      JEU DU PENDU     ############################
##############################################################################



#-------------------- fonction qui enlève les accents ----------------------
        
def nom_simple(nom) :
    nouveau_nom = ""
    dictionnaire_symboles = {"à" : "a", "À" : "a", 
                             "â" : "a", "Â" : "a", 
                             "ä" : "a", "Ä" : "a", 
                             "é" : "e", "É" : "e",
                             "è" : "e", "È" : "e",
                             "ê" : "e", "Ê" : "e",
                             "ë" : "e", "Ë" : "e",
                             "î" : "i", "Î" : "i",
                             "ï" : "i", "Ï" : "i",
                             "ô" : "o", "Ô" : "o",
                             "ö" : "o", "Ö" : "o",
                             "ù" : "u", "Ù" : "u",
                             "û" : "u", "Û" : "u",
                             "ü" : "u", "Ü" : "u",
                             "ÿ" : "y", "Ÿ" : "y", 
                             "ç" : "c", "Ç" : "c"
                             }
                         
    for lettre in nom :
        if lettre in dictionnaire_symboles :
            nouveau_nom += dictionnaire_symboles.get(lettre)
        else :
            nouveau_nom += lettre
    return nouveau_nom

        
# ------ fonction qui enregistre la liste des mots (pour ajout de mots) ------
                
def sauvegarde_liste_de_mots(casse = False, accentuation = False):
    with open("liste_francais.txt", "r", encoding = "utf-8") as liste :
        liste = liste.readlines()
        for mot in range(len(liste)) :
            liste[mot] = liste[mot][:-1]
            if not accentuation :
                liste[mot] = nom_simple(liste[mot])
            if not casse :
                liste[mot] = liste[mot].upper()
            
                
    nom_du_fichier = "liste_francais" + '.data'
    with open(nom_du_fichier, 'wb') as donnees :
        sauvegarde = pickle.Pickler(donnees)
        sauvegarde.dump(liste)
    #print(liste)
    
# ------------------- fonction qui charge le fichier .data -------------------

def charger(nom_fichier):
     nom_du_fichier = nom_fichier + '.data'
     
     with open(nom_du_fichier, 'rb') as donnes :
         chargement = pickle.Unpickler(donnes)
         liste = chargement.load()
         return liste    
     
# ---------------- fonction qui donne la lettre la plus probable --------------
     
def meilleure_lettre(liste, lettres_fausses = []):
    alphabet = ['-', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    dictionnaire = {}
    for lettre in alphabet :
        dictionnaire[lettre] = 0
    for mot in liste :
        for lettre in alphabet :
            if lettre in mot :
                dictionnaire[lettre]+=1
    lettre_max = " "
    iterations_max = 0
    for i in dictionnaire.items():
        if i[0] not in lettres_fausses :
            if i[1] > iterations_max :
                lettre_max = i[0]
                iterations_max = i[1]
    return lettre_max

# --------------------- Ajout d'un mot au dictionnaire -----------------------

def ajout(mot):
    with open("liste_francais.txt", "a", encoding = "utf-8") as liste :
        liste.write(mot + "\n")
    sauvegarde_liste_de_mots()
    print("\n\n      Le mot " + mot + " a bien été ajouté au dictionnaire !")
    


def fn_nouveau_mot():
    nouveau_mot = input("Quel est ce nouveau mot ? (merci de vous assurer que ce mot est bien correct) ").lower()
    validation = input("Vous êtes certain de vouloir ajouter le mot " + nouveau_mot + " ? ").upper()
    while validation.lstrip() != "OUI" and validation.lstrip() != "NON" :
        print("Entrez OUI ou NON")
        validation = input("Vous êtes certain de vouloir ajouter le mot " + nouveau_mot + " ? ").upper()
    if validation.lstrip() == "OUI" :
        ajout(nouveau_mot)
    else :
        reecrire = input("Voulez-vous réécrire votre mot ? ").upper()
        while reecrire.lstrip() != "OUI" and reecrire.lstrip() != "NON" :
            print("Entrez OUI ou NON")
            reecrire = input("Voulez-vous réécrire votre mot ? ").upper()
        if reecrire == "OUI" :
            fn_nouveau_mot()
        else :
            print("Ce mot ne sera donc pas ajouté ! ")

def erreur(n):
    if n == 0 :
        ajout = input("Ce mot n'est pas dans le dictionnaire. Voulez-vous le rajouter ? ").upper()
    if n == 1 :
        ajout = input("Ce mot n'est pas dans le dictionnaire alors. Voulez-vous le rajouter ? ").upper()
    while ajout.lstrip() != "OUI" and ajout.lstrip() != "NON" :
        print("Entrez OUI ou NON")
        ajout = input("Ce mot n'est pas dans le dictionnaire. Voulez-vous le rajouter ? ").upper()
    if ajout.lstrip() == "OUI" :
        fn_nouveau_mot()
    else :
        print("Aucun mot n'a été ajouté au dictionnaire")
        
# ------------------------ Bonhomme pendu ascii art -------------------------    
    
def dessin(score):
    if score == 1:
        print("                    _________")
    if score == 2:
        print("                             ")
        print("                     |       ")
        print("                     |       ")
        print("                     |       ")
        print("                     |       ")
        print("                     |       ")
        print("                    _|_______")
    if score == 3:
        print("                    _________")
        print("                     |       ")
        print("                     |       ")
        print("                     |       ")
        print("                     |       ")
        print("                     |       ")
        print("                    _|_______")
    if score == 4:
        print("                    _________")
        print("                     |/      ")
        print("                     |       ")
        print("                     |       ")
        print("                     |       ")
        print("                     |       ")
        print("                    _|_______")
    if score == 5:
        print("                    _________")
        print("                     |/   |  ")
        print("                     |       ")
        print("                     |       ")
        print("                     |       ")
        print("                     |       ")
        print("                    _|_______")
    if score == 6:
        print("                    _________")
        print("                     |/   |  ")
        print("                     |    O  ")
        print("                     |       ")
        print("                     |       ")
        print("                     |       ")
        print("                    _|_______")
    if score == 7:
        print("                    _________")
        print("                     |/   |  ")
        print("                     |    O  ")
        print("                     |    |  ")
        print("                     |    |  ")
        print("                     |       ")
        print("                    _|_______")
    if score == 8:
        print("                    _________")
        print("                     |/   |  ")
        print("                     |    O  ")
        print("                     |    |/ ")
        print("                     |    |  ")
        print("                     |       ")
        print("                    _|_______")
    if score == 9:
        print("                    _________")
        print("                     |/   |  ")
        print("                     |    O  ")
        print("                     |   \|/ ")
        print("                     |    |  ")
        print("                     |       ")
        print("                    _|_______")
    if score == 10:
        print("                    _________")
        print("                     |/   |  ")
        print("                     |    O  ")
        print("                     |   \|/ ")
        print("                     |    |  ")
        print("                     |   /   ")
        print("                    _|_______")
    if score == 11:
        print("                    _________")
        print("                     |/   |  ")
        print("                     |    O  ")
        print("                     |   \|/ ")
        print("                     |    |  ")
        print("                     |   / \ ")
        print("                    _|_______")
    if score == 12 :        
        print("     _____   ____    __    _    _____     _   _     _      ")
        print("    |#####\ |####|  |##\  |#|  |#####\   |#| |#|   |#|     ")
        print("    |#|_|#| |#|_    |###\ |#|  |#|  \#\  |#| |#|   |#|     ")
        print("    |# ##/  |# #|   |#|\#\|#|  |#|  |#|  |#| |#|   |#|     ")
        print("    |#|     |#|__   |#| \###|  |#|__/#/  |#\_/#|    _      ")
        print("    |#|     |####|  |#|  \##|  |#####/   \#####/   |#|     ")
        print("                                                           ")
    
# -------------------------- fonction principale ----------------------------
        
def solveur_pendu():
    score = 0
    liste = charger("liste_francais")
    fin = False
    lettres_incorrectes = []
    entree = input("Donnez ce que vous voulez (de la forme E____ par exemple) : ")
    while not fin :        
        longueur_du_mot = len(entree)
        possibles = []
        contraintes = []
        for mot in liste :
            if len(mot) == longueur_du_mot :
                possibles.append(mot)
        #print(possibles)
        for lettre in range(len(entree)) :
            if entree[lettre] != '_' :
                contraintes.append((lettre, entree[lettre].upper()))
        #print(contraintes)
        mot = 0
        while mot < len(possibles) :
            for contrainte in contraintes :
                if possibles[mot][contrainte[0]] != contrainte[1]:
                    del possibles[mot]
                    mot -=1
                    break
            mot +=1
        #print(possibles)
        if len(possibles) == 0:
            erreur(0)
            break
        mots_pareils = 0                        
        for i in range(len(possibles)):
            if possibles[i] == possibles[0]:
                mots_pareils +=1
            else :
                break
        if mots_pareils == len(possibles):
            i = 0
            possibles = [possibles[0]]

           
        if len(possibles) == 1:
            verif = input("C'est forcément " + possibles[0] + " n'est-ce pas ? ").upper()
            while verif.lstrip() != "OUI" and verif.lstrip() !=  "NON":
                print("Entrez OUI ou NON ")
                verif = input("C'est forcément " + possibles[0] + " n'est-ce pas ? ").upper()
            if verif == "OUI" :
                print("\n\n      Trop Facile ! \n\n")
                break
            else :
                erreur(1)
                break
        for i in contraintes :
            lettres_incorrectes.append(i[1])
            #print(lettres_prises)
        lettre_choisie = meilleure_lettre(possibles, lettres_fausses = lettres_incorrectes)
        reponse = input("Y a-t-il la lettre "+ lettre_choisie + " ? (oui ou non) ").upper()
        while reponse != "OUI" and reponse != "NON" :
            print("veuillez saisir oui ou non")
            reponse = input("Y a-t-il la lettre "+ lettre_choisie + " ? (oui ou non) ").upper()
        if reponse == "OUI" :
            entree = input("Où se situe-t-elle ? (entrez à nouveaux les lettres trouvées) ")
        else :
            lettres_incorrectes.append(lettre_choisie)
            score += 1
        dessin(score)
        if score == 12 :
            fin = True

alphabet = ['-', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
def lettre_suivante(lettre):
    alphabet = ['-', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    dictionnaire = {}
    for caract in alphabet :
        dictionnaire[caract] = 0
    lettre = lettre.upper()
    liste = charger("liste_francais")
    #print(liste)
    for mot in liste :
        for caractere in range(len(mot)-1) :
            if mot[caractere] == lettre :
                dictionnaire[mot[caractere+1]]+=1
    print(dictionnaire['S'])
    '''
    lettre_max = " "
    iterations_max = 0
    for i in dictionnaire.items():
        if i[1] > iterations_max :
            lettre_max = i[0]
            iterations_max = i[1]
    ''' 
    return dictionnaire
                
#initiale = 'R'

#dictionnaire = lettre_suivante(initiale)



def plus_long_mot():
    liste = charger("liste_francais")
    nb_lettres = 0
    plus_long_mot = " "
    for mot in liste :
        nb_lettre = 0
        lettres_presentes = []
        for lettre in mot :
            for i in alphabet :
                if lettre == i and lettre not in lettres_presentes :
                    lettres_presentes.append(lettre)
                    nb_lettre += 1
        if len(lettres_presentes) >= nb_lettres :
            plus_long_mot = mot
            nb_lettres = nb_lettre
    print(plus_long_mot)
    print(nb_lettres)
            









