#!/usr/bin/env python 
# -*- coding: UTF-8 -*-
#*****************************************************************************
# Title         : config.py
# Author        : Ljz
# Created       : 4th December 2016
# Last Modified : 
# Version       : 1.0
# 
# Description   : support base conf
#*****************************************************************************
import sys,os
from mylogger import log
import hashlib


logger = log('config.py')


class Resource:
    def __init__(self):
        self.ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.orders = self.ROOT_PATH + os.sep + 'orders'
        self.lenderdata = self.ROOT_PATH + os.sep + 'lenderdata'
        self.orders_path=''
        if not os.path.exists(self.ROOT_PATH):  # 创建根目录
            os.makedirs(os.path.join(self.ROOT_PATH, self.orders))
            os.makedirs(os.path.join(self.ROOT_PATH, self.lenderdata, '1'))

    @property
    def get_orders_path(self):
        return self.orders_path

    def get_md5(self, filepath):
        m = hashlib.md5()
        a_file = open(filepath, 'rb')    #需要使用二进制格式读取文件内容
        m.update(a_file.read())
        a_file.close()

        return m.hexdigest()


    def set_orders_path(self, place):
        self.orders_path = os.path.join(self.orders, place)
        try:
            if not os.path.exists(self.orders_path):
                os.makedirs(self.orders_path)
            return True
        except BaseException,e:
            logger.error(e)
            return False

    #根据id获取目录，如果目录不存在，则创建
    #获取规则，取模：
    #1-99 -》0
    #100- 199 > 1
    def get_data_path(self, id):
        data_path = os.path.join(self.lenderdata, str(id/100), str(id))
        try:
            if not os.path.exists(data_path):
                os.makedirs(data_path)  # 创建
            return data_path
        except BaseException, e:
            logger.error(e)
            return None


resource = Resource()

# 测试
# for id in range(1, 305):
#     resource.set_data_path(id)

# resource.set_data_path('20161212')
# logger.debug(resource.get_data_path)






