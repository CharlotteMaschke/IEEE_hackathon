import scipy.io
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



"""
 load Data
 - P1 = paradigm 1
 - P2 = paradigm 2
 - high / low accuracy
"""
load_data = __import__("load_data")

def plot_functions(trig1, X1):
    trig2 = trig1 # [offset:offset+500]
    X2 = X1 # = X1[offset:offset+500]
    print(" TRIG ---------------------------------")
    print(trig2)
    print(X2)
    print(" TRIG END")
    
    y = pd.Series(np.arange(0,len(X2),1))
    print(y)
    print(X2[2])
    
    f = np.poly1d(np.polyfit(y, X2[2], 3))
    
    # t = np.linspace()
    
    print("Function", f)    
    
    print(min(X2[2]))
    print("hey")
    
    # np.polyfit(y, X2, 10)
    
#    x = np.linspace(0, 1, 20)
 #   y = np.cos(x) + 0.3*np.random.rand(20)
    
    # plt.plot(y, X2[2], 'o', t, p(t), '-')
    plt.plot(y, f(y))
    plt.show()
    

def load_dataset(filename, offset):
    data = scipy.io.loadmat("data/"+filename)
    trig = pd.DataFrame(data['trig'])
    X = pd.DataFrame(data['y'])
    
    return trig, X # trig2, X2[2]





    
