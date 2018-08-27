# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 16:34:28 2018

@author: Tommy
"""

from math import cos
from math import sin

for i in range(1,90): #for hver vinkel

    c = 15/cos(i) #regner ut hypotenus
    b = sin(i)*c #regner ut motstående katet til vinkel
    s_p = 200 - b #regner ut lengde promerade når man kommer opp til den
    t_1 = (c + 15)/0.8 #regner tid for å gå i sand, hypotenus og 15 meter
    t_2 = s_p / 3 #regner ut tid brukt på å gå i promerade
    t = t_1 + t_2 #tid totalt
    print(min(t))
    
# må ta vinkler til radianer