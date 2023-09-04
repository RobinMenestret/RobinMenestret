import random
import ast
from pprint import pprint
import os
import numpy as np



table = {
                     0 : "Bulle",           # Par la forme
                     1 : "Bâton",           # Par la forme
                     2 : "Cygne",           # Par la forme
                     3 : "Couronne",        # Trois -> Roi -> Couronne
                     4 : "Carré",           # Les 4 cotés du carré
                     5 : "Etoile",          # Etoile à 5 branches
                     6 : "France",          # Hexagone -> France
                     7 : "Cèpe",            # Sonorité proche
                     8 : "Huitre",          # Sonorité proche
                     9 : "Oeuf",            # Sonorité proche
                    10 : "Zidane",          # Maillot de foot
                    11 : "Bronze",          # Sonorité proche
                    12 : "Bouse",           # Sonorité proche
                    13 : "Braise",          # Sonorité proche
                    14 : "Lion",            # Calvados -> Normandie -> Enblème
                    15 : "Ambulance",       # Numéro urgences
                    16 : "Bière",           # 1664 
                    17 : "Pistolet",        # Numéro police
                    18 : "Feu",             # Numéro pompier
                    19 : "Boeuf",           # Sonorité proche + B deuxième lettre
                    20 : "Vin",             # Sonorité proche
                    21 : "Jeton",           # Las Vegas 21
                    22 : "Rubik's cube",    # Nombre théorique minimum de coup pour le résoudre
                    23 : "Ballon",          # Nombre de personne sur un terrain de foot
                    24 : "Horloge",         # Nombre d'heure dans une journée
                    25 : "Fromage",         # Doubs
                    26 : "Corde",           # Nombre de dimensions en théorie des cordes
                    27 : "Guitare",         # Age de décès de grands musiciens et guitaristes
                    28 : "Lune",            # Nombre de jour dans un mois lunaire
                    29 : "Triskel",         # Finistère -> Bretagne -> emblème
                    30 : "Menthe",          # Sonorité proche
                    31 : "Train",           # Sonorité proche
                    32 : "Carte",           # Nombre de cartes dans un petit jeu
                    33 : "Canette",         # Nombre de cl dans une canette
                    34 : "Théatre",         # Sonorité proche
                    35 : "Pellicule",       # 35mm est un format de pellicule
                    36 : "Chandelle",       # Expression : 36 chandelles
                    37 : "Sang",            # Températur du sang humain
                    38 : "Truite",          # Sonorité proche
                    39 : "Telephone",       # Sonorité proche de T9 
                    40 : "Balle de tennis", # Nombre de points max dans un jeu de tennis
                    41 : "Piano",           # Nom de code de Bach
                    42 : "Spock",           # La réponse de la vie, star trek
                    43 : "Croix",           # Sonorité proche
                    44 : "Quatre quarts",   # Sonorité proche
                    45 : "Bombe",           # Bombe nucléaire de 1945
                    46 : "Cassis",           # Sonorité proche de kiss -> bisou
                    47 : "Cassette",        # Sonorité proche
                    48 : "Carotte cuite",   # Sonorité proche
                    49 : "Carafe",          # Sonorité proche
                    50 : "Manche",          # département
                    51 : "Pastis",          # Du pastis 51
                    52 : "Vélo",            # Jeu de carte Bicycle 
                    53 : "Sable",           # Sonorité proche de 50 rois -> Afrique -> desert
                    54 : "Sac",             # Sonorité proche
                    55 : "Echiquier",       # 5 - 5 le temps pur une partie en Blitz
                    56 : "Epée",            # Sonorité proche de Saint Cyr
                    57 : "fil",             # Nombre premier de Grotendieck -> Fields -> fil
                    58 : "Moustache",       # Charles de Gaulle élu
                    59 : "Frite",           # département du Nord
                    60 : "montre",          # Durée d'une heure en minutes
                    61 : "Flûte",           # Sonorité proche de Sylvain -> Durif -> flûte de pan
                    62 : "Nez",             # Département des caps nez
                    63 : "Soie",            # Sonorité proche
                    64 : "Riz",             # L'histoire de l'echiquier
                    65 : "Dentier",         # Age de la retraire
                    66 : "Trident",         # Chiffres du diable
                    67 : "Bretzel",         # Departement d'Alsace
                    68 : "Télé",            # Année de Naissance de mon père
                    69 : "Chapeau",         # Couvre chef
                    70 : "Raie",            # Haute-Sâone -> Ré sur Sâone
                    71 : "Vase",            # Ressemble à Soisson 
                    72 : "Ventouse",        # Sonorité proche
                    74 : "Livre",           # Année de naissance de ma mère
                    75 : "Pyramide",        # Paris -> Louvre
                    76 : "Container",       # Seine-maritime : Le Havre
                    77 : "Coquelicot",      # Symbole du département
                    78 : "Chateau",         # Versailles
                    79 : "Donut",           # Rime avec Duff -> Homer Simpson
                    80 : "Coeur",           # Napoléon
                    81 : "Raisin",          # Tarn
                    82 : "Olive",           # Ressemble à 80 dieux -> Grèce
                    
    }

def simplifier(word):
    for letter in range(len(word)) :
        if word[letter] in ['é','è','ê','ë']:
            word = word[:letter]+'e'+ word[letter+1:]
        if word[letter] in ['à','â','ä']:
            word = word[:letter]+'a'+ word[letter+1:]
        if word[letter] in ['ò','ô','ö']:
            word = word[:letter]+'o'+ word[letter+1:]
        if word[letter] in ['ù','û','ü']:
            word = word[:letter]+'u'+ word[letter+1:]
        if word[letter] in ['ç']:
            word = word[:letter]+'c'+ word[letter+1:]
        if word[letter] in ['î','ï']:
            word = word[:letter]+'i'+ word[letter+1:]
        if word[letter] in ['œ']:
            word = word[:letter]+'oe'+ word[letter+1:]
    return word


def saving_dic(dict_path, dic):
    with open(dict_path, "w") as f:
        f.write(str(dic))
        
        
def importing_dic(dict_path):     
    with open(dict_path, 'r') as f1:
        dic = ast.literal_eval(f1.read())
    return dic
           
        
def init_score(table_de_rappel, player_name, init_score = 5):
    path = "data/" + player_name + "_score.data"
    erase = True
    if os.path.exists(path):
        erase = input('WARNING : Ce fichier existe déjà. Voulez-vous continuer et écraser ce fichier ? (y/[n])')
        erase = True if erase.lower() == 'y' else False
    if erase :
        scores = dict()
        for i in range(len(table_de_rappel)+1):
            scores[i] = [init_score, init_score]
        with open(path, 'w') as f:
            f.write(str(scores))
    else :
        add = input('Voulez-vous mettre à jour la table de rappel ? (y/[n])')
        add = True if add.lower() == 'y' else False
        if add:
            with open(path, 'r') as f:
                scores = ast.literal_eval(f.read())
            for i in range(len(table_de_rappel)+1):
                if i not in scores : 
                    scores[i] = [init_score, init_score]
            with open(path, 'w') as f:
                f.write(str(scores))
        else :
            print("init_score interrompue !")

           
def upgrade_score(number:int, value:int, sens:int, player_name:str):
    path = "data/" + player_name + "_score.data"
    if not os.path.exists(path):
        print("Ce joueur n'existe pas !")
    else :
        with open(path, 'r') as f:
            scores = ast.literal_eval(f.read())
        if scores[number][sens] != 0 :
            scores[number][sens] += value
        with open(path, 'w') as f:
            f.write(str(scores))


def table_trainer(n, path, player_name, table_de_rappel):
    score = 0
    for i in range(n):
        with open(path, 'r') as f:
            ponderations = ast.literal_eval(f.read())
        poids = list()
        poids_tot = 0
        for key in ponderations:
            poids_act = ponderations[key][0]+ponderations[key][1]
            poids.append(poids_act)
            poids_tot += poids_act
        for poid in range(len(poids)):
            poids[poid] = poids[poid]/poids_tot

        nombre = np.random.choice(list(table_de_rappel.keys()),1, p = poids)[0]
        valeur = table_de_rappel[nombre]
        if ponderations[nombre][0] == ponderations[nombre][1]: 
            sens = random.randint(0,1)
        else:
            sens = 0 if ponderations[nombre][0]>ponderations[nombre][1] else 1
        if sens == 0 :
            user_value = input("Quel mot correspond au nombre {} ? ".format(nombre))
            user_value = simplifier(user_value.lower())
            valeur = simplifier(valeur.lower())
            if user_value == valeur :
                print("Correct !")
                score += 1
                
                upgrade_score(nombre, -1, sens, player_name)
            else :
                print("Faux ! La réponse correcte était {}".format(valeur))
                upgrade_score(nombre, 1, sens, player_name)
        else :
            user_number = input("Quel nombre correspond au mot {} ? ".format(valeur))
            try : 
                user_number = int(user_number)
            except :
                print("Ce n'est pas un nombre !")
            if user_number == nombre :
                print("Correct !")
                score += 1
                
                upgrade_score(nombre, -1, sens, player_name)
            else :
                print("Faux ! La réponse correcte était {}".format(nombre))
                
                upgrade_score(nombre, 1, sens, player_name)
                
    print("Vous avez un resultat de {}/{}".format(score, n))
    if score < n//2 :
        print("Essaie encore !")
    elif score == n :
        print("C'est Parfait !")
    else :
        print("Bravo !")
        
def new_player(table_de_rappel):
    new_name = input("Quel est votre nom ? ").lower()
    init_score(table_de_rappel, new_name)
    return new_name


player_name = 'robin'
        
def main(player_name):
    
    score_path = "data/" + player_name + "_score.data"
    dict_path = "data/" + player_name + "_dictionnary.data"
    
    table_de_rappel = importing_dic(dict_path)
    
    choix = input("\n\n Joueur actuel : {} \n\n\n          Que voulez-vous faire ? \n\n          1 - Entrainement\n          2 - Mise à jour de la Table\n          3 - Changer de Joueur\n          4 - Initialiser les scores\n          5 - Retour au menu principal\n\n\n          CHOIX : ".format(player_name[0].upper()+player_name[1:]))
    print("\n")
    try :
        choix = int(choix)
    except :
        print("Erreur ce n'est pas un nombre !")
        return
    
    if choix == 1 :
        table_trainer(100, score_path, player_name, table_de_rappel)
        main(player_name)
    
    elif choix == 2 :
        saving_dic(dict_path, table)
        print("Done !")
        main(player_name)
    
    elif choix == 3 :
        player_name = new_player(table)
        saving_dic(dict_path, table)
        main(player_name)
        
    elif choix == 4 :
        init_score(table_de_rappel, player_name)
        main(player_name)
    
    elif choix == 5 :
        main(player_name)
        
    else :
        print("Ce nombre n'est pas valide")
        main()
    
main(player_name)