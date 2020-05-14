import numpy as np
import pandas as pd

def retrieve_and_split(path):
    """Retrieve and split data
    into train/val/test datasets"""
    size_1 = 0.70
    size_2 = 0.85

    X = pd.read_csv(path).to_numpy()
    Y = pd.read_csv(path).to_numpy()[:, -1]
    
    n = len(X)
    n_1 = int(size_1*n)
    n_2 = int(size_2*n)
    
    r = np.random.permutation(n)

    X_train = X[r[0:n_1], :]
    Y_train = Y[r[0:n_1]]
    X_val = X[r[n_1:n_2], :]
    Y_val = Y[r[n_1:n_2]]
    X_test = X[r[n_2:], :]
    Y_test = Y[r[n_2:]]

    return X_train, Y_train, X_val, Y_val, X_test, Y_test

