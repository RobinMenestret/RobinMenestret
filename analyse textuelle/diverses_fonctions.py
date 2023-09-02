# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 10:38:37 2023

@author: RM275199
"""

f = open("liste_francais.txt", "r", encoding='utf-8')

file = f.read()

dico = file.split("\n")

def how_many_in_the_word(letter, word):
    score = 0

    for let in word :
        if let.lower() == letter.lower() :
            score += 1
    return score

def the_word_with_the_most(letter):
    current_best_words = list(dico[0])
    current_best_score = how_many_in_the_word(letter, current_best_words[0])
    for word in dico :
        current_score = how_many_in_the_word(letter, word)
        if current_score > current_best_score :
            current_best_words = [word]
            current_best_score = current_score
        elif current_score == current_best_score :
            current_best_words.append(word)
    return current_best_words, current_best_score

def split_word_verify(word):
    letter = len(word)//2
    for cut in range(len(word)):
        part1 = word[:letter]
        if part1 in dico :
            part2 = word[letter:]
            if part2 in dico :
                print('le mot "{}" se sépare en "{}" et "{}".'.format(word, part1, part2))
                return word


def print_the_list(letter):
    words, score = the_word_with_the_most(letter)
    print('les mots avec le plus de {} sont {} avec {} "{}" dedans.'.format(letter, words, score, letter))

def print_short(letter):
    words, score = the_word_with_the_most(letter)
    print("{} : {}".format(letter, score))

letters = ['é', "a","b", 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def forall():
    for letter in letters :
        print_short(letter)        
        
        
def find_all_cutable_words():
    liste = []
    for word in dico:
        mot = split_word_verify(word)
        if mot != None:
            liste.append(mot)
    print(liste)
    return liste
        
    
def levenshtein_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
    
    return dp[m][n]


def furthest_words():
    word1 = dico[0]
    word2 = dico[0]
    max_dist = 0
    for w1 in dico:
        for w2 in dico :
            if max(len(w1), len(w2)) > max_dist :
                curr_dist = levenshtein_distance(w1,w2)
                if curr_dist >= max_dist :
                    word1 = w1
                    word2 = w2
                    max_dist = curr_dist
                    print(f"La distance de Levenshtein entre '{word1}' et '{word2}' est : {max_dist}")

    return word1, word2, max_dist

def search_short_words(letter):
    for word in dico:
        if len(word) <= 4 and letter in word:
            print(word)
            
search_short_words('se')
            