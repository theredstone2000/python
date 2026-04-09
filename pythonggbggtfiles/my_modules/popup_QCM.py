import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
"""ask_question uses tkinter's simpledialog and messagebox to ask a question to the user"""
def ask_question(a: str, b: str, c: str, d: str, e: int):
    """a is the question, b the first proposition, c the second one, d the last one, and e the right answer's number(1, 2 or 3). returns 1 if right answer and 0 if wrong answer."""
    b = "1 : " + b
    c = "2 : " + c
    d = "3 : " + d
    user_input = simpledialog.askinteger("QCM", a + b + c + d + "1, 2, ou 3 : ")
    user_input = int(user_input)
    if user_input == e:
        messagebox.showinfo("réponse", "bonne réponse !")
        return(1)
    else:
        messagebox.showinfo("réponse", "mauvaise réponse. bonne réponse : " + str(e))
        return(0)
