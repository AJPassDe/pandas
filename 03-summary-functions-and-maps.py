# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 15:27:13 2020

@author: AJ
"""

import pandas as pd

reviews = pd.read_csv("input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

# Summary for numerical data
reviews.points.describe()

# To get specific summary
reviews.points.mean()


# Summary for string data
reviews.taster_name.describe()

# To get all unique tasters
reviews.taster_name.unique()

# To get how often unique values occur in full dataset
reviews.taster_name.value_counts()

# mapping
review_points_mean = reviews.points.mean()
reviews.points.map(lambda p: p - review_points_mean)

# applying
def remean_points(row):
    row.points = row.points - review_points_mean
    return row

reviews.apply(remean_points, axis='columns')

# easier way
review_points_mean = reviews.points.mean()
reviews.points - review_points_mean

# concatenate country and region 
reviews.country + " - " + reviews.region_1

# 5. I'm an economical wine buyer. Which wine is the "best bargain"? Create a 
# variable bargain_wine with the title of the wine with the highest points-to-price ratio in the dataset.
bargain_idx = (reviews.points / reviews.price).idxmax() #index of max value
bargain_wine = reviews.loc[bargain_idx, 'title'] # get the title (name) of the wine with previous index

# 6. There are only so many words you can use when describing a bottle of wine. Is a wine more likely to be 
# "tropical" or "fruity"? Create a Series descriptor_counts counting how many times each of these two words 
# appears in the description column in the dataset.
n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum() #
n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
descriptor_counts = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])


# =============================================================================
# 7. We'd like to host these wine reviews on our website, but a rating system ranging from 80 to 100 points is too hard
# to understand - we'd like to translate them into simple star ratings. A score of 95 or higher counts as 3 stars, 
# a score of at least 85 but less than 95 is 2 stars. Any other score is 1 star.
# 
# Also, the Canadian Vintners Association bought a lot of ads on the site, so any wines from Canada should 
# automatically get 3 stars, regardless of points.
# 
# Create a series star_ratings with the number of stars corresponding to each review in the dataset.
# =============================================================================

def stars(row):
    if row.country == 'Canada':
        return 3
    elif row.points >= 95:
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1

star_ratings = reviews.apply(stars, axis='columns') # apply function stars with parameter columns

