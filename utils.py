"""Useful functions for algorithms"""

import numpy as np
from sklearn.metrics import r2_score

def error(Y_pred, Y):
    """Measures accuracy of a
    regression prediction"""
    error = np.abs(Y_pred - Y) / Y
    r2 = r2_score(Y, Y_pred)
    print("R² score: " + str(r2))
    print(str(round(error.mean(), 2)) + " % experimental error") # Mean experimental error

def add_ones(X):
    """ Adds a column of ones in the beginning of X"""
    return np.concatenate((np.ones(X.shape[0]), X), axis=1)
