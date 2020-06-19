# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 11:37:09 2020

Info from:
https://www.kaggle.com/residentmario/data-types-and-missing-values

@author: AJ
"""

import pandas as pd

reviews = pd.read_csv("input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

# =============================================================================
# Data types
# =============================================================================

# grab type of specific column
reviews.price.dtype

# returns dtype of every column
reviews.dtypes

# convert column poiints from int64 to float 64
reviews.points.astype('float64')

# index has its own datatype
reviews.index.dtype

# =============================================================================
# Missing Data
# =============================================================================

# entries missing values are given value NaN = "Not a Number". NaN are always float64 dtype.

# to select Nan data use pd.isnull() or pd.notnull otherwise.
countryNull = reviews[pd.isnull(reviews.country)]

# replacing missing values is common operation. Handy method: fillna(). Replace each "NaN" with "Unknown".
reviews.region_2.fillna("Unknown")

# Backfill strategy:  fill each missing value with the first non-null value that appears sometime 
# after the given record in the database

# we may have a non-null value that we would like to replace. For example, suppose that since this
# dataset was published, reviewer Kerin O'Keefe has changed her Twitter handle from 
# @kerinokeefe to @kerino. One way to reflect this in the dataset is using the replace() method:

reviews.taster_twitter_handle.replace("@kerinokeefe", "@kerino")

# The replace() method is worth mentioning here because it's handy for replacing missing data which is given 
# some kind of sentinel value in the dataset: things like "Unknown", "Undisclosed", "Invalid", and so on.

# 2. Create a Series from entries in the points column, but convert the entries to strings. 
# Hint: strings are str in native Python.
point_strings = reviews.points.astype('str')

# 3. Sometimes the price column is null. How many reviews in the dataset are missing a price?
missing_price_reviews = reviews[reviews.price.isnull()]
n_missing_prices = len(missing_price_reviews)

# 4. What are the most common wine-producing regions? Create a Series counting the number of times each value
# occurs in the region_1 field. This field is often missing data, so replace missing values with Unknown. 
# Sort in descending order. Your output should look something like this:

reviews_per_region = reviews.region_1.fillna("Unknown").value_counts().sort_values(ascending=False)
