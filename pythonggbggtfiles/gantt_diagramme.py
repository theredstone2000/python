from my_modules import boards_and_list_for_pygame as bd
from tkinter import messagebox
import time

input_board = bd.board("input_board", False)

letter_column = bd.column("letters")
t = bd.case("first_case")
t.define_type(0)
t.define_str("task letters")
letter_column.add_case(t)

helper = 26
letter = "A"
helper_list = []

while helper > 0:
    if helper == 26: letter = "A"
    elif helper == 25: letter = "B"
    elif helper == 24: letter = "C"
    elif helper == 23: letter = "D"
    elif helper == 22: letter = "E"
    elif helper == 21: letter = "F"
    elif helper == 20: letter = "G"
    elif helper == 19: letter = "H"
    elif helper == 18: letter = "I"
    elif helper == 17: letter = "J"
    elif helper == 16: letter = "K"
    elif helper == 15: letter = "L"
    elif helper == 14: letter = "M"
    elif helper == 13: letter = "N"
    elif helper == 12: letter = "O"
    elif helper == 11: letter = "P"
    elif helper == 10: letter = "Q"
    elif helper == 9: letter = "R"
    elif helper == 8: letter = "S"
    elif helper == 7: letter = "T"
    elif helper == 6: letter = "U"
    elif helper == 5: letter = "V"
    elif helper == 4: letter = "W"
    elif helper == 3: letter = "X"
    elif helper == 2: letter = "Y"
    elif helper == 1: letter = "Z"

    t.define_str(letter)
    t.change_id(letter)
    letter_column.add_case(t)
    helper -= 1
    helper_list.append(letter)

input_board.add_line_or_column(letter_column)

priority_column = bd.column("priority")
q = bd.case("start")
q.define_type(0)
q.define_str("priority")
priority_column.add_case(q)

q.__delattr__("value")
q.define_type(2)
q.define_list(["choose each priority here !"])
for t in helper_list:
    q.add_to_list(t)
for t in helper_list:
    q.change_id(t)
    priority_column.add_case(q)

input_board.add_line_or_column(priority_column)

duration_column = bd.column("duration_column")
g = bd.case("duration")
g.define_type(1)
g.define_str("duration")
duration_column.add_case(g)

g.variable_type(int)
g.define_int(0)
for t in helper_list:
    g.change_id(t)
    duration_column.add_case(g)

#this line of code is supposed to display the board
a = 0
while a == 0:
    time.sleep(15)
    a = messagebox.askyesno("is he done ?", "Are You Done ?")
#and this line of code is supposed to undisplay it

class something_duration_weird_I_guess:
    def start_date(self, day:int):
        self.start_date = day
    def finish_date(self, day:int):
        self.finish_date = day
    def duration(self, duration:int):
        self.duration = duration

# create 26 task objects
tasks = {}
for ch in helper_list:
    tasks[ch] = something_duration_weird_I_guess()

# assign durations from input board
for ch in helper_list:
    tasks[ch].duration(input_board.get_values("duration_column", ch))

# schedule tasks A -> Z
for idx, ch in enumerate(helper_list):
    task = tasks[ch]
    task.start_date(0)
    # check all previous tasks for priority
    for prev in helper_list[:idx]:
        if input_board.get_values("priority", ch).count(prev):
            if task.start_date < tasks[prev].finish_date:
                task.start_date(tasks[prev].finish_date)
    task.finish_date(task.start_date + task.duration)
    tasks[ch] = task

output_board = bd.board("output",True)
lines = {}
cases = {}
other_helper_list = []
b = 1
while not b == tasks["Z"].finish_date:
    b = str(b)
    other_helper_list.append(b)
    b = int(b)
    b += 1
for idx in other_helper_list:
    cases[idx] = bd.case(idx)
for ch in helper_list:
    lines[ch] = bd.line(ch)
    for idx in helper_list:
        lines[ch].add_case(idx)
