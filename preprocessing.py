# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 21:43:38 2020

@author: Prinzessin
"""

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
from sklearn.utils import shuffle
from sklearn import preprocessing
import numpy as np
from sklearn.model_selection import train_test_split

#preprocessing = __import__("preprocessing")

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
    
def plot_data(trig, X, filename, trig_value=2):
    plt.plot(X)
    plt.vlines(np.where(trig == trig_value)[0], -150, 150, colors='lightgrey')
    plt.title(filename[:-4] + ' with target ' + str(trig_value) +  ' in grey')
    plt.xlabel('time')
    plt.ylabel('electrical activity')
    plt.show()


def average_Nms(trig,data,start,duration):
    tar = np.empty((duration-start,8,len(np.where(trig == 2)[0])))
    non = np.empty((duration-start,8,len(np.where(trig == 1)[0])))
    trig = np.array(trig)

    n = 0
    t = 0

    for i in range(len(trig)-duration):
        if trig[i][0] == 2:
            tar[:,:,t] = data.iloc[i+start:i+duration,:]
            t += 1
        if trig[i][0] == 1:
            non[:,:,n] = data.iloc[i+start:i+duration,:]
            n += 1

    target_values = np.mean(tar[:,:,:],axis=0)
    nontar_values = np.mean(non[:,:,:],axis=0)

    X = np.transpose(np.column_stack((target_values,nontar_values)))
    Y = np.concatenate((np.ones(target_values.shape[1]),np.zeros(nontar_values.shape[1])))

    X, Y = shuffle(X, Y, random_state=0)

    return X,Y

def scale_data(data):
    data_scaled = preprocessing.scale(data)
    return data


def clip_big_amp_values(trig, X):
    series = (X >= -100) & (X <= 100)
    
    new_trig = trig[series.all(1)]
    new_x = X[series.all(1)]
    
    new_trig = new_trig.reset_index(drop=True)
    new_x = new_x.reset_index(drop=True)
    
    return new_trig, new_x


def traintest_split(X_train,Y_train,X_test,Y_test):

    X = np.row_stack((X_train,X_test))
    Y = np.concatenate((Y_train,Y_test))

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size = 0.2, random_state = 42)

    return X_train, Y_train, X_test, Y_test


