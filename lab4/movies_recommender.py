# # MovieAndTVShowRecommender

# ## Instalation

# 1. Install Python (recommended min. 3.9)
# 2. Install libs:

# ```text
# pip3 install numpy
# ```

# or

# ```text
# pip install numpy
# ```

# ## Run

# ```text
# python3 movies_recommender.py
# ```

# or

# ```text
# python movies_recommender.py
# ```

# ## Description

# Program computes provided data (person->movie/tv-show:rating) and helps you find 7 movies / tv shows that you will like and points another 7 that you should avoid.

# ## About & Creators

# - Jakub Pilachowski s17999
# - Michał Ptok s16665

# **_hehe_**

import argparse
import json
import numpy as np

class MovieAndTVShowRecommender:
    """
    Class that helps you find 7 new movies / tv shows that you will like
    and points another 7 that you should avoid.
    """
    def __init__(self, score_type):
        """
        Initialize class
        """
        self.score_type = score_type

    def euclidean_score(self, dataset, user1, user2):
        """
        Uses Euclidean algorythm to compute distance between users

        Parameters:
        dataset (dictionary)
            json with set of movies/tv shows and their rating grouped by viewers
        user1 (string)
            name of user for whom we are looking for matches
        user2 (string)
            name of user in whose data we are looking for matches

        Returns:
        level of matching in range from 0 to 1 (float)
        """

        common_movies = {} 

        for item in dataset[user1]:
            if item in dataset[user2]:
                common_movies[item] = 1

        if len(common_movies) == 0:
            return 0

        squared_diff = [] 

        for item in dataset[user1]:
            if item in dataset[user2]:
                squared_diff.append(np.square(dataset[user1][item] - dataset[user2][item]))

        return 1 / (1 + np.sqrt(np.sum(squared_diff))) 

    def pearson_score(self, dataset, user1, user2):
        """
        Uses Pearson correlation coefficient to compute score between users

        Parameters:
        dataset (dictionary)
            json with set of movies/tv shows and their rating grouped in objects by viewer
        user1 (string)
            name of user for whom we are looking for matches
        user2 (string)
            name of user in whose data we are looking for matches

        Returns:
            level of matching in number (float)
        """

        common_movies = {}

        for item in dataset[user1]:
            if item in dataset[user2]:
                common_movies[item] = 1

        num_ratings = len(common_movies) 

        if num_ratings == 0:
            return 0

        user1_sum = np.sum([dataset[user1][item] for item in common_movies])
        user2_sum = np.sum([dataset[user2][item] for item in common_movies])

        user1_squared_sum = np.sum([np.square(dataset[user1][item]) for item in common_movies])
        user2_squared_sum = np.sum([np.square(dataset[user2][item]) for item in common_movies])

        sum_of_products = np.sum([dataset[user1][item] * dataset[user2][item] for item in common_movies])

        Sxy = sum_of_products - (user1_sum * user2_sum / num_ratings)
        Sxx = user1_squared_sum - np.square(user1_sum) / num_ratings
        Syy = user2_squared_sum - np.square(user2_sum) / num_ratings
        
        if Sxx * Syy == 0:
            return 0

        return Sxy / np.sqrt(Sxx * Syy)

    def compute(self, dataset, user1, user2):
        """
        Chooses computing method based on score_type and passes parameters to computing methods

        Parameters:
        dataset (dictionary)
            json with set of movies/tv shows and their rating grouped in objects by viewer
        user1 (string)
            name of user for whom we are looking for matches
        user2 (string)
            name of user in whose data we are looking for matches

        Returns:
            level of matching in number (float)
        """

        if self.score_type == "Euclidean":
            return self.euclidean_score(dataset, user1, user2)
        elif self.score_type == "Pearson":
            return self.pearson_score(dataset, user1, user2)
        else:
            raise TypeError('Score Type ' + self.score_type + ' does not exists!')
        
    def take_positive_movies(self, dataset, user, filtered_list):
        """
            Taking movies from user with positive scores
            
            Parameters:
            dataset (dictionary)
                json with set of movies/tv shows and their rating grouped in objects by viewer
            user (string)
                user of user who we take scores for
            filtered list(list) 
                list of movies without comparing user movies

            Returns:
                list of movies with scores ((str, float))
        """
        positive_movies = []

        for item in filtered_list:
            if dataset[user][item] >= 8:
                positive_movies.append((item, dataset[user][item]))

        positive_movies.sort(key=takeSecond, reverse=True)

        return positive_movies

    def take_negative_movies(self, dataset, user, filtered_list):
        """
            Taking movies from user with negative scores
            
            Parameters:
            dataset (dictionary)
                json with set of movies/tv shows and their rating grouped in objects by viewer
            user (string)
                user of user who we take scores for
            filtered list(list) 
                list of movies without comparing user movies

            Returns:
                list of movies with scores ((str, float))
        """

        negative_movies = []

        for item in filtered_list:
            if dataset[user][item] < 6:
                negative_movies.append((item, dataset[user][item]))

        negative_movies.sort(key=takeSecond)

        return negative_movies

    
    def recommend_positive_negative_movies(self, data, input_user):
        """
            Recommends on output positive and negative movies by most matched users 
            
            Parameters:
            dataset (dictionary)
                json with set of movies/tv shows and their rating grouped in objects by viewer
            input_user (string)
                name of user for whom we are looking for matches

        """
        user_scores = []
        positive_movies = []
        negative_movies = []
        for user in [x for x in data if x != input_user]:
            user_score = recommender.compute(data, input_user, user)

            if user_score <= 0:
                continue

            user_scores.append((user, user_score))

        user_scores.sort(key=takeSecond, reverse=True)
        
        for x, item in enumerate(user_scores):
            user = item[0]

            filtered_list = [x for x in data[user] if x not in \
                    data[input_user] or data[input_user][x] == 0]

            for movie in self.take_positive_movies(data, user, filtered_list):
                if len(positive_movies) == 7:
                    break

                positive_movies.append(movie[0])
            
            for movie in self.take_negative_movies(data, user, filtered_list):
                if len(negative_movies) == 7:
                    break

                negative_movies.append(movie[0])
        
            if len(positive_movies) == 7 and len(negative_movies) == 7:
                break
        

        print("Recommended movies or tv shows: ")
        for index, movie in enumerate(positive_movies):
            print(str(index+1) + " " + movie)

        print("You better stay away from them: ")
        for index, movie in enumerate(negative_movies):
            print(str(index+1) + " " + movie)


def takeSecond(elem):
    """
        Compare method to sort list by second parameter in object

        Parameters:
            element comparing (object)
        
        Returns: 
            second property of element (float)
    """
    return elem[1]

if __name__=='__main__':
    recommender = MovieAndTVShowRecommender("Pearson")
    ratings_file = 'ratings.json'

    with open(ratings_file, 'r') as f:
        data = json.loads(f.read())

    input_user = str(input())
    
    recommender.recommend_positive_negative_movies(data, input_user)
