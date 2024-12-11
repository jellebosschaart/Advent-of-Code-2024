import pandas as pd
import numpy as np

path = r'C:\Data\00 - Prive\20 - GITHUB REPO\Advent-of-Code-2024\1\data.txt'

def get_data(path):
    data = pd.read_csv(path, sep=r'\s+', header=None)
    return data

data = get_data(path)

sorted_data = pd.DataFrame({col: np.sort(data[col]) for col in data.columns})

def get_total():
    return np.sum(np.abs(np.subtract(sorted_data[0], sorted_data[1])))

print(get_total())