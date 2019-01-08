#!/usr/bin/env python 
# -*- coding: UTF-8 -*-
#*****************************************************************************
# Title         : test_log.py
# Author        : Ljz
# Created       : 4th December 2016
# Last Modified : 
# Version       : 1.0
# 
# Description   : mylogger模块使用demo
#*****************************************************************************

import bottle
import os
import sys

# 当前绝对路径
def get_path(name, parent=False):
    path = os.path.dirname(os.path.abspath(__file__))
    path_comp = path.split(os.sep)
    if parent:
        path_comp.pop()
    path_comp[-1] = name
    return os.sep.join(path_comp)

def common_path():
    return get_path('common')

# 导入mylogger.py
execfile(common_path() + os.sep + 'mylogger.py')

def test():
    logger = log("test_log") # 调用log方法，传入此文件名称
    logger.debug("this is debug message") # 输出不同级别log
    logger.info("this is info message")

test()