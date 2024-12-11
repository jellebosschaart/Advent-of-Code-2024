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
max_shift = 3

n_cols = len(source_data.columns)

def get_compliancy_of_shifts(source_data):
    
    data = source_data.fillna(0, inplace=False)
    data = data.apply(lambda x: x.astype(int))
    n_shifts = len(data.columns) - 1
    
    shifts = (data.T.shift(-1).T - data).drop(columns=n_shifts, axis=1)
    
    notna = source_data.notna().drop(columns=0, axis=1)
    na = source_data.isna().drop(columns=0, axis=1)
    notna.columns = range(n_shifts)
    na.columns = range(n_shifts)

    report_defies_max_shift = (np.sum(((shifts.abs() > max_shift) | 
                                    (shifts.abs() == 0)) * notna, axis=1))

    report_complies_all_incr_or_decr = ((np.sum((shifts < 0) + na, axis=1) == n_shifts) |
                                        (np.sum((shifts > 0) + na, axis=1) == n_shifts))

    return pd.Series((report_defies_max_shift == 0) & (report_complies_all_incr_or_decr == 1))

df_safe_reports = pd.DataFrame(get_compliancy_of_shifts(source_data), columns=['all_data'])

for drop_col in range(n_cols): #-1?
    sub_data = source_data.drop(columns=drop_col, axis=1)
    sub_data.columns = range(n_cols-1)
    df_safe_reports[f'no_{drop_col}'] = get_compliancy_of_shifts(sub_data)

print(np.sum(np.sum(df_safe_reports, axis=1) >= 1))