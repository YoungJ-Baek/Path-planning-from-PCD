#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Utilities for path planning from PCD file

Useful functions for the project.
Developed functions through process.

Todo:
    1. Add gridmap loader
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import cv2
import numpy as np
import configuration as cf

def gridmap_loader(file_path):
    """Load grid map with binary file
    
    Result of PCL to grid map conversion is usually binary file.
    This function helps to visualize binary formatted grid map file.
    
    Args:
        file_path(str): directory where PCD file is.
    """
    gridmap = np.fromfile(file_path,dtype=np.float)
    gridsize = gridmap[:2].astype(int)
    grid = gridmap[2:]
    grid = np.reshape(grid,gridsize)

    grid = cv2.resize(grid,(500,500),interpolation=cv2.INTER_LINEAR)

    cv2.imshow("window",grid)
    cv2.waitKey(0)
    