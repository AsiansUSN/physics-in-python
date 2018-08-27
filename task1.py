# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 16:34:28 2018

@author: Tommy
"""
import math
import numpy
import matplotlib

x = float(input('Please input the width of the gap: '))
y = float(input('please input the distance you wanna go: '))

Min_angle = math.atan(x/(y/2))
Max_angle = math.pi/2

alpha = numpy.linspace(Min_angle, Max_angle, 1000)
Tid = y/0.8 #initial time set as go directly to the end
ang = 0

for I in alpha:
    if Tid > ((y - 2*x/(numpy.tan(I)))/3.0 + (2*x/numpy.sin(I))/0.8):
        Tid = ((y - 2*x/(numpy.tan(I)))/3.0 + (2*x/numpy.sin(I))/0.8)
        ang = I
        
print('the minimum time is %.1f' % Tid) 
print('the angle should be %.1f' % math.degrees(ang), ' degrees')
print('which is %.1f' % ang, ' radians')

Tid = (y - 2*x/(numpy.tan(alpha)))/3.0 + (2*x/numpy.sin(alpha))/0.8

matplotlib.pyplot.plot(alpha, Tid)