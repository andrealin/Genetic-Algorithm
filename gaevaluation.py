# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 16:06:13 2016

@author: Andrea
"""
from gacomparesimulation import distance


# The evaluation, or average error and diversity calculator module

def ga_ave_error(target, population): # returns average parametric error of the population to the target
    sum = 0
    for gene in population:
        average_error = distance(target, gene)/(3**0.5) # averaged parametric distance
        sum += average_error
    return sum/len(population)
    
def ga_diversity(population): # returns expected averaged parametric distance between two genes chosen randomly from the population
    sum = 0
    counter = 0
    for i in range (0, len(population) - 1):
        for j in range(i + 1, len(population)):
            sum += distance(population[i], population[j])/(3**0.5) # average distance
            counter = counter + 1
#            print(counter)
    return sum/counter