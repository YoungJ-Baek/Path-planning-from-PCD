#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Main function for path planning from PCD file project

0. Execute with 'python [pcd file name]'
1. Convert PCL to binary Grid Map
2. Path planning using quadtree and A* algorithm

Todo:
    1. Modify to be able to set up start, end point with arguments(now, configuration file)
    2. Eliminate unnecessary parts of other modules
    3. Lists for modification needed are astar, graph, quadtree
"""
import sys
import src.pclgrid_converter
import src.utils
import src.quadtree
import src.graph
import src.astar
import configuration as cf


if __name__ == '__main__':
    file_path = sys.argv[1]
    grid_map = src.pclgrid_converter.pcl2grid_converter(file_path)
    map_image = src.utils.gridmap_loader(grid_map)
    tree = src.quadtree.Tile(map_image, limit=100)
    adjacent_graph = src.graph.make_adjacent_function(tree)
    start = tree.get(cf.STARTX, cf.STARTY)
    goal = tree.get(cf.ENDX, cf.ENDY)
    path, distance, considered = src.astar.astar(adjacent_graph, src.graph.euclidian, src.graph.euclidian, start, goal)
    # print(path)