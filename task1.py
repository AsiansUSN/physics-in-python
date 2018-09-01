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

Min_angle_alpha = math.atan(x/(y))
Max_angle_alpha = math.pi/2

alpha = numpy.linspace(Min_angle_alpha, Max_angle_alpha, 1000)
Tid = y/0.8 #initial time set as go directly to the end
ang = 0

for I in alpha:
    if (y - x/numpy.tan(I)) == 0:
        Min_angle_beta = math.pi/2
    else:
        Min_angle_beta = math.atan(x/(y - x/numpy.tan(I)))
    Max_angle_beta = math.pi/2
    beta = numpy.linspace(Min_angle_beta, Max_angle_beta, 1000)
    for J in beta:
        tid2 = (x/numpy.sin(I))/0.8 + (x/numpy.sin(J))/0.8 + (y - x/(numpy.tan(I)) - x/(numpy.tan(J)))/3.0
        if Tid > tid2:
            Tid = tid2
            ang1 = I
            ang2 = J
        
print('the minimum time is %.1f' % Tid) 

print('the angle1 should be %.1f' % math.degrees(ang1), ' degrees')
print('which is %.1f' % ang1, ' radians')

print('the angle2 should be %.1f' % math.degrees(ang2), ' degrees')
print('which is %.1f' % ang2, ' radians')

Tid = (y - 2*x/(numpy.tan(alpha)))/3.0 + (2*x/numpy.sin(alpha))/0.8

matplotlib.pyplot.plot(alpha, Tid)