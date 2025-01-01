import numpy as np

path = r'C:\Data\00 - Prive\20 - GITHUB REPO\Advent-of-Code-2024\11\data.txt'

def get_data(path):
    with open(path, 'r') as file:
        lines = file.readlines()
    return lines[0]
    
source_string = get_data(path).split()

input_list = np.array(list(map(int, source_string)), dtype=np.int64)

def split(value):
    middle = len(value) // 2
    return int(value[:middle]), int(value[middle:])
    
def blink(i):
    print(i)    
    global input_list
    
    last_rule = (input_list != 0) & (np.char.str_len(input_list.astype(str)) % 2 != 0)
    first_rule = input_list == 0
    second_rule = ~(last_rule | first_rule)

    input_list[last_rule] *= 2024
    input_list[first_rule] = 1

    input_list = np.concatenate([input_list[~second_rule], np.concatenate([np.array(split(str(value))) for value in input_list[second_rule]])])
    
result = [blink(i) for i in range(75)]

print(len(input_list))