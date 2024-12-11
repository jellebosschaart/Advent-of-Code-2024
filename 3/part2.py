import pandas as pd
import numpy as np
import re

path = r'C:\Data\00 - Prive\20 - GITHUB REPO\Advent-of-Code-2024\3\data.txt'

def get_data(path):
    with open(path, 'r') as file:
        lines = file.readlines()
        return "".join(lines)
    
source_data = get_data(path)

multiplications = re.findall("(do\(\)|don't\(\)|mul\(\d+,\d+\))", source_data)

do = True
sum = 0

for v in multiplications:
    if v == "do()":
        do = True
        continue
    if v == "don't()":
        do = False
        continue
    if do:
        numbers = re.findall("([\d]+)", v)
        sum += int(numbers[0]) * int(numbers[1])
        
print(sum)