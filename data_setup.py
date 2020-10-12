import load_data
from scipy import stats
from os import listdir
import scipy.io
import pandas as pd
import fnmatch

files = ["P1_high2.mat", "P1_low1.mat", "P1_low2.mat","P2_high1.mat", "P2_high2.mat", "P2_low2.mat"]


def process_allfiles() :
    df = pd.DataFrame()
    for i in files:
        P_df = set_up(i)
        df = df.append(P_df)
    return df

def set_up(filename):
    data = load_data.load_dataset(filename)
    col_names = {0:"Fz", 1:"C3", 2:"Cz", 3:"C4", 4:"CP1", 5:"CPz", 6:"CP2", 7:"Pz"}
    df = pd.DataFrame.from_dict(data["y"])
    df.rename(columns=col_names, inplace=True)
    df_trig = pd.DataFrame.from_dict(data["trig"])
    df_trig.rename(columns={0:"trigger"}, inplace=True)
    df_full = pd.concat([df_trig, df.reindex(df.index)], axis=1)
    df_full.reset_index(inplace=True)
    df_full.rename(columns={'index':'time'}, inplace=True)
    df_full['filename'] = filename
    df_full['subject'] = filename[0:2]
    df_full['condition'] = filename[3:].replace(".mat","")
    return df_full