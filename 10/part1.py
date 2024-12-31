import numpy as np
from itertools import chain

path = r'C:\Data\00 - Prive\20 - GITHUB REPO\Advent-of-Code-2024\10\data.txt'

def get_data(path):
    with open(path, 'r') as file:
        lines = file.readlines()
    return lines
    
source_data = get_data(path)

data = np.char.rstrip(source_data, chars="\n").tolist()
data_array = np.array([list(map(int, row)) for row in data])

max_x = len(data_array[0]) - 1
max_y = len(data_array) - 1

zeros = [(y, x) for y, row in enumerate(data_array) 
                     for x, s in enumerate(row) if s == 0]

def next_step(y, x, num):
    if num == 9:
        return [(y,x)]
    
    positions = np.array([(y, x+1), (y, x-1), (y-1, x), (y+1, x)])
    
    positions = positions[
    (positions[:,1] >= 0) &
    (positions[:,0] >= 0) &
    (positions[:,1] <= max_x) &
    (positions[:,0] <= max_y)]
    
    results = []
    for pos in positions:
        if data_array[pos[0], pos[1]] == (num+1):
            results.extend(next_step(pos[0], pos[1], data_array[pos[0], pos[1]]))
    return results

result = [next_step(zero[0], zero[1], 0) for zero in zeros]

print(sum([len(list(set(res))) for res in result]))