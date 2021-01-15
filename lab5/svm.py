import numpy as np
import csv
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import OneHotEncoder
from congressionalVotingDatasetSvn import CongressionalVotingDatasetSvn
from seedsDatasetSvn import SeedsDatasetSvn


if __name__ == "__main__":
    option = int(input("What SVN model would you like to run (0-seedsDatasetSvn, 1-congressionalVotingDatasetSvn: "))
    if option == 0:
        seed_svn = SeedsDatasetSvn()
        seed_svn.getInput()
        seed_svn.trainAndCalculate()
        output = seed_svn.getPredictedResult()
    else:
        congress_vote_svn = CongressionalVotingDatasetSvn()
        congress_vote_svn.getInput()
        congress_vote_svn.trainAndCalculate()
        output = congress_vote_svn.getPredictedResult()
    
    print(output)
