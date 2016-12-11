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

import xlrd
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

def scripts_path():
    return get_path('scripts')

execfile(common_path()+os.sep+'db.py')
filepath = os.path.join(scripts_path(),'orderstpl.xlsx')

data = xlrd.open_workbook(filepath)
table = data.sheets()[0]

nrows = table.nrows # 行数
ncols = table.ncols # 列数

# for i in range(nrows):
#     print table.row_values(i)[1]

total_datas=[] # 总条数
order_insert_dict = {} # 插入order表中的数据
lender_insert_dict = {} # 插入lender表中的数据

for i in range(nrows):
    total_datas.append(table.row_values(i))

total_datas.pop(0) # 去掉标题栏

for one_data in total_datas:
    if one_data[1]: # 姓名
        lender_insert_dict['name'] = one_data[1]
    if one_data[2]: # 电话
        lender_insert_dict['tel'] = one_data[2]
    if one_data[3]: # 身份证
        lender_insert_dict['idcard'] = one_data[3]
    if one_data[4]: # 学院区域
        lender_insert_dict['univers_area'] = one_data[4]
    if one_data[5]: # 学校
        lender_insert_dict['university'] = one_data[5]
    if one_data[6]: # 家庭区域
        lender_insert_dict['family_area'] = one_data[6]
    if one_data[7]: # 家庭住址
        lender_insert_dict['family_addr'] = one_data[7]





    
        

