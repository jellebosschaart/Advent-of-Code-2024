import pandas as pd
import numpy as np

path = r'C:\Data\00 - Prive\20 - GITHUB REPO\Advent-of-Code-2024\2\data.txt'

def get_data(path):
    with open(path, 'r') as file:
        lines = file.readlines()

        processed_lines = [line.strip().split(' ') for line in lines]
        max_columns = max(len(line) for line in processed_lines)
        processed_lines = [line + [np.nan] * (max_columns - len(line)) for line in processed_lines]

        return pd.DataFrame(processed_lines)

source_data = get_data(path)

data = source_data.fillna(0, inplace=False)

n_shifts = len(data.columns) - 1
max_shift = 3

data = data.apply(lambda x: x.astype(int))

notna = source_data.notna().drop(columns=0, axis=1)
na = source_data.isna().drop(columns=0, axis=1)
notna.columns = range(n_shifts)
na.columns = range(n_shifts)

shifts = (data.T.shift(-1).T - data).drop(columns=n_shifts, axis=1)

report_defies_max_shift = (np.sum(((shifts.abs() > max_shift) | (shifts.abs() == 0)) * notna, axis=1))

report_complies_all_incr_or_decr = ((np.sum((shifts < 0) + na, axis=1) == n_shifts) |
                                    (np.sum((shifts > 0) + na, axis=1) == n_shifts))

print(report_complies_all_incr_or_decr)

print(np.sum((report_defies_max_shift == 0) & (report_complies_all_incr_or_decr == 1)))