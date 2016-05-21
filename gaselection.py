# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 19:48:39 2016

@author: Andrea
"""

# The selection module


import random
q = 2 # 0 to 1, decreases dynamic range. 0 flattens it out.

q = 4.6 # the value I found that optimizes the algorithm for accuracy

def ga_select_specify(strength, half_matrix, population):
    global q
    q = strength
    ga_select(half_matrix, population)


def ga_select(half_matrix, population):

#    print(q)

    matrix = fill_matrix(half_matrix) # convert into a filled matrix

    for i in range(0, len(population)): # find fitness and sort
        fitness = sum_row(matrix[i]) # number of wins
        population[i].append(fitness) # temporarily append fitness
    new_population = sorted(population, key=lambda x: x[len(x) -1])
    new_population.reverse() # so it goes from highest fitness lowest


    #assign probability of surviving based on hypergeometric fitness -----------------------------
    for i in range(0, len(new_population)): # change fitness to hypergeometric rank
        probability = 1/((i+1)**q) # hypergeometric probability based on rank
        new_population[i].pop()
        new_population[i].append(probability)

#    print("hypergeometric probability ", new_population)

    #order surviving genes based on hypergeoemtric rank ------------------------------------

    hypergeometric_population = []
    for i in range(0, len(new_population)):
        y = 0
        for gene in new_population: # recalculate sum
            y += gene[len(gene) - 1]

        random_selector = random.uniform(0, y)
        for j in range(0, len(new_population)):
            partial_sum = 0
            for s in range(0, j+1):
                gene = new_population[s]
                partial_sum += gene[len(gene) - 1]

            if random_selector < partial_sum:
                # gene is chosen and added to the new hypergeometric population
                hypergeometric_population.append(new_population[j])
                new_population.pop(j) # delete selected gene from old population so we don't choose it again
                break # exit this j for-loop


#    print("random hypergeomtric probability sort ", hypergeometric_population) # sorted based on hypergeometric


    #copying each item back into the original population, and deleting the fitness value from each gene ----------
    for i in range(0, len(hypergeometric_population)): 
        hypergeometric_population[i].pop()
        population[i] = hypergeometric_population[i]

    # zero the two deleted genes ---------------------------------------------------------------------------------
    population[len(population) - 2] = []
    population[len(population) - 1] = []

#    print("the actual ", population) # the actual population


#helping methods. private. ------------------------------------------------

def sum_row(row): # sums the numbers in a given array
    sum = 0
    for j in row:
        sum += j
    return sum

def fill_matrix(half_matrix): # fills in a matrix based on a half matrix
    matrix = []
    full_length = len(half_matrix) + 1 # should be same as number_of_genes

    for i in range (0, full_length): # all rows
        row = []

        for j in range (0, full_length): # all columns
            if (i < j): # if row less than column, its the upper triangle that's already filled
                column = len(half_matrix[i]) - (full_length - j) # column of interest in the half matrix
                row.append(half_matrix[i][column])
            elif (i == j):
                row.append(0.5)
            else: # if row greater than column, so the lower triangle
                #lower triangle is complement transpose of upper triangle
                column = len(half_matrix[j]) - (full_length - i) # column of interest using matrix row
                row.append((half_matrix[j][column] + 1) % 2)


        matrix.append(row)

    return matrix
