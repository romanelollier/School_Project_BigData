#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 18:11:32 2021

@author: mathisagathe
"""

from pymongo import MongoClient


client = MongoClient("10.35.7.4", username = "mathis", password = "MathisM21", authsource = "mathisdb")

db=client.mathisdb

collection = db["TripAdvisor"]

r1 = {"country":"France"}

nbrestoFR = collection.find((r1)).count()

print("Le nombre total de restaurants en France sur TA est de : ",nbrestoFR)

#Nombre de restaurants en France servant des repas végétariens et sans gluten

r2 = {"$and":
      [
       {"country":"France"},
       {"vegetarian_friendly":"Y"},
       {"gluten_free":"Y"}
       ]
      }

nbr2 = collection.find((r2)).count()

print("Le nombre total de restaurants en France servant des repas végétariens et sans gluten est de : ",nbr2)

#Top 5 des villes européennes avec le plus de restaurants
    
r3 = collection.aggregate([
    {"$group":{"_id":"$city","nb":{"$sum":1}}},
    {"$sort":{"nb":-1}},
    {"$limit":6}
     ])

for i in r3:
    print(i)
    
