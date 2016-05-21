# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 19:52:21 2016

@author: Andrea
"""

# The mutation module

import random


l = 0.05 # mutation strength. Ranges from 0 to 1. The higher it is the more mutations, hypothesized the more diversity

l = 0.1 # the value that I found that optimizes GA for accuracy


def ga_mutate_specify(strength, population):
    global l
    l = strength
    ga_mutate(population)
    
    
def ga_mutate(population):
    for gene in population:
        ga_gene_mutate(gene)




def ga_gene_mutate(gene):

    s = 5 # number of changes in a parameter
    stdev = l*s # not sure if this is the real formula
    
    for x in range(0, len(gene)):
        mutation = random.gauss(0, stdev)
        mutation = round(mutation)
#        print(mutation,)
        gene[x] += mutation
        if (gene[x] > s):
            gene[x] = s
        elif (gene[x] < 1):
            gene[x] = 1

