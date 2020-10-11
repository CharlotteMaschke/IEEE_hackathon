# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 21:43:38 2020

@author: Prinzessin
"""

import matplotlib.pyplot as plt
import numpy as np

preprocessing = __import__("preprocessing")

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

def plot_data(trig,y):
    plt.plot(y)
    plt.vlines(np.where(trig == 2)[0], -600, 600, colors='lightgrey')
    plt.title('dataP1h2 with target +2 in grey')
    plt.xlabel('time')
    plt.ylabel('electrical activity')
    plt.show()