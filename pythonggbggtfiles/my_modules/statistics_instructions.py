import math
import random
import statistics
def mean(numbers: list[float|int]) -> float:
    return sum(numbers) / len(numbers) 
def median(numbers: list[float|int]) -> int|float:
    numbers.sort()
    first_index = len(numbers) / 2
    index = math.ceil(first_index) if not math.ceil(first_index) == first_index else int(first_index + 1)
    index = int(index)
    if first_index == index - 1:
        return mean([numbers[int(first_index-1)],numbers[index-1]])
    else: return(numbers[index-1])
def etendue(numbers: list[int|float]):
    numbers.sort()
    return numbers[-1] - numbers[0]