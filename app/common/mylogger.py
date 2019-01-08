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
import time

# 使用方法见 main/test_log.py
def log(model):
    # 创建一个logger
    logger = logging.getLogger(model)

    # 日志级别 ：
    logger.setLevel(10)

    # 创建一个handler，用于写入日志文件
    fh = logging.FileHandler(os.path.join("../../../",
                            time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))+'.log'))
    
    # 再创建一个handler，用于输出到控制台
    ch = logging.StreamHandler()
    
    # 定义handler的输出格式
    formatter = logging.Formatter('[%(asctime)s][%(levelname)s][%(name)s][%(funcName)s][line %(lineno)d]: %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    
    # 给logger添加handler
    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger