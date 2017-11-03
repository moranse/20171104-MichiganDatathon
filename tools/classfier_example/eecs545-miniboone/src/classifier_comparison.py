#!/usr/bin/python
# -*- coding: utf-8 -*-

# Code source: Gaël Varoquaux
#              Andreas Müller
# Modified for documentation by Jaques Grobler
# Modified for MiniBooNE by Bradley Dice
# License: BSD 3 clause

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

from train_test import get_train_test
from datetime import datetime

names = ["Nearest Neighbors",
         "Linear SVM",
         "RBF SVM",
         "Gaussian Process",
         "Decision Tree",
         "Random Forest",
         "Neural Net",
         "AdaBoost",
         "Naive Bayes",
         "QDA"]

classifiers = [
    KNeighborsClassifier(3),
    SVC(kernel="linear", C=0.025),
    SVC(gamma=2, C=1),
    GaussianProcessClassifier(1.0 * RBF(1.0), warm_start=True),
    DecisionTreeClassifier(max_depth=5),
    RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
    MLPClassifier(alpha=1),
    AdaBoostClassifier(),
    GaussianNB(),
    QuadraticDiscriminantAnalysis()]

X_train, X_test, y_train, y_test = get_train_test()

# iterate over classifiers
for i, name, clf in zip(range(len(names)), names, classifiers):
    if i in [1, 2, 3]:
        # Skip SVM and Gaussian Process since they take forever
        continue
    print('{}:'.format(name))
    start=datetime.now().timestamp()
    clf.fit(X_train, y_train)
    print('\tTraining took {:.4f} seconds.'.format(
        datetime.now().timestamp() - start))
    start = datetime.now().timestamp()
    score = clf.score(X_test, y_test)
    print('\tTesting took {:.4f} seconds.'.format(
        datetime.now().timestamp() - start))
    print('\tScore: {:.4f}'.format(score))
