def QCM(a, b, c, d, e):
    print(a)
    print(b)
    print(c)
    print(d)
    fanswer = input("1, 2 or 3 ?")
    try:
        ranswer = int(fanswer)
    except ValueError:
        print("not a number, quit")
        quit(1)
    if ranswer == e:
        print("right answer !")
        return(1)
    else:
        print("wrong answer !")
        print(e, end=" is the right answer !")
        return(0)
