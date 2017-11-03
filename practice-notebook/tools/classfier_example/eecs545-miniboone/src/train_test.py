from sklearn.model_selection import StratifiedShuffleSplit
import numpy as np


def get_train_test(n_splits=1, random_state=42, test_size=0.25, sample_size=1):
    """Loads and shuffles data to create training and test sets.
    n_splits determines how many times the data is re-shuffled and split.
    Note that the splits are random, i.e. not k-fold.
    """

    X = np.load('../data/data.npy')
    y = np.load('../data/labels.npy')
    sss = StratifiedShuffleSplit(
            n_splits=n_splits,
            test_size=test_size,
            random_state=random_state)
    for train_index, test_index in sss.split(X, y):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
        train_sample_length = int(sample_size * len(y_train))
        test_sample_length = int(sample_size * len(y_test))
        return X_train[:train_sample_length], \
               X_test[:test_sample_length], \
               y_train[:train_sample_length], \
               y_test[:test_sample_length]
