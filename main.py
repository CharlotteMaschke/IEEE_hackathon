# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 21:43:28 2020

@author: Prinzessin
"""

# own modules
from load_data import *
from preprocessing import *
from machine_learning import *

# other modules
from os import listdir
import matplotlib.pyplot as plt

def main():

    filenames = listdir("data")

    filename = filenames[1]
    data = load_dataset(filename)
    
    # start with data from a single dataset
    trig = pd.DataFrame(data['trig'])
    X = pd.DataFrame(data['y'])
    
    trig, X = clip_big_amp_values(trig, X)
    
    # call or not call
    analyse_data(trig, X)
    plot_data(trig, X, filename)
    #plot_data(trig, X, filename, 0)
    #plot_data(trig, X, filename, 1)
    #plot_data(trig, X, filename, 2)
    #plot_data(trig, X, filename, -1)

    plot_data(trig, X, filename) # call or not call

    scores_LDA = run_LDA_cv(X,trig)


main()