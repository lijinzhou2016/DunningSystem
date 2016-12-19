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

# resource.set_save_path(123)
# logger.debug(resource.get_save_path)
@bottle.error(404)
def error404():
    return bottle.static_file('404.html', root=www_path())


# # 返回登陆页面
# @bottle.route('/dunning/<filepath:path>')
# def index(filepath):
#     if filepath in ['login', 'index']:
#         return bottle.static_file('index.html', www_path())
#     return bottle.static_file(filepath, www_path())

# 静态信息文件 127.0.0.1:8080/
@bottle.route('/:filepath')
def server_www(filepath):
    logger.debug(filepath)

    file_name, file_type = os.path.splitext(filepath)

    if file_name in ['index','login']:
        return bottle.static_file('index.html', root=www_path())
    if file_type == '.html':
        return bottle.static_file(filename, root=www_path())
    if file_type == '.css':
        return bottle.static_file(filepath, root=css_path())
    if file_type == '.js':
        return bottle.static_file(filepath, root=js_path())
    if file_type in ['.png','.PNG','.jpg','.jpeg','.JPEG','.JPG','.gif']:
        return bottle.static_file(filepath, root=images_path())

# 日期插件静态文件
@bottle.route('/skin/default/<filename>')
def skin_default(filename):
    logger.debug(filename)
    return bottle.static_file(filename, root=os.sep.join([js_path(),'skin','default']))

@bottle.route('/skin/whygreen/<filename>')
def skin_whyGreen(filename):
    logger.debug(filename)
    return bottle.static_file(filename, root=os.sep.join([js_path(),'skin','whyGreen']))

@bottle.route('/skin/<filename>')
def skin(filename):
    logger.debug(filename)
    return bottle.static_file(filename, root=os.sep.join([js_path(),'skin']))

@bottle.route('/lang/<filename>')
def lang(filename):
    return bottle.static_file(filename, root= os.sep.join([js_path(),'lang']))
###############

# 登陆用户验证接口
@bottle.route('/checkuser', method='POST')
def checkuser():
    logger.debug('check the user')
    database = MySQLDatabase('dunning', **{'host': 'localhost', 'port': 3306, 'user': 'root','passwd':'123456'})
    name = bottle.request.forms.get('username')
    passwd = bottle.request.forms.get('password')
    userinfo = Userinfo.check_login(name, passwd)
    if not userinfo:
        return {'result':'error'}
    else:
        return get_userinfo_dic(userinfo)


# 返回订单列表页面
@bottle.route('/orderlist')
@bottle.view('orderlist')
def orderlist():
    #获取URL中的session，校验并获取URL信息
    session = bottle.request.query.session
    logger.debug('Got session ' + session)

    userinfo = Userinfo.get_by_session(session)
    if not userinfo:
        logger.info('session check invalid, redirect to login')
        bottle.redirect("/login")

    condition = bottle.request.query.condition
    page_index = bottle.request.query.pageIndex
    logger.debug('Got conditon : '+condition)
    orderlist_cls = OrderList(page_index, userinfo.dict_format(), condition)
    orderlist_cls.set_orders_data()

    return orderlist_cls.get_orders_data


# 上传订单文件接口
@bottle.route('/upload', method='POST')
def upload_server():
    logger.debug('i am upload server.............')
    return OrderList.save_orders_file()

# 上传数据文件接口
@bottle.route('/uploadlenderfile', method='POST')
def uploadlenderfile_server():
    logger.debug('i am uploadlenderfile server.............')
    return save_orderdetail_file()


@bottle.route('/orderdetail/<id:int>', method = 'GET')
@bottle.view('orderDetail')
def orderdetail(id):
    #获取URL中的session，校验并获取URL信息
    session = bottle.request.query.session
    logger.debug('Got session ' + session)
    userinfo = Userinfo.get_by_session(session)
    if not userinfo:
        logger.info('session check invalid, redirect to login')
        bottle.redirect("/login")
    #获取订单信息
    #如果为0则返回空白信息，用于创建新订单
    if id == 0:
        order_detail = Orderinfo.get_blank_dict()
    else:
        order_info = Orderinfo(id)
        if order_info.get_order_detail_all():
            order_detail = order_info.get_format_dict()
    #封装管理员信息到订单信息中
    order_detail['user'] = userinfo.dict_format()
    return order_detail

# 提交用户信息表单处理
@bottle.route('/orderdetail', method='POST')
def checkuser():
    logger.debug('post to orderdetail')
    action = bottle.request.forms.get('action')
    section = bottle.request.forms.get('section')
    if action == 'update':
        if section == 'lender':
            return update_lender_info()
        elif section == 'orderbasic':
            return update_order_basic_info()
        elif section == 'relatives':
            return update_lender_relatives_info()
        elif section == 'operations':
            return update_operations_info()
        else:
            return {'result': 'error'}

# 返回设置页面
@bottle.route('/setting')
@bottle.view('setting')
def setting_index():
    #获取URL中的session，校验并获取URL信息
    session = bottle.request.query.session
    logger.debug('Got session ' + session)
    userinfo = Userinfo.get_by_session(session)
    if not userinfo:
        logger.info('session check invalid, redirect to login')
        return 'unknown'
    setting_info['username']=userinfo.dict_format()['name']
    setting_info['session']=userinfo.dict_format()['session']
    return init_setting_html()

# 订单相关文件
@bottle.route('/orderdata/<filename>')
def orderdata_file(filename):
    idx = bottle.request.query.idx
    logger.debug("idx " + idx)
    id  = bottle.request.query.id
    logger.debug("id " + id)
    filepath = os.sep.join([str(idx), str(id), filename])
    logger.debug("filepath " + filepath)
    return bottle.static_file(filepath, root=orderdata_path())


# 设置操作接口
@bottle.route('/set', method='POST')
def set_data():
    #获取URL中的session，校验并获取URL信息
    session = bottle.request.forms.get('session')
    logger.debug('Got session ' + session)
    userinfo = Userinfo.get_by_session(session)
    logger.debug(str(userinfo))
    if not userinfo:
        logger.info('session check invalid, redirect to login')
        bottle.redirect("/login")
    action = bottle.request.forms.get('action')
 
    if action == 'yunpan':
        return yunpan()

    if action == 'adduser':
        return adduser()

    if action == 'deluser':
        return deluser()
        

#用户信息封装成json返回
def get_userinfo_dic(userinfo):
    return dict(zip(['result','name','passwd','is_admin', 'session'],
        ['success',userinfo.name, userinfo.passwd, userinfo.is_admin, userinfo.session.session]))



bottle.run(host='127.0.0.1', port='8080', debug=False)

