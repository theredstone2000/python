"""converts every letter of a phrase into other letters using a hardcoded expression. unconvert does the opposite. does not support special characters."""
from letter_converter import letter_converter as leco
def convert(a: str):
    """convert every letter of a phrase to another letter using a hardcoded expression"""
    c = 0
    output = ""
    while c < a.__len__():
        d = a.__getitem__(c)
        if not d == " ":
            d = leco.convert(d)
        c = c + 1
        output = output + d
    return(output)
def unconvert(a: str):
    """same process as convert, but the phrase goes back to the original one"""
    c = 0
    output = ""
    while c < a.__len__():
        d = a.__getitem__(c)
        if not d == " ":
            d = leco.unconvert(d)
        c = c + 1
        output = output + d
    return(output)