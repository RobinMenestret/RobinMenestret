#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 16:17:14 2022

@author: pc
"""

import math
import time

def is_prime(n):
  for i in range(2,int(math.sqrt(n))+1):
    if (n%i) == 0:
      return False
  return True


base = 10

def primes(a=1):
    a+=1
    if a == 1 :
        print("c'est tout")
    elif is_prime(a):
        print(a)
        return primes(base*a)
    elif a % base != 0 :
        return primes(a)
    elif a%base == 0 :
        return primes((a-1)//base)
        print(a)
    
primes()