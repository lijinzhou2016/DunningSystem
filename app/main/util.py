#!/usr/bin/env python 
# -*- coding: UTF-8 -*-
#*****************************************************************************
# Title         : util.py
# Author        : Ljz
# Created       : 4th December 2016
# Last Modified : 
# Version       : 1.0
# 
# Description   : support base conf
#*****************************************************************************

import os
import sys


# 当前绝对路径
def get_path(name, parent=False):
    path = os.path.dirname(os.path.abspath(__file__))
    path_comp = path.split(os.sep)
    if parent:
        path_comp.pop()
    path_comp[-1] = name
    return os.sep.join(path_comp)

def root_path():
    return get_path('',parent=True)

def common_path():
    return get_path('common')

def lib_path():
    return get_path('lib')

sys.path.append(lib_path())
from userinfo import Userinfo 

def www_path():
    return get_path('www',parent=True)
def data_path():
    return get_path('data',parent=True)
def scripts_path():
    return get_path('scripts',parent=True)
def js_path():
    return www_path()+os.sep+'js'
def css_path():
    return www_path()+os.sep+'css'
def images_path():
    return www_path()+os.sep+'images'


# os.sep 自适配系统路径分隔符
execfile(common_path() + os.sep + 'db.py')
execfile(common_path() + os.sep + 'config.py')
execfile(common_path() + os.sep + 'mylogger.py')

# orderlist.tpl
order_list_info ={
    'username':'Test',

    'name_0':'', 'detailurl_0':'', 'ordernumber_0':'', 'phone_0':'', 'qiankuan_0':'',
    'orderdata_0':'', 'acquiringdata_0':'', 'school_0':'', 'state_0':'',

    'name_1':'', 'detailurl_1':'', 'ordernumber_1':'', 'phone_1':'', 'qiankuan_1':'',
    'orderdata_1':'', 'acquiringdata_1':'', 'school_1':'', 'state_1':'',
    
    'name_2':'', 'detailurl_2':'', 'ordernumber_2':'', 'phone_2':'', 'qiankuan_2':'',
    'orderdata_2':'', 'acquiringdata_2':'', 'school_2':'', 'state_2':'',
    
    'name_3':'', 'detailurl_3':'', 'ordernumber_3':'', 'phone_3':'', 'qiankuan_3':'',
    'orderdata_3':'', 'acquiringdata_3':'', 'school_3':'', 'state_3':'',
    
    'name_4':'', 'detailurl_4':'', 'ordernumber_4':'', 'phone_4':'', 'qiankuan_4':'',
    'orderdata_4':'', 'acquiringdata_4':'', 'school_4':'', 'state_4':'',
    
    'name_5':'', 'detailurl_5':'', 'ordernumber_5':'', 'phone_5':'', 'qiankuan_5':'',
    'orderdata_5':'', 'acquiringdata_5':'', 'school_5':'', 'state_5':'',
    
    'name_6':'', 'detailurl_6':'', 'ordernumber_6':'', 'phone_6':'', 'qiankuan_6':'',
    'orderdata_6':'', 'acquiringdata_6':'', 'school_6':'', 'state_6':'',
    
    'name_7':'', 'detailurl_7':'', 'ordernumber_7':'', 'phone_7':'', 'qiankuan_7':'',
    'orderdata_7':'', 'acquiringdata_7':'', 'school_7':'', 'state_7':'',
    
    'name_8':'', 'detailurl_8':'', 'ordernumber_8':'', 'phone_8':'', 'qiankuan_8':'',
    'orderdata_8':'', 'acquiringdata_8':'', 'school_8':'', 'state_8':'',
    
    'name_9':'', 'detailurl_9':'', 'ordernumber_9':'', 'phone_9':'', 'qiankuan_9':'',
    'orderdata_9':'', 'acquiringdata_9':'', 'school_9':'', 'state_9':''
}

# setting.tpl
# users: 'account1#passwd1#name1,account2#passwd#name2'
setting_info = {
    'username':'Test',
    
    'account':'', 'password':'', 'backuptime':'', 'intval':'',

    'users':''
}


