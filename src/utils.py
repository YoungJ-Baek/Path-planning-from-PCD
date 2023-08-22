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
from PIL import Image


def gridmap_loader(file, size=cf.MAPSIZE, visualize=False):
    """Load grid map with binary file
    
    Result of PCL to grid map conversion is usually binary file.
    This function helps to visualize binary formatted grid map file.
    
    Args:
        file(str or ndarray): if string -> directory where grid map file is, else -> grid map data
        size(int): map image size(we assume that width==height).
        visualize(bool): open image window if True, else not.
    """
    if type(file) == str:
        gridmap = np.fromfile(file,dtype=np.float)
    else:
        gridmap = file
    gridsize = gridmap[:2].astype(int)
    grid = gridmap[2:]
    grid = np.reshape(grid,gridsize)
    grid = grid * cf.PASSABLE
    im = Image.fromarray(grid).resize(size)

    if visualize:
        grid = cv2.resize(grid,size,interpolation=cv2.INTER_LINEAR)

        cv2.imshow("window",grid)
        cv2.waitKey(0)
    
    return im
