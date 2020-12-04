# ## About & Creators
# -   Jakub Pilachowski s17999
# -   Michał Ptok s16665

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import math

class StudentEvaluation:
    """
    Class that uses fuzzy logic - will help you rate your next coop partner

    Attributes:
    memes_count (Antecedent)
        represent amount of memes sent to you by your coop candidate
    last_coop_score (Antacedent)
        represents score of last coop project of your coop candidate
    available_time_for_project (Antacedent)
        represents time (in hours) that your coop candidate can dedicate to studying
    final_grade (Consequent)
        represents final rating based on entered data of your coop candidate
    """
    def __init__(self):
        """
        Initialize class - init fuzzy objects, membership, rules and simulator
        """
        self.__set_objects()
        self.__set_membership_functions()
        self.__set_rules()
        self.__simulator = ctrl.ControlSystemSimulation(self.system)

    def __set_objects(self):
        """
        Prepares objects and sets their range
        """
        self.memes_count = ctrl.Antecedent(np.arange(0, 21, 1), 'Memes count sent in a week')
        self.last_coop_score = ctrl.Antecedent(np.arange(0, 101, 1), 'Last coop score')
        self.available_time_for_project = ctrl.Antecedent(np.arange(0, 41, 1), 'Hours a week')

        self.final_grade = ctrl.Consequent(np.arange(0, 101, 1), '5-star rating')

    def __set_membership_functions(self):
        """
        Prepares and divides ranges to sections
        """
        self.memes_count['A1'] = fuzz.trimf(self.memes_count.universe, [0, 0, 10])
        self.memes_count['A3'] = fuzz.trimf(self.memes_count.universe, [0, 10, 20])
        self.memes_count['A2'] = fuzz.trimf(self.memes_count.universe, [10, 20, 20])

        self.last_coop_score['B1'] = fuzz.trimf(self.last_coop_score.universe, [0, 0, 50])
        self.last_coop_score['B2'] = fuzz.trimf(self.last_coop_score.universe, [0, 50, 100])
        self.last_coop_score['B3'] = fuzz.trimf(self.last_coop_score.universe, [50, 100, 100])

        self.available_time_for_project['C1'] = fuzz.trimf(self.available_time_for_project.universe, [0, 0, 20])
        self.available_time_for_project['C2'] = fuzz.trimf(self.available_time_for_project.universe, [0, 20, 40])
        self.available_time_for_project['C3'] = fuzz.trimf(self.available_time_for_project.universe, [20, 40, 40])

        self.final_grade['one_star'] = fuzz.trimf(self.final_grade.universe, [0, 0, 20])
        self.final_grade['two_stars'] = fuzz.trimf(self.final_grade.universe, [0, 20, 40])
        self.final_grade['three_stars'] = fuzz.trimf(self.final_grade.universe, [20, 40, 60])
        self.final_grade['four_stars'] = fuzz.trimf(self.final_grade.universe, [40, 60, 80])
        self.final_grade['five_stars'] = fuzz.trimf(self.final_grade.universe, [80, 100, 100])


    def __set_rules(self):
        """
        Prepares sets of rules that fuzzy logic will use to calculate and match to the result object
        """
        self.rules = []

        rule1 = ctrl.Rule(antecedent=(
            (self.memes_count['A1'] & self.last_coop_score['B1'] & self.available_time_for_project['C1']) |
            (self.memes_count['A2'] & self.last_coop_score['B1'] & self.available_time_for_project['C1'])
            ),
            consequent=self.final_grade['one_star'])
        self.rules.append(rule1)

        rule2 = ctrl.Rule(antecedent=(
            (self.memes_count['A1'] & self.last_coop_score['B1'] & self.available_time_for_project['C2']) |
            (self.memes_count['A1'] & self.last_coop_score['B2'] & self.available_time_for_project['C1']) |
            (self.memes_count['A2'] & self.last_coop_score['B1'] & self.available_time_for_project['C2']) |
            (self.memes_count['A2'] & self.last_coop_score['B2'] & self.available_time_for_project['C1'])
        ), consequent=self.final_grade['two_stars'])
        self.rules.append(rule2)

        rule3 = ctrl.Rule(antecedent=(
            (self.memes_count['A1'] & self.last_coop_score['B1'] & self.available_time_for_project['C3']) |
            (self.memes_count['A1'] & self.last_coop_score['B1'] & self.available_time_for_project['C3']) |
            (self.memes_count['A1'] & self.last_coop_score['B3'] & self.available_time_for_project['C1']) |
            (self.memes_count['A2'] & self.last_coop_score['B1'] & self.available_time_for_project['C3']) |
            (self.memes_count['A2'] & self.last_coop_score['B1'] & self.available_time_for_project['C3']) |
            (self.memes_count['A2'] & self.last_coop_score['B3'] & self.available_time_for_project['C1']) |
            (self.memes_count['A3'] & self.last_coop_score['B1'] & self.available_time_for_project['C1']) |
            (self.memes_count['A3'] & self.last_coop_score['B1'] & self.available_time_for_project['C2']) |
            (self.memes_count['A3'] & self.last_coop_score['B2'] & self.available_time_for_project['C1']) |
            (self.memes_count['A3'] & self.last_coop_score['B2'] & self.available_time_for_project['C2'])
        ), consequent=self.final_grade['three_stars'])
        self.rules.append(rule3)

        rule4 = ctrl.Rule(antecedent=(
            (self.memes_count['A3'] & self.last_coop_score['B3'] & self.available_time_for_project['C2']) |
            (self.memes_count['A3'] & self.last_coop_score['B2'] & self.available_time_for_project['C3']) |
            (self.memes_count['A3'] & self.last_coop_score['B3'] & self.available_time_for_project['C1']) |
            (self.memes_count['A3'] & self.last_coop_score['B1'] & self.available_time_for_project['C3']) |
            (self.memes_count['A1'] & self.last_coop_score['B3'] & self.available_time_for_project['C2']) |
            (self.memes_count['A1'] & self.last_coop_score['B2'] & self.available_time_for_project['C3']) |
            (self.memes_count['A1'] & self.last_coop_score['B3'] & self.available_time_for_project['C3']) |
            (self.memes_count['A2'] & self.last_coop_score['B3'] & self.available_time_for_project['C2']) |
            (self.memes_count['A2'] & self.last_coop_score['B2'] & self.available_time_for_project['C3']) |
            (self.memes_count['A2'] & self.last_coop_score['B3'] & self.available_time_for_project['C3'])
            ), consequent=self.final_grade['four_stars'])
        self.rules.append(rule4)

        rule5 = ctrl.Rule(antecedent=(
            (self.memes_count['A3'] & self.last_coop_score['B3'] & self.available_time_for_project['C3'])),
            consequent=self.final_grade['five_stars'])
        self.rules.append(rule5)

        self.system = ctrl.ControlSystem(self.rules)

    def simulate(self, memes_count, last_coop_score, available_time_for_project):
        """
        Calculates rating based on the entered parameters.

        Parameters:
        memes_count (int)
            amout of memes sent to you by your coop candidate
        last_coop_score (int)
            score of last coop project of your coop candidate
        available_time_for_project (int)
            hours a week that your coop candidate can dedicate to studying
        """
        self.__simulator.input['Memes count sent in a week'] = memes_count
        self.__simulator.input['Last coop score'] = last_coop_score
        self.__simulator.input['Hours a week'] = available_time_for_project
        self.__simulator.compute()

    def get_output(self):
        """
        Returns the rating of your coop candidate.

        Returns:
        final_grade in percents (int)
        """
        return self.__simulator.output['5-star rating']

if __name__ == "__main__":
    studentEvaluation = StudentEvaluation()

    memes_count = int(input("Enter memes amount that coop candidate sent you in last week (0-20): "))
    last_coop_score = int(input("Enter the score that coop candidate got from last coop project (in %): "))
    available_time_for_project = int(input("Enter how much time does coop canidate have for this project (0-40 hours a week): "))

    studentEvaluation.simulate(memes_count, last_coop_score, available_time_for_project)
    score = math.floor(studentEvaluation.get_output())

    print("Your candidate will help you in ", score, "% if you coop!", sep="")
