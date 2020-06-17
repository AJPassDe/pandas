# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 12:14:36 2020

@author: AJ
"""

import pandas as pd


# yes & no are column names 
# values are a list of entries  
simpleTable = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})

# 2 versions, same table
fruits = pd.DataFrame({'Apples': [30], 'Bananas':[21]})
fruits = pd.DataFrame([[30, 21]], columns=['Apples', 'Bananas'])

# index: row labels list
tableWColumns = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])


# single column of a dataFrame, has one overall name
productA = pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')

# Reading data files
# .csv: comma separated values
wine_reviews = pd.read_csv("input/wine-reviews/winemag-data-130k-v2.csv")

# .shape: check how large the resulting dataframe is
wine_reviews.shape # (129971, 14)

#To grab first 5 rows
head = wine_reviews.head()

# =============================================================================
# Flour     4 cups
# Milk       1 cup
# Eggs     2 large
# Spam       1 can
# Name: Dinner, dtype: object
# =============================================================================


quantities = ['4 cups', "1 cup", "2 large", "1 can"]
items = ["Flour", "Milk", "Eggs", "Spam"]

ingredients = pd.Series(quantities, index=items, name='Dinner')


#create animals dataframe
animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])

#save dataframe to csv file
animals.to_csv("cows_and_goats.csv")

# index_col to assign column with increasing integers as index
reviews = pd.read_csv("../input/wine-reviews/winemag-data_first150k.csv", index_col=0)

