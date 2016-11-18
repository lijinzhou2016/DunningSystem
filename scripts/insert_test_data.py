#!/usr/bin/env python 
# -*- coding: UTF-8 -*-
#*****************************************************************************
# Title         : insert_test_data.py
# Author        : Ljz
# Created       : 18th December 2016
# Last Modified : 
# Version       : 1.0
# 
# Description   : insert test data
#*****************************************************************************

import os
import sys


#当前绝对路径
def get_path(name, parent=False):
    path = os.path.dirname(os.path.abspath(__file__))
    path_comp = path.split(os.sep)
    if parent:
        path_comp.pop()
    path_comp[-1] = name
    return os.sep.join(path_comp)

def common_path():
    path='app'+os.sep+'common'
    return get_path(path)

execfile(common_path()+os.sep+'db.py')

def insert_user():
    sql_admin='insert Admin values (1,"admin","admin","123456",1,1);'
    sql_common='insert Admin values (2,"test","test","123456",0,1);'
    database.execute_sql(sql_admin)
    database.execute_sql(sql_common)

def insert_order():
    value = 

