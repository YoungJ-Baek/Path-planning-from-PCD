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