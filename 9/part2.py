import numpy as np

path = r'C:\Data\00 - Prive\20 - GITHUB REPO\Advent-of-Code-2024\9\data.txt'

def get_data(path):
    with open(path, 'r') as file:
        lines = file.readlines()
    return lines[0]
    
source_string = get_data(path)

source_list = list(map(int, source_string))

# free_id: [file_ids]
moves = {}
moved_files = []

files = source_list[0::2]
frees = source_list[1::2]
frees.append(0)
frees = np.array(frees)
file_ids = list(range(len(files)))
free_ids = np.array(list(range(len(frees))))


# Get moves
for file_id, file_size in reversed(list(enumerate(files))):
    possible_locations = free_ids[frees>=file_size]
    if not len(possible_locations):
        continue
    # There is a free space where the file fits.
    location = possible_locations[0]
    
    if location >= file_id:
        continue
    # Location is on the left of the file.
    
    # Save the move of file_id to free location and update the availablility of the free spot.
    moved_files.append(file_id)
    if location in moves:
        moves[location].append(file_id)
    else:
        moves[location] = [file_id]
    frees[location] -= file_size

result = []
for id in file_ids:
    #print(f"id={id}; file={files[id]}; free={frees[id]}(old={frees_copy[id]})")
    # file space
    if id in moved_files:
        result.extend([None] * files[id])
    else:
        result.extend([id] * files[id])
    
    # free space:
    if id in moves:
        to_be_entered_in_free_space = moves[id]
        to_be_added_free_spaces = frees[id]
        for file_id in to_be_entered_in_free_space:
            result.extend([file_id] * files[file_id])
        if to_be_added_free_spaces > 0:
            result.extend([None] * to_be_added_free_spaces)
    else:
        result.extend([None] * frees[id])


results = [i*pos for i, pos in enumerate(result) if pos is not None]

print(np.sum(results, dtype=np.int64))
print(sum(results))