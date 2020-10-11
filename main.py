# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 21:43:28 2020

@author: Prinzessin
"""

# own modules
from load_data import *
from preprocessing import *
from machine_learning import *
from os import listdir
import matplotlib.pyplot as plt

def main():

    filenames = listdir("data")

    filename = filenames[4]
    dataP1h2 = load_dataset(filename)
    
    # start with data from a single dataset
    trig = pd.DataFrame(dataP1h2['trig'])
    X = pd.DataFrame(dataP1h2['y'])
    
<<<<<<< Updated upstream
    # call or not call
    #analyse_data(trig, y) 
    plot_data(trig, y, 0)
    plot_data(trig, y, 1)
    plot_data(trig, y, 2)
    plot_data(trig, y, -1)
=======
    analyse_data(trig, X) # call or not call
    plot_data(trig, X, filename) # call or not call

    scores_LDA = run_LDA_cv(X,trig)

>>>>>>> Stashed changes

main()