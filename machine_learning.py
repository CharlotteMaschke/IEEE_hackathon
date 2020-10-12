"""
Created on Sun Oct 11 21:43:38 2020
@author: Charlotte
"""
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score
from sklearn import svm
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report

from sklearn.neural_network import MLPClassifier

from sklearn.neighbors import NearestNeighbors

from mlxtend.plotting import plot_decision_regions

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

def run_rfc(X_train, y_train, X_test, y_test):
    rfc = RandomForestClassifier(n_estimators=200, min_samples_split=4) # was 200
    rfc.fit(X_train, y_train)
    pred_rfc = rfc.predict(X_test)
    pred_rfc[30:40]
    
    print(classification_report(y_test, pred_rfc))
    print(confusion_matrix(y_test, pred_rfc))
    print(accuracy_score(y_test, pred_rfc))
    
def run_nn(X_train, y_train, X_test, y_test):
    
    mlpc = MLPClassifier(hidden_layer_sizes=(3,3,3), max_iter=1000)
    mlpc.fit(X_train, y_train)
    pred_mlpc = mlpc.predict(X_test)
    print(classification_report(y_test, pred_mlpc))
    print(confusion_matrix(y_test, pred_mlpc))
    from sklearn.metrics import accuracy_score
    cm = accuracy_score(y_test, pred_mlpc)
    print(cm)    