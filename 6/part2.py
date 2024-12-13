import pandas as pd
import numpy as np
from math import prod
import re

path = r'C:\Data\00 - Prive\20 - GITHUB REPO\Advent-of-Code-2024\6\data.txt'

def get_data(path):
    with open(path, 'r') as file:
        lines = file.readlines()
    return lines
    
source_data = get_data(path)
data = [list(x.strip("\n")) for x in source_data]
data = np.array(data)

blocking_coordinates = [(x, y) for y, row in enumerate(source_data) 
                     for x, s in enumerate(row) if s == "#"]

blocking_coordinates.sort()

start_coordinates = [(x, y) for y, row in enumerate(source_data) 
                     for x, s in enumerate(row) if s in ["^"]][0]

def turn_right(direction):
    if direction < 3:
        direction += 1
    else:
        direction = 0
    return direction

max_x = len(data[:,0])
max_y = len(data[0])

travelled = []

def travel(current_coordinates, direction, print_info, current_blocking_coordinates):
    current_x = current_coordinates[0]
    current_y = current_coordinates[1]
    if print_info: print(f"\nFROM (x,y): {current_coordinates} (DIRECT: {direction})")
    new_coord = current_coordinates
    
    if direction == 0:
        if print_info: print("MOVING UP")
        try:
            new_y = np.max([coordinate[1] for coordinate in current_blocking_coordinates if (coordinate[0] == current_x) and (coordinate[1] < current_y)]) + 1
            new_coord = (current_x, new_y)
        except:
            new_y = 0
            new_coord = (current_x, new_y)
        [travelled.append((current_x, range_y)) 
         for range_y in range(new_y, current_y+1)]
            
    elif direction == 1:
        if print_info: print("MOVING RIGHT")
        try:
            new_x = np.min([coordinate[0] for coordinate in current_blocking_coordinates if (coordinate[1] == current_y) and (coordinate[0] > current_x)]) - 1
            new_coord = (new_x, current_y)
        except:
            new_x = max_x
            new_coord = (new_x, current_y)
            
        [travelled.append((range_x, current_y)) 
         for range_x in range(current_x, new_x+1)]
    
    elif direction == 2:
        if print_info: print("MOVING DOWN")
        try:
            new_y = np.min([coordinate[1] for coordinate in current_blocking_coordinates if (coordinate[0] == current_x) and (coordinate[1] > current_y)]) - 1
            new_coord = (current_x, new_y)
        except:
            new_y = max_y
            new_coord = (current_x, 0)
            
        [travelled.append((current_x, range_y)) 
         for range_y in range(current_y, new_y+1)]
        
    elif direction == 3:
        if print_info: print("MOVING LEFT")
        try:
            new_x = np.max([coordinate[0] for coordinate in current_blocking_coordinates if (coordinate[1] == current_y) and (coordinate[0] < current_x)]) + 1
            new_coord = (new_x, current_y)
        except:
            new_x = 0
            new_coord = (new_x, current_y)
        
        [travelled.append((range_x, current_y)) 
         for range_x in range(new_x, current_x+1)] 
    else:
        return (0,0)

    new_x, new_y = new_coord[0], new_coord[1]

    if print_info: print(f"TO   (x,y): {new_x, new_y}")
    return new_coord


def try_to_get_out(new_coordinates, direction, current_blocking_coordinates, print_info):
    moving = True
    got_out = True
    i = 0
    old_len_traveled = len(set(travelled))

    while moving:
        i += 1
        new_coordinates = travel(new_coordinates, direction, print_info=print_info, current_blocking_coordinates = current_blocking_coordinates)
        x = new_coordinates[0]
        y = new_coordinates[1]
        
        direction = turn_right(direction)
    
        if i%8 == 0:
            if old_len_traveled == (len(set(travelled))):
                #print("I'm stuck!!!")
                return False
            old_len_traveled = len(set(travelled))
        
        if (y in [0, max_y]) or (x in [0, max_x]):
            return True
    
    return True
    
try_to_get_out(start_coordinates, 0, blocking_coordinates, print_info = False)
print(f"\nUnique locations to check: {len(set(travelled))}\n")

possible_block_locations = travelled.copy()
possible_block_locations = list(set(possible_block_locations))
possible_block_locations.pop(possible_block_locations.index(start_coordinates))

got_out = 0
for possible_block_location in possible_block_locations:
    travelled = []
    got_out += try_to_get_out(new_coordinates=start_coordinates, direction=0, current_blocking_coordinates=blocking_coordinates + [possible_block_location], print_info=False)

#got_stuck_in_a_loop_locations = [possible_block_location for i, possible_block_location in enumerate(possible_block_locations) if not got_out[i]]
tried = len(possible_block_locations)

print(f"Looked at {tried} possible block locations")
print(f"Guard gets stuck in a loop in {tried-(got_out)} of those locations")