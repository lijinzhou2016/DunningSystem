#!/usr/bin/env python 
# -*- coding: UTF-8 -*-
#*****************************************************************************
# Title         : util.py
# Author        : Ljz
# Created       : 4th December 2016
# Last Modified : 
# Version       : 1.0
# 
# Description   : support base conf
#*****************************************************************************

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

def root_path():
    return get_path('',parent=True)

def common_path():
    return get_path('common')

def lib_path():
    return get_path('lib')

sys.path.append(lib_path())
from userinfo import Userinfo 

def www_path():
    return get_path('www',parent=True)
def data_path():
    return get_path('data',parent=True)
def scripts_path():
    return get_path('scripts',parent=True)
def js_path():
    return www_path()+os.sep+'js'
def css_path():
    return www_path()+os.sep+'css'
def images_path():
    return www_path()+os.sep+'images'

# 执行Windows 命令
def do_cmd(cmd):
    return os.popen(cmd)


# os.sep 自适配系统路径分隔符
execfile(common_path() + os.sep + 'db.py')
execfile(common_path() + os.sep + 'config.py')
execfile(common_path() + os.sep + 'mylogger.py')


