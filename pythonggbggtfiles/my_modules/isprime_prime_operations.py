import keyboard
import pygame
import math
import operator
import numpy
import random

def isint(number:int|float):
    """just returns True if number is convertible to int and false otherwise"""
    if math.floor(number) == number:
        return(True)
    else: return(False)

def isprime(number:int) -> bool:
    """returns True if number is prime and False otherwise"""
    sub = 1
    while not sub == number-1:
        a = number/(number-sub)
        if isint(a):
            return(False)
        sub = sub+1
    return(True)

def facteur_premier(number:int):
    """returns a list of the prime factors of number"""
    list = []
    b = 2
    while not isprime(number):
        a = True
        while a == True:
            if isint(number/b):
                number = number/b
                list.append(b)
            else: a = False
        b = b + 1
        while not isprime(b):
            b = b + 1
    list.append(number)
    return(list)
