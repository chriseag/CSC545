import random
# Author Fan Zhang
class Individual:
	# Updates the fitness value based on the genom and the map.
    def updateFitness(self):
        #TODO implement fitness function - done?
        
        violations = 0
        
        for border in self.map.borders:
            state1_color = self.genom[border.index1]
            state2_color = self.genom[border.index2]
            
            if state1_color == state2_color:
                violations += 1
        
        self.fitness = len(self.map.borders) - violations

    def __init__(self,map):
        self.map=map# the map
        self.fitness=0# fitness is cached and only updated on request whenever necessary
        
        self.genom = [random.randint(0,3) for _ in range(len(map.states))]
        
        # TODO some representation of the genom of the individual - done?
        # TODO implement random generation of an individual - done?
        self.updateFitness()

    # Reproduces a child randomly from two individuals (see textbook).
	# x The first parent.
	# y The second parent.
	# return The child created from the two individuals.
    def reproduce(self, y):
        child = Individual(self.map)
        # TODO reproduce child from individuals x and y - done?
        
        crossover_point = random.randint(0, len(self.genom) - 1)
        
        child.genom = self.genom[:crossover_point] + y.genom[crossover_point:]
        
        child.updateFitness()
        return child

	# Randomly mutates the individual.
    def mutate(self):
        # TODO implement random mutation of the individual - done?
        
        mutation_index = random.randint(0, len(self.genom) - 1)
        
        self.genom[mutation_index] = random.randint(0, 3)
        
        self.updateFitness()

	# Checks whether the individual represents a valid goal state.
	# return Whether the individual represents a valid goal state.
    def isGoal(self):
        return self.fitness == len(self.map.borders)

    def printresult(self):
        print("Your result:")
        # TODO implement printing the individual in the following format:
        
        print("Fitness: ", self.fitness)
        for index, state in enumerate(self.map.states):
            print(state, ": ", self.genom[index])
        
        # fitness: 15
        # North
        # Carolina: 0
        # South Carolina: 2
        # ...
