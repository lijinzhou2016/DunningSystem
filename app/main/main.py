#!/usr/bin/env python 
# -*- coding: UTF-8 -*-
#*****************************************************************************
# Title         : main.py
# Author        : chxs&Ljz
# Created       : 4th December 2016
# Last Modified : 
# Version       : 1.0
# 
# Description   : server api
#*****************************************************************************

import bottle
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')

execfile(os.path.dirname(os.path.abspath(__file__))+os.sep+'util.py')
logger = log('main.py')

login_result={}


@bottle.error(404)
def error404():
    pass

# 静态信息文件 127.0.0.1:8080/
@bottle.route('/:filepath')
def server_www(filepath):
    file_name, file_type = os.path.splitext(filepath)
    if file_name == 'index':
        return bottle.static_file('index.html', root=www_path())
    elif file_type == '.html':
        return bottle.static_file(filename, root=www_path())
    elif file_type == '.css':
        return bottle.static_file(filepath, root=css_path())
    elif file_type == '.js':
        return bottle.static_file(filepath, root=js_path())
    elif file_type in ['.png','.PNG','.jpg','.JPG','.gif']:
        return bottle.static_file(filepath, root=images_path())

@bottle.route('/login', method='POST')
def login():
    logger.debug('i am login')
    name = bottle.request.forms.get('username')
    passwd = bottle.request.forms.get('password')
    logger.debug(name)
    userinfo = Userinfo.check_login(name, passwd)
    if not userinfo:
        return {'result':'error'}
    else:
        return get_userinfo_dic(userinfo)

@bottle.route('/order/list')
@bottle.view('orderlist')
def orderlist():
    page_index = bottle.request.query.pageIndex
    logger.debug(page_index)
    # 查询数据库，封装模板
    # return oderlist.tpl
    return "this is page ",page_index

@bottle.route('/order/detail')
def orderdetail():
    pass 


@bottle.route('/setting')
def setting():
    pass

def get_userinfo_dic(userinfo):
    return dict(zip(['result','name','passwd','is_admin'],['success',userinfo.name, userinfo.passwd, userinfo.is_admin]))

bottle.run(host='127.0.0.1', port='8080', debug=False)

