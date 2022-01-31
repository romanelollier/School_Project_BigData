# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 01:36:21 2021

@author: Blue
"""


# library
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly
import plotly.graph_objects as go
import plotly.express as px
import squarify    # pip install squarify (algorithm for treemap)

restaurants_df = pd.read_csv('C:/Users/Blue/Documents/2021-2022 M2 INSFA/Computer Sci for BigData/Projet/TripAdvisor.csv',
                             encoding='utf8', low_memory=False)

restaurants_total = len(restaurants_df)
print(restaurants_total)

restaurants_df.head(5)

# Treemap
squarify.plot(sizes=restaurants_df['country'], label=restaurants_df['avg_rating'], alpha=.8 )
plt.axis('off')
plt.show()












# adding manually the country code - required for the geographical mapping with plotly
#countries_dict = {'Austria': 'AUT', 'Belgium': 'BEL', 'Bulgaria': 'BGR', 'Croatia': 'HRV', 'Czech Republic': 'CZE',
#                  'Denmark': 'DNK', 'England': 'GBR', 'Finland': 'FIN', 'France': 'FRA', 'Germany': 'DEU',
#                  'Greece': 'GRC', 'Hungary': 'HUN', 'Ireland': 'IRL', 'Italy': 'ITA', 'Northern Ireland': 'GBR',
#                  'Poland': 'POL', 'Portugal': 'PRT', 'Romania': 'ROU', 'Scotland': 'GBR', 'Slovakia': 'SVK',
#                  'Spain': 'ESP', 'Sweden': 'SWE', 'The Netherlands': 'NLD', 'Wales': 'GBR'}
#restaurants_df['country_code'] = restaurants_df['country'].map(countries_dict).fillna(restaurants_df['country'])

# average price in euro
#restaurants_df['minimum_range'] = pd.to_numeric(restaurants_df['price_range'].str.split('-').str[0].str.replace('€', '').str.replace(',', ''), errors='coerce')
#restaurants_df['maximum_range'] = pd.to_numeric(restaurants_df['price_range'].str.split('-').str[1].str.replace('€', '').str.replace(',', ''), errors='coerce')
#restaurants_df['avg_price'] = (restaurants_df['minimum_range'] + restaurants_df['maximum_range']) / 2

# drop the fields used for average_price calculation
#restaurants_df.drop(['minimum_range', 'maximum_range'], axis=1, inplace=True)

#restaurants_df.head(5)

