#import modules
import math
import operator

#get number and operators, and convert them.
a = bin((int(input("premier nombre : "))))
b = bin((int(input("deuxième nombre : "))))
c = input("+, -, * or / : ")

#calculate using binary logic gates
if c == "+":
    z = 0
    d = operator.xor()
    