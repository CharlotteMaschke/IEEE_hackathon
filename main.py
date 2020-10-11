# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 21:43:28 2020

@author: Prinzessin
"""

# own modules
from load_data import *
from preprocessing import *
from os import listdir

def main():

    filenames = listdir("data")
    dataP1h2 = load_dataset(filenames[0])
    
    # start with data from a single dataset
    trig = pd.DataFrame(dataP1h2['trig'])
    y = pd.DataFrame(dataP1h2['y'])
    
    analyse_data(trig, y) # call or not call
    plot_data(trig, y) # call or not call

    
    
main()