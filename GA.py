#-------------------------------------------------------------------------------
# Name:        Genetic Algorithm for Sound Externalization
# Purpose:     Science Fair
#
# Author:      Andrea
#
# Created:     30/12/2015
# Edits:       1/22/2016
#
# Copyright:   (c) Andrea 2015
# Licence:     <your licence>

"""
Notes:
 
Analysis, experimentation: -----------------------------------------
Crossover: random choice vs crossover point.
  Currently, the crossover favors putting two parameters together. This works for
  some problems where we want params to stay together to maintain the solution benefits
  but for this problem, it's just three separate variables
  no two of them go together better than the other. Solved 2/2/2015! For analysis
  I could look at difference between my way and Durant's way. My hypothesis is that
  my way is better.
Convergence: pool size versus number of iterations versus convergence
  Which one matters more? Which one saves the number of comparisons the participant
  has to make? Which combination increases convergence?
  Keep comparisons number constant. Fixed amount of time.
Selection: q. Range 0 to 1. Default 2
  The higher, the quicker convergence. Set at 1 right now.
Mutation: mutation strength. Set at 0.05 right now.
  The higher, the more frequent and larger mutation.
  

Problems and questions and TODO ---------------------------------------------
check-Where in my algorithm do I clean up repeats. In the gainit
Not sure if I got stdev = ls for the ga_gene_mutate right

Accuracy problem: Converges too quickly, but not on the right solution.
  I know. That's the large problem. But it does. Ways to solve:
  - increase mutation strength
  - check-delete repeatsa: initial gene pool. partial check in crossover.
  - increase pool size
check-It's easier for this algorithm to converge on 5,5,5 than 1,1,1 WHy??? Oh actually,
  maybe not. It may just be my perception.


Cool TODOS -------------------------------------------------------------------
Holland 1975.
Convergence plots.
Keeping number of rounds constant
"""

# The main module for the GA

import numpy as np

from gainit import ga_init
from gacomparesimulation import ga_compare
from gaselection import ga_select, ga_select_specify
from gacrossover import ga_crossover
from gamutation import ga_mutate, ga_mutate_specify
from gaevaluation import ga_ave_error, ga_diversity


target = [5,5,5] #chosen optimum. Corner for now
number_of_genes = 5 # a.k.a pool size. must at least be four due to crossover
iterations = 20
number_of_trials = 1000

number_of_parameter_symbols = 5

#s_s_var = 5*10 # selection strength number of variations

def main():
    
    print("Andrea's GA")
    

#    population_print()
    
    population_print()

#    comparison_results = ga_compare(population)
#    print(comparison_results)
#    matrix = fill_matrix(comparison_results)
#    print(matrix) # comparison matrix
#    ga_select(comparison_results, population)
#    ga_mutate(population)
#    print(population)
#    ga_crossover(population)
#    print(population)
#    for tester in range(0, 10):
#        print(random.gauss(0, 1))

def population_print():
    population = ga_init(number_of_genes, number_of_parameter_symbols)
    matrix = [] # the fitness tracker
    print (population)

    for i in range(0, iterations):

        matrix = ga_compare(target, population)

        ga_select(matrix, population)
        ga_crossover(population)
        ga_mutate(population)

        print(population)

def simple_print():
    population = ga_init(number_of_genes, number_of_parameter_symbols)
    matrix = [] # the fitness tracker

    for i in range(0, iterations):

        matrix = ga_compare(target, population)

        ga_select(matrix, population)
        ga_crossover(population)
        ga_mutate(population)

        print(i+1, "\t", ga_ave_error(target, population), "\t", ga_diversity(population) )

def trial_print():
    
    
    results = [] # contains average data for each iteration
    ave_errors = []
    diversities = []
    
    for i in range(0, iterations):
        ave_errors.append([])
        diversities.append([])


    for j in range(0, number_of_trials):
        population = ga_init(number_of_genes, number_of_parameter_symbols)
        matrix = [] # the fitness tracker
        for i in range(0, iterations):
    
            matrix = ga_compare(target, population)
    
            ga_select(matrix, population)
            ga_crossover(population)
            ga_mutate(population)
    
            ave_errors[i].append(ga_ave_error(target, population))
            diversities[i].append(ga_diversity(population))
        
        
    for i in range (0, iterations):
        average_of_errors = np.average(ave_errors[i])
        ae_stdev = np.std(ave_errors[i])
        average_of_diversities = np.average(diversities[i])
        ad_stdev = np.std(diversities[i])
        results.append([average_of_errors, ae_stdev, average_of_diversities, ad_stdev])
    
        
    result_print(results)

def strength_print():
    results = [] # contains average data for each iteration
    ave_errors = []
    diversities = []
    for m in range(0, 1*20):
        ave_errors.append([])
        diversities.append([])
    
    for m in range (0, 1*20): # m is the selection strength
        strength = m/20
        
        for j in range(0, number_of_trials):        
            
            population = ga_init(number_of_genes, number_of_parameter_symbols)
            matrix = [] # the fitness tracker
            for i in range(0, 20):
        
                matrix = ga_compare(target, population)
        
#                ga_select_specify(strength, matrix, population)
                ga_select(matrix, population)
                ga_crossover(population)
                ga_mutate_specify(strength, population)
            
            ave_errors[m].append(ga_ave_error(target, population))
            diversities[m].append(ga_diversity(population))
    
    for m in range (0, 1*20):
        
        strength = m/20
        
        average_of_errors = np.average(ave_errors[m])
        ae_stdev = np.std(ave_errors[m])
        average_of_diversities = np.average(diversities[m])
        ad_stdev = np.std(diversities[m])
        results.append([strength, average_of_errors, ae_stdev, average_of_diversities, ad_stdev])
    
    result_strength_print(results)
    


def result_print(results):
    for i in range(0, len(results)): # average error, ae standard deviation, average diversity, ad standard deviation
        info = results[i]        
        print(i+1, "\t", info[0], "\t", info[1], "\t", info[2], "\t", info[3])

def result_strength_print(results):
    for i in range(0, len(results)): # average error, ae standard deviation, average diversity, ad standard deviation
        info = results[i]        
        print(info[0], "\t", info[1], "\t", info[2], "\t", info[3], "\t", info[4])
        
        
        

if __name__ == '__main__':
    main()
