# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 21:43:28 2020

@author: Prinzessin
"""

# own modules
from load_data import *
from preprocessing import *

def main():
    
    dataP1h2 = load_dataset()
    
    # start with data from a single dataset
    trig = pd.DataFrame(dataP1h2['trig'])
    y = pd.DataFrame(dataP1h2['y'])
    
    # call or not call
    #analyse_data(trig, y) 
    plot_data(trig, y, 0)
    plot_data(trig, y, 1)
    plot_data(trig, y, 2)
    plot_data(trig, y, -1)

    
    
main()