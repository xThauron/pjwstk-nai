import numpy as np
import csv
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import OneHotEncoder

def convertToFloat(vote):
    if vote == 'y':
        return 1
    if vote == 'n':
        return -1
    if vote == '?':
        return 0

class CongressionalVotingDatasetSvn:
    def __init__(self):
        self.svclassifier = SVC(kernel='linear')
    
    def getInput(self):
        print('You will be asked to vote on 16 subjects refered by titles.')
        handicapped_infants = convertToFloat(str(input('Handicapped infants protection act  - Vote by typing "y" or "n" or "?": ')))
        water_project_cost_sharing = convertToFloat(str(input('Water_project_cost_sharing  - Vote by typing "y" or "n" or "?": ')))
        adoption_of_the_budget_resolution = convertToFloat(str(input('Adoption of the budget resolution - Vote by typing "y" or "n" or "?": ')))
        physician_fee_freeze = convertToFloat(str(input('Physician fee freeze - Vote by typing "y" or "n" or "?": ')))
        el_salvador_aid = convertToFloat(str(input('El salvador aid - Vote by typing "y" or "n" or "?": ')))
        religious_groups_in_schools = convertToFloat(str(input('Religious groups in schools - Vote by typing "y" or "n" or "?": ')))
        anti_satellite_test_ban = convertToFloat(str(input('Anti satellite test ban - Vote by typing "y" or "n" or "?": ')))
        aid_to_nicaraguan_contras = convertToFloat(str(input('Aid to nicaraguan contras - Vote by typing "y" or "n" or "?": ')))
        mx_missile = convertToFloat(str(input('Mx missile - Vote by typing "y" or "n" or "?": ')))
        immigration = convertToFloat(str(input('Immigration - Vote by typing "y" or "n" or "?": ')))
        synfuels_corporation_cutback = convertToFloat(str(input('Synfuels corporation cutback - Vote by typing "y" or "n" or "?": ')))
        education_spending = convertToFloat(str(input('Education spending - Vote by typing "y" or "n" or "?": ')))
        superfund_right_to_sue = convertToFloat(str(input('Superfund right to sue - Vote by typing "y" or "n" or "?": ')))
        crime = convertToFloat(str(input('Crime - Vote by typing "y" or "n" or "?": ')))
        duty_free_exports = convertToFloat(str(input('Duty free exports - Vote by typing "y" or "n" or "?": ')))
        export_administration_act_south_africa = convertToFloat(str(input('Export administration act south africa - Vote by typing "y" or "n" or "?": ')))

        self.inputData = np.array([handicapped_infants,water_project_cost_sharing,adoption_of_the_budget_resolution,physician_fee_freeze,el_salvador_aid,religious_groups_in_schools,anti_satellite_test_ban,aid_to_nicaraguan_contras,mx_missile,immigration,synfuels_corporation_cutback,education_spending,superfund_right_to_sue,crime,duty_free_exports,export_administration_act_south_africa])
    
    def trainAndCalculate(self):
        f = open("congressional_voting_dataset.csv")
        data = np.genfromtxt(fname = f, delimiter=',', dtype=str, encoding=None)
        X = data[:, :-1]
        y = data[:, -1]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)
        self.svclassifier.fit(X_train, y_train)

    def getPredictedResult(self):
        output = self.svclassifier.predict([self.inputData])
        return output