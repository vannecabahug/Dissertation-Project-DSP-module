# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 02:11:12 2020

@author: vanne
"""


import pandas as pd
import numpy as np
import sklearn
from sklearn.decomposition import TruncatedSVD
import warnings
from IPython.display import display
import sys


rec_amount = 20



restaurants = pd.read_csv('TA_restaurants_London.csv', sep=',')


cutdown = restaurants.drop_duplicates(['Name'])

display(cutdown.head(5))

print('\n')


#       MATRIX FACTORIZATION        #

restaurants_matrix = cutdown.pivot_table(index = 'Cuisine Style', columns = 'Name', values = 'Rating').fillna(0)
# place dataset into a matrix and factorize 
display(restaurants_matrix.head())
display(restaurants_matrix.shape)

classifyRatings = restaurants_matrix.values.T
#display(classifyRatings.shape)


SVD = TruncatedSVD(n_components=rec_amount, random_state=0)
# n_components can change how much recomendations are produced, scales result
decomposedM = SVD.fit_transform(classifyRatings)
display(decomposedM.shape)
# attempts to lower results in order to classify best results


warnings.filterwarnings("ignore", category =RuntimeWarning)
coef = np.corrcoef(decomposedM)
display(coef.shape)

print('\n')


#       RECOMMENDATIONS             #

feature = restaurants_matrix.columns
feature_list = list(feature)
recommendMe = input('Please enter a restaurant to generate recommendations\n')
# if recommendMe != restaurants_matrix:
#     print("Restaurant not found")
#     sys.exit()
# else:
bringRating = feature_list.index(recommendMe)
corr_rating = coef[bringRating]
display(list(feature[(corr_rating >= 0.9)]))