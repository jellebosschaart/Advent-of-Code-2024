import pandas as pd
import numpy as np
from math import prod
import re

path = r'C:\Data\00 - Prive\20 - GITHUB REPO\Advent-of-Code-2024\5\data.txt'

def get_data(path):
    with open(path, 'r') as file:
        lines = file.readlines()
    return lines
    
source_data = get_data(path)
source_data = np.char.rstrip(source_data, chars = "\n").tolist()

divider = source_data.index("")

rules_source = source_data[0:divider]
updates = source_data[divider+1:]

# 97|75 -> 75 must have 97 before it.
# {75: [97]} -> 75 must have 97 before it.
# key must have numbers in value before it
rules_dict = {f'{a}': [] for a in range(10, 100)}

n_chars = 2
[rules_dict[(s[n_chars+1:])].append((s[:n_chars])) for s in rules_source]

update_logs = [[set(update.split(',')[:len(update.split(',')) - (i_page+1)]).issubset(rules_dict[(page)])
      for i_page, page in enumerate(update.split(',')[::-1])]  
      for i_update, update in enumerate(updates)]

# Check per update if there is a False, then set it to 0, else 1.
update_logs = [prod(update_log) for update_log in update_logs]

sum_middle_numbers = np.sum([int(update.split(',')[int((len(update.split(',')) - 1) / 2)]) for update, log in zip(updates, update_logs) if log])

print(sum_middle_numbers)