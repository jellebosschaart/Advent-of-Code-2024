import numpy as np
from itertools import chain

path = r'C:\Data\00 - Prive\20 - GITHUB REPO\Advent-of-Code-2024\12\data.txt'

def get_data(path):
    with open(path, 'r') as file:
        lines = file.readlines()
    return lines
    
source_data = get_data(path)

data = np.char.rstrip(source_data, chars="\n").tolist()
data_array = np.array([list(map(str, row)) for row in data])

ys, xs = (np.where(data_array))

coords_left = [(y,x) for y, x in zip(ys, xs)]

rows = len(data_array)
cols = len(data_array[0]) if rows > 0 else 0

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def find_touching_cells(grid, x, y, plant):
    # Recursive function to explore surrounding cells
    def explore(x, y, visited):
        if x < 0 or x >= rows or y < 0 or y >= cols:
            return
        if (x, y) in visited:
            return
        if data_array[x][y] != plant:
            return
        
        visited.add((x, y))
        
        # Explore all surrounding cells (up, down, left, right)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            explore(nx, ny, visited)

    visited = set()
    explore(x, y, visited)
    
    # Get touches
    touches = 0
    for cx, cy in visited:
        # Count how many of its non-diagonal neighbors have the same value (plant)
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < rows and 0 <= ny < cols and data_array[nx][ny] == plant:
                touches += 1
    
    return list(visited), touches

price = 0
while len(coords_left) != 0:
    start_coord = coords_left[0]
    y, x = start_coord[1], start_coord[0]
    plant = data_array[x, y]
    
    touching_cells, touches = find_touching_cells(data_array, x, y, plant)

    area = len(touching_cells)
    
    price += 4*(area**2) - (touches)*area

    coords_left = np.delete(coords_left, 
                            [i for i, coord in enumerate(coords_left) if tuple(coord) in touching_cells], 
                            axis=0)
    
print(price)