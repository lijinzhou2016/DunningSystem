#!/usr/bin/env python 
# -*- coding: UTF-8 -*-
#*****************************************************************************
# Title         : Orderinfo.py
# Author        : chenxiaosuo
# Created       : 21th Nov 2016
# Last Modified : 
# Version       : 1.0
# 
# Description   : Get order info by order id
#*****************************************************************************

import time
import uuid
import os
from peewee import *

def get_path(name, parent=False):
    path = os.path.dirname(os.path.abspath(__file__))
    path_comp = path.split(os.sep)
    if parent:
        path_comp.pop()
    path_comp[-1] = name
    return os.sep.join(path_comp)

def common_path():
    return get_path('common')


execfile(common_path() + os.sep + 'db.py')

#用户信息
class Orderinfo:

    def __init__(self, id = 0):
        self.id = id
        #订单详情，list，可能有多个订单
        self.order = []
        #欠款人， Lender类型 只有一个欠款人
        self.lender = Lender()
        #订单操作，dict,格式为dict {order_id: op}，其中op为操作list
        self.operation = []

    #根据订单ID获取订单详情
    def get_order_detail_by_id(self, id):
        query = (Orders.select().where((Orders.id == id) 
                & (Orders.is_del == 0) ))
        if(len(query) == 1):
            self.order.append(query[0])
            print "lender: " + self.order[0].lender.name
        else:
            return False
        query = (Lender.select().where((Lender.id == self.order[0].lender.id) 
                & (Lender.is_del == 0) ))
        if(len(query) == 1):
            self.lender = query[0]
        else:
            return False
        query = (Operation
                    .select(Operation, Admin)
                    .join(Admin)
                    .where((Operation.lender_id == self.order[0].lender.id))
                    .order_by(Operation.time.desc()))
        for item in query:
            self.operation.append(item)
        return True
        

   #获取订单详情
    def get_order_detail(self):
        return self.get_order_detail_by_id(self.id)

   #获取订单详情，同时获取用户下所有订单
    def get_order_detail_all(self):
        if self.get_order_detail_by_id(self.id):
            query = (Orders.select().where((Orders.lender_id == self.lender.id) 
                    & (Orders.is_del == 0) & (Orders.id != self.id)))
            for item in query:
                self.order.append(item)
            return True
        else:
            return False
    
    #格式化订单、欠款人、操作条目，返回一个字典，query格式化为字典
    def get_format_dict(self):
        orders_list = []
        for order in self.order:
            #生成订单字典
            orders_list.append({'id':order.id, 'source': order.source, 
            'disp_id': order.disp,
            'account_day': order.account_day, 'product': order.product,
            'amount': order.amount, 'month_pay': order.month_pay,
            'periods': order.periods, 'paid_periods':order.paid_periods,
            'recv_amount': order.received_amount, 
            'order_date':order.order_date, 
            'takeorder_date': order.takeorder_data,
            'call_details': order.call_details,
            'contract': order.contract, 
            'lender_pic': order.lender_pic,
            'parent': order.parent, 'parent_call': order.parent_call,
            'roommate': order.roommate, 'roommate_call': order.roommate_call,
            'classmate': order.classmate, 
            'classmate_call': order.classmate_call,
            'status': order.status})
        lender = {'id': self.lender.id, 'idcard': self.lender.idcard,
            'name': self.lender.name, 'tel': self.lender.tel,
            'university': self.lender.university, 
            'univers_area': self.lender.univers_area,
            'family_addr': self.lender.family_addr,
            'family_area': self.lender.family_area}
        #获取operation的list
        ops = self.operation
        order_ops = []
        for op in ops:
            order_ops.append({'id': op.id, 'admin': op.admin.name, 
            'op_desc':  op.op_desc, 'time': op.time})
        return {'orders':orders_list, 'lender': lender, 'operations': order_ops}