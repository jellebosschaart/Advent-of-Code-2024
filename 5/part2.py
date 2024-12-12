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

updates = [update.split(',') for update in updates]

# 97|75 -> 75 must have 97 before it.
# {75: [97]} -> 75 must have 97 before it.
# key must have numbers in value before it
rules_dict = {f'{a}': [] for a in range(10, 100)}

n_chars = 2
[rules_dict[(s[n_chars+1:])].append((s[:n_chars])) for s in rules_source]

update_logs = [[set(update[:len(update) - (i_page+1)]).issubset(rules_dict[(page)])
      for i_page, page in enumerate(update[::-1])]  
      for update in updates]

# Check per update if there is a False, then set it to 0, else 1.
update_logs = [prod(update_log) for update_log in update_logs]

for update, log in zip(updates, update_logs):
    if not log:
        while not log:
            for page in update:
                rules_pages_relevant = [page for page in rules_dict[page] if page in update]
                indexes_rules_pages_relevant = [update.index(rules_page_relevant) for rules_page_relevant in rules_pages_relevant]
                if indexes_rules_pages_relevant == []:
                    continue
                max_index_rules_page_relevant = np.max(indexes_rules_pages_relevant)
                index_page = update.index(page)
                
                # page on index_page must have indexes_rules_pages_relevant before it (max=max_index_rules_page_relevant)
                if index_page < max_index_rules_page_relevant:
                    update.pop(index_page)
                    update.insert(max_index_rules_page_relevant, page)

            log = prod([set(update[:len(update) - (i_page+1)]).issubset(rules_dict[(page)]) for i_page, page in enumerate(update[::-1])])
    

sum_middle_numbers_of_originally_wrong_pages = np.sum([int(update[int((len(update) - 1) / 2)]) for update, log in zip(updates, update_logs) if not log])

print(sum_middle_numbers_of_originally_wrong_pages)