import os
import pandas as pd

def read_all_csvs(folder):
    files = {}
    for f in os.listdir(data_folder):
        if 'csv' in f:
            obj_name = f.split('.csv')[0]
            cmd = "global {}; {} = pd.read_csv('{}')".format(obj_name, obj_name, data_folder + f)
            print(cmd)
            exec(cmd, globals(), locals())
