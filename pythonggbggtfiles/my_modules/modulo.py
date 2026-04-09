"""do modulo operation"""
import math
def mod(a: int, b: int):
    """do modulo operation"""
    c = a / b
    c = math.floor(c)
    c = c * b
    c = a - c
    return(c)