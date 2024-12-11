import pandas as pd
import numpy as np

def get_data():
    data = pd.read_csv('data.txt')
    return data

data = get_data()
print(data)