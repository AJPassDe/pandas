# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 11:59:24 2020

@author: AJ
"""

import pandas as pd

reviews = pd.read_csv("input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

# =============================================================================
# Grouping
# =============================================================================

# group by points column then count how many have x points 
reviews.groupby('points').points.count()

# cheapest wine in each point value category
reviews.groupby('points').price.min()

# get first wine name of each winery
reviews.groupby('winery').apply(lambda df: df.title.iloc[0])

# pick out the best wine by country and province
reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])

# statistical summary of our dataframe
reviews.groupby(['country']).price.agg([len, min, max])

# Multi indexes
countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])

# multi indexes to regular index
countries_reviewed.reset_index()

# =============================================================================
# Sorting
# =============================================================================
# default to ascending sort
countries_reviewed = countries_reviewed.reset_index()
countries_reviewed.sort_values(by='len') 
countries_reviewed.sort_values(by='len', ascending=False) # descending sort

countries_reviewed.sort_index()

countries_reviewed.sort_values(by=['country', 'len']) #sort by more than one column

# =============================================================================
# Exercises
# =============================================================================

# 1. Who are the most common wine reviewers in the dataset?
reviews_written = reviews.groupby('taster_twitter_handle').taster_twitter_handle.count()

# 2. What is the best wine I can buy for a given amount of money?
best_rating_per_price = reviews.groupby('price').points.max()

# 3. What are the minimum and maximum prices for each variety of wine?
price_extremes = reviews.groupby('variety').price.agg([min, max])
price_extremes

# 4. What are the most expensive wine varieties? Create a variable sorted_varieties containing 
# a copy of the dataframe from the previous question where varieties are sorted in descending order
# based on minimum price, then on maximum price (to break ties).
sorted_varieties = price_extremes.sort_values(by=['min', 'max'], ascending=False) # first soprted by column min then by max

# 5. Create a Series whose index is reviewers and whose values is the average review score given out by that reviewer.
# Hint: you will need the taster_name and points columns.
reviews.groupby('taster_name').points.mean()

# 6. What combination of countries and varieties are most common? Create a Series whose index is a MultiIndexof 
# {country, variety} pairs. For example, a pinot noir produced in the US should map to {"US", "Pinot Noir"}. 
# Sort the values in the Series in descending order based on wine count.

mostCommon = reviews.groupby(['country', 'variety']).size()
country_variety_counts = mostCommon.sort_values(ascending=False)




















