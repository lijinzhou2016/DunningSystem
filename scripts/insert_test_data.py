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
import time


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
    sql_list=[]
    for id in xrange(7,100):
        value = (id,'借贷宝','320321111','20161111','中国传媒大学南广学院',
        '南京','徐州','/home/test','父亲','185111111','室友','1350000000','同学','152999999',0,id)
        sql_order='insert lender values {0}'.format(value)
        sql_list.append(sql_order)
    map(do_insert, sql_list)


def do_insert(sql_cmd):
    time.sleep(0.1)
    database.execute_sql(sql_cmd)

insert_user()
#insert_order()

