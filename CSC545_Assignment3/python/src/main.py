#! /usr/bin/env python3

from environment import Environment
from node import Node
from vector2d import Vector2D
import math

def greedySearch(env):
    #
    # TODO
    #
    return []

def uniformCostSearch(env):
    #
    # TODO
    #
    return []
    

def line_collision(v1, v2, v3, v4):
    tmp = (v1.x-v2.x)*(v3.y-v4.y)-(v1.y-v2.y)*(v3.x-v4.x)
    if tmp == 0:
        return False
    p = Vector2D(((v1.x * v2.y - v1.y * v2.x) * (v3.x - v4.x) - (v1.x - v2.x) * (v3.x * v4.y - v3.y * v4.x)) / tmp, ((v1.x*v2.y-v1.y*v2.x)*(v3.y-v4.y)
                 -(v1.y-v2.y)*(v3.x*v4.y-v3.y*v4.x))/tmp)
    l1 = ((v3.x - v4.x) * (p.x - v4.x) + (v3.y - v4.y) * (p.y - v4.y)) / (pow(v3.x - v4.x, 2) + pow(v3.y - v4.y, 2))
    l2 = ((v1.x-v2.x)*(p.x-v2.x)+(v1.y-v2.y)*(p.y-v2.y)) /(pow(v1.x-v2.x,2)+pow(v1.y-v2.y,2))
    return 0 <= l1 <= 1 and 0 + 0.001 < l2 < 1 - 0.001

def successors(start, env):
    successors = []
    valid_successors = []
    successors.append(env.goal)
    for polygon in env.obstacles:
        for vertex in polygon.vertices:
            successors.append(vertex)

    for i in range(len(successors)):
        intersect = False
        for polygon in env.obstacles:
            for j in range(len(polygon.vertices)):
                for k in range(len(polygon.vertices)):
                    if line_collision(start, successors[i], polygon.vertices[j], polygon.vertices[k]):
                        intersect = True
        if not intersect:
            valid_successors.append(Node(successors[i]))
    return valid_successors
    
    

def astarSearch(env):
    
    print("A* Search")
    
    start_node = Node(env.start)
    start_node.g = start_node.h = start_node.f = 0
    goal_node = Node(env.goal)
    goal_node.g = goal_node.h = goal_node.f = 0
    
    open_list = []
    closed_list = []
    
    open_list.append(start_node)
    #print("Open List: ", open_list)
    
    while len(open_list) > 0:
        
        current_node = open_list[0]
        
        for item in (open_list):
            if item not in (closed_list):
                if item.f < current_node.f:
                    current_node = item
                
        open_list.remove(current_node)
        closed_list.append(current_node)
        
        
        
        if current_node == goal_node:
            #print("current node: ", current_node)
            #print("goal node: ", goal_node)
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            #print("Path from start to goal: ", path[::-1])
            return path[::-1]
        
        children = successors(current_node.position, env)
        #print("passed successor function")
        #print("children: ", children)
        
        for child in children:
            
            child_node = Node(child.position, current_node)
            
            if child in closed_list:
                continue
            
            child.g = current_node.g + math.sqrt((child.position.x - current_node.position.x) ** 2 + (child.position.y - current_node.position.y) ** 2)
            child.h = math.sqrt(((child.position.x - goal_node.position.x) ** 2) + ((child.position.y - goal_node.position.y) ** 2))
            child.f = child.g + child.h
            
            #print("child f value: ", child.f)
            
            should_add = True
            
            for open_node in open_list:
                if child == open_node:
                    if child.f >= open_node.f:
                        should_add = False
                        break
                if child.f >= open_node.f:
                   should_add = False
                   break
                
            if should_add: 
                open_list.append(child_node)
        
            
            

    

if __name__ == '__main__':
    env = Environment('output/environment.txt')
    print("Loaded an environment with {} obstacles.".format(len(env.obstacles)))

    searches = {
        'greedy': greedySearch,
        'uniformcost': uniformCostSearch,
        'astar': astarSearch
    }

    for name, fun in searches.items():
        print("Attempting a search with " + name)
        Environment.printPath(name, fun(env))
