"""using a hardcoded expression, convert converts the letter into another one. unconvert reverses the prossess."""
#import modules
import math
import operator

def convert(a: str):
    """convert a letter into another one using a hardcoded expression"""
    #initialize list to convert letter to number
    b = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    #convert letter to number
    a = b.index(a)

    #find coded number
    a = 7 * a + 4
    a = a % 26

    #convert back to letter
    a = b.__getitem__(a)
    return(a)
def unconvert(a: str):
    """convert the letter into the one that would have been the original if put into convert"""
    d = 0
    while d < 11:
        a = convert(a)
        d = d + 1
    return(a)
