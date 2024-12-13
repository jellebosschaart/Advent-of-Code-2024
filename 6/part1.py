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

coordinates = [(x, y) for y, row in enumerate(source_data) 
                     for x, s in enumerate(row) if s == "#"]

current_coordinates = [(x, y) for y, row in enumerate(source_data) 
                     for x, s in enumerate(row) if s in ["^"]][0]

def turn_right(direction):
    return (direction + 1) % 4

x = [coordinate[0] for coordinate in coordinates] 
y = [coordinate[1] for coordinate in coordinates]

max_x, max_y = np.max(x), np.max(y)

travelled = []

def travel(current_coordinates, direction, print):
    current_x = current_coordinates[0]
    current_y = current_coordinates[1]
    if print: print(f"\nFROM (x,y): {current_coordinates} (DIRECT: {direction})")
    new_coord = current_coordinates
    
    if direction == 0:
        if print: print("MOVING UP")
        try:
            new_y = np.max([coordinate[1] for coordinate in coordinates if (coordinate[0] == current_x) and (coordinate[1] <= current_y)]) + 1
            new_coord = (current_x, new_y)
        except:
            new_y = 0
            new_coord = (current_x, new_y)
        [travelled.append((current_x, range_y)) 
         for range_y in range(new_y, current_y+1)]
            
    elif direction == 1:
        if print: print("MOVING RIGHT")
        try:
            new_x = np.min([coordinate[0] for coordinate in coordinates if (coordinate[1] == current_y) and (coordinate[0] >= current_x)]) - 1
            new_coord = (new_x, current_y)
        except:
            new_x = max_x
            new_coord = (new_x, current_y)
        [travelled.append((range_x, current_y)) 
         for range_x in range(current_x, new_x+1)]
    
    elif direction == 2:
        if print: print("MOVING DOWN")
        try:
            new_y = np.min([coordinate[1] for coordinate in coordinates if (coordinate[0] == current_x) and (coordinate[1] >= current_y)]) - 1
            new_coord = (current_x, new_y)
        except:
            new_y = max_y
            new_coord = (current_x, 0)
        [travelled.append((current_x, range_y)) 
         for range_y in range(current_y, new_y+1)]
        
    elif direction == 3:
        if print: print("MOVING LEFT")
        try:
            new_x = np.max([coordinate[0] for coordinate in coordinates if (coordinate[1] == current_y) and (coordinate[0] <= current_x)]) + 1
            new_coord = (new_x, current_y)
        except:
            new_x = 0
            new_coord = (new_x, current_y)
        [travelled.append((range_x, current_y)) 
         for range_x in range(new_x, current_x+1)]
        
    else:
        return (0,0)

    new_x, new_y = new_coord[0], new_coord[1]

    if print: print(f"TO   (x,y): {new_x, new_y}")
    return new_coord

new_coordinates = current_coordinates
direction = 0
moving = True

while moving:
    new_coordinates = travel(new_coordinates, direction, print=False)
    x = new_coordinates[0]
    y = new_coordinates[1]
    
    direction = turn_right(direction)
    
    if (y in [0, max_y]) or (x in [0, max_x]):
        moving=False
    
print(f"\nUnique locations: {len(set(travelled))}")