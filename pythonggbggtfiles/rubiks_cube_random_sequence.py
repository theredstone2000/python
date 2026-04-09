import math
import random
import operator

all_moves = ["A","AI","A2","B","BI","B2","H","HI","H2","P","PI","P2","G","GI","G2","D","DI","D2"]
a = 0
result = []
while a < 20:
    result.insert(result.__len__(), all_moves.__getitem__(random.randint(0,17)))
    a = a + 1

while not a == 2:
    result.insert(result.__len__(), all_moves.__getitem__(random.randint(0,17)))
    a = random.randint(1,2)

print(result)
