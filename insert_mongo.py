#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 17:09:24 2021

@author: mathisagathe
"""

from pymongo import MongoClient

import pandas as pd

client = MongoClient("10.35.7.4", username = "mathis", password = "MathisM21", authsource = "mathisdb")

db=client.mathisdb

col = db["TripAdvisor"]

datacsv = pd.read_csv("/Users/mathisagathe/tripadvisor.csv")

col.insert_many(datacsv.to_dict('records'))