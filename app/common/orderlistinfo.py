#!/usr/bin/env python 
# -*- coding: UTF-8 -*-
#*****************************************************************************
# Title         : Orderinfo.py
# Author        : ljz
# Created       : 21th Nov 2016
# Last Modified : 
# Version       : 1.0
# 
# Description   : Get order info by order id
#*****************************************************************************

import time
import uuid
import os
import math
from peewee import *

def get_path(name, parent=False):
    path = os.path.dirname(os.path.abspath(__file__))
    path_comp = path.split(os.sep)
    if parent:
        path_comp.pop()
    path_comp[-1]=name
    return os.sep.join(path_comp)

def common_path():
    return get_path('common')

execfile(common_path() + os.sep + 'db.py')
execfile(common_path() + os.sep + 'config.py')

orderStatus = {0:'已结清', 1:'联系本人', 2:'联系亲属',3:'联系同学',
                4:'失联',5:'待外访',6:'外访中',7:'承诺还款',8:'部分还款'}

class OrderList:
    def __init__(self, pageindex, userinfo):
        self.userinfo = userinfo    # 用户信息
        self.orders_count = Orders.select().count()   # 订单总条数
        self.total_pages = int(math.ceil(self.orders_count/10.0))   # 分页数
        self.url_head='http://127.0.0.1:8080/'
        self.orders_one_info={'name':'','detailurl':'','ordernumber':'','phone':'','qiankuan':'','orderdata':'','acquiringdata':'','school':'','state':''}
        self.orders_return_info = {'userinfo':{},'fenyeinfo':{}, 'orders_list':[]}   # 返回字典
        self.orders_return_info['userinfo']=self.userinfo
        self.orders_return_info['fenyeinfo']={
            'pageIndex'   : pageindex, 
            'total_pages' : self.total_pages, 
            'total_orders': self.orders_count, 
            'setting_url' : self.url_head+r'setting?session='+self.userinfo['session'],
            'detail_url'  : self.url_head+r'setting?session='+self.userinfo['session'] #
        }
        
        # 按请求索引查找相应数据
        if self.orders_count > int(pageindex)*10:
            self.orders_list_info = Orders.select().where( (Orders.id>(int(pageindex)-1)*10) & (Orders.id<=int(pageindex)*10) )
        else:
            self.orders_list_info = Orders.select().where( (Orders.id>(int(pageindex)-1)*10) & (Orders.id<=self.orders_count) )
  
    def set_order_data(self):
        '''初始化返回字典的值

        '''
        for order_info_tmp in self.orders_list_info:
            lender_query=Lender.select().join(Orders).where(Orders.lender==order_info_tmp.lender).get()

            self.orders_return_info['orders_list'].append({
                'name' : lender_query.name,
                'detailurl' : self.url_head + r'orderdetail/'+ str(order_info_tmp.id) + r'?;session=' + self.userinfo['session'],
                'ordernumber' : order_info_tmp.disp,
                'phone' : lender_query.tel,
                'qiankuan' : 888, # 需要计算
                'orderdata' : order_info_tmp.order_date,
                'acquiringdata' : order_info_tmp.takeorder_data,
                'school' : lender_query.university,
                'state' : orderStatus[order_info_tmp.status]
            })

        # 不足10条数据，补空，满足前端显示一致
        for i in range(10 - len(self.orders_list_info)):
            self.orders_return_info['orders_list'].append(self.orders_one_info)


    def get_order_data(self):
        return self.orders_return_info

    @staticmethod
    def save_orders():
        logger.debug('i am save_ordersource......')
        name = request.forms.name #订单来源名称
        file_md5 = request.forms.testmd5
        data = request.files.data
        ext  = data.filename.split('.')[-1] #上传文件后缀
        save_name = file_md5 + '.' + ext

        if resource.set_orders_path(name) :
            new_file=os.path.join(resource.get_orders_path,save_name)
            if not os.path.exists(new_file):
                data.filename=save_name
                data.save(resource.get_orders_path, overwrite=True)
                if resource.get_md5(new_file)==file_md5:
                    return '上传成功'
                else:
                    os.remove(new_file)
                    return '上传失败,请重新上传'
            else:
                return '文件已存在，请勿重复上传'
        else:
            return '创建路径失败'
