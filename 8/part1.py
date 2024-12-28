import numpy as np
from itertools import combinations as itercombinations

path = r'C:\Data\00 - Prive\20 - GITHUB REPO\Advent-of-Code-2024\8\data.txt'

def get_data(path):
    with open(path, 'r') as file:
        lines = file.readlines()
    return lines
    
source_data = get_data(path)
data = [list(x.strip("\n")) for x in source_data]
data = np.array(data)

frequencies = np.setdiff1d(np.unique(data), np.array(['.']))

# {'freq': [(x,y), (x,y), ...], 
# ...:...}
antenna_coordinates = {frequency: [(x, y) for y, row in enumerate(source_data) 
                     for x, s in enumerate(row) if s == frequency]
                     for frequency in frequencies}

min_x, min_y, max_x, max_y = 0, 0, len(data[0]), len(data)

max_coord = (max_x, max_y)
min_coord = (min_x, min_y)

def get_antinode_locations(antenna_coordinates):
    combinations = itercombinations(antenna_coordinates,r=2)
    antinode_locations = []
    
    for combination in combinations:
        min_antenna, max_antenna = min(combination), max(combination)
        
        max_x = max(min_antenna[0], max_antenna[0])
        min_x = min(min_antenna[0], max_antenna[0])
        max_y = max(min_antenna[1], max_antenna[1])
        min_y = min(min_antenna[1], max_antenna[1])
        
        diff = (np.subtract(max_antenna, min_antenna))
        
        dx = diff[0]
        dy = diff[1]
        
        if dx == 0:
            left, right = np.inf, np.inf
        else:
            left = min_x/np.abs(dx)
            right = (max_coord[0] - max_x - 1)/np.abs(dx)
        if dy == 0:
            up, down = np.inf, np.inf
        else:
            up = (max_coord[1] - max_y - 1)/np.abs(dy)
            down = (min_y)/np.abs(dy)
        
        if dx >= 0 and dy >= 0:
            n_add = np.floor(np.min([right, up]))
            n_subtract = np.floor(np.min([left, down]))
        
        if dx >= 0 and dy < 0:
            n_subtract = np.floor(np.min([left, up]))
            n_add = np.floor(np.min([right, down]))
            
        if n_subtract > 0:
            antinodes_subtract = np.subtract(min_antenna, [i*diff for i in range(1, int(n_subtract+1))])
            antinode_locations.extend(antinodes_subtract)
        if n_add > 0:
            antinodes_add = np.add(max_antenna, [i*diff for i in range(1, int(n_add+1))])
            antinode_locations.extend(antinodes_add)
        
    return antinode_locations


antinode_locations = [location for freq in antenna_coordinates.keys() 
                 for location in get_antinode_locations(antenna_coordinates[freq])]

# Add antenna's
antinode_locations.extend([t for freq in antenna_coordinates for t in antenna_coordinates[freq]])

antinode_locations = np.array(antinode_locations)

antinode_locations_within_bounds = antinode_locations[
    (antinode_locations[:, 0] < max_x) &
    (antinode_locations[:, 0] >= min_x) &
    (antinode_locations[:, 1] < max_y) &
    (antinode_locations[:, 1] >= min_y)
]

antinode_locations_within_bounds = np.unique(antinode_locations_within_bounds, axis=0)

print(f"\n{len(antinode_locations_within_bounds)} unique locations within the bounds of the map contain an antinode.\n")