import pandas as pd
import numpy as np
import re

path = r'C:\Data\00 - Prive\20 - GITHUB REPO\Advent-of-Code-2024\4\data.txt'

def get_data(path):
    with open(path, 'r') as file:
        lines = file.readlines()
    return lines
    
source_data = get_data(path)

len_strings = len(source_data[0]) - 1
depth_strings = len(source_data)

data = np.char.rstrip(source_data, chars = "\n").tolist()
data_array = np.array([list(row) for row in data])

size_maps = 3

total = 0

for y in range(0, depth_strings):
    for x in range(0, len_strings): 
        # diag
        if (x + size_maps <= len_strings) and (y + size_maps <= depth_strings):
            diag = "".join(data_array[y+np.arange(size_maps), x+np.arange(size_maps)])
            diag_T = "".join(data_array[y+np.arange(size_maps), x+np.arange(size_maps)[::-1]])
            if ((diag == 'MAS') or (diag == 'SAM')) and ((diag_T == 'MAS') or (diag_T == 'SAM')): total += 1

print(total)