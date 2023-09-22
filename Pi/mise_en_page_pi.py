# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 07:58:58 2023

@author: RM275199
"""

def mise_en_page(n, lap = True):
    if lap :
        sup = "lap"
        line = 10
    else :
        sup = "desk"
        line = 15
    with open("1million_pi.txt", 'r') as f :
        doc = f.read()
    with open(str(n) + "_for_" + sup + ".txt", 'w') as f:
        for i in range(n):
            if i % line == 0 :
                f.write("\n\n\n")
            f.write("\t")
            f.write(doc[i])

mise_en_page(500)