"""
Created on Sun Oct 11 21:43:38 2020
@author: Charlotte
"""
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import cross_val_score

def binarize_label(trig):
    label = np.zeros(len(trig))
    label[np.where(trig==2)[0]] = 2
    return label

def run_LDA_cv (X, trig):
    label = binarize_label(trig)
    clf = LinearDiscriminantAnalysis()
    scores = cross_val_score(clf, X, label, cv=10)
    print("LDA Accuracy: %0.2f (+/- %0.2f)" % (scores.mean()*100, scores.std() * 2))
    return scores

