import pandas as pd
import numpy as np

path = r'C:\Data\00 - Prive\20 - GITHUB REPO\Advent-of-Code-2024\1\data.txt'

def get_data(path):
    data = pd.read_csv(path, sep=r'\s+', header=None)
    return data

data = get_data(path)

freq_dict = data[1].value_counts().to_dict()

def get_freq(value):
    try:
        return freq_dict[value]
    except KeyError:
        return 0

score = np.sum(data[0] * data[0].apply(get_freq))

print(score)