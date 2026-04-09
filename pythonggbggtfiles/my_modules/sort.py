"""implement bogo sort and bubble sort."""
import random as rng
def bubble(a: list[int]):
    """just sorts list a using bubble sort"""
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
        if d == a.__len__() and not a == e:
            d = 0
        elif a == e:
            return(a)

def bogo(a: list[int]):
    """sorts list a using bogo sort"""
    d = 0
    while(True):
        while(d<(a.__len__())):
            a.__setitem__(d,a.__getitem__(rng.randint(d+1,a.__len__()-1)))
            e = a
            e.sort()
            if a == e:
                return(a)
            if not d == a.__len__():
                d = 0
            else:
                d = d + 1
