# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 19:47:34 2016

@author: Andrea
"""

# The comparison simulation module


import random


def ga_compare(target, population):
    matrix = [] # there are r rows with j columns inside each
    for i in range (0, len(population) - 1): # going through the beginning row to second to last
        row = []
        for j in range (i + 1, len(population)): # going from the column after the row to the last column
            #result from ga_compsim tells us whether the first, aka row, wins over the column
            #1 = win, 0 = loss, 0.5 = tie
            comparison_result = ga_compsim(target, population[i], population[j])
            row.append(comparison_result)
        matrix.append(row)
    return matrix

def ga_compsim(target, solution1, solution2):
    # distance = sqrt(x^2 + y^2 + z^2)
    distance1 = distance(target, solution1)
    distance2 = distance(target, solution2)
    if (distance1 < distance2): #solution1 is closer, so wins
        return 1
    elif (distance1 > distance2): # solution1 is further away, so loses
        return 0
    else: # tie
        return 0.5
        
        
def distance(point1, point2): # in a 3-D space
    sum = 0
    for a, b in zip(point1, point2):
        sum += (a-b)**2
    return sum**0.5