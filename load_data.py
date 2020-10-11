import scipy.io
import numpy as np
import pandas as pd

"""
 load Data
 - P1 = paradigm 1
 - P2 = paradigm 2
 - high / low accuracy
"""

dataP1h2 = scipy.io.loadmat('data/P1_high2.mat')
#dataP1l1 = scipy.io.loadmat('data/P1_low1.mat')
#dataP1l2 = scipy.io.loadmat('data/P1_low2.mat')

#dataP2h1 = scipy.io.loadmat('data/P2_high1.mat')
#dataP2h2 = scipy.io.loadmat('data/P2_high2.mat')
#dataP2l2 = scipy.io.loadmat('data/P2_low2.mat')


# start with data from a single dataset
trig = pd.DataFrame(dataP1h2['trig'])
y = pd.DataFrame(dataP1h2['y'])

def analyse_data(trig, y):
    ''' can be moved to other file '''
    # get head
    print('******* TRIG HEAD *******')
    print(trig.head())
    print('******* Y HEAD *******')
    print(y.head())
    
    # get info
    print('******* TRIG INFO *******')
    print(trig.info())
    print('******* Y INFO *******')
    print(y.info())
    
    # describe
    print('******* TRIG DESCRIBE *******')
    print(trig.describe())
    print('******* Y DESCRIBE *******')
    print(y.describe())
    
    print('******* TRIG VALUES (0, 1, 2, -1 *******')
    print(trig[0].value_counts())
    
analyse_data(trig, y) # call or not call