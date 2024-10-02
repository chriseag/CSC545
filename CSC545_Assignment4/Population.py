#Class representing a population of individuals
# Author Fan Zhang
import random

from Individual import Individual

class Population:
	# Actual standard ctor.
	# param map The map.
	# param initialSize The initial size of the population.
    def __init__(self,map,initialSize):
        self.vector=[]
        for i in range(initialSize):
            self.vector.append(Individual(map))

    # Randomly selects an individual out of the population
    # proportionally to its fitness.
    # return The selected individual.
    def randomSelection(self):
        # TODO implement random selection - done?
        # an individual should be selected with a probability
        # proportional to its fitness
        
        total_fitness = sum(individual.fitness for individual in self.vector)
        
        selection_point = random.uniform(0, total_fitness)
        
        cumulative_fitness = 0
        for individual in self.vector:
            cumulative_fitness += individual.fitness
            if cumulative_fitness >= selection_point:
                return individual
        
        return Individual