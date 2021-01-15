import numpy as np
import csv
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import OneHotEncoder

class SeedsDatasetSvn:
    def __init__(self):
        self.svclassifier = SVC(kernel='linear')
    
    def getInput(self):
        area = float(input("Enter area: "))
        perimeter = float(input("Enter perimeter: "))
        compactness = float(input("Enter compactness: "))
        length_of_kernel = float(input("Enter length of kernel: "))
        width_of_kernel = float(input("Enter width of kernel: "))
        asymmetry_coefficient = float(input("Enter asymmetry coefficient: "))
        length_of_kernel_groove = float(input("Enter length of kernel groove: "))

        self.inputData = np.array([area, perimeter, compactness, length_of_kernel, width_of_kernel, asymmetry_coefficient, length_of_kernel_groove])
    
    def trainAndCalculate(self):
        f = open("seeds_dataset.txt")
        data = np.genfromtxt(fname = f, dtype=float, encoding=None)
        X = data[:, :-1]
        y = data[:, -1]
        y = y.astype(int)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)
        self.svclassifier.fit(X_train, y_train)

    def getPredictedResult(self):
        output = self.svclassifier.predict([self.inputData])
        return output