#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Configuration file

Configuration file for modules in this directory.

Todo:
    1. Add PCD configuration formats.
    2. Add Display options.
"""


""" Configuration for PCD format """
HEADER_LINE_NUM = 11
THRESHOLD1 = 8
THRESHOLD2 = 32
SCALE = 4
OFFSET = 10

""" Configuration for PCD to Grid Converter Test Function """
PCD_FILE_PATH = 'data/ldso_kitti00_map_inliners.pcd'
SAVE_GRID = False
PRINT_INFO = False

""" Configuration for path planning """
PASSABLE = 220
IMPASSABLE = 0.0
STARTX = 256
STARTY = 256
ENDX = 217
ENDY = 122
