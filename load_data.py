import scipy.io
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics 

from preprocessing import *


"""
 load Data
 - P1 = paradigm 1
 - P2 = paradigm 2
 - high / low accuracy
"""
load_data = __import__("load_data")

def load_dataset(filename, offset):
    data = scipy.io.loadmat("data/"+filename)
    trig = pd.DataFrame(data['trig'])
    X = pd.DataFrame(data['y'])
    
    plot_functions(trig, X)
        
    return trig, X # trig2, X2[2]

def load_dataset_wrong(filename, offset):
    data = scipy.io.loadmat("data/"+filename)
    trig = pd.DataFrame(data['trig'])
    X = pd.DataFrame(data['y'])
    
    print(X[1][4])
    
    print("I don't understand this: ", trig.at[5, 0])
    
    print("Len", len(X))
    
    print("X before")
    print(X)
    
    
    
    print("Mean", statistics.mean(X[1][:500]))
    
    count = 0
    for index in range (0, len(X)):
        if (trig.at[index, 0] == 2):
            for n in range (0, 8):
                    X.loc[index, n] = statistics.mean(X[(index-300):index][n])
                    # X.loc[index,n] - X.loc[index+500,n]
                    # kind of good: 
                    # statistics.mean(X[index:index+500][n])
                    #X.loc[index+500, n] # 
        else:
            for n in range (0, 8):
                    X.loc[index, n] = 0
                    
                # print("count: ", count, " ", X.loc[index, n])
            # count = count + 1
                # X[index][n] = max(X[:500])
              
    print("X after")
    print(X)
        
    return trig, X # trig2, X2[2]

def plot_functions(trig, X):
    
    for index in range (0, len(X)):
        if (trig.at[index, 0] == 2):
            for n in range (0, 8):
                    X.loc[index, n] = statistics.mean(X[(index-300):index][n])
                    X2 = X[index-100:index+700]
                    y = pd.Series(np.arange(index-100, index+700,1))
                    #plt.vlines(index, -500, 500, colors='lightgrey')
                    #plt.plot(y, X2)
                    #plt.legend(('Fz', 'C3', 'Cz', 'C4', 'CP1', 'CPz', 'CP2', 'Pz'),
                    #           loc='upper right')
                    #plt.show()
                    # break
    
    out1, out2 = average_Nms(trig,X,0,700)
    plt.vlines(100, -500, 500, colors='lightgrey')
    y = pd.Series(np.arange(0, 800, 1))
    plt.plot(y, out1)
    plt.legend(('Fz', 'C3', 'Cz', 'C4', 'CP1', 'CPz', 'CP2', 'Pz'),
               loc='upper right')
    plt.show()
    
    
    #0:"Fz", 1:"C3", 2:"Cz", 3:"C4", 4:"CP1", 5:"CPz", 6:"CP2", 7:"Pz"
    
    print(" TRIG ---------------------------------")
    # print(trig2)
    # print(X2)
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
    
