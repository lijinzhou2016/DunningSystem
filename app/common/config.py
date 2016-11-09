#!/usr/bin/env python 
# -*- coding: UTF-8 -*-
#*****************************************************************************
# Title         : config.py
# Author        : Ljz
# Created       : 4th December 2016
# Last Modified : 
# Version       : 1.0
# 
# Description   : support base conf
#*****************************************************************************
import sys,os  


# 当前绝对路径
def get_path(name, parent=False):
    path = os.path.dirname(os.path.abspath(__file__))
    path_comp = path.split(os.sep)
    if parent:
        path_comp.pop()
    path_comp[-1] = name
    return os.sep.join(path_comp)




