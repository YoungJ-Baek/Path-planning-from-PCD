#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Convert PCL to Grid Map

Convert PCL to binary Grid Map module & test function.
Also, can save the result grid map with binary format.

Attributes:
    file_path(str): directory where PCD file is.
    save_grid(bool): save binary grid map if True, else don't.
    print_info(bool): print information for debugging if True, else don't

Todo:
    1. Add test function.
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import cv2
import numpy as np
import configuration as cf

def pcl2grid_converter(file_path=cf.FILE_PATH,save_grid=cf.SAVE_GRID,print_info=cf.PRINT_INFO):
    """Convert PCL to Grid Map
    
    Convert PCL to binary Grid Map
    
    Args:
        file_path(str): directory where PCD file is.
        save_grid(bool): save binary grid map if True, else don't.
        print_info(bool): print information for debugging if True, else don't

    Returns:
        grid_bin(ndarray): top view of PCD map, can use this for path planning.
    """
    try:
        pcd = open(file_path, 'r')
    except FileNotFoundError:
        print(f'There is no such file named {file_path}')
        exit()

    """ Get number of point in PCD """
    pointNum = 0
    if print_info: print('reading PCD file...')
    for index in range(cf.HEADER_LINE_NUM):
        line = pcd.readline()
        tokens = line.split()
        if(tokens[0] == 'POINTS'): pointNum = int(tokens[1])

    if not pointNum:
        print(f'Wrong header format information, POINTS not found in {cf.HEADER_LINE_NUM}')
        exit()
    
    """ Read point data from PCD """
    points = np.zeros((pointNum,3))
    for index in range(pointNum):
        line = pcd.readline()
        tokens = line.split()
        points[index] = list(map(float,tokens))

    """ Initialize grid map """
    x_max = np.max(points[:,0])
    x_min = np.min(points[:,0])
    z_max = np.max(points[:,2])
    z_min = np.min(points[:,2])

    gridsize = np.array([int(z_max//cf.SCALE + abs(x_min)//cf.SCALE + 2*cf.OFFSET), int(x_max//cf.SCALE + abs(x_min)//cf.SCALE + 2*cf.OFFSET)])
    grid = np.zeros((gridsize))

    if print_info:
        print("(x max, x min) : ",x_max, x_min)
        print("(z max, z min) : ",z_max, z_min)
        print("grid size : ",gridsize)

    """ Generate grid map """
    if print_info: print('generating grid map...')
    for i in range(points.shape[0]):
        x, y, z = points[i].astype(int)
        x=int(x//cf.SCALE + abs(x_min)//cf.SCALE)
        z=int(z//cf.SCALE + abs(z_min)//cf.SCALE)
        grid[z+cf.OFFSET][x+cf.OFFSET]+=1

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] < cf.THRESHOLD1:
                grid[r][c] = 0
            elif grid[r][c] < cf.THRESHOLD2:
                grid[r][c] = 0.5
            else:
                grid[r][c] = 1
    
    gridmap = np.concatenate((gridsize,grid.flatten())) 
    
    if save_grid: gridmap.tofile(file_path[:-4] +".bin")
    if print_info:
        grid = cv2.resize(grid,(500,500),interpolation=cv2.INTER_LINEAR)
        cv2.imshow("window",grid)
        cv2.waitKey(0)
    
    return gridmap


if __name__ == '__main__':
    pcl2grid_converter()