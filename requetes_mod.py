#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 18:11:32 2021

@author: mathisagathe
"""

from pymongo import MongoClient
import matplotlib.pyplot as plt


client = MongoClient("10.35.7.4", username = "mathis", password = "MathisM21", authsource = "mathisdb")

db=client.mathisdb

collection = db["TripAdvisor"]

r1 = {"country":"France"}

nbrestoFR = collection.find((r1)).count()

print("Le nombre total de restaurants en France sur TA est de : ",nbrestoFR)

#Nombre de restaurants en France servant des repas végétariens

r2 = {"$and":
      [
       {"country":"France"},
       {"vegetarian_friendly":"Y"}
       ]
      }

nbvege = collection.find((r2)).count()

#Nombre de restaurants en France servant des repas gluten free

r3 = {"$and":
      [
       {"country":"France"},
       {"gluten_free":"Y"}
       ]
      }

nbgf = collection.find((r3)).count()

# Graphique : Pourcentage de restaurants Végétariens et sans gluten en France
# https://www.python-graph-gallery.com/pie-plot-matplotlib-basic
# https://www.kaggle.com/stefanoleone992/tripadvisor-european-restaurants-eda

print("Le nombre total de restaurants en France servant des repas végétariens est de : ",nbvege)
print("Le nombre total de restaurants en France servant des repas sans gluten est de : ",nbgf)

#Top 5 des villes européennes avec le plus de restaurants
    
r3 = collection.aggregate([
    {"$group":{"_id":"$city","nb":{"$sum":1}}},
    {"$sort":{"nb":-1}},
    {"$limit":6}
     ])

for i in r3:
    print(i)
    

