#!/usr/bin/env python 
# -*- coding: UTF-8 -*-
#*****************************************************************************
# Title         : config.py
# Author        : chenxiaosuo
# Created       : 1th December 2016
# Last Modified : 
# Version       : 1.0
# 
# Description   : 
#*****************************************************************************
import sys,os  


#获取lender信息生成字典
def get_lender_forms():
    id = bottle.request.forms.get('id')
    idcard = bottle.request.forms.get('idcard')
    name = bottle.request.forms.get('name')
    tel = bottle.request.forms.get('tel')
    univers = bottle.request.forms.get('univers')
    universarea = bottle.request.forms.get('universarea')
    familyaddr = bottle.request.forms.get('familyaddr')
    familyarea = bottle.request.forms.get('familyarea')
    return {'name': name, 'tel': tel, 'idcard':idcard,
        'university': univers, 'univers_area': universarea,
        'family_addr': familyaddr, 'family_area': familyarea,
        'id': id}

#更新lender信息到数据库中
def update_lender_info():
    lender = get_lender_forms()
    if lender['id'].strip() != '':
        result = LenderTable.update(lender['id'], lender)
        id = lender['id']
    else:
        result, id = LenderTable.insert(lender)
    return {'result': result, 'id': id}

#获取order信息生成字典
def get_order_basic_forms():
    id = bottle.request.forms.get('id')
    dispid = bottle.request.forms.get('dispid')
    source = bottle.request.forms.get('source')
    accountday = bottle.request.forms.get('accountday')
    product = bottle.request.forms.get('product')
    amount = bottle.request.forms.get('amount')
    monthpay = bottle.request.forms.get('monthpay')
    periods = bottle.request.forms.get('periods')
    paidperiods = bottle.request.forms.get('paidperiods')
    recvamount = bottle.request.forms.get('recvamount')
    orderdate = bottle.request.forms.get('orderdate')
    takeorderdate = bottle.request.forms.get('takeorderdate')
    call_details = bottle.request.forms.get('call_details')
    contract = bottle.request.forms.get('contract')
    status = bottle.request.forms.get('status')
    return {'dispid': dispid, 'source': source, 'accountday':accountday,
        'product': product, 'amount': amount,
        'monthpay': monthpay, 'periods': periods,
        'paidperiods': paidperiods, 'recvamount': recvamount,
        'orderdate': orderdate, 'takeorderdate': takeorderdate,
        'call_details': call_details, 'contract': contract,
        'status': status, 'id': id}

#更新order信息到数据库中
def update_order_basic_info():
    order = get_order_basic_forms()
    if order['id'].strip() != '':
        result = OrderTable.updatebasic(order['id'], order)
        id = order['id']
    else:
        result, id = OrderTable.insertbasic(order)
    return {'result': result, 'id': id}

#获取order的借款人亲属信息生成字典
def get_lender_relatives_forms():
    id = bottle.request.forms.get('id')
    parent = bottle.request.forms.get('parent')
    parentcall = bottle.request.forms.get('parentcall')
    roommate = bottle.request.forms.get('roommate')
    roommatecall = bottle.request.forms.get('roommatecall')
    classmate = bottle.request.forms.get('classmate')
    classmatecall = bottle.request.forms.get('classmatecall')
    return {'parent': parent, 'parentcall': parentcall,
        'roommate': roommate, 'roommatecall': roommatecall,
        'classmate': classmate, 'classmatecall': classmatecall,
        'id': id}

#更新order借款人亲属信息到数据库中
def update_lender_relatives_info():
    order = get_lender_relatives_forms()
    if order['id'].strip() != '':
        result = OrderTable.updaterelatives(order['id'], order)
        id = order['id']
    else:
        result, id = OrderTable.insertrelatives(order)
    return {'result': result, 'id': id}

#获取操作信息生成字典
def get_operations_forms():
    id = bottle.request.forms.get('id')
    opdesc = bottle.request.forms.get('opdesc')
    adminid = bottle.request.forms.get('adminid')
    lenderid = bottle.request.forms.get('lenderid')
    forms = {'id': id, 'opdesc': opdesc,
        'adminid': adminid, 'lenderid': lenderid}
    print forms
    return forms

#更新操作信息到数据库中
def update_operations_info():
    op = get_operations_forms()
    if op['id'].strip() != '':
        result = OperationTable.update(op['id'], op)
        id = op['id']
    else:
        result,id = OperationTable.insert(op)
    return {'result': result, 'id': id}