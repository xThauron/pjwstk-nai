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
from congressionalVotingDatasetSvm import CongressionalVotingDatasetSvm
from seedsDatasetSvm import SeedsDatasetSvm


if __name__ == "__main__":
    """
    Lets user decide which model to run and prints predicted data
    based on choosen SVM model and user input.
    """
    option = int(input("What SVM model would you like to run (0 - seedsDatasetSvm, 1 - congressionalVotingDatasetSvm: "))
    if option == 0:
        seed_svm = SeedsDatasetSvm()
        seed_svm.getInput()
        seed_svm.trainAndCalculate()
        output = seed_svm.getPredictedResult()
    else:
        congress_vote_svm = CongressionalVotingDatasetSvm()
        congress_vote_svm.getInput()
        congress_vote_svm.trainAndCalculate()
        output = congress_vote_svm.getPredictedResult()

    print("Result: ", output)
