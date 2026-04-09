import math
import random
import modulo
import QCM
import QCManglais

op = input("choose your operation. if you don't know the sign, type list. ")
if op == "+":
    terme = input("choose first number : ")
    try:
        terme1 = int(terme)
    except ValueError:
        print("not a number")
        quit(1)
    terme = input("choose second number : ")
    try:
        terme2 = int(terme)
    except ValueError:
        print("not a number")
        quit(1)
    result = terme1 + terme2
    print("result : ", result)
elif op == "-":
    terme = input("choose first number : ")
    try:
        terme1 = int(terme)
    except ValueError:
        print("not a number")
        quit(1)
    terme = input("choose second number : ")
    try:
        terme2 = int(terme)
    except ValueError:
        print("not a number")
        quit(1)
    result = terme1 - terme2
    print("result : ", result)
elif op == "*":
    terme = input("choose first number : ")
    try:
        terme1 = int(terme)
    except ValueError:
        print("not a number")
        quit(1)
    terme = input("choose second number : ")
    try:
        terme2 = int(terme)
    except ValueError:
        print("not a number")
        quit(1)
    result = terme1 * terme2
    print("result : ", result)
elif op == "/":
    terme = input("choose first number : ")
    try:
        terme1 = int(terme)
    except ValueError:
        print("not a number")
        quit(1)
    terme = input("choose second number : ")
    try:
        terme2 = int(terme)
    except ValueError:
        print("not a number")
        quit(1)
    result = terme1 / terme2
    print("result : ", result)
elif op == "mod":
    terme = input("choose first number : ")
    try:
        terme1 = int(terme)
    except ValueError:
        print("not a number")
        quit(1)
    terme = input("choose second number : ")
    try:
        terme2 = int(terme)
    except ValueError:
        print("not a number")
        quit(1)
    result = modulo.mod(terme1, terme2)
    print("result : ", result)
elif op == "^":
    terme = input("choose first number : ")
    try:
        terme1 = int(terme)
    except ValueError:
        print("not a number")
        quit(1)
    terme = input("choose second number : ")
    try:
        terme2 = int(terme)
    except ValueError:
        print("not a number")
        quit(1)
    result = terme1 ^ terme2
    print("result : ", result)
elif op == "sqr":
    terme = input("choose number : ")
    try:
        terme1 = int(terme)
    except ValueError:
        print("not a number")
        quit(1)
    result = math.sqrt(terme1)
    print("result : ", result)
elif op == "cbr":
    terme = input("choose number : ")
    try:
        terme1 = int(terme)
    except ValueError:
        print("not a number")
        quit(1)
    result = math.cbrt(terme1)
    print("result : ", result)
elif op == "rand":
    result = random.randint(0, 100000)/100000
    print("result : ", result)
elif op == "randb":
    terme = input("choose first number : ")
    try:
        terme1 = int(terme)
    except ValueError:
        print("not a number")
        quit(1)
    terme = input("choose second number : ")
    try:
        terme2 = int(terme)
    except ValueError:
        print("not a number")
        quit(1)
    result = terme1 ^ terme2
    print("result : ", result)
