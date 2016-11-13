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
reload(sys)
sys.setdefaultencoding('utf8')

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

logger = log('main')
logger.debug('start server')

@bottle.route('/index')
def index():
    return bottle.static_file('index.html',root=www_path()) 

@bottle.error(404)
def error404():
    pass

# 静态信息文件 127.0.0.1:8080/index.html
@bottle.route('/:filepath')
def server_www(filepath):
    logger.debug("server_www api")
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

@bottle.route('/login', method='POST')
def login():
    name = bottle.request.forms.get('username')
    passwd = bottle.request.forms.get('password')
    logger.debug(name)
    userinfo = Userinfo.check_login(name, passwd)
    if not userinfo:
        return bottle.static_file('index.html',root=www_path()) 
    else:
        #return "<p>用户名：%s</p><p>姓名：%s</p><p>密码：%s</p><p>session：%s</p>" \
        #        %(userinfo.user, userinfo.name, userinfo.passwd, userinfo.session.session)
        return bottle.static_file('orderlist.html',root=www_path()) 

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

