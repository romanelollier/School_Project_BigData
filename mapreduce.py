#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 17:58:18 2021

@author: mathisagathe
"""

#from pymongo import MongoClient
from pyspark import SparkConf, SparkContext

#Config Spark
conf = SparkConf().setMaster("local").setAppName("Test")
#sc = SparkContext(conf=conf)
sc = SparkContext.getOrCreate(conf=conf)


#Connexion MongoDB
#client = MongoClient("10.35.7.4", username = "mathis", password = "MathisM21", authsource = "mathisdb")
#db=client.mathisdb
#collection = db["TripAdvisor"]

restoRDD = sc.textFile("/Users/mathisagathe/tripadvisor.csv")

nb = restoRDD.count()
print("Total: ", nb)

franceRDD = restoRDD.filter(lambda x: "France" in x)
print("France: ", franceRDD.count())

#Séparation des Tags

tags = restoRDD.flatMap(lambda x: x.split(","))
counttags = tags.map(lambda x:(x,1)).reduceByKey(lambda x,y: x+y)
print(counttags.collect())
