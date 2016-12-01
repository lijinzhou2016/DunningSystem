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
from bottle import *
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')

execfile(os.path.dirname(os.path.abspath(__file__))+os.sep+'util.py')

# load .tpl dir
bottle.TEMPLATE_PATH.append(www_path())
# create log obj
logger = log('main.py')
logger.debug('dunning server start')


@bottle.error(404)
def error404():
    return bottle.static_file('404.html', root=www_path())


# 返回登陆页面
@bottle.route('/dunning/<filepath:path>')
def index(filepath):
    if filepath in ['login', 'index']:
        return bottle.static_file('index.html', www_path())
    return bottle.static_file(filepath, www_path())


# 登陆用户验证接口
@bottle.route('/checkuser', method='POST')
def checkuser():
    logger.debug('check the user')
    name = bottle.request.forms.get('username')
    passwd = bottle.request.forms.get('password')
    userinfo = Userinfo.check_login(name, passwd)
    if not userinfo:
        return {'result':'error'}
    else:
        return get_userinfo_dic(userinfo)


# 返回订单列表页面
@bottle.route('/orderlist/<filepath:path>')
@bottle.view('orderlist')
def orderlist(filepath):
    # page_index = bottle.request.query.pageIndex
    # logger.debug(page_index)
    logger.debug('i am orderlist')
    if '.' in filepath:
        return bottle.static_file(filepath, www_path())

    return order_list_info


# 上传订单文件接口
@bottle.route('/upload', method='POST')
def upload_server():
    logger.debug('i am upload server.............')
    return save_ordersource()


@bottle.route('/order/detail')
def orderdetail():
    pass 


# 返回设置页面
@bottle.route('/setting/<filepath:path>')
@bottle.view('setting')
def setting_index(filepath):
    if '.' in filepath:
        return bottle.static_file(filepath, www_path())
    return init_setting_html()


# 设置操作接口
@bottle.route('/set', method='POST')
def set_data():
    action = bottle.request.forms.get('action')
 
    if action == 'yunpan':
        return yunpan()

    if action == 'adduser':
        return adduser()

    if action == 'deluser':
        return deluser()
        

#用户信息封装成json返回
def get_userinfo_dic(userinfo):
    return dict(zip(['result','name','passwd','is_admin'],['success',userinfo.name, userinfo.passwd, userinfo.is_admin]))



bottle.run(host='127.0.0.1', port='8080', debug=False)

