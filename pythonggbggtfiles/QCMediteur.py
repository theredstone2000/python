import QCM
a = input("écrit la question 1: ")
b = input("écrit 1 : puis la première réponse possible ")
c = input("écrit 2 : puis la deuxième réponse possible ")
d = input("écrit 3 : puis la troisième réponse possible ")
e = input("écrit le numéro de la bonne réponse")
e = int(e)
yn = input("commencer le qcm(y) ou y ajouter une autre question(n) ? ")
if yn == "y":
    i = 0
    i = i + QCM.QCM(a, b, c, d, e)
    print(i, end="/1 bonnes réponses ")
    print("merci d'avoir participer ")
elif yn == "n":
    f = input("écrit la question 2")
    g = input("écrit 1 : puis la première réponse possible ")
    h = input("écrit 2 : puis la deuxième réponse possible ")
    j = input("écrit 3 : puis la troisième réponse possible ")
    k = input("écrit le numéro de la bonne réponse ")
    k = int(k)
    yn = 0
    yn = input("commencer le qcm(y) ou y ajouter une autre question(n) ? ")
    if yn == "y":
        i = 0
        i = i + QCM.QCM(a, b, c, d, e)
        i = i + QCM.QCM(f, g, h, j, k)
        print(i, end="/2 bonnes réponses ")
        print("merci d'avoir participer ") 
    elif yn == "n":
        l = input("écrit la question 3 ")
        m = input("écrit 1 : puis la première réponse possible ")
        n = input("écrit 2 : puis la deuxième réponse possible ")
        o = input("écrit 3 : puis la troisième réponse possible ")
        p = input("écrit le numéro de la bonne réponse ")
        p = int(p)
        yn = 0
        yn = input("commencer le qcm(y) ou y ajouter une autre question(n) ? ")
        if yn == "y":
            i = 0
            i = i + QCM.QCM(a, b, c, d, e)
            i = i + QCM.QCM(f, g, h, j, k)
            i = i + QCM.QCM(l, m, n, o, p)
            print(i, end="/3 bonnes réponses ")
            print("merci d'avoir participer ")
        elif yn == "n":
            q = input("écrit la question 4 ")
            r = input("écrit 1 : puis la première réponse possible ")
            s = input("écrit 2 : puis la deuxième réponse possible ")
            t = input("écrit 3 : puis la troisième réponse possible ")
            u = input("écrit le numéro de la bonne réponse ")
            u = int(u)
            yn = 0
            yn = input("commencer le qcm(y) ou y ajouter une autre question(n) ? ")
            if yn == "y":
                i = 0
                i = i + QCM.QCM(a, b, c, d, e)
                i = i + QCM.QCM(f, g, h, j, k)
                i = i + QCM.QCM(l, m, n, o, p)
                i = i + QCM.QCM(q, r, s, t, u)
                print(i, end="/4 bonnes réponses ")
                print("merci d'avoir participer ")
            elif yn == "n":
                v = input("écrit la question 5 ")
                w = input("écrit 1 : puis la première réponse possible ")
                x = input("écrit 2 : puis la deuxième réponse possible ")
                y = input("écrit 3 : puis la troisième réponse possible ")
                z = input("écrit le numéro de la bonne réponse ")
                z = int(z)
                yn = 0
                yn = input("dès que vous mettez quelque chose peut importe quoi le QCM va commencer ")
                i = 0
                i = i + QCM.QCM(a, b, c, d, e)
                i = i + QCM.QCM(f, g, h, j, k)
                i = i + QCM.QCM(l, m, n, o, p)
                i = i + QCM.QCM(q, r, s, t, u)
                i = i + QCM.QCM(v, w, x, y, z)
                print(i, end="/5 bonnes réponses ")
                print("merci d'avoir participer ")
            else:
                print("pas y ou n, le programme s'arrète ")
                quit(1)  
        else:
            print("pas y ou n, le programme s'arrète ")
            quit(1)
    else:
        print("pas y ou n, le programme s'arrète ")
        quit(1)
else:
    print("pas y ou n, le programme s'arrète ")
    quit(1)