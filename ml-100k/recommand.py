# coding=utf-8
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

ml_100k = 'ml-100k/'
# reading users file
u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
users = pd.read_csv(ml_100k + 'u.user', sep='|', names=u_cols, encoding='latin-1')

# reding ratins file
r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings = pd.read_csv(ml_100k + 'u.data', sep='\t', names=r_cols, encoding='latin-1')

# reading items file
i_cols = ['movie id', 'movie title' ,'release date','video release date', 'IMDb URL', 'unknown', 'Action', 'Adventure',
'Animation', 'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy',
'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
items = pd.read_csv(ml_100k + 'u.item', sep='|', names=i_cols, encoding='latin-1')

r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings_train = pd.read_csv(ml_100k + 'ua.base', sep='\t', names=r_cols, encoding='latin-1')
ratings_test = pd.read_csv(ml_100k + 'ua.test', sep='\t', names=r_cols, encoding='latin-1')