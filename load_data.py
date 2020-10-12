import scipy.io
import numpy as np
import pandas as pd

"""
 load Data
 - P1 = paradigm 1
 - P2 = paradigm 2
 - high / low accuracy
"""

load_data = __import__("load_data")

def load_dataset(filename):
    data = scipy.io.loadmat("data/"+filename)
    trig = pd.DataFrame(data['trig'])
    X = pd.DataFrame(data['y'])

    return trig, X





    
