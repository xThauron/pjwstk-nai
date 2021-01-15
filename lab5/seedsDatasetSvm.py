# # SeedsDatasetSvm & CongressionalVotingDatasetSvm

# ## Instalation

# 1. Install Python (recommended min. 3.9)
# 2. Install libs:

# ```text
# pip3 install numpy
# pip3 install sklearn
# ```

# or

# ```text
# pip install numpy
# pip install sklearn
# ```

# ## Run

# ```text
# python3 svm.py
# ```

# or

# ```text
# python svm.py
# ```

# ## Description

# Program predicts result based on SVM dataset and user input.
# There are two dataset that program can works with:
# [Wheat Seeds Dataset](https://machinelearningmastery.com/standard-machine-learning-datasets/) & [Congressional Voting Dataset](https://www.mldata.io/dataset-details/congressional_voting/).

# ## Creators

# - Jakub Pilachowski s17999
# - Michał Ptok s16665

import numpy as np
import csv
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import OneHotEncoder

class SeedsDatasetSvm:
    def __init__(self):
        """
        Initialize class and svclassifier with linear kernel.
        """
        self.svclassifier = SVC(kernel='linear')

    def getInput(self):
        """
        Gets inputs from user and saves its to the respective variables
        that are collected in array.
        """
        area = float(input("Enter area: "))
        perimeter = float(input("Enter perimeter: "))
        compactness = float(input("Enter compactness: "))
        length_of_kernel = float(input("Enter length of kernel: "))
        width_of_kernel = float(input("Enter width of kernel: "))
        asymmetry_coefficient = float(input("Enter asymmetry coefficient: "))
        length_of_kernel_groove = float(input("Enter length of kernel groove: "))

        self.inputData = np.array([area, perimeter, compactness, length_of_kernel, width_of_kernel, asymmetry_coefficient, length_of_kernel_groove])

    def trainAndCalculate(self):
        """
        Takes dataset from file and prepares before
        passing them to the fit method to train algorithm
        """
        f = open("seeds_dataset.txt")
        data = np.genfromtxt(fname = f, dtype=float, encoding=None)
        X = data[:, :-1]
        y = data[:, -1]
        y = y.astype(int)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)
        self.svclassifier.fit(X_train, y_train)

    def getPredictedResult(self):
        """
        Prepares classified output based on inputData before printing.

        Returns
        (int) first value of output array
        """
        output = self.svclassifier.predict([self.inputData])
        return output[0]