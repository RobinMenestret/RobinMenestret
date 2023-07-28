# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 16:15:03 2023

@author: RM275199
"""
# Program to check if a number is prime or not

num = 28785866289100396890228041

# To take input from the user
#num = int(input("Enter a number: "))

# define a flag variable
flag = False

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

    # check if flag is True
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")


def importlist():
    f = open("1.txt", "r").read().split('\n')
    del(f[-1])

    for i in range(len(f)):
        f[i] = int(f[i])
    return f
    
prime_list = importlist()

primeth = []

def suite(place = 1, liste1 = prime_list, liste2 = primeth):
    liste2.append(place)
    print(place)
    try:
        return suite(liste1[place-1], liste1)
    except : 
        print("c'est fini")
        
    