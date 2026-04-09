def sort(a):
    d = 0
    while(True):
        b = a.__getitem__(d)
        c = a.__getitem__(d+1)
        if b>c:
            a.__setitem__(d,c)
            a.__setitem__(d+1,b)
        d = d + 1
        e = a
        e.sort()
        if d == 4 and not a == e:
            d = 0
        elif a == e:
            return(a)