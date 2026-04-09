"""recreates the filter class as a function"""

def filter(func, arg_list, result:any = True):
    """returns a list with all the arguments of list that return result if func is called with them. if a tuple is in the list, the function will be called with all of the tuple's argument, but only up to four. if you want to input a tuple as just one argument, put two () around it instead of one."""
    b = len(arg_list)
    idx = 0
    list_final = []
    while not arg_list == []:
        g = arg_list.pop(0)
        if g.__class__ == tuple:
            a = func(g.__getitem__(0),g.__getitem__(1),g.__getitem__(2),g.__getitem__(3))
        else: a = func(g)
        if a == result: list_final.append(g)
    return(list_final)


        
