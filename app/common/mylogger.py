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
import ConfigParser


# 当前绝对路径
def get_path(name, parent=False):
    path = os.path.dirname(os.path.abspath(__file__))
    path_comp = path.split(os.sep)
    if parent:
        path_comp.pop()
    path_comp[-1] = name
    return os.sep.join(path_comp)


def read_conf(model):
    try:
        cf = ConfigParser.ConfigParser()
        if os.path.exists(os.path.join(get_path("",parent=True), "..", 'conf.ini')):
            cf.read(os.path.join(get_path("",parent=True), "..", 'conf.ini'))
            item = dict(cf.items(model))
            #print dict(item)
            return dict(item)
        else:
            return {}
    except Exception as e:
        return {}

def get_log_path():
    '''log保存路径根目录从配置文件加载

        若配置文件缺失，默认系统上级目录为跟目录
    '''
    root_path = read_conf('log')
    if root_path:
        path =  os.path.join(root_path['path'], 'log')
    else:
        path =  get_path(os.path.join('..', 'log'),parent=True)
    if not os.path.exists(path):
        os.makedirs(path)
    return path

def get_log_level():
    '''读取日志级别，

    读取失败时，默认级别debug
    '''
    level = read_conf('log')
    if level:
        return int(level['level'])
    else:
        return 10

# 使用方法见 main/test_log.py
def log(model):
    # 创建一个logger
    logger = logging.getLogger(model)

    # 日志级别 ：
    logger.setLevel(get_log_level())

    # 创建一个handler，用于写入日志文件
    fh = logging.FileHandler(os.path.join(get_log_path(), 
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