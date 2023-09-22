# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 15:48:24 2023

@author: RM275199
"""

with open("pi_1_million.txt", 'r') as f :
    doc = f.read()
    doc1 = ""
    i=865
    while i < len(doc):
        if doc[i] == ":":
            while doc[i] != '\n':
                i+=1
        elif doc[i] == " " or doc[i] == "\n":
            i+=1
        else :
            doc1 += doc[i]
            i+=1

with open('1million_pi.txt', 'w') as f:
    f.write(doc1)