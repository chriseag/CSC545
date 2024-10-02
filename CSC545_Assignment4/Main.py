import random

from Border import Border
from Individual import Individual
from Map import Map
from Population import Population

# Author Fan Zhang

def initMap(map):
    map.states.append("North Carolina")
    map.states.append("South Carolina")
    map.states.append("Virginia")
    map.states.append("Tennessee")
    map.states.append("Kentucky")
    map.states.append("West Virginia")
    map.states.append("Georgia")
    map.states.append("Alabama")
    map.states.append("Mississippi")
    map.states.append("Florida")

    map.borders.append(Border(0, 1))
    map.borders.append(Border(0, 2))
    map.borders.append(Border(0, 3))
    map.borders.append(Border(0, 6))
    map.borders.append(Border(1, 6))
    map.borders.append(Border(2, 3))
    map.borders.append(Border(2, 4))
    map.borders.append(Border(2, 5))
    map.borders.append(Border(3, 4))
    map.borders.append(Border(3, 6))
    map.borders.append(Border(3, 7))
    map.borders.append(Border(3, 8))
    map.borders.append(Border(4, 5))
    map.borders.append(Border(6, 7))
    map.borders.append(Border(6, 9))
    map.borders.append(Border(7, 8))
    map.borders.append(Border(7, 9))
    


def initMap(map, filename=None):
    if filename:
        with open(filename, 'r') as file:
            for line in file:
                # Split each line into a list of states
                states = line.strip().split(',')
                # Add the first state to the map's states
                current_state = states[0]
                if current_state not in map.states:
                    map.states.append(current_state)

                # Add borders for each state listed
                for border_state in states[1:]:
                    if border_state not in map.states:
                        map.states.append(border_state)  # Ensure the bordering state is added
                    # Append the border (as indices) to the borders list
                    # Find the indices after adding to the states list
                    current_index = map.states.index(current_state)
                    border_index = map.states.index(border_state)
                    map.borders.append(Border(current_index, border_index))
    else:
        map.states.append("North Carolina")
        map.states.append("South Carolina")
        map.states.append("Virginia")
        map.states.append("Tennessee")
        map.states.append("Kentucky")
        map.states.append("West Virginia")
        map.states.append("Georgia")
        map.states.append("Alabama")
        map.states.append("Mississippi")
        map.states.append("Florida")

        map.borders.append(Border(0, 1))
        map.borders.append(Border(0, 2))
        map.borders.append(Border(0, 3))
        map.borders.append(Border(0, 6))
        map.borders.append(Border(1, 6))
        map.borders.append(Border(2, 3))
        map.borders.append(Border(2, 4))
        map.borders.append(Border(2, 5))
        map.borders.append(Border(3, 4))
        map.borders.append(Border(3, 6))
        map.borders.append(Border(3, 7))
        map.borders.append(Border(3, 8))
        map.borders.append(Border(4, 5))
        map.borders.append(Border(6, 7))
        map.borders.append(Border(6, 9))
        map.borders.append(Border(7, 8))
        map.borders.append(Border(7, 9))



if __name__ == '__main__':
    map = Map()
    selection = input("Do you want to run this program with the \"51\" states or the \"10\" states? ")
    if selection == "10":
        initMap(map)
    elif selection == "51":
        initMap(map, "us_states_51_ij.txt")
    
    populationSize = 500 # TODO find reasonable value - done?
    population = Population(map, populationSize)

    maxIterations = 5000 # TODO find reasonable value - done?
    currentIteration = 0
    goalFound = False
    bestIndividual = Individual(map) # to hold the individual representing the goal, if any
    while currentIteration < maxIterations and goalFound==False:
        newPopulation = Population(map,0)
        for i in range(populationSize):
            x= population.randomSelection()
            y = population.randomSelection()
            child = x.reproduce(y)
            if random.random() < 0.05:
                child.mutate()
            if child.isGoal():
                goalFound = True
                bestIndividual = child
            newPopulation.vector.append(child)
        currentIteration += 1
        population = newPopulation

        if currentIteration % 100 == 0:  # Check every 100 iterations
            best_fitness = max(ind.fitness for ind in population.vector)
            print(f"Iteration {currentIteration}: Best Fitness = {best_fitness}")

    if goalFound :
        print("Found a solution after ",currentIteration," iterations" )
        bestIndividual.printresult()
    else:
        print("Did not find a solution after ",currentIteration," iterations")