"""
Created on Sun Oct 11 21:43:38 2020
@author: Charlotte
"""
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score
from sklearn import svm
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import NearestNeighbors

def plot_confusion_matrix(Y_pred, Y_test):
    sns.heatmap(confusion_matrix(Y_pred, Y_test), annot=True, fmt="d")
    plt.xticks([0.5, 2 - 0.5], ['non-target', 'target'])
    plt.yticks([0.5, 2 - 0.5], ['non-target', 'target'])
    plt.ylabel('Predicted value')
    plt.xlabel('True value')
    plt.show()

def run_LDA_cv(X_train, Y_train, X_test, Y_test):
    clf = LinearDiscriminantAnalysis()
    scores = cross_val_score(clf, X_train, Y_train, cv=10)
    print("LDA Accuracy: %0.2f (+/- %0.2f)" % (scores.mean()*100, scores.std() * 2))
    return scores

def run_LDA (X_train, Y_train, X_test, Y_test):
    clf = LinearDiscriminantAnalysis()
    clf.fit(X_train,Y_train)
    Y_pred = clf.predict(X_test)
    score = accuracy_score(Y_pred, Y_test)
    plot_confusion_matrix(Y_pred, Y_test)
    print("LDA Accuracy: %0.2f" % (score*100) + '%')
    return score


def run_SVM (X_train, Y_train, X_test, Y_test):
    clf = svm.SVC(max_iter=1000000)
    clf.fit(X_train,Y_train)
    Y_pred = clf.predict(X_test)
    score = accuracy_score(Y_pred, Y_test)
    plot_confusion_matrix(Y_pred, Y_test)
    print("SVM Accuracy: %0.2f" % (score*100) + '%')
    return score

