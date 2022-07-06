#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Find shortest path via A* algorithm

Path planning with A* algorithm.

Attributes:
    adjacent_graph(function): function that generate adjacent graph with input node, return all adjacent of current node into list
    dist_function(function): function that calculate a distance b/w two nodes, return distance in double type
    start_point(node): node that represent starting point
    end_point(node): node that represent ending point
    waypoint(list(node)): list of node that represent waypoints if necessary

Todo:
    1. Add astar function
    2. Add test function
    3. Add waypoint function in the main function
"""
from pqdict import pqdict


def astar(adjacent_graph, dist_function, heuristic_function, start_point, end_point, waypoint=None):
    """Find shortest path via A* algorithm

    Path planning with A* algorithm.
    
    Args:
        adjacent_graph(function): function that generate adjacent graph with input node, return all adjacent of current node into list
        dist_function(function): function that calculate a distance b/w two nodes, return distance in double type
        start_point(node): node that represent starting point
        end_point(node): node that represent ending point
        waypoint(list(node)): list of node that represent waypoints if necessary

    Returns:
        path(list(node)): list of node that represent the shortest path
        distance(double): absolute distance from starting point to ending point
        candidates(list(node)): list of node that represent the log of path planning, used for debugging
    """
    D = {start_point: 0}                   # final absolute distances
    P = {}                           # predecessors
    Q = pqdict({start_point: 0})           # fringe/frontier maps unexpanded node to estimated dist to goal

    considered = 0           # count how many nodes have been considered on multiple paths

    # keep expanding nodes from the fringe
    # until goal node is reached
    # or no more new nodes can be reached and fringe runs empty
    
    for n, estimation in Q.popitems():   # pop node with min estimated costs from queue
        if n == end_point:                    # reached goal node
            break                        # stop expanding nodes

        for neighb in adjacent_graph(n):      # for all neighbours/adjacent of current node n
            considered += 1
            dist = D[n] + dist_function(n, neighb)        # calculate distance to neighbour: cost to current + cost reaching neighbour from current
            if neighb not in D or D[neighb] > dist:  # if neighbour never visited or shorter using this way
                D[neighb] = dist                     # found (shorter) distance to neighbour
                Q[neighb] = dist + heuristic_function(neighb, end_point)   # estimate distance from neighbour to goal
                P[neighb] = n                        # remember we reached neighbour via n  

    # expanding done: distance map D populated

    if end_point not in D:                # goal node not in distance map
        return None, D, considered   # no path to goal found

    # build path from start to goal
    # by walking backwards on the predecessor map

    path = []              # start with empty path
    n = end_point               # at the goal node
    
    while n != start_point:      # while not yet at the start node
        path.insert(0, n)  #     prepend node to path
        n = P[n]           #     get predecessor of node
        
    path.insert(0, start_point)  # dont forget the start node
    # print(len(path))
    # for index in range(0, len(path)):
    #     print(path[index])
    return path, D, considered
