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
import datetime
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
execfile(common_path()+os.sep+'mylogger.py')

logger = log('Orderinfo.py')
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
        #图片操作
        self.orderfiles = []
        #冲突信息
        self.duplicate_cont = []

    #根据订单ID获取订单详情
    def get_order_detail_by_id(self, id):
        #获取订单信息
        query = (Orders.select().where((Orders.id == id) 
                & (Orders.is_del == 0) ))
        if(len(query) == 1):
            self.order.append(query[0])
            print "lender: " + self.order[0].lender.name
        else:
            return False
        #获取欠款人信息
        query = (Lender.select().where((Lender.id == self.order[0].lender.id) 
                & (Lender.is_del == 0) ))
        if(len(query) == 1):
            self.lender = query[0]
        else:
            return False
        #获取单个订单操作信息
        query = (Operation
                    .select(Operation, Admin)
                    .join(Admin)
                    .where((Operation.lender_id == self.order[0].lender.id))
                    .order_by(Operation.time.desc()))
        for item in query:
            self.operation.append(item)
        #获取订单附件信息
        query = (Files
                    .select()
                    .where(Files.order == id)
                    .order_by(Files.time.desc()))
        files = []
        for item in query:
            files.append({'id': item.id,'type':item.type, 'name': item.path})
        self.orderfiles.append(files)
        #检查订单下面的联系人信息是否跟数据库中其他订单有冲突
        res = self.get_duplicate_contract(self.order[0])
        self.duplicate_cont.append(res)
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
                #获取单个id文件列表详情
                files = []
                filequery =  (Files
                                .select()
                                .where(Files.order == item.id)
                                .order_by(Files.time.desc()))
                for fileitem in filequery:
                    files.append({'id': fileitem.id,'type':fileitem.type, 'name': fileitem.path})
                self.orderfiles.append(files)
                #获取单个文件ID的联系人冲突状况
                res = self.get_duplicate_contract(item)
                self.duplicate_cont.append(res)
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
            'payment_day': order.payment_day,
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
        return {'orders':orders_list, 'lender': lender, 'operations': order_ops, 'files':self.orderfiles, 'dupcontact': self.duplicate_cont}

        #获取一个空白订单用于渲染模板
    @classmethod
    def get_blank_dict(self):
        orders_list = []
        orders_list.append({'id':'', 'source': '', 
        'disp_id': '',
        'account_day': '', 'product': '',
        'amount': '', 'month_pay': '',
        'periods': '', 'paid_periods':'',
        'recv_amount': '', 
        'payment_day': '',
        'order_date':'', 
        'takeorder_date': '',
        'call_details': '',
        'contract': '', 
        'lender_pic': '',
        'parent': '', 'parent_call': '',
        'roommate': '', 'roommate_call': '',
        'classmate': '', 
        'classmate_call': '',
        'status': ''})
        lender = {'id': '', 'idcard': '',
        'name': '', 'tel': '',
        'university': '', 
        'univers_area': '',
        'family_addr': '',
        'family_area': ''}
        order_ops = []
        duplicate_cont = [{'parent':[], 'roommate':[], 'classmate':[]}]
        return {'orders':orders_list, 'lender': lender, 'operations': order_ops, 'files': [[]], 'dupcontact': duplicate_cont}

    #获取特定order query，检查对应的联系人是否有重复
    #返回一个字典{'parent':[], 'roommate': [], 'classmate':[{'id': 1, 'name': '贝贝'}]}
    #如果不重复，则字典里面对应的列表为空，否则为重复的订单信息和借款人名字
    #如果联系方式为空，则不进行检查
    @classmethod
    def get_duplicate_contract(self, record):
        result = {'parent':[], 'roommate': [], 'classmate':[]}
        #检查parent号码
        if record.parent_call is not None and record.parent_call.strip() != "":
            search_str = record.parent_call.strip()
            query = Orders.select(Orders, Lender).join(Lender).where((
                (Orders.parent_call.contains(search_str))
                | (Orders.roommate_call.contains(search_str))
                | (Orders.classmate_call.contains(search_str)))
                &(Orders.id != record.id))
            if len(query) >= 1:
                for item in query:
                    result['parent'].append({'id': item.id, 'name': item.lender.name})
        #检查roommate号码
        if record.roommate_call is not None and record.roommate_call.strip() != "":
            search_str = record.roommate_call.strip()
            query = Orders.select(Orders, Lender).join(Lender).where((
                (Orders.parent_call.contains(search_str))
                | (Orders.roommate_call.contains(search_str))
                | (Orders.classmate_call.contains(search_str)))
                &(Orders.id != record.id))
            if len(query) >= 1:
                for item in query:
                    result['roommate'].append({'id': item.id, 'name': item.lender.name})
        #检查classmate号码
        if record.classmate_call is not None and record.classmate_call.strip() != "":
            search_str = record.classmate_call.strip()
            query = Orders.select(Orders, Lender).join(Lender).where((
                (Orders.parent_call.contains(search_str))
                | (Orders.roommate_call.contains(search_str))
                | (Orders.classmate_call.contains(search_str)))
                &(Orders.id != record.id))
            if len(query) >= 1:
                for item in query:
                    result['classmate'].append({'id': item.id, 'name': item.lender.name})
        return result


#欠款人信息
class LenderTable:

    def __init__(self, id = 0):
        self.id = id
    
    #传入字典更新数据库
    @classmethod
    def update(self, id, dict):
        try:
            query = Lender.update(name=dict['name'], tel=dict['tel'],
                        idcard = dict['idcard'], family_addr = dict['family_addr'],
                        family_area = dict['family_area'], university = dict['university'],
                        univers_area = dict['univers_area']).where(Lender.id == id).execute()
            return 'success'
        except BaseException,e:
            logger.error(e)
            return 'error'
    
    #传入字典插入数据
    @classmethod
    def insert(self, dict):
        try:
            #判断如果存在名字和身份证信息相同的人，则认为是同一个人，直接更新信息即可
            query = Lender.select().where((Lender.idcard == dict['idcard']) 
                    & (Lender.name == dict['name']) & (Lender.is_del == 0))
            if len(query) >= 1:
                id = query[0].id
                Lender.update(name=dict['name'], tel=dict['tel'],
                        idcard = dict['idcard'], family_addr = dict['family_addr'],
                        family_area = dict['family_area'], university = dict['university'],
                        univers_area = dict['univers_area']).where(Lender.id == query[0].id).execute()
                return ('success', id)
            else:
                Lender.insert(name=dict['name'], tel=dict['tel'],
                        idcard = dict['idcard'], family_addr = dict['family_addr'],
                        family_area = dict['family_area'], university = dict['university'],
                        univers_area = dict['univers_area'], is_del = 0).execute()
                query = Lender.select().where((Lender.idcard == dict['idcard']) & (Lender.is_del == 0))
                id = query[0].id
                return ('success', id)
        except BaseException,e:
            logger.error(e)
            return ('error', 0)

#订单信息
class OrderTable:

    def __init__(self, id = 0):
        self.id = id
    
    #传入字典更新数据库
    @classmethod
    def updatebasic(self, id, dict):
        try:
            query = Orders.update(disp=dict['dispid'], source=dict['source'],
                        account_day = dict['accountday'], product = dict['product'],
                        amount = float(dict['amount']), month_pay = float(dict['monthpay']),
                        periods = dict['periods'], paid_periods = dict['paidperiods'],
                        received_amount = float(dict['recvamount']), order_date = dict['orderdate'],
                        takeorder_data = dict['takeorderdate'], modify_time=datetime.datetime.now(),
                        status = dict['status']).where(Orders.id == id).execute()
            return 'success'
        except BaseException,e:
            logger.error(e)
            return 'error'
    
    #传入字典插入数据
    @classmethod
    def insertbasic(self, dict):
        try:
            Orders.insert(disp=dict['dispid'], source=dict['source'],lender = dict['lenderid'],
                        account_day = dict['accountday'], product = dict['product'],
                        amount = float(dict['amount']), month_pay = float(dict['monthpay']),
                        periods = dict['periods'], paid_periods = dict['paidperiods'],
                        received_amount = float(dict['recvamount']), order_date = dict['orderdate'],
                        takeorder_data = dict['takeorderdate'], status = dict['status'], 
                        create_time=datetime.datetime.now(),modify_time=datetime.datetime.now(),is_del = 0).execute()
            query = Orders.select().where((Orders.disp == dict['dispid']) & (Orders.is_del == 0))
            id = query[0].id
            return ('success', id)
        except BaseException,e:
            logger.error(e)
            return ('error', 0)

    #传入字典更新数据库
    @classmethod
    def updaterelatives(self, id, dict):
        try:
            query = Orders.update(parent=dict['parent'], parent_call=dict['parentcall'],
                        roommate = dict['roommate'], roommate_call = dict['roommatecall'],
                        classmate = dict['classmate'], classmate_call = dict['classmatecall']).where(Orders.id == id).execute()
            return 'success'
        except BaseException,e:
            logger.error(e)
            return 'error'
    
    #传入字典插入数据
    @classmethod
    def insertrelatives(self, dict):
        try:
            Orders.insert(parent=dict['parent'], parent_call=dict['parentcall'],
                        roommate = dict['roommate'], roommate_call = dict['roommatecall'],
                        classmate = dict['classmate'], classmate_call = dict['classmatecall'], is_del = 0).execute()
            query = Orders.select().where((Orders.parent == dict['parent'])& (Orders.is_del == 0))
            id = query[0].id
            return ('success', id)
        except BaseException,e:
            logger.error(e)
            return ('error', 0)

#订单信息
class OperationTable:

    def __init__(self, id = 0):
        self.id = id
    
    #传入字典更新数据库
    @classmethod
    def update(self, id, dict):
        try:
            query = Operation.update(admin =dict['adminid'], lender=dict['lenderid'],
                        op_desc = dict['opdesc']).where(Operation.id == id).execute()
            return 'success'
        except BaseException,e:
            logger.error(e)
            return 'error'
    
    #传入字典插入数据
    @classmethod
    def insert(self, dict):
        try:
            id = Operation.insert(admin =dict['adminid'], lender=dict['lenderid'],
                        op_desc = dict['opdesc'], time=datetime.datetime.now()).execute()
            return 'success', id
        except BaseException,e:
            logger.error(e)
            return 'error',0

#文件信息
class FilesTable:

    def __init__(self, id = 0):
        self.id = id
    
    #传入字典删除记录
    @classmethod
    def delete(self, id):
        try:
            query = Files.delete().where(Files.id == id).execute()
            return 'success'
        except BaseException,e:
            logger.error(e)
            return 'error'
    
    #传入字典插入数据
    @classmethod
    def insert(self, order_id, type, path):
        try:
            id = Files.insert(order =order_id, type=type,
                        path = path, time=datetime.datetime.now()).execute()
            return 'success', id
        except BaseException,e:
            logger.error(e)
            return 'error',0
    
    #传入字典查询数据
    @classmethod
    def query(self, order_id):
        try:
            query = (Files
                    .select()
                    .where(Files.order == orderid)
                    .order_by(Files.time.desc()))
            files = []
            for item in query:
                file = {'id': item.id, 'type': item.type, 'path': item.path}
                files.append(file)
            return  files
        except BaseException,e:
            logger.error(e)
            return  None