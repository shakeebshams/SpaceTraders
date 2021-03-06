# -*- coding: utf-8 -*-
"""
Created on Thu May  3 20:10:53 2018

@author: USER
"""
import random

class Planet:
    
    planetsList = []
    
    def __init__(self, name):
        techArray = ["Pre-Agriculture", "Agriculture", "Medieval", "Renaissance", "Early Industrial", "Industrial", "Post-Industrial", "Hi-Tech"]
        resourceArray = ["NOSPECIALRESOURCES", "MINERALRICH", "MINERALPOOR", "DESERT", "LOTSOFWATER", "RICHSOIL", "POORSOIL", "RICHFAUNA", "LIFELESS", "WEIRDMUSHROOMS", "LOTSOFHERBS", "ARTISTIC", "WARLIKE"]
        self.name = name
        self.supply = {'Water': random.randint(0, 1000),
                       'Furs': random.randint(0,1000),
                       'Food': random.randint(50, 2000),
                       'Ore': random.randint(10, 100),
                       'Firearms': random.randint(200, 3000),
                       'Narcotics': random.randint(10000, 15000)}
        
        self.population = random.randint(1000, 1000000)
        
        self.prices = {'Water': round(random.uniform(1.0, 5.0), 2),
                       'Furs': round(random.uniform(3, 10), 2),
                       'Food': round(random.uniform(1, 2), 2),
                       'Ore': round(random.uniform(5, 15), 2),
                       'Firearms': round(random.uniform(2, 4), 2),
                       'Narcotics': round(random.uniform(0.1, 2), 2)}
        
        self.economy = random.randint(10000, 20000)
        techVal = random.randint(0, 7)
        resourceVal = random.randint(0, 12)
        self.tech = techArray[techVal]
        self.resource = resourceArray[resourceVal]
        coor = (0, random.randint(0, 999))
        self.coordinates =coor
        
        Planet.planetsList.append(name)
        
    def supplyReport(self, key=None):
        if key == None:
            for item in self.supply:
                print("{}: {}".format(item, self.supply[item]))
        else:
            print("{}: {}".format(key, self.supply[key]))
            
    def pricesReport(self, key=None):
        if key == None:
            for item in self.prices:
                print("{}: ${}".format(item, self.prices[item]))
        else:
            print("{}: ${}".format(key, self.supply[key]))