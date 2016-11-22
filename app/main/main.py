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

# load .tpl dir
bottle.TEMPLATE_PATH.append(www_path())
# create log obj
logger = log('main.py')

logger.debug('dunning server start')

@bottle.error(404)
def error404():
    return '404 error'

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

@bottle.route('/orderlist')
@bottle.view('orderlist')
def orderlist():
    page_index = bottle.request.query.pageIndex
    logger.debug(page_index)

    # util.py 中定义
    return order_list_info

@bottle.route('/order/detail')
def orderdetail():
    pass 


@bottle.route('/setting')
@bottle.view('setting')
def setting():
    logger.debug('i am setting')
    action = bottle.request.forms.get('action') #post
    if not action:
        action = bottle.request.query.action #get
    logger.debug(action)
    if action == 'yunpan':
        yaccount  = bottle.request.forms.get('account')
        ypassword = bottle.request.forms.get('password')
        ytime     = bottle.request.forms.get('time')

        
    elif action == 'adduser':
        pass 
    elif action == 'deluser':
        pass
    elif action == 'jump':
        system_query = System.select()
        admin_query = Admin.select()
        user_str=''
        if (len(system_query) == 1):
            setting_info['account'] = system_query[0].username
            setting_info['password'] = system_query[0].passwd
            setting_info['backuptime'] = str(system_query[0].backuptime)
            setting_info['intval'] = str(system_query[0].intval)
        if (len(admin_query) >= 1):
            for item in admin_query:
                if not item.is_admin:
                    user_str += item.user 
                    user_str += '#'
                    user_str += item.passwd
                    user_str += '#'
                    user_str += item.name
                    user_str += ','
            user_str = user_str[0:-1]
        
        setting_info['users'] = user_str 
        logger.debug(setting_info)
        return setting_info


    else:
        logger.debug('unknown')

#用户信息封装成json返回
def get_userinfo_dic(userinfo):
    return dict(zip(['result','name','passwd','is_admin'],['success',userinfo.name, userinfo.passwd, userinfo.is_admin]))

bottle.run(host='127.0.0.1', port='8080', debug=False)

