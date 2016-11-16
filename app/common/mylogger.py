#!/usr/bin/env python 
# -*- coding: UTF-8 -*-
#*****************************************************************************
# Title         : mylogger.py
# Author        : Ljz
# Created       : 16th December 2016
# Last Modified : 
# Version       : 1.0
# 
# Description   : log system
#*****************************************************************************

import logging
import os
import sys

# 在此修改日志级别
# NOTSET=0、 DEBUG=10、 INFO=20、  WARNING=30、  ERROR=40
level = 10

# 当前绝对路径
def get_path(name, parent=False):
    path = os.path.dirname(os.path.abspath(__file__))
    path_comp = path.split(os.sep)
    if parent:
        path_comp.pop()
    path_comp[-1] = name
    return os.sep.join(path_comp)


def log_path():
    return get_path('log',parent=True)

# 使用方法见 main/test_log.py
def log(model):
    # 创建一个logger
    logger = logging.getLogger(model)

    # 日志级别 ：
    logger.setLevel(level)

    # 创建一个handler，用于写入日志文件
    fh = logging.FileHandler(log_path()+os.sep+'test.log')
    
    # 再创建一个handler，用于输出到控制台
    ch = logging.StreamHandler()
    
    # 定义handler的输出格式
    formatter = logging.Formatter('%(asctime)s %(name)s %(funcName)s %(lineno)d %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    
    # 给logger添加handler
    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger