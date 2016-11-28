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


def static_file_server(filepath):
    return bottle.static_file(filepath, root=www_path())

@bottle.error(404)
def error404():
    return bottle.static_file('404.html', root=www_path())

# 静态信息文件 127.0.0.1:8080/
@bottle.route('/dunning/<filepath:path>')
def index(filepath):
    logger.debug(filepath)
    return static_file_server(filepath)

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

@bottle.route('/orderlist/<filepath:path>')
@bottle.view('orderlist')
def orderlist(filepath):
    # page_index = bottle.request.query.pageIndex
    # logger.debug(page_index)
    logger.debug('i am orderlist')
    if '.' in filepath:
        return static_file_server(filepath)

    # util.py 中定义
    return order_list_info

@bottle.route('/order/detail')
def orderdetail():
    pass 

@bottle.route('/setting/<action:path>')
@bottle.view('setting')
def setting(action):
    if '.' in action:
        return static_file_server(action)

    if action == 'yunpan':
        """ 网盘账号设置 """
        yaccount  = bottle.request.query.get('username').decode('utf-8')
        ypassword = bottle.request.query.get('passwd').decode('utf-8')
        ytime     = bottle.request.query.get('backuptime')+':00'
        if (len(System.select()) == 1):
            # 更新网盘
            System.update(username=yaccount, passwd=ypassword, backuptime=ytime).where(System.id==1).execute()
        else: #插入
            System.insert(id=1, username=yaccount, passwd=ypassword, backuptime=ytime).execute()

    elif action == 'adduser':
        """ 添加管理员 """
        logger.debug('start add user.......')

        user_id=bottle.request.query.get('id').decode('utf-8')
        user = bottle.request.query.get('user').decode('utf-8')
        passwd = bottle.request.query.get('passwd').decode('utf-8')
        name = bottle.request.query.get('name').decode('utf-8')

        Admin.insert(id=user_id, user=user, name=name,passwd=passwd,is_admin=0,enable=1).execute()

    elif action == 'deluser':
        """ 删除管理员 """
        user_id=bottle.request.query.get('id')
        Admin.delete().where(Admin.id==user_id).execute()

    elif action == 'jump':
        """ 加载设置页面 """
        try:
            system_query = System.select()
            admin_query = Admin.select()
        except BaseException,e:
            logger.error(e)
        user_str=''
        if (len(system_query) == 1):
            setting_info['account'] = system_query[0].username
            setting_info['password'] = system_query[0].passwd
            setting_info['backuptime'] = str(system_query[0].backuptime)[0:-3]
            setting_info['intval'] = str(system_query[0].intval)
        if (len(admin_query) >= 1):
            for item in admin_query:
                if not item.is_admin:
                    user_str += str(item.id)
                    user_str += '#'
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
        logger.debug('-------unknown-------')

#用户信息封装成json返回
def get_userinfo_dic(userinfo):
    return dict(zip(['result','name','passwd','is_admin'],['success',userinfo.name, userinfo.passwd, userinfo.is_admin]))

def op_sql(sql_cmd):
    try:
        logger.debug(sql_cmd)
        database.execute_sql(sql_cmd)
        result={'state':'success'}
        logger.debug(result['state'])
    except BaseException,e:
        logger.error(e)
        result = {'state':e}
    finally:
        return result

bottle.run(host='127.0.0.1', port='8080', debug=False)

