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


# 当前绝对路径
def get_path(name, parent=False):
    path = os.path.dirname(os.path.abspath(__file__))
    path_comp = path.split(os.sep)
    if parent:
        path_comp.pop()
    path_comp[-1] = name
    return os.sep.join(path_comp)

def common_path():
    return get_path('common')

execfile(common_path()+os.sep+'mylogger.py')
logger = log('config.py')

class Resource:

    def __init__(self):
        self.ROOT_PATH = get_path('DunningSystemUpload',parent=True) #部署时，手动配置此路径
        self.orders = self.ROOT_PATH + os.sep + 'orders'
        self.lenderdata = self.ROOT_PATH + os.sep + 'lenderdata'
        self.orders_path=''
        self.data_path=''
        if not os.path.exists(self.ROOT_PATH): # 创建根目录
            os.makedirs(os.path.join(self.ROOT_PATH, self.orders))
            os.makedirs(os.path.join(self.ROOT_PATH, self.lenderdata, '1'))


    @property
    def get_data_path(self):
        return self.data_path

    @property
    def get_orders_path(self):
        return self.orders_path

    def get_md5(self, filepath):
        m = md5()
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


    def set_data_path(self, id):
        order_parent_dir_count = len(os.listdir(self.lenderdata))
        max_num_dir = max(os.listdir(self.lenderdata))

        if len(os.listdir(os.path.join(self.lenderdata, max_num_dir))) < 100 :
            self.data_path = os.path.join(self.lenderdata, max_num_dir, str(id))
        else:
            self.data_path = os.path.join(self.lenderdata, str(int(max_num_dir)+1), str(id))
        try:
            if not os.path.exists(self.data_path):
                os.makedirs(self.data_path) # 创建
            return True
        except BaseException,e:
            logger.error(e)
            return False


resource = Resource()

# 测试
# for id in range(1, 305):
#     resource.set_data_path(id)

# resource.set_data_path('20161212')
# logger.debug(resource.get_data_path)






