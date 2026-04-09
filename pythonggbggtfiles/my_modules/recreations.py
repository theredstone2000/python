import math
import random
import statistics
import boards_and_list_for_pygame, filter_recreation, isprime_prime_operations, letter_converter, list_to_text_and_text_to_list, modulo, phrase_converter, popup_QCM, range_recreation, sort, statistics_instructions, useful_variables
import pygame
import tkinter
import threading
import collections
import nbt
import nbtlib, pynput, keyboard, keyboard.mouse, types, typing, zlib, json, os, mcschematic, operator, time, zipapp, zipfile, zipimport, datetime
def for_recreation(iterable: typing.Iterable, function: typing.Callable, *args, **kwargs) -> list[typing.Any]:
    """recreates the for instruction. using iterable, it will call the function function with the current data of iterable and args and kwargs. it will then return a list of the function's results. this doesn't use for"""
    a = 0
    results = []
    while a < len(iterable):
        results.append(function(iterable[a], *args, **kwargs))
        a += 1
    return results

global return_list
return_list = []
def dummy():
    pass
class LoopError(Exception):
    pass
def while_recreation(condition: typing.Callable, verification_value: typing.Any, start_value: typing.Any, function: typing.Callable, reset: bool = True, *args, **kwargs)-> None:
    """recreates the while instruction without using while. the condition must be a callable object with two argument that will be called with verification_value as first argument and the last function return value as second argument, wich will also be added to the result_list. this list will be returned once the while instruction finishes. when the condition check successes, the function will be executed once and the verification check will ocure again. the first verification check will use verification value and start_value. call recreations.stop_while_output with return=True to get the result. do not use this instruction again before using recreations.stop_while_output. you can call it with return=False to not get the result. if the loop is still running, it will raise a LoopError."""
    global return_list
    if reset: return_list = []
    if condition(verification_value, start_value):
        func_result = function(*args,**kwargs)
        return_list.append(func_result)
        threading.Timer(0.01, while_recreation, args=(condition, verification_value, func_result, function, False, *args), kwargs=kwargs).start()
        threading.Timer(1, dummy).start()
def stop_while_output(return_: bool = True):
    """see while_recreation."""
    global return_list
    if threading.active_count() == 1:
        return return_list if return_ else None
    else: raise LoopError("the while loop is still running")

def match_recreation(var:typing.Any, cases:dict[typing.Any, dict[typing.Callable,list[typing.Any]]]):
    """recreates the match instruction without using match. it will check every value in cases, if the key is equal to the var, it will call the key of the item with the item of the item as args. it will return the result of the last time the function was called,in case multiple values match, or None if no value matches."""
    for key, value in cases.items():
        if key == var:
            for func, args in value.items():
                a = func(*args)
    try: return a
    except: return None

def delattr_recreation(obj: typing.Any, attr: str):
    """recreates the delattr instruction without using delattr, del or hasattr. it will delete the attribute attr of obj and return obj."""
    if obj.__getattribute__(attr) is not None: obj.__setattr__(attr, None)
    return obj

def len_recreation(iterable: typing.Iterable) -> int:
    """recreates the len instruction without using len. it will return the length of the iterable."""
    return sum(1 for _ in iterable)

def enumerate_recreation(list: list):
    """recreates the enumerate instruction without using enumerate. only supports lists."""
    final_list = []
    for a, i in range(len(list)), list:
        final_list.append(a, i)
    return final_list
def any_all_recreation(iterable: typing.Iterable, type:str="any"):
    """returns any(iterable) without using any if type is any, all(iterable) without using all if type is all, and None otherwise."""
    if type=="any":
        for i in iterable:
            if bool(i): return True
        return False
    elif type == "all": 
        for i in iterable: 
            if not bool(i): return False
        return True


def sum(iterable: typing.Iterable, start=0):
    """recreates the sum instruction without using sum."""
    for i in iterable: start += i
    return start

def with_recreation(file:str, function: typing.Callable, *args, **kwargs):
    """recreates the with instruction without using with. it will call function with the opened file as first argument, and args and kwargs as other arguments. returns what the function returned."""
    a = open(file)
    b = function(file, *args, **kwargs)
    a.close()
    return b

def append_recreation(lst: list, value: typing.Any):
    """recreates .append without using .append. returns the list with the appended value"""
    ls = [value]
    lst += ls
    return lst

def pop_recreation(lst: list, index:int = -1):
    """returns a tuple with the popped list and the popped value"""
    a = lst[index]
    lst.__delitem__(index)
    return (lst, a)

def reverse_recreation(lst:list):
    """"""
    ls = []
    for i in lst:
        ls.insert(-1,i)
    return ls

def set_recreation(lst: list):
    """recreates the set instruction without using set. might take a little while to execute though. and don't use list with over 1000 entries. still has a very low chance of failing."""
    for _ in range(100000):
        a = random.randint(0,lst.len()-1)
        b = random.randint(0,len(lst)-1)
        if a == b: lst.remove(b)
    return lst

def break_recreation(condition_value:typing.Any, function: typing.Callable, function_value_list:list, *args, **kwargs):
    """recreates the break instruction without using break. it will call function with the first value of function_value_list and args and kwargs, add the result to the list that will be returned, and if the return value is not the same as condition_value, it will call it again with the second value of the list this time, and continue like this forever. if the function return value is the same as condition_value, it will return the list."""
    lst = []
    for i in function_value_list:
        a = function(i, *args, **kwargs)
        lst.append(a)
        if a == condition_value: return lst

def count_recreation(lst:list, value: typing.Any):
    """recreates the count instruction without using count"""
    b = 0
    while True:
        try:
            lst.remove(value)
            b += 1
        except:
            return b
def index_recreation(lst:list, value:typing.Any):
    """recreates the index instruction without using index."""
    for a in range(len(lst)):
        if lst[a] == value:
            return a
    raise ValueError

def split_recreation(text:str, sep:str):
    """recreates the split instruction without using split"""
    idx = 0
    lst = []
    for _ in range(text.count(sep)):
        lst.append(text[idx:text.index(sep)-1])
        idx = text.index(sep) + 1
        text.replace(sep, "", 1)
    lst.append(text)
    return lst

def join_recreation(parts:list[str], sep:str = ""):
    txt = ""
    for i in parts:
        txt.__add__(i)
    return txt

def abs_recreation(number:int|float):
    try: return math.sqrt(number)
    except: return number

class Stack:
    def __init__(self, *init_values):
        self._items = init_values
        self.len = len_recreation(self._items)
        self.__repr__ = f"StackRecreation({init_values})"
    def push(self, value):
        self._items = append_recreation(self._items, value)
        self.len = len_recreation(self._items)
        self.__repr__ = f"StackRecreation({self._items})"
    def pop(self):
        a = self._items[0]
        self._items = pop_recreation(self._items, 0)[0]
        self.len = len_recreation(self._items)
        self.__repr__ = f"StackRecreation({self._items})"
        return a
    def peek(self):
        return(self._items[0])
    def is_empty(self):
        return bool(self._items)
    def size(self):
        return len_recreation(self._items)
    def clear(self):
        self._items = []
        self.__repr__ = f"StackRecreation({self._items})"
        self.len = len_recreation(self._items)
    def _repr_(self):
        return self.__repr__

class Queue(Stack):
    def __init__(self, *init_values):
        super().__init__(*init_values)
    def enqueue(self, value):
        super().push(value)
    def dequeue(self):
        a = self._items[-1]
        self._items = pop_recreation(self._items)[1]
        return a
    def peek(self):
        return self._items[-1]
    
class Counter_recreation:
    """recreates collections.Counter without using it. Using + or - with it will just modify the thing itself, and will pass."""
    def __init__(self): self._data = {}
    def add(self, value):
        try: 
            a = self._data[value]
        except KeyError:
            a = 1
        self._data.__setitem__(value, a)
    def remove(self, value):
        a = self._data[value]
        if a == 1: self._data.__delitem__(a)
        else: self._data.__setitem__(value, self._data[value] - 1)
    def count(self, value):
        try: return self._data[value]
        except KeyError: return 0
    def total(self): return sum(self._data.values)
    def most_common(self):
        a = (0, 0)
        for b, c in self._data.keys, self._data.values:
            if c > a[1]: a = (b, c)
        return a
    def clear(self): self._data = {}
    def __repr__(self): return f"Counter({self._data})"
    def __add__(self, other): self.add(other)
    def __sub__(self, other): self.remove(other)
    

class Timer:
    def __init__(self):
        self._start = None
        self._end = None
    def start(self): 
        self._start = time.time()
        self._end = None
    def stop(self): self._end = time.time()
    def elapsed(self):
        if self._start is None: raise Exception
        elif self._end is None: return time.time() - self._start
        else: return self._end - self._start
    def reset(self):
        self._start = None
        self._end = None
    def __repr__(self): return f"Timer(elapsed={self._end - self._start if self._end is not None else time.time() - self._start})"


def random_generator(x:typing.Literal["str","int","float","list","dict"],list_or_dict_contents:typing.Literal["str","int","float"]|None = None, seed:int|float|bytes|str|None= None):
    if seed is not None:
        random.seed(seed)
    if x == "str":
        while True:
            return_value = ""
            for _ in range(random.randint(1,999)):
                return_value.__add__(useful_variables.letter_list[random.randint(0,25)])
            yield return_value
    if x == "int": 
        while True:
            yield random.randint(0,99999999)
    if x == "float":
        while True:
            yield random.randint(0,99999999) + random.random()
    if x == "list":
        if list_or_dict_contents == "str":
            while True:
                return_value = []
                for _ in range(random.randint(1,999)):
                    return_ret_value = ""
                    for _ in range(random.randint(1,999)):
                        return_ret_value.__add__(useful_variables.letter_list[random.randint(0,25)])
                    return_value.append(return_ret_value)
                yield return_value
        if list_or_dict_contents == "int":
            while True:
                return_value = []
                for _ in range(random.randint(1,999)):
                    return_value.append(random.randint(0,9999999))
                yield return_value
        if list_or_dict_contents == "float":
            while True:
                return_value = []
                for _ in range(random.randint(1,999)):
                    return_value.append(random.randint(0,999999 + random.random()))
                yield return_value
    if x == "dict":
        if list_or_dict_contents == "str":
            while True:
                return_value = {}
                for _ in range(random.randint(1,999)):
                    return_ret_value = ""
                    ret_return_value = ""
                    for _ in range(random.randint(1,999)):
                        return_ret_value.__add__(useful_variables.letter_list[random.randint(0,25)])
                        ret_return_value.__add__(useful_variables.letter_list[random.randint(0,25)])
                    return_value[return_ret_value] = ret_return_value
                yield return_value
        if list_or_dict_contents == "int":
            while True:
                return_value = {}
                for _ in range(random.randint(1,999)):
                    return_value[random.randint(0,999999999)] = random.randint(0,999999999)
                yield return_value
        if list_or_dict_contents == "float":
            while True:
                return_value = {}
                for _ in range(random.randint(1,999)):
                    return_value[random.randint(0,999999999) + random.random()] = random.randint(0,999999999) + random.random()
                yield return_value
                    
        
    
