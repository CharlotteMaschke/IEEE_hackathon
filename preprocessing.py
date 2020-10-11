# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 21:43:38 2020

@author: Prinzessin
"""

import matplotlib.pyplot as plt
import matplotlib
import numpy as np


preprocessing = __import__("preprocessing")

def analyse_data(trig, X):
    ''' can be moved to other file '''
    # get head
    print('******* TRIG HEAD *******')
    print(trig.head())
    print('******* Y HEAD *******')
    print(X.head())
    
    # get info
    print('******* TRIG INFO *******')
    print(trig.info())
    print('******* Y INFO *******')
    print(X.info())
    
    # describe
    print('******* TRIG DESCRIBE *******')
    print(trig.describe())
    print('******* Y DESCRIBE *******')
    print(X.describe())
    
    # values available in "trig"
    print('******* TRIG VALUES (0, 1, 2, -1) *******')
    print(trig[0].value_counts())

def plot_data(trig,y,trig_value=2):
    plt.plot(y)
    plt.vlines(np.where(trig == trig_value)[0], -600, 600, colors='lightgrey')
    plt_title = 'dataP1h2 with target ' + str(trig_value) +  ' in grey'
    plt.title(plt_title)

def plot_data(trig,X, filename):
    plt.plot(X)
    plt.vlines(np.where(trig == 2)[0], -600, 600, colors='lightgrey')
    plt.title(filename + 'with target +2 in grey')
    plt.xlabel('time')
    plt.ylabel('electrical activity')
    plt.show()
