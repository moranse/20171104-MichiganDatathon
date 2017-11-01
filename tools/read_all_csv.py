import os
import pandas as pd

def read_all_csvs(data_folder):
    files = {}
    for f in os.listdir(data_folder):
        if 'csv' in f:
            obj_name = f.split('.csv')[0]
            files[obj_name] = pd.read_csv(data_folder + f)
    return files
