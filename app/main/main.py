#!/usr/bin/env python 
# -*- coding: UTF-8 -*-
#*****************************************************************************
# Title         : main.py
# Author        : Ljz
# Created       : 4th December 2016
# Last Modified : 
# Version       : 1.0
# 
# Description   : support base conf
#*****************************************************************************

import bottle
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

def common_path():
    return get_path('common')

sys.path.append(common_path())
from mylogger import MyLogger 

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



@bottle.error(404)
def error404():
    pass

# 静态信息文件 127.0.0.1:8080/
@bottle.route('/:filepath')
def server_www(filepath):
    print filepath
    file_type=os.path.splitext(filepath)[1]
    print file_type
    if file_type == '.html':
        return bottle.static_file(filepath, root=www_path())
    elif file_type == '.css':
        return bottle.static_file(filepath, root=css_path())
    elif file_type == '.js':
        return bottle.static_file(filepath, root=js_path())
    elif file_type in ['.png','.PNG','.jpg','.JPG','.gif']:
        return bottle.static_file(filepath, root=images_path())

@bottle.route('/login')
def login():
    pass

@bottle.route('/order/list.action')
def orderlist():
    pass 

@bottle.route('/order/detail.cation')
def orderdetail():
    pass 

@bottle.route('/setting')
def setting():
    pass

bottle.run(host='127.0.0.1', port='8080', debug=False)

