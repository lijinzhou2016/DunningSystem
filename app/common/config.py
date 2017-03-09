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
import ConfigParser


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

def read_conf(model):
    try:
        cf = ConfigParser.ConfigParser()
        if os.path.exists(os.path.join(get_path("",parent=True), "..", 'conf.ini')):
            cf.read(os.path.join(get_path("",parent=True), "..", 'conf.ini'))
            item = dict(cf.items(model))
            return dict(item)
        else:
            return {}
    except Exception as e:
        return {}
#print os.path.join(get_path("",parent=True), "..", 'conf.ini')
def get_root_path():
    '''上传文件保存路径根目录从配置文件加载

        若配置文件缺失，默认系统上级目录为跟目录
    '''
    root_path = read_conf('upload')
    if root_path:
        return os.path.join(root_path['root'], 'Upload')
    else:
        return get_path(os.path.join('..', 'Upload'),parent=True)

class Resource:
    def __init__(self):
        self.ROOT_PATH = get_root_path()
        self.orders = self.ROOT_PATH + os.sep + 'orders'
        self.lenderdata = self.ROOT_PATH + os.sep + 'lenderdata'
        self.orders_path=''
        if not os.path.exists(self.ROOT_PATH): # 创建根目录
            os.makedirs(os.path.join(self.ROOT_PATH, self.orders))
            os.makedirs(os.path.join(self.ROOT_PATH, self.lenderdata, '1'))

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

    #根据id获取目录，如果目录不存在，则创建
    #获取规则，取模：
    #1-99 -》0
    #100- 199 > 1
    def get_data_path(self, id):
        data_path = os.path.join(self.lenderdata, str(id/100), str(id))
        try:
            if not os.path.exists(data_path):
                os.makedirs(data_path) # 创建
            return data_path
        except BaseException,e:
            logger.error(e)
            return None


resource = Resource()

# 测试
# for id in range(1, 305):
#     resource.set_data_path(id)

# resource.set_data_path('20161212')
# logger.debug(resource.get_data_path)






