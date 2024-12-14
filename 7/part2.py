import pandas as pd
import numpy as np
from math import prod
import random
import re
from copy import deepcopy
from itertools import product

path = r'C:\Data\00 - Prive\20 - GITHUB REPO\Advent-of-Code-2024\7\data.txt'

def get_data(path):
    with open(path, 'r') as file:
        lines = file.readlines()
    return lines
    
source_data = get_data(path)

data = ([[int(t) for t in re.split(r'[-\s]', line.replace(': ', '-').strip()) if t.isdigit()] for line in source_data])

# For insight in developing
map_operators = {0: '+', 1:'*', 2:'||'}

# For insight in developing
def get_calc_string(numbers, operators):
    calc_string = ""
    for operator, number in zip(operators,numbers):
        calc_string += (f' {number} ' + map_operators[operator])
    calc_string += f' {numbers[-1]}'
    return calc_string

def cumulative_calculation(numbers, operators):
    cum = numbers[0]
    for i in range(1, len(numbers)):
        current_operator = operators[i-1]
        if i < len(numbers):
            if current_operator == 2:cum = int(f"{cum}{numbers[i]}")
            if current_operator == 1:cum *= numbers[i]
            elif current_operator==0:cum+=numbers[i]
    return cum

def get_test_value_if_row_correct(row):
    test_value, remaining_numbers = row[0], row[1:]
    permutations = product([0,1,2],repeat=len(remaining_numbers)-1)

    if test_value in [cumulative_calculation(deepcopy(remaining_numbers), permutation) for permutation in permutations]:
        return test_value
    else:
        return 0

correct_test_values = [get_test_value_if_row_correct(line) for line in data]
print(np.sum(correct_test_values))