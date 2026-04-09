"""get_words convert a TEXT into a list, deleting each split. list_to_text does the opposite"""
def get_words(TEXT: str, split: str):
    """convert a whole TEXT of N number of words into a list with a word for each object, changing word at each split"""
    list_final = TEXT.split(split)
    return(list_final)

def list_to_text(LIST: list[str], split: str):
    """convert a LIST into a text, adding a split each word."""
    N = LIST.__len__()
    TEXT = ""
    while not N == 0:
        TEXT = f"{TEXT}{LIST.pop(0)}{split}"
        N = N - 1
    return(TEXT)


