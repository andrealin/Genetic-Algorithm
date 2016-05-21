# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 19:45:52 2016

@author: Andrea
"""

# The initializing module. Initializes the population

import random

def ga_init(number_of_genes, range_parameter):
    
    x = random.randint(1, range_parameter)
    y = random.randint(1, range_parameter)
    z = random.randint(1, range_parameter)
    population = [[x,y,z]]
    
    while (len(population) < number_of_genes):
        x = random.randint(1, range_parameter)
        y = random.randint(1, range_parameter)
        z = random.randint(1, range_parameter)
        population.append([x,y,z])
        for i in range(0, len(population) - 1): # check for duplicates
            if (are_same(population[i], population[len(population) - 1])):
                population.pop()

    return population
    
def are_same(gene1, gene2): # returns true if two arrays are the same
    for i in range(0, len(gene1)):
        if gene1[i] != gene2[i]:
            return False
    return True