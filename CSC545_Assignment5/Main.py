import random
import time
from collections import defaultdict
from copy import deepcopy

class Map:
    def __init__(self):
        self.borders = []
        self.states = []
        
class Border:
    def __init__(self, index1, index2):
        self.state1 = index1
        self.state2 = index2

colors = [0, 1, 2, 3]
color_names = {0: 'Red', 1: 'Green', 2: 'Blue', 3: 'Yellow'}

def initMap(map_obj):
    map_obj.states.append("North Carolina")
    map_obj.states.append("South Carolina")
    map_obj.states.append("Virginia")
    map_obj.states.append("Tennessee")
    map_obj.states.append("Kentucky")
    map_obj.states.append("West Virginia")
    map_obj.states.append("Georgia")
    map_obj.states.append("Alabama")
    map_obj.states.append("Mississippi")
    map_obj.states.append("Florida")

    map_obj.borders.append(Border(0, 1))
    map_obj.borders.append(Border(0, 2))
    map_obj.borders.append(Border(0, 3))
    map_obj.borders.append(Border(0, 6))
    map_obj.borders.append(Border(1, 6))
    map_obj.borders.append(Border(2, 3))
    map_obj.borders.append(Border(2, 4))
    map_obj.borders.append(Border(2, 5))
    map_obj.borders.append(Border(3, 4))
    map_obj.borders.append(Border(3, 6))
    map_obj.borders.append(Border(3, 7))
    map_obj.borders.append(Border(3, 8))
    map_obj.borders.append(Border(4, 5))
    map_obj.borders.append(Border(6, 7))
    map_obj.borders.append(Border(6, 9))
    map_obj.borders.append(Border(7, 8))
    map_obj.borders.append(Border(7, 9))
    


def initMap(map_obj, filename=None):
    if filename:
        with open(filename, 'r') as file:
            for line in file:
                # Split each line into a list of states
                states = line.strip().split(',')
                # Add the first state to the map's states
                current_state = states[0]
                if current_state not in map_obj.states:
                    map_obj.states.append(current_state)

                # Add borders for each state listed
                for border_state in states[1:]:
                    if border_state not in map_obj.states:
                        map_obj.states.append(border_state)  # Ensure the bordering state is added
                    # Append the border (as indices) to the borders list
                    # Find the indices after adding to the states list
                    current_index = map_obj.states.index(current_state)
                    border_index = map_obj.states.index(border_state)
                    map_obj.borders.append(Border(current_index, border_index))
    else:
        map_obj.states.append("North Carolina")
        map_obj.states.append("South Carolina")
        map_obj.states.append("Virginia")
        map_obj.states.append("Tennessee")
        map_obj.states.append("Kentucky")
        map_obj.states.append("West Virginia")
        map_obj.states.append("Georgia")
        map_obj.states.append("Alabama")
        map_obj.states.append("Mississippi")
        map_obj.states.append("Florida")

        map_obj.borders.append(Border(0, 1))
        map_obj.borders.append(Border(0, 2))
        map_obj.borders.append(Border(0, 3))
        map_obj.borders.append(Border(0, 6))
        map_obj.borders.append(Border(1, 6))
        map_obj.borders.append(Border(2, 3))
        map_obj.borders.append(Border(2, 4))
        map_obj.borders.append(Border(2, 5))
        map_obj.borders.append(Border(3, 4))
        map_obj.borders.append(Border(3, 6))
        map_obj.borders.append(Border(3, 7))
        map_obj.borders.append(Border(3, 8))
        map_obj.borders.append(Border(4, 5))
        map_obj.borders.append(Border(6, 7))
        map_obj.borders.append(Border(6, 9))
        map_obj.borders.append(Border(7, 8))
        map_obj.borders.append(Border(7, 9))


def is_safe(state, color, assignment, neighbors):
    for neighbor in neighbors[state]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False

def backtrack(assignment, neighbors, map_obj):
    if len(assignment) == len(map_obj.states):
        return assignment
    unassigned = [v for v in range(len(map_obj.states)) if v not in assignment]
    state = unassigned[0]
    for color in colors:
        if is_safe(state, color, assignment, neighbors):
            assignment[state] = color
            result = backtrack(assignment, neighbors, map_obj)
            if result:
                return result
            del assignment[state]
    return None

def forward_check(state, color, domains, neighbors):
    removed = {}
    for neighbor in neighbors[state]:
        if color in domains[neighbor]:
            domains[neighbor].remove(color)
            if not domains[neighbor]:
                return False
            removed.setdefault(neighbor, []).append(color)
    return removed
            

def backtrack_forward(assignment, domains, neighbors, map_obj):
    if len(assignment) == len(map_obj.states):
        return assignment
    
    unassigned = [v for v in range(len(map_obj.states)) if v not in assignment]
    state = unassigned[0]
    for color in domains[state]:
        if is_safe(state, color, assignment, neighbors):
            assignment[state] = color
            removed = forward_check(state, color, domains, neighbors)
            if removed is not False:
                result = backtrack_forward(assignment, domains, neighbors, map_obj)
                if result:
                    return result
            for var, vals in removed.items():
                domains[var].extend(vals)
            del assignment[state]
    return None


def revise(xi, xj, domains):
    revised = False
    for color in domains[xi][:]:
        if not any(color != color2 for color2 in domains[xj]):
            domains[xi].remove(color)
            revised = True
        return revised
        

def ac3(domains, neighbors):
    queue = [(xi, xj) for xi in neighbors for xj in neighbors[xi]]
    while queue:
        xi, xj = queue.pop(0)
        if revise(xi, xj, domains):
            if not domains[xi]:
                return False
            for xk in neighbors[xi]:
                if xk != xj:
                    queue.append((xk, xi))
    return True

def backtrack_ac3(assignment, domains, neighbors, map_obj):
    if len(assignment) == len(map_obj.states):
        return assignment
    
    unassigned = [v for v in range(len(map_obj.states)) if v not in assignment]
    state = unassigned[0]
    for color in domains[state]:
        if is_safe(state, color, assignment, neighbors):
            assignment[state] = color
            local_domains = deepcopy(domains)
            local_domains[state] = [color]
            if ac3(local_domains, neighbors):
                result = backtrack_ac3(assignment, local_domains, neighbors, map_obj)
                if result:
                    return result
            del assignment[state]
    return None


def min_conflicts(map_obj, max_steps=50):
    neighbors = get_neighbors(map_obj)
    
    current = {v: random.choice(colors) for v in range(len(map_obj.states))}
    for _ in range(max_steps):
        conflicted = [v for v in current if any (current[v] == current[neighbor] for neighbor in neighbors[v])]
        if not conflicted:
            return current
        var = random.choice(conflicted)
        
        conflict_counts = defaultdict(int)
        for color in colors:
            conflict_counts[color] = sum(current[neighbor] == color for neighbor in neighbors[var])
        min_conflict = min(conflict_counts.values())
        min_colors = [color for color in colors if conflict_counts[color] == min_conflict]
        current[var] = random.choice(min_colors)
    return None

def get_neighbors(map_obj):
    neighbors = defaultdict(list)
    for border in map_obj.borders:
        neighbors[border.state1].append(border.state2)
        neighbors[border.state2].append(border.state1)
    return neighbors

def run_experiment(map_obj, algorithm, initial_assignment=None, runs=500):
    neighbors = get_neighbors(map_obj)
    total_time = 0.0
    for _ in range(runs):
        assignment = {}
        domains = {v: colors.copy() for v in range (len(map_obj.states))}
        if initial_assignment:
            for var, color in initial_assignment.items():
                assignment[var] = color
                domains[var] = [color]
        start_time = time.time()
        if algorithm == 'backtrack':
            result = backtrack(assignment, neighbors, map_obj)
        elif algorithm == 'forward':
            result = backtrack_forward(assignment, domains, neighbors, map_obj)
        elif algorithm == 'ac3':
            result = backtrack_ac3(assignment, domains, neighbors, map_obj)
        elif algorithm == 'min_conflicts':
            result = min_conflicts(map_obj)
        end_time = time.time()
        total_time += end_time - start_time
    average_time_ms = (total_time / runs) * 1000
    return average_time_ms


if __name__ == '__main__':
    map_obj = Map()
    
    algorithms = ['backtrack', 'forward', 'ac3', 'min_conflicts']
    runs = 500
    initial_assignment = {0: 0}
    results = {}
    
    selection = input("Do you want to run this program with the \"51\" states or the \"10\" states? ")
    if selection == "10":
        initMap(map_obj)
    elif selection == "51":
        initMap(map_obj, "us_states_51_ij.txt")
        
    for algo in algorithms:
        avg_time_no_init = run_experiment(map_obj, algo, initial_assignment=None, runs=runs)
        avg_time_with_init = run_experiment(map_obj, algo, initial_assignment=initial_assignment, runs=runs)
        results[algo] = {
            'no_init': avg_time_no_init,
            'with_init': avg_time_with_init
        }
    print(f"Algorithm: {algo}")
    print(f"  Average Time without Initial Assignment: {avg_time_no_init:.6f} ms")
    print(f"  Average Time with Initial Assignment: {avg_time_with_init:.6f} ms\n")
    
    print("Average Run Times (in milliseconds):")
    print("| Algorithm                    | Without Initial Assignment | With Initial Assignment |")
    print("|------------------------------|----------------------------|-------------------------|")
    for algo in algorithms:
        no_init = f"{results[algo]['no_init']:.6f}"
        with_init = f"{results[algo]['with_init']:.6f}"
        print(f"| {algo.capitalize():<28} | {no_init:<26} | {with_init:<23} |")