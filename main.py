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

    #filenames = listdir("data")
    #filename = filenames[1]
    trig_train, data_train = load_dataset('P1_high1.mat')
    trig_test, data_test = load_dataset('P1_high2.mat')

    # call or not call
    #analyse_data(trig_train, X_train)
    #plot_data(trig_train, X_train, 'train')
    #plot_data(trig_test, X_test, 'test')

    X_train,Y_train = average_Nms(trig_train,data_train,-50,150)
    X_test, Y_test = average_Nms(trig_test,data_test,-50,150)

    X_train, Y_train, X_test, Y_test = traintest_split(X_train, Y_train, X_test, Y_test)

    #X_train = scale_data(X_train)
    #X_test = scale_data(X_test)

    #scores_LDA = run_LDA_cv(X_train,Y_train,X_test,Y_test)
    #scores_LDA = run_LDA(X_train,Y_train,X_test,Y_test)
    scores_SVM = run_SVM(X_train,Y_train,X_test,Y_test)
    #scores_GNB = run_GNB(X_train,Y_train,X_test,Y_test)

main()