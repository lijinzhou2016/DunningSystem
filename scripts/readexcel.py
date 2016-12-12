#!/usr/bin/env python 
# -*- coding: UTF-8 -*-
#*****************************************************************************
# Title         : insert_test_data.py
# Author        : Ljz
# Created       : 18th December 2016
# Last Modified : 
# Version       : 1.0
# 
# Description   : 调试用
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
filepath = os.path.join(scripts_path(),'订单模板2.xlsx')

data = xlrd.open_workbook(filepath)
table = data.sheets()[0]

nrows = table.nrows # 行数
ncols = table.ncols # 列数

# for i in range(nrows):
#     print table.row_values(i)[1]

total_datas=[] # 总条数
existence_disp=[] # 插入的数据订单号数据中已存在
order_insert_dict = {'is_del':0} # 插入order表中的数据
lender_insert_dict = {'is_del':0} # 插入lender表中的数据
# 用来把前端传过来的状态，转换成数据库对应数值的列表
orderStatusKey = {u'已结清':0, u'联系本人':1, u'联系亲属':2, u'联系同学':3,
                u'失联':4, u'待外访':5, u'外访中':6, u'承诺还款':7, u'部分还款':8}
order_file_title=[u'订单编号',u'姓名',u'电话',u'身份证',u'学校区域',u'学校',u'家庭区域',u'家庭住址',u'订单状态',
                    u'账期',u'产品名称',u'分期金额',u'首次还款日',u'月供',u'期数',u'已还期数',
                    u'订单日期',u'接单日期',u'已还金额',u'父母',u'父母电话',u'同寝',u'同寝电话',u'同学',u'同学电话']


for i in range(nrows):
    total_datas.append(table.row_values(i))

title = total_datas.pop(0) # 去掉标题栏
print title
for item in title:
    print item
if title == order_file_title:
    print '文件正确'

for one_data in total_datas:
    # 订单来源字段
    order_insert_dict['source'] = ''

    if one_data[0]: # 订单编号(必要字段)
        if Orders.select().where(Orders.disp == one_data[0]): #重复订单
            existence_disp.append(one_data)
            #print '重复订单：',one_data[0]
            continue
        order_insert_dict['disp'] = one_data[0]
    else:
        pass

    if one_data[8]: # 订单状态
        order_insert_dict['status'] = orderStatusKey[one_data[8]]
    if one_data[9]: # 账期
        order_insert_dict['account_day'] = one_data[9]
    if one_data[10]: # 产品名称
        order_insert_dict['product'] = one_data[10]
    if one_data[11]: # 分期金额
        order_insert_dict['amount'] = one_data[11]
    if one_data[12]: # 首次还款日
        order_insert_dict['payment_day'] = one_data[12]
    if one_data[13]: # 月供
        order_insert_dict['month_pay'] = one_data[13]
    if one_data[14]: # 期数
        order_insert_dict['periods'] = int(one_data[14])
    if one_data[15]: # 已付期数
        order_insert_dict['paid_periods'] = int(one_data[15])
    if one_data[16]: # 订单日期
        order_insert_dict['order_date'] = one_data[16]
    if one_data[17]: # 接单日期
        order_insert_dict['takeorder_data'] = one_data[17]
    if one_data[18]: # 已还金额
        order_insert_dict['received_amount'] = str(one_data[18])
    if one_data[19]: # 父母
        order_insert_dict['parent'] = one_data[19]
    if one_data[20]: # 父母电话
        order_insert_dict['parent_call'] = str(int(one_data[20]))
    if one_data[21]: # 同寝
        order_insert_dict['roommate'] = one_data[21]
    if one_data[22]: # 同寝电话
        order_insert_dict['roommate_call'] = str(int(one_data[22]))
    if one_data[23]: # 同学
        order_insert_dict['classmate'] = one_data[23]
    if one_data[24]: # 同学电话
        order_insert_dict['classmate_call'] = str(int(one_data[24]))

    #################################################################

    if one_data[1]: # 姓名
        lender_insert_dict['name'] = one_data[1]
    if one_data[2]: # 电话
        lender_insert_dict['tel'] = str(int(one_data[2]))
    if one_data[3]: # 身份证
        lender_insert_dict['idcard'] = (str(one_data[3])).split('.')[0]
    if one_data[4]: # 学院区域
        lender_insert_dict['univers_area'] = one_data[4]
    if one_data[5]: # 学校
        lender_insert_dict['university'] = one_data[5]
    if one_data[6]: # 家庭区域
        lender_insert_dict['family_area'] = one_data[6]
    if one_data[7]: # 家庭住址
        lender_insert_dict['family_addr'] = one_data[7]

    ##################################################
    
    #print one_data[10]
    Lender.insert(lender_insert_dict).execute()
    order_insert_dict['lender'] = (Lender.select().where(Lender.idcard == lender_insert_dict['idcard']).get()).id
    Orders.insert(order_insert_dict).execute()









    
        

