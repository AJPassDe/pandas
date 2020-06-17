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
# #Sorting
# =============================================================================
# default to ascending sort
countries_reviewed = countries_reviewed.reset_index()
countries_reviewed.sort_values(by='len') 
countries_reviewed.sort_values(by='len', ascending=False) # descending sort

countries_reviewed.sort_index()

countries_reviewed.sort_values(by=['country', 'len']) #sort by more than one column

best_rating_per_price = reviews.groupby('price').points.max()
