import pandas as pd
import numpy as np
import re

path = r'C:\Data\00 - Prive\20 - GITHUB REPO\Advent-of-Code-2024\3\data.txt'

def get_data(path):
    with open(path, 'r') as file:
        lines = file.readlines()
        return "".join(lines)
    
source_data = get_data(path)

multiplications = re.findall("([m][u][l][(][\d]+[,][\d]+[)])", source_data)
numbers = re.findall("([\d]+)", "".join(multiplications))

odd_pos_numbers = np.array(numbers[0::2]).astype(int)
even_pos_numers = np.array(numbers[1::2]).astype(int)

print(np.sum(odd_pos_numbers * even_pos_numers))