#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Main function for path planning from PCD file project

1. Convert PCL to binary Grid Map
2. Path planning using quadtree and A* algorithm

Todo:
    1. Add test function.
"""
import sys
from src.pclgrid_converter import pcl2grid_converter

if __name__ == '__main__':
    file_path = sys.argv[1]
    pcl2grid_converter(file_path)