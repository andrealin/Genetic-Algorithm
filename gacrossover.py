# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 19:50:09 2016

@author: Andrea
"""

# The crossover module



import random



def ga_crossover(population):
    gene1 = population[0]
    gene2 = population[1]
    p = len(gene1) #number of parameter indices. It's 3
    child1 = []
    child2 = []

#    #Durants way, choosing an index and having a cross over point   
#    index = random.randint(1, p)
##    print(index)
#    for i in range (0, index):
#        child1.append(gene1[i])
#        child2.append(gene2[i])
#    for i in range (index, p):
#        child1.append(gene2[i])
#        child2.append(gene1[i])


    #My way, randomly choosing which parameter goes to which child
    for i in range(0, len(gene1)):
        flip = random.randint(0, 1) # 0 means same, 1 means switch
#        print(flip)
        if (flip == 0):
            child1.append(gene1[i])
            child2.append(gene2[i])
        else:
            child1.append(gene2[i])
            child2.append(gene1[i])


    population[len(population) - 2] = child1
    population[len(population) - 1] = child2