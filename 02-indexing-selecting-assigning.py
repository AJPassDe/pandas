# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 13:27:26 2020

@author: AJ
"""
import pandas as pd

reviews = pd.read_csv("input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

# extract a column
reviews.country #pd indexing
reviews['country'] #python dictionary indexing

# extract first row of column 'country'
reviews['country'][0]

# index-based selection: selecting data based on its numerical position in the data. iloc follows this paradigm.
reviews.iloc[0] # select first row

# NOTE
# Both loc and iloc are row-first, column-second. This is the opposite of what we do in native Python, 
# which is column-first, row-second.

# This means that it's marginally easier to retrieve rows, and marginally harder to get retrieve columns. 
# To get a column with iloc, we can do the following:

reviews.iloc[:, 0] # get all values of first column ('country' column)

# first 3 values (0,1,2)
reviews.iloc[:3, 0]
reviews.iloc[[0, 1, 2], 0] # possible to pass a list

reviews.iloc[1:3, 0] # values from 1 to 3 (1, 2)

reviews.iloc[-5:] # five last rows

# The second paradigm for attribute selection is the one followed by the loc operator: label-based selection.
# In this paradigm, it's the data index value, not its position, which matters.

reviews.loc[0, 'country'] # first value from column 'country'

reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']] # values from multiples columns 


#reviews.set_index("title") #manipulating index
# This is useful if you can come up with an index for the dataset which is better than the current one.

reviews.country == 'Italy'

reviews.loc[reviews.country == 'Italy'] # for relevant data, like a sql query
plus90italianWines = reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)]
reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)] # also works or

# Selector isin 
reviews.loc[reviews.country.isin(['Italy', 'France'])] # select wines from italy and france

reviews.loc[reviews.price.notnull()] #to filter wines with no price tag


# assigning data
# reviews['critic'] = 'everyone'

#5. Select the records with index labels 1, 2, 3, 5, and 8, assigning the result to the variable sample_reviews.
sample_reviews = reviews.iloc[[1,2,3,5,8]]

#6. Create a variable df containing the country, province, region_1, and region_2 columns of the records with the
# index labels 0, 1, 10, and 100.
df = reviews.loc[[0,1,10,100], ['country', 'province', 'region_1', 'region_2']]

# 7. Create a variable df containing the country and variety columns of the first 100 records.
df = reviews.loc[0:99, ['country', 'variety']]

# 8. Create a DataFrame italian_wines containing reviews of wines made in Italy. Hint: reviews.country equals what?
italian_wines = reviews.loc[reviews.country.isin(['Italy'])]
italian_wines = reviews.loc[reviews.country == 'Italy' ]

#9. Create a DataFrame top_oceania_wines containing all reviews with at least 95 points (out of 100) 
# for wines from Australia or New Zealand.

top_oceania_wines = reviews.loc[(reviews.points >= 95) & (reviews.country.isin(['Australia', 'New Zealand']))]




