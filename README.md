# Genetic-Algorithm

Abstract: This study proposes a genetic algorithm for use in modeling sound externalization. It uses subjective feedback and contains a new method of crossover, a process copied from natural reproduction. Genetic algorithms are search methods that borrow ideas from evolution and natural selection, and the goal is to converge on the best solution in a solution space. The application is sound externalization, the degree to which a sound is perceived to be outside the head. Increasing externalization provides a more realistic and thus more understandable sound to the listener. However, measuring each individual’s physical properties to modify a sound wave for better externalization is often expensive and time consuming. An estimate can be achieved by playing sound files generated according to various physical properties to a listener and using their feedback to determine the best unique sound. My goal was to design a genetic algorithm that chooses the appropriate physical properties that modify the sounds played to the listener for the most efficient and accurate search. I used a set of three variables to define the solution space: head size, ear canal length, and the size of the pinna (the outer part of the ear). I tested the initial algorithm extensively using a computer simulation of a listener and the results indicate the best choices. Final results suggest that the genetic algorithm designed shows promise as a way to accurately predict sound variables while reducing the number of sounds a listener must listen to.

# Modules
GA is the main module that can be run. Currently, it prints out the 5 solutions for 20 rounds.

gainit contains methods to initiate the population in the beginning.

gacrossover, gamutation, and gaselection are modules that contain code for the main parts of the genetic algorithm - crossover, mutation, and selection, respectivetly.

gacomparesimulation is a simulation of a listener that would be played files based on the three properties the genetic algorithm determines.

Finally, gaevaluation contains methods relating to my scientific testing, calculating average parametric error and diversity.
