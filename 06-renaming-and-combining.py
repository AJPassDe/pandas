# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 17:28:50 2020

Info from:
https://www.kaggle.com/residentmario/renaming-and-combining

@author: AJ
"""


import pandas as pd

reviews = pd.read_csv("input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

# =============================================================================
# Renaming
# =============================================================================

# The first function we'll introduce here is rename(), which lets you change index 
# names and/or column names. For example, to change the points column in our dataset to score, we would do:

reviewsNewScore = reviews.rename(columns={'points': 'score'})

# rename() lets you rename index or column values by specifying a index or column keyword parameter, respectively. 
# It supports a variety of input formats, but usually a Python dictionary is the most convenient.
# Here is an example using it to rename some elements of the index.

reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'})

# You'll probably rename columns very often, but rename index values very rarely. 
# For that, set_index() is usually more convenient.

# Both the row index and the column index can have their own name attribute. 
# The complimentary rename_axis() method may be used to change these names. For example:

reviews.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns')


# =============================================================================
# Combining 
# =============================================================================

# When performing operations on a dataset, we will sometimes need to combine different 
# DataFrames and/or Series in non-trivial ways. Pandas has three core methods for doing this.
# In order of increasing complexity, these are concat(), join(), and merge(). 
# Most of what merge() can do can also be done more simply with join(), so we will omit it and
# focus on the first two functions here.

# The simplest combining method is concat(). 
# Given a list of elements, this function will smush those elements together along an axis.

# This is useful when we have data in different DataFrame or Series objects but having the same fields (columns). 
# One example: the YouTube Videos dataset, which splits the data up based on country of origin 
# (e.g. Canada and the UK, in this example). If we want to study multiple countries simultaneously, 
# we can use concat() to smush them together:

canadian_youtube = pd.read_csv("input/youtube-new/CAvideos.csv")
british_youtube = pd.read_csv("input/youtube-new/GBvideos.csv")

pd.concat([canadian_youtube, british_youtube])


# join() lets you combine different DataFrame objects which have an index in common.
# pull down videos that happened to be trending on the same day in both Canada and the UK:

left = canadian_youtube.set_index(['title', 'trending_date'])
right = british_youtube.set_index(['title', 'trending_date'])

left.join(right, lsuffix='_CAN', rsuffix='_UK')


# =============================================================================
# Exercises
# =============================================================================

# 1. region_1 and region_2 are pretty uninformative names for locale columns in the dataset. 
# Create a copy of reviews with these columns renamed to region and locale, respectively.
renamed = reviews.rename(columns={'region_1':'region', 'region_2':'locale'})

# 2. Set the index name in the dataset to wines.
reindexed = reviews.rename_axis("wines", axis='rows')

# 3. The Things on Reddit dataset includes product links from a selection of top-ranked forums
# ("subreddits") on reddit.com. Run the cell below to load a dataframe of products mentioned on 
# the /r/gaming subreddit and another dataframe for products mentioned on the r//movies subreddit.

gaming_products = pd.read_csv("input/things-on-reddit/top-things/top-things/reddits/g/gaming.csv")
gaming_products['subreddit'] = "r/gaming"
movie_products = pd.read_csv("input/things-on-reddit/top-things/top-things/reddits/m/movies.csv")
movie_products['subreddit'] = "r/movies"

# Create a DataFrame of products mentioned on either subreddit.
combined_products = pd.concat([gaming_products, movie_products])

# 4. The Powerlifting Database dataset on Kaggle includes one CSV table for powerlifting meets and 
# a separate one for powerlifting competitors. Run the cell below to load these datasets into dataframes:

powerlifting_meets = pd.read_csv("input/powerlifting-database/meets.csv") 
powerlifting_competitors = pd.read_csv("input/powerlifting-database/openpowerlifting.csv")

left = powerlifting_meets.set_index('MeetID')
right = powerlifting_competitors.set_index('MeetID')
powerlifting_combined = left.join(right, lsuffix='_meet', rsuffix='_comp')






