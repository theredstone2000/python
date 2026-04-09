"""this helps you create boards and lists where the user can choose values to implement
or let the program user change the values. every one of them must be initialized with an id (str)
"""

import random
import pygame
import time



class case:
    """create cases to put in each line or column of the board, don't forget to use .define_type."""
    def __init__(self, id: str):
        self.id = id

    def change_id(self, new_id: str):
        self.id = new_id

    def define_type(self, type: int):
        if type < 0 or type > 3:
            raise ValueError(type)
        self.type = type

    def variable_type(self, type: type = str | int | float | bool):
        self.var_type = type

    def define_str(self, value: str):
        if not self.type < 2:
            raise TypeError(self)
        self.var_type = str
        self.value = value

    def define_int(self, value: int):
        if not self.type < 2:
            raise TypeError(self)
        self.var_type = int
        self.value = value

    def define_float(self, value: float):
        if not self.type < 2:
            raise TypeError(self)
        self.var_type = float
        self.value = value

    def define_list(self, list: list[str]):
        if self.type > 1:
            self.title = list.pop(0)
            self.list = list
            self.selected = []
        else:
            raise TypeError

    def add_to_list(self, arg: str):
        if self.type > 1:
            self.list.append(arg)
        else:
            raise TypeError

    def list_title(self, title: str):
        if self.type > 1:
            self.title = title
        else:
            raise TypeError

    def define_bool(self, value: bool):
        if self.type < 2:
            self.var_type = bool
            self.value = value
        else:
            raise TypeError



class line:
    def __init__(self, id: str):
        self.case_number = 0
        self.cases = []
        self.id = id

    def change_id(self, new_id: str):
        self.id = new_id

    def add_case(self, case: case):
        self.case_number += 1
        self.cases.append(case)

    def remove_case(self):
        self.case_number -= 1
        self.cases.pop()


class column:
    def __init__(self, id: str):
        self.case_number = 0
        self.cases = []
        self.id = id

    def change_id(self, new_id: str):
        self.id = new_id

    def add_case(self, case: case):
        self.case_number += 1
        self.cases.append(case)

    def remove_case(self):
        self.case_number -= 1
        self.cases.pop()


class board:
    """always init with type : True for line board and type : False for column board as the argument ! default True"""

    def __init__(self, id: str, type: bool = True):
        self.line_number = 0
        self.column_number = 0
        self.lines = []
        self.columns = []
        self.type = type
        self.id = id



    def change_id(self, new_id: str):
        self.id = new_id

    def add_line_or_column(self, obj: line | column):
        if self.type:
            self.lines.append(obj)
        else:
            self.columns.append(obj)

    def remove_line_or_column(self, index: int = -1):
        if self.type:
            self.lines.pop(index)
        else:
            self.columns.pop(index)

    
    

    def get_values(self, line_or_column_id: str, case_id: str):
        
        return()
