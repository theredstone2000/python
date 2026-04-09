"""recreates the class range as a function"""

def range(start:int = 0, stop:int = 10, step:int = 1):
    idx = start
    list_final = []
    while not idx >= stop:
        list_final.append(idx)
        idx += step
    return(list_final)



