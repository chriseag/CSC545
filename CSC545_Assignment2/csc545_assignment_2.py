# -*- coding: utf-8 -*-
"""CSC545 Assignment 2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16KvdZNeDQJHPdbk0-v9kJlklK6hcpBWS
"""

class State:
    def __init__(self, left_sheep, left_wolves, right_sheep, right_wolves, boat_position):
        self.left_sheep = left_sheep
        self.left_wolves = left_wolves
        self.right_sheep = right_sheep
        self.right_wolves = right_wolves
        self.boat_position = boat_position

    def __eq__(self, other):
        return (self.left_sheep == other.left_sheep and
                self.left_wolves == other.left_wolves and
                self.right_sheep == other.right_sheep and
                self.right_wolves == other.right_wolves and
                self.boat_position == other.boat_position)

    def __str__(self):
        return f"Left side: {self.left_sheep} Sheep, {self.left_wolves} Wolves | Right side: {self.right_sheep} Sheep, {self.right_wolves} Wolves | Boat: {self.boat_position}"

    def goal_state(self):
        return self.right_sheep == 3 and self.right_wolves == 3

    def constraint(self):
        if (self.left_sheep < 0 or self.left_wolves < 0 or
            self.right_sheep < 0 or self.right_wolves < 0 or
            (self.left_sheep > 0 and self.left_wolves > self.left_sheep) or
            (self.right_sheep > 0 and self.right_wolves > self.right_sheep)):
            return False
        return True

    def get_moves(self):
        moves = []
        if self.boat_position == 'L':
            if self.left_sheep > 0:
                moves.append(State(self.left_sheep - 1, self.left_wolves, self.right_sheep + 1, self.right_wolves, 'R'))
            if self.left_wolves > 0:
                moves.append(State(self.left_sheep, self.left_wolves - 1, self.right_sheep, self.right_wolves + 1, 'R'))
            if self.left_sheep > 1:
                moves.append(State(self.left_sheep - 2, self.left_wolves, self.right_sheep + 2, self.right_wolves, 'R'))
            if self.left_wolves > 1:
                moves.append(State(self.left_sheep, self.left_wolves - 2, self.right_sheep, self.right_wolves + 2, 'R'))
            if self.left_sheep > 0 and self.left_wolves > 0:
                moves.append(State(self.left_sheep - 1, self.left_wolves - 1, self.right_sheep + 1, self.right_wolves + 1, 'R'))
        else:
            if self.right_sheep > 0:
                moves.append(State(self.left_sheep + 1, self.left_wolves, self.right_sheep - 1, self.right_wolves, 'L'))
            if self.right_wolves > 0:
                moves.append(State(self.left_sheep, self.left_wolves + 1, self.right_sheep, self.right_wolves - 1, 'L'))
            if self.right_sheep > 1:
                moves.append(State(self.left_sheep + 2, self.left_wolves, self.right_sheep - 2, self.right_wolves, 'L'))
            if self.right_wolves > 1:
                moves.append(State(self.left_sheep, self.left_wolves + 2, self.right_sheep, self.right_wolves - 2, 'L'))
            if self.right_sheep > 0 and self.right_wolves > 0:
                moves.append(State(self.left_sheep + 1, self.left_wolves + 1, self.right_sheep - 1, self.right_wolves - 1, 'L'))
        return moves

def bfs(start_state):
    queue = [(start_state, [])]
    visited = []

    while queue:
        state, path = queue.pop(0)

        if state.goal_state():
            return path + [state]

        visited.append(state)

        for next_state in state.get_moves():
            if next_state.constraint() and not any(next_state == v for v in visited):
                queue.append((next_state, path + [state]))

    return []

def print_solution(path):
    for state in path:
        print(state)
        print()


start_state = State(3, 3, 0, 0, 'L')
solution_path = bfs(start_state)
print_solution(solution_path)