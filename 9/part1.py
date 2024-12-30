path = r'C:\Data\00 - Prive\20 - GITHUB REPO\Advent-of-Code-2024\9\data.txt'

def get_data(path):
    with open(path, 'r') as file:
        lines = file.readlines()
    return lines[0]
    
source_string = get_data(path)

source_list = list(map(int, source_string))

files = source_list[0::2]
frees = source_list[1::2]
ids = list(range(len(files)))

i_file = len(files) - 1
i_free = 0
curr_free = frees[i_free]
result = []
result.extend([0] * files[0])
biggest_file_inserted_betweenfrees = 0

while i_file and i_file > biggest_file_inserted_betweenfrees:
    file = files[i_file]
    id = ids[i_file]
    while file and i_file > biggest_file_inserted_betweenfrees:
        if file > curr_free:
            # File does not fit in curr_free
            result.extend([id] * curr_free)
            file -= curr_free
            
            # Move to new free space
            i_free += 1
            curr_free = frees[i_free]
            # Add the file that is inbetween the free spaces
            if ids[i_free] == id:
                # only the last part of the last file is left
                result.extend([id] * file)
                i_file -= 1
                biggest_file_inserted_betweenfrees = i_free
                continue
            else:
                result.extend([ids[i_free]] * files[i_free])
                biggest_file_inserted_betweenfrees = i_free

        elif file <= curr_free:
            # File does fit in curr_free
            result.extend([id] * file)
            curr_free -= file
            i_file -= 1
            file = 0

print(sum([i*pos for i, pos in enumerate(result)]))